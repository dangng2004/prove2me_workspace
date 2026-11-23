"""Combine and compare informal proofs of a statement with headless Codex and Claude.

Each statement lives in results/exposition/<name>/ with
  statement.tex   the statement being proved
  context.tex     optional: results the proofs may cite
  versions/*.tex  the proofs to compare (original.tex is the paper's proof)

Subcommands:
  extract  turn a Lean proof into an informal LaTeX proof in versions/
  combine  write a new proof from all versions, saved as versions/combined_<family>.tex
  judge    have each judge rank all versions blind, saved to judges/<model>.json
  table    print a markdown table of rankings, one row per statement, one column per judge

Codex models (names starting with "gpt") run through `codex exec`. Claude models run through
`claude -p` under the default login, or the one in CLAUDE_ALT_CONFIG if set.
"""
import argparse
import json
import os
import random
import re
import string
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "prompts"
BASE = ROOT / "results" / "exposition"
CODEX_JUDGES = ["gpt-6-astra", "gpt-5.6-sol"]
CLAUDE_JUDGES = ["claude-sonnet-5-5", "claude-opus-5-5"]


def run_model(model, prompt, log_path):
    """Send one prompt to a model with no tools and return its final text answer."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        if model.startswith("gpt"):
            out = Path(tmp) / "answer.txt"
            cmd = ["codex", "exec", "--model", model, "-c", 'model_reasoning_effort="high"',
                   "--sandbox", "read-only", "--skip-git-repo-check", "--cd", tmp,
                   "--output-last-message", str(out), "-"]
            proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=7200)
            log_path.write_text(proc.stdout + "\n" + proc.stderr)
            if not out.exists():
                raise RuntimeError(f"{model} produced no answer, see {log_path}")
            return out.read_text()
        if os.environ.get("CLAUDE_VIA_FILES"):
            # Two-phase mode for when `claude -p` is unavailable: write the prompt for a Claude
            # subagent to answer, and read its answer back on the next run.
            answer = log_path.with_suffix(".answer.md")
            if answer.exists():
                return answer.read_text()
            log_path.with_suffix(".prompt.md").write_text(prompt)
            raise RuntimeError(f"wrote {log_path.with_suffix('.prompt.md')}; save the answer to {answer}")
        env = {"HOME": os.environ["HOME"], "PATH": os.environ["PATH"]}
        if os.environ.get("CLAUDE_ALT_CONFIG"):
            env["CLAUDE_CONFIG_DIR"] = os.environ["CLAUDE_ALT_CONFIG"]
        cmd = ["claude", "-p", "--model", model, "--output-format", "json", "--permission-mode", "dontAsk"]
        proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True, env=env, cwd=tmp, timeout=7200)
        log_path.write_text(proc.stdout + "\n" + proc.stderr)
        result = json.loads(proc.stdout)
        if result.get("is_error"):
            raise RuntimeError(f"{model} failed, see {log_path}")
        return result["result"]


def family(model):
    return "codex" if model.startswith("gpt") else "claude"


def statement_block(d):
    parts = ["# Statement\n\n" + (d / "statement.tex").read_text()]
    if (d / "context.tex").exists():
        parts.append("# Context: results the proofs may cite\n\n" + (d / "context.tex").read_text())
    return "\n\n".join(parts)


def versions(d, only=None):
    return {p.stem: p.read_text() for p in sorted((d / "versions").glob("*.tex")) if not only or p.stem in only}


def word_count(tex):
    """Words of a LaTeX proof, ignoring commands, braces and math delimiters."""
    return len(re.sub(r"\\[a-zA-Z]+|[{}$\\]", " ", tex).split())


def extract(args):
    d = BASE / args.statement
    prompt = "\n\n".join([(PROMPTS / "lean_to_informal.md").read_text(), statement_block(d),
                          "# Lean formalization\n\n```lean\n" + Path(args.lean).read_text() + "\n```"])
    text = run_model(args.model, prompt, d / "logs" / f"extract_{args.name}.log")
    m = re.search(r"\\begin\{(lemma|proof)\}.*\\end\{proof\}", text, re.S)
    (d / "versions").mkdir(parents=True, exist_ok=True)
    (d / "versions" / f"{args.name}.tex").write_text((m.group(0) if m else text).strip() + "\n")


def combine(args):
    d = BASE / args.statement
    vs = {k: v for k, v in versions(d, args.sources).items() if not k.startswith(("combined", "rewrite"))}
    blocks = []
    for i, (name, text) in enumerate(sorted(vs.items(), key=lambda kv: kv[0] != "original"), 1):
        origin = "the original proof from the paper" if name == "original" else "derived from a formalization"
        blocks.append(f"## Version {i} ({origin})\n\n{text}")
    parts = [(PROMPTS / f"{args.prompt}.md").read_text()]
    suffix = ""
    if args.max_words:
        budget = round(args.max_words * word_count(vs["original"]))
        parts.append(f"Length limit: your proof (everything inside the <proof> block) must be at most {budget} words, "
                     "counting words of prose and mathematics but not LaTeX commands. This is about the length of the "
                     "original proof. Meet the limit by choosing what to include, not by skipping steps a careful reader needs.")
        suffix = f"_{args.max_words:g}x"
    parts += [(PROMPTS / "exposition_rubric.md").read_text(), statement_block(d), "# Proofs\n\n" + "\n\n".join(blocks)]
    prompt = "\n\n".join(parts)
    text = run_model(args.model, prompt, d / "logs" / f"{args.prefix}_{args.model}{suffix}.log")
    proof = re.search(r"<proof>(.*?)</proof>", text, re.S)
    notes = re.search(r"<notes>(.*?)</notes>", text, re.S)
    name = f"{args.prefix}_{family(args.model)}{suffix}"
    (d / "versions" / f"{name}.tex").write_text((proof.group(1) if proof else text).strip() + "\n")
    (d / "combine_notes").mkdir(exist_ok=True)
    (d / "combine_notes" / f"{name}.md").write_text((notes.group(1) if notes else "").strip() + "\n")


def judge_one(d, model, only=None, tag=""):
    vs = versions(d, only)
    names = list(vs)
    random.Random(f"{d.name}:{model}").shuffle(names)
    labels = dict(zip(string.ascii_uppercase, names))
    blocks = [f"## Proof {lab}\n\n{vs[name]}" for lab, name in labels.items()]
    prompt = "\n\n".join([(PROMPTS / "judge_proofs.md").read_text(), (PROMPTS / "exposition_rubric.md").read_text(),
                          statement_block(d), "# Proofs\n\n" + "\n\n".join(blocks)])
    text = run_model(model, prompt, d / "logs" / f"judge{tag}_{model}.log")
    answer = json.loads(text[text.index("{"):text.rindex("}") + 1])
    record = {"model": model, "labels": labels,
              "ranking": [labels[x] for x in answer["ranking"]],
              "scores": {labels[k]: v for k, v in answer["scores"].items()},
              "rationale": answer.get("rationale", "")}
    (d / f"judges{tag}").mkdir(exist_ok=True)
    (d / f"judges{tag}" / f"{model}.json").write_text(json.dumps(record, indent=2))
    return model


def judge(args):
    d = BASE / args.statement
    models = args.models or CODEX_JUDGES + CLAUDE_JUDGES
    with ThreadPoolExecutor(len(models)) as pool:
        for fut in [pool.submit(judge_one, d, m, args.only, f"_{args.tag}" if args.tag else "") for m in models]:
            try:
                print("judged by", fut.result())
            except Exception as e:  # keep the other judges' results
                print("judge failed:", e)


def table(args):
    models = CODEX_JUDGES + CLAUDE_JUDGES
    rows = ["| Statement | " + " | ".join(models) + " |", "|---" * (len(models) + 1) + "|"]
    for name in args.statements:
        cells = []
        for m in models:
            p = BASE / name / "judges" / f"{m}.json"
            cells.append(" > ".join(json.loads(p.read_text())["ranking"]) if p.exists() else "missing")
        rows.append(f"| {name} | " + " | ".join(cells) + " |")
    print("\n".join(rows))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("extract"); p.add_argument("statement"); p.add_argument("name"); p.add_argument("lean")
    p.add_argument("--model", default="claude-opus-5-5"); p.set_defaults(fn=extract)
    p = sub.add_parser("combine"); p.add_argument("statement"); p.add_argument("--model", required=True)
    p.add_argument("--max-words", type=float, help="word budget as a multiple of the original proof's length")
    p.add_argument("--sources", nargs="*", help="versions to give the combiner (default: all non-generated ones)")
    p.add_argument("--prompt", default="combine_proofs", help="prompt file in prompts/, without .md")
    p.add_argument("--prefix", default="combined", help="name prefix of the output version")
    p.set_defaults(fn=combine)
    p = sub.add_parser("judge"); p.add_argument("statement"); p.add_argument("--models", nargs="*")
    p.add_argument("--only", nargs="*", help="judge only these versions"); p.add_argument("--tag", help="suffix for judges/ and logs")
    p.set_defaults(fn=judge)
    p = sub.add_parser("table"); p.add_argument("statements", nargs="+"); p.set_defaults(fn=table)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
