"""One scheduled agent-mode run.

    python3 scripts/agent_mode/run.py              # what the scheduler calls
    python3 scripts/agent_mode/run.py --dry-run    # pick and log actions; no agent, no submissions
    python3 scripts/agent_mode/run.py --now        # ignore quiet hours (budget still applies)
    python3 scripts/agent_mode/run.py prepare      # desktop mode: pick one action, print its task
    python3 scripts/agent_mode/run.py finish       # desktop mode: charge usage, record the outcome

Each run: settle earlier submissions → read usage → go/no-go → repeat
{pick action + target → run the agent headless → charge its usage} until the
per-run cap, either window's budget, or max_actions_per_run is reached.
"""
from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import json
import random
import subprocess
import sys
import time
import urllib.error
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
import budget  # noqa: E402
from common import (STATE_DIR, WORKSPACE, P2M, load_config, load_ledger, log, now,  # noqa: E402
                    save_ledger, skill_version)
from policy import pick  # noqa: E402
import sessions  # noqa: E402

PLAYBOOK = "references/agent_mode.md"
CLIENT_TAG = "agent_mode"
FINAL = {"ACCEPTED", "SKETCH_ACCEPTED", "FAILED", "CE", "WA", "SORRY", "ERROR"}
LIMIT_MARKERS = ("usage limit", "rate limit", "rate_limit", "limit reached", "quota")


# ---------------------------------------------------------------- prompt


def build_prompt(action: str, target: Dict[str, Any], run_dir: Path) -> str:
    return f"""You are running in Prove2Me AGENT MODE, unattended, on behalf of your human.

Read {PLAYBOOK} first and follow it exactly; it overrides conflicting guidance in the
other references for this run. In particular, agent mode OVERRIDES the rule in
references/missions.md that says "Do NOT re-formalize or re-prove" a completed
milestone: alternative formalizations of proved theorems and completed milestones are
a goal of this mode, as long as they are tagged as such (see the playbook).

ACTION: {action}
TARGET:
{json.dumps(target, indent=1, ensure_ascii=False)}

Workspace: {WORKSPACE} (credentials.json is here; never print the API key or tokens).
Run directory: {run_dir}

Before you stop, write {run_dir}/result.json:
{{"outcome": "submitted" | "declined" | "failed",
  "theorem_id": "...", "submission_ids": ["..."], "comment_ids": ["..."],
  "reason": "one or two sentences", "difference": "for reformalize: how yours differs"}}
"declined" means your scout step judged the target not worth this budget; say why.
"""


# ---------------------------------------------------------------- agent invocation


def run_agent(cfg: Dict[str, Any], prompt: str, run_dir: Path, led: Dict[str, Any]
              ) -> Tuple[Optional[budget.Reading], Optional[budget.Reading], float, str, int, Dict[str, Any]]:
    """Run one headless agent action.

    Returns (before, after, usd, tail_of_output, exit_code, session) where session
    has the session id and transcript path, for resuming or side-chatting later.
    """
    a = cfg["agent"]
    timeout = 60 * float(a["action_timeout_min"])
    out_path = run_dir / "agent.jsonl"
    started = now()
    if a["provider"] == "claude":
        cmd = ["claude", "-p", prompt, "--output-format", "stream-json", "--verbose",
               "--max-turns", str(a["max_turns"]), "--max-budget-usd", str(a["action_usd_cap"]),
               "--permission-mode", "acceptEdits", "--add-dir", str(run_dir),
               "--allowedTools", *a["allowed_tools"]]
        if a.get("model"):
            cmd += ["--model", a["model"]]
        before = led.get("last_reading")
    else:
        cmd = ["codex", "exec", "--json", "-C", str(WORKSPACE), "--skip-git-repo-check",
               "--sandbox", "workspace-write", "-c", "sandbox_workspace_write.network_access=true",
               "--add-dir", str(run_dir), prompt]
        if a.get("model"):
            cmd[2:2] = ["-m", a["model"]]
        before = budget.codex_reading() or led.get("last_reading")
    code = 0
    with open(out_path, "w") as fh:
        try:
            p = subprocess.run(cmd, cwd=WORKSPACE, stdout=fh, stderr=subprocess.STDOUT,
                               timeout=timeout, text=True)
            code = p.returncode
        except subprocess.TimeoutExpired:
            code = -9
            log(f"agent timed out after {a['action_timeout_min']} min")
    text = out_path.read_text(errors="replace")
    usd = 0.0
    if a["provider"] == "claude":
        rs = budget.claude_readings_from_stream(text.splitlines())
        stale = not before or before.get("provider") != "claude" or started - before["at"] > 600
        if rs and stale:
            before = rs[0]  # first event of this run ≈ usage before it
        after = rs[-1] if rs else None
        sid = sessions.claude_session_id(text)
        session = {"session_id": sid, "transcript": sessions.claude_transcript(sid) if sid else None}
        for line in text.splitlines():
            if '"type":"result"' in line.replace(" ", ""):
                try:
                    usd = float(json.loads(line).get("total_cost_usd") or 0)
                except ValueError:
                    pass
    else:
        after = budget.codex_reading(since=started - 5)
        session = sessions.codex_session_since(started)
    return before, after, usd, text[-4000:], code, session


