"""Typeset one proof version of a statement as a standalone PDF.

Usage: python3 pdf/build_pdf.py <statement> <version> [<version> ...]

Each PDF has a source note, the statement (with the section's conventions, if any), the results
from the paper that the proofs may cite (context.tex, if any), and the proof. It uses the paper's
own preamble so the macros match. Output goes to pdf/<statement>_<version>.pdf, with a
"_claude_1x" suffix dropped from the version name.
"""
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / "results" / "exposition"
PAPER = ("\\emph{The Falconer distance conjecture in all dimensions} "
         "(OpenAI, 23 September 2026)")
TITLES = {"linear_projection_gain": "Linear projection gain (Theorem 4.1)",
          "contact_interval": "A contact interval (Lemma 5.2)"}
SOURCES = {
    "original": "The proof is verbatim from " + PAPER + ". Typeset for comparison.",
    "rewrite_claude_1x": "A rewrite of the paper's proof by Claude (Opus), from the paper's proof alone, "
                         "with a word budget equal to the paper's proof.",
    "combined_claude_1x": "A proof by Claude (Opus) that combines the paper's proof with informal versions of "
                          "two Lean formalizations (by Claude and Codex), with a word budget equal to the "
                          "paper's proof.",
}
LABELS = {"original": "the original proof", "rewrite_claude_1x": "a rewrite",
          "combined_claude_1x": "a combined proof"}
# Displays from the paper's proof of the slice-selection lemma that the original proof of
# Theorem 4.1 cites; the context gives only that lemma's statement.
EXTRA_DISPLAYS = r"""
\medskip\noindent\emph{Two displays from the paper's proof of Lemma~\ref{ang:slice-selection}}, cited by the proof below. Write $M(V)=\|\nu_V\|$ and $L(V,z)=\|\mu_{V,z}\|$. Uniformly in $V$,
\begin{equation}\label{ang:point-slice-total}
 \int L(V,z)\,dz\le C.
\end{equation}
The two-vector estimate in a projective chart gives the direction-pair kernel
\begin{equation}\label{ang:direction-pair-kernel}
 \delta^{-2h}\Pr\{w,w'\text{ both within }\delta\text{ of }V\}
       \le C(|w-w'|+\delta)^{-h}.
\end{equation}
"""


def body(statement, version):
    d = BASE / statement
    stmt = (d / "statement.tex").read_text().split("\n", 1)[1]  # drop the macros comment
    stmt = stmt.replace("Section~\\ref{sec:conventions}", "Section~2 of the paper")
    parts = []
    if "% Section conventions:" in stmt:
        conv, thm = stmt.split("% Section conventions:\n", 1)[1].split("\\begin{theorem}", 1)
        parts += ["\\section*{Conventions}\n" + conv.strip(), "\\section*{Statement}\n\\begin{theorem}" + thm.strip()]
    else:
        parts.append("\\section*{Statement}\n" + stmt.strip())
    proof = (d / "versions" / f"{version}.tex").read_text().strip()
    if (d / "context.tex").exists():
        ctx = (d / "context.tex").read_text().split("\n", 2)[2].strip()
        cited = "\\section*{Results cited from the paper}\nProofs omitted; numbering here is local.\n\n" + ctx
        if "ang:direction-pair-kernel" in proof:
            cited += "\n" + EXTRA_DISPLAYS
        parts.append(cited)
    parts.append("\\section*{Proof}\n" + proof)
    return "\n\n".join(parts)


def build(statement, version):
    tex = HERE / f"{statement}_{version.removesuffix('_claude_1x')}.tex"
    tex.write_text("\\documentclass[11pt,reqno]{amsart}\n\\input{preamble}\n"
                   "\\renewcommand{\\thetheorem}{\\arabic{theorem}}\n\\renewcommand{\\theequation}{\\arabic{equation}}\n"
                   f"\\title{{{TITLES[statement]}: {LABELS[version]}}}\n\\begin{{document}}\n\\maketitle\n"
                   f"\\noindent\\emph{{Source.}} The statement is from {PAPER}. {SOURCES[version]}\n\n"
                   + body(statement, version) + "\n\\end{document}\n")
    subprocess.run(["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", tex.name],
                   cwd=HERE, capture_output=True)
    log = tex.with_suffix(".log").read_text(errors="replace")
    problems = sorted(set(re.findall(r"^!.*|.*undefined.*", log, re.M)))
    pages = re.search(r"Output written on .*?\((\d+) pages?", log)
    print(f"{tex.with_suffix('.pdf').name}: {pages.group(1) + ' pages' if pages else 'FAILED'}",
          *problems, sep="\n  ")
    subprocess.run(["latexmk", "-c", tex.name], cwd=HERE, capture_output=True)


if __name__ == "__main__":
    for v in sys.argv[2:]:
        build(sys.argv[1], v)