def hit_limit(after: Optional[budget.Reading], tail: str, code: int) -> bool:
    if after and after.get("status") == "rejected":
        return True
    return code != 0 and any(m in tail.lower() for m in LIMIT_MARKERS)


# ---------------------------------------------------------------- bookkeeping


def settle_submissions(api: P2M, led: Dict[str, Any]) -> None:
    """Poll earlier submissions; credit accepted alternative proofs."""
    credits = led.setdefault("credits", {"alternative_proofs": 0, "proofs": 0, "sketches": 0})
    for act in led["actions"]:
        pend = act.setdefault("pending", list(act.get("submission_ids") or []))
        if not pend:
            continue
        still = []
        for sid in pend:
            try:
                r = api.get("/verify", submission_id=sid)
            except urllib.error.HTTPError as e:
                log(f"poll {sid}: HTTP {e.code}")
                still.append(sid)
                continue
            st = r.get("status")
            if st not in FINAL:
                still.append(sid)
                continue
            act.setdefault("verdicts", {})[sid] = st
            if st == "ACCEPTED" and act["action"] == "reformalize":
                credits["alternative_proofs"] += 1
                act.setdefault("credited", []).append(sid)
            elif st == "ACCEPTED":
                credits["proofs"] += 1
            elif st == "SKETCH_ACCEPTED":
                credits["sketches"] += 1
        act["pending"] = still


def record_result(led: Dict[str, Any], action: str, target: Dict[str, Any], run_dir: Path,
                  charged: Dict[str, Optional[float]], usd: float, code: int,
                  session: Optional[Dict[str, Any]] = None, mode: str = "headless") -> Dict[str, Any]:
    res: Dict[str, Any] = {}
    rp = run_dir / "result.json"
    if rp.exists():
        try:
            res = json.loads(rp.read_text())
        except ValueError:
            res = {"outcome": "failed", "reason": "unreadable result.json"}
    else:
        res = {"outcome": "failed", "reason": f"agent exited {code} without result.json"}
    entry = {
        "ts": now(), "action": action, "theorem_id": target["theorem_id"],
        "theorem_name": target.get("theorem_name"), "mission_name": target.get("mission_name"),
        "score": target.get("score"), "outcome": res.get("outcome"), "reason": res.get("reason"),
        "difference": res.get("difference"), "submission_ids": res.get("submission_ids") or [],
        "comment_ids": res.get("comment_ids") or [], "charged": charged, "usd": round(usd, 4),
        "run_dir": str(run_dir), "mode": mode,
        "session_id": (session or {}).get("session_id"), "transcript": (session or {}).get("transcript"),
    }
    led["actions"].append(entry)
    led["attempted"][target["theorem_id"]] = {"ts": now(), "action": action, "outcome": entry["outcome"]}
    return entry


def write_digest(led: Dict[str, Any], closed: Dict[str, Any]) -> None:
    start = closed["id"] - 7 * 86400
    acts = [a for a in led["actions"] if start <= a.get("ts", 0) < closed["id"]]
    by: Dict[str, int] = {}
    for a in acts:
        by[f"{a['action']}/{a.get('outcome')}"] = by.get(f"{a['action']}/{a.get('outcome')}", 0) + 1
    c = led.get("credits", {})
    lines = [f"# Agent mode — week ending {dt.datetime.fromtimestamp(closed['id']):%Y-%m-%d}", "",
             f"- Budget spent: {closed['spent']:.1%} of your weekly window (${closed.get('usd', 0):.2f})",
             f"- Actions: {len(acts)} — " + ", ".join(f"{k}: {v}" for k, v in sorted(by.items())),
             f"- Credits so far: {c.get('alternative_proofs', 0)} alternative proofs, "
             f"{c.get('proofs', 0)} proofs, {c.get('sketches', 0)} sketches", "", "## Submissions", ""]
    for a in acts:
        if a.get("submission_ids"):
            lines.append(f"- {a['action']} `{a.get('theorem_name')}`: {', '.join(a['submission_ids'])}"
                         f" — {a.get('difference') or a.get('reason') or ''}")
    path = STATE_DIR / "digest.md"
    path.write_text("\n".join(lines) + "\n")
    log(f"weekly digest written to {path}")


# ---------------------------------------------------------------- desktop mode
#
# In desktop mode a scheduled task in the Claude or Codex desktop app opens a
# normal, visible session that runs `prepare`, does the task, then runs
# `finish`. The human can open that session at any time to steer it, or ask
# follow-ups in a side chat. One action per session.


def desktop_task_prompt() -> str:
    return f"""Prove2me agent mode (scheduled).

1. In {WORKSPACE}, run: python3 scripts/agent_mode/run.py prepare
2. If it prints a line starting with WAIT, reply with that line and stop.
3. Otherwise carry out the task it prints, following references/agent_mode.md.
   Your human may join this session to steer you; their instructions take priority.
4. When the task is done (result.json written), run: python3 scripts/agent_mode/run.py finish
   and reply with a two-line summary of what you did.
"""


def _reading_now(cfg: Dict[str, Any], led: Dict[str, Any], since: float = 0.0) -> Optional[budget.Reading]:
    if cfg["agent"]["provider"] == "claude":
        return budget.claude_probe(cfg["budget"].get("probe_model", "haiku")) or led.get("last_reading")
    return budget.codex_reading(since=since) or budget.codex_reading()


def finish(cfg: Dict[str, Any], led: Dict[str, Any], quiet: bool = False) -> int:
    pend = led.get("desktop_pending")
    if not pend:
        if not quiet:
            print("nothing to finish")
        return 0
    after = budget.fresh(_reading_now(cfg, led, pend["started"]))
    charged = budget.charge(led, pend.get("before"), after, 0.0)
    session = sessions.codex_session_since(pend["started"]) if cfg["agent"]["provider"] == "codex" else None
    entry = record_result(led, pend["action"], pend["target"], Path(pend["run_dir"]), charged, 0.0, 0,
                          session, mode="desktop")
    led["desktop_pending"] = None
    if hit_limit(after, "", 0):
        w = (after or {}).get("five_hour") or (after or {}).get("weekly")
        led["paused_until"] = (w or {}).get("resets_at")
    save_ledger(led)
    print(f"recorded {pend['action']} on {pend['target'].get('theorem_name')}: {entry['outcome']}; "
          f"charged {(charged.get('weekly') or 0):.2%} of your weekly window")
    return 0


def prepare(cfg: Dict[str, Any], led: Dict[str, Any], api: P2M, rng: random.Random, now_flag: bool) -> int:
    if led.get("desktop_pending"):
        log("previous desktop action never called finish; settling it now")
        finish(cfg, led, quiet=True)
    try:
        settle_submissions(api, led)
    except Exception as e:  # noqa: BLE001
        log(f"could not settle earlier submissions: {e}")
    reading = budget.fresh(_reading_now(cfg, led))
    for name, closed in budget.roll_windows(led, reading):
        if name == "weekly":
            write_digest(led, closed)
    ok, why = budget.check_go(cfg, led, reading, ignore_schedule=now_flag)
    if not ok:
        save_ledger(led)
        print("WAIT: " + "; ".join(why))
        return 0
    action, target, trace = pick(cfg, led, api, rng)
    for t in trace:
        log("policy: " + t)
    if not target:
        save_ledger(led)
        print("WAIT: no viable target right now")
        return 0
    run_dir = STATE_DIR / "runs" / f"{dt.datetime.now():%Y%m%d-%H%M%S}-{action}"
    run_dir.mkdir(parents=True, exist_ok=True)
    prompt = build_prompt(action, target, run_dir)
    (run_dir / "prompt.md").write_text(prompt)
    led["desktop_pending"] = {"action": action, "target": target, "run_dir": str(run_dir),
                              "before": reading, "started": now()}
    save_ledger(led)
    print(prompt)
    print("When you are done, run: python3 scripts/agent_mode/run.py finish")
    return 0


# ---------------------------------------------------------------- main


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", nargs="?", choices=["prepare", "finish"],
                    help="desktop mode steps; omit for a headless run")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--now", action="store_true", help="ignore quiet hours")
    ap.add_argument("--seed", type=int)
    args = ap.parse_args()

    STATE_DIR.mkdir(parents=True, exist_ok=True)
    lock = open(STATE_DIR / "run.lock", "w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        log("another agent-mode run is in progress; exiting")
        return 0

    cfg, led = load_config(), load_ledger()
    rng = random.Random(args.seed)
    if args.step == "finish":
        return finish(cfg, led)
    api = P2M()
    if args.step == "prepare":
        return prepare(cfg, led, api, rng, args.now)
    run = {"started": now(), "dry_run": args.dry_run, "actions": 0, "stopped": None}

    try:
        settle_submissions(api, led)
    except Exception as e:  # noqa: BLE001
        log(f"could not settle earlier submissions: {e}")

    reading = budget.current_reading(cfg, led)
    for name, closed in budget.roll_windows(led, reading):
        if name == "weekly":
            write_digest(led, closed)
    ok, why = budget.check_go(cfg, led, reading, ignore_schedule=args.now)
    if not ok:
        log("not running: " + "; ".join(why))
        run["stopped"] = why
        led["runs"].append(run)
        save_ledger(led)
        return 0

    sv = skill_version()
    if api.server_version and sv and api.server_version != sv:
        log(f"warning: skill is {sv} but the platform is {api.server_version}; pull the workspace repo")

    run_spent = 0.0
    for i in range(int(cfg["schedule"]["max_actions_per_run"])):
        action, target, trace = pick(cfg, led, api, rng)
        for t in trace:
            log("policy: " + t)
        if not target:
            run["stopped"] = ["no viable target"]
            break
        run_dir = STATE_DIR / "runs" / f"{dt.datetime.now():%Y%m%d-%H%M%S}-{action}"
        run_dir.mkdir(parents=True, exist_ok=True)
        prompt = build_prompt(action, target, run_dir)
        (run_dir / "prompt.md").write_text(prompt)
        if args.dry_run:
            log(f"[dry-run] would run {action} on {target.get('theorem_name')} (score {target.get('score')})")
            led["actions"].append({"ts": now(), "action": action, "theorem_id": target["theorem_id"],
                                   "theorem_name": target.get("theorem_name"), "outcome": "dry_run",
                                   "score": target.get("score"), "run_dir": str(run_dir)})
            run["actions"] += 1
            save_ledger(led)
            continue

        log(f"running {action} on {target.get('theorem_name')} with {cfg['agent']['provider']}")
        before, after, usd, tail, code, session = run_agent(cfg, prompt, run_dir, led)
        charged = budget.charge(led, before, after, usd)
        run_spent += charged.get("weekly") or 0.0
        entry = record_result(led, action, target, run_dir, charged, usd, code, session)
        run["actions"] += 1
        log(f"{action}: {entry['outcome']} — weekly +{(charged.get('weekly') or 0):.2%}, "
            f"5-hour +{(charged.get('five_hour') or 0):.2%}, ${usd:.2f}")
        log("resume or side-chat:\n" + sessions.resume_hint(cfg["agent"]["provider"],
                                                           entry["session_id"], entry["transcript"]))
        if hit_limit(after, tail, code):
            w = (after or {}).get("five_hour") or (after or {}).get("weekly")
            led["paused_until"] = (w or {}).get("resets_at") or now() + 5 * 3600
            run["stopped"] = ["provider limit hit"]
            save_ledger(led)
            break
        save_ledger(led)
        ok, why = budget.check_go(cfg, led, led.get("last_reading"), run_spent, ignore_schedule=True)
        if not ok:
            run["stopped"] = why
            log("stopping: " + "; ".join(why))
            break
        time.sleep(5)

    run["ended"] = now()
    run["spent_weekly"] = run_spent
    led["runs"].append(run)
    save_ledger(led)
    return 0


if __name__ == "__main__":
    sys.exit(main())
