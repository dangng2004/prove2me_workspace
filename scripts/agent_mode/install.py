"""Install, inspect, pause, or remove the agent-mode schedule.

    python3 scripts/agent_mode/install.py install [--headless|--desktop] [--dry-run] [--print]
    python3 scripts/agent_mode/install.py status
    python3 scripts/agent_mode/install.py sessions [-n 10]
    python3 scripts/agent_mode/install.py pause [--days N]
    python3 scripts/agent_mode/install.py resume
    python3 scripts/agent_mode/install.py uninstall

Two modes (agent.mode in the config; "auto" picks desktop when the app is installed):

* desktop: a scheduled task in the Claude or Codex desktop app. Each run is a
  visible session: open it to steer the agent live, or side-chat with it.
* headless: launchd (macOS) or cron (Linux) runs `claude -p` / `codex exec`.
  Each action's session id is logged; resume it or fork a side chat afterwards.

Either way each wake-up exits within seconds unless budget is left.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import platform
import plistlib
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import budget  # noqa: E402
import sessions  # noqa: E402
from run import desktop_task_prompt  # noqa: E402
from common import (CONFIG_PATH, EXAMPLE_CONFIG, STATE_DIR, load_config, load_ledger,  # noqa: E402
                    now, save_ledger)

LABEL = "me.prove2.agentmode"
PLIST = Path.home() / "Library" / "LaunchAgents" / f"{LABEL}.plist"
CRON_MARK = "# prove2me-agent-mode"
RUN_PY = Path(__file__).resolve().parent / "run.py"


def _python() -> str:
    return sys.executable or shutil.which("python3") or "python3"


def _env_path() -> str:
    # launchd/cron start with a bare PATH; keep the user's so claude/codex/lake resolve
    extra = [str(Path.home() / ".elan" / "bin"), str(Path.home() / ".local" / "bin")]
    parts = os.environ.get("PATH", "").split(os.pathsep)
    return os.pathsep.join(dict.fromkeys(parts + extra))


def _args(dry: bool) -> list:
    return [_python(), str(RUN_PY)] + (["--dry-run"] if dry else [])


def resolve_mode(cfg: dict, force: str = "") -> str:
    mode = force or cfg["agent"].get("mode", "auto")
    if mode == "auto":
        return "desktop" if sessions.desktop_app(cfg["agent"]["provider"]) else "headless"
    return mode


def install_desktop(cfg: dict, show_only: bool) -> int:
    provider = cfg["agent"]["provider"]
    app = sessions.desktop_app(provider) or ("the Claude app" if provider == "claude" else "the Codex app")
    prompt = desktop_task_prompt()
    path = STATE_DIR / "desktop_task.md"
    if not show_only:
        path.write_text(prompt)
    print(f"""Desktop mode ({app}).

Create a scheduled task in the app:
  folder:   {RUN_PY.parents[2]}
  repeat:   every {cfg['schedule']['every_hours']} hours
  prompt:   the text below (also saved to {path})

Each run opens as a normal session: open it to steer the agent, or use a side chat.
Pre-approve curl, lake and file edits for this folder so an unattended run doesn't stall
on a permission prompt. The app must be open for scheduled tasks to fire.

----- prompt -----
{prompt}------------------""")
    return 0


def install(dry: bool, show_only: bool, force_mode: str = "") -> int:
    cfg = load_config()
    mode = resolve_mode(cfg, force_mode)
    if mode == "desktop":
        if not CONFIG_PATH.exists() and not show_only:
            CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(EXAMPLE_CONFIG, CONFIG_PATH)
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        if dry:
            print("note: --dry-run applies to headless mode; for desktop, run `run.py --dry-run --now` by hand")
        return install_desktop(cfg, show_only)
    if not CONFIG_PATH.exists() and not show_only:
        CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(EXAMPLE_CONFIG, CONFIG_PATH)
        print(f"wrote default config to {CONFIG_PATH} (edit it to change budgets and weights)")
    for tool in (cfg["agent"]["provider"], "lake"):
        if not shutil.which(tool):
            print(f"warning: `{tool}` is not on PATH; agent runs will fail until it is")
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    interval = int(float(cfg["schedule"]["every_hours"]) * 3600)
    if platform.system() == "Darwin":
        plist = {
            "Label": LABEL,
            "ProgramArguments": _args(dry),
            "StartInterval": interval,
            "RunAtLoad": False,
            "WorkingDirectory": str(RUN_PY.parents[2]),
            "EnvironmentVariables": {"PATH": _env_path(), "HOME": str(Path.home())},
            "StandardOutPath": str(STATE_DIR / "scheduler.log"),
            "StandardErrorPath": str(STATE_DIR / "scheduler.log"),
            "ProcessType": "Background",
            "LowPriorityIO": True,
        }
        if show_only:
            sys.stdout.write(plistlib.dumps(plist).decode())
            return 0
        PLIST.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["launchctl", "bootout", f"gui/{os.getuid()}", str(PLIST)], capture_output=True)
        PLIST.write_bytes(plistlib.dumps(plist))
        r = subprocess.run(["launchctl", "bootstrap", f"gui/{os.getuid()}", str(PLIST)],
                           capture_output=True, text=True)
        if r.returncode:
            print(r.stderr.strip())
            return r.returncode
        print(f"installed launchd agent {LABEL}: every {cfg['schedule']['every_hours']}h"
              + (" (dry run)" if dry else ""))
        return 0
    hours = max(1, int(round(float(cfg["schedule"]["every_hours"]))))
    line = (f"0 */{hours} * * * PATH={_env_path()} {' '.join(_args(dry))} "
            f">> {STATE_DIR / 'scheduler.log'} 2>&1 {CRON_MARK}")
    if show_only:
        print(line)
        return 0
    cur = subprocess.run(["crontab", "-l"], capture_output=True, text=True).stdout
    keep = [ln for ln in cur.splitlines() if CRON_MARK not in ln]
    subprocess.run(["crontab", "-"], input="\n".join(keep + [line]) + "\n", text=True, check=True)
    print(f"installed crontab entry: every {hours}h" + (" (dry run)" if dry else ""))
    return 0


def uninstall() -> int:
    if platform.system() == "Darwin":
        subprocess.run(["launchctl", "bootout", f"gui/{os.getuid()}", str(PLIST)], capture_output=True)
        PLIST.unlink(missing_ok=True)
    else:
        cur = subprocess.run(["crontab", "-l"], capture_output=True, text=True).stdout
        keep = [ln for ln in cur.splitlines() if CRON_MARK not in ln]
        subprocess.run(["crontab", "-"], input="\n".join(keep) + "\n", text=True, check=True)
    print("agent mode schedule removed (config and ledger kept in ~/.prove2me)")
    print("in desktop mode, also delete the scheduled task in the Claude/Codex app")
    return 0


def installed() -> str:
    if platform.system() == "Darwin":
        if not PLIST.exists():
            return "not installed"
        r = subprocess.run(["launchctl", "print", f"gui/{os.getuid()}/{LABEL}"], capture_output=True)
        args = plistlib.loads(PLIST.read_bytes())["ProgramArguments"]
        return ("loaded" if r.returncode == 0 else "plist present but not loaded") + (
            " (dry run)" if "--dry-run" in args else "")
    cur = subprocess.run(["crontab", "-l"], capture_output=True, text=True).stdout
    line = next((ln for ln in cur.splitlines() if CRON_MARK in ln), None)
    return "not installed" if not line else "crontab entry present" + (" (dry run)" if "--dry-run" in line else "")


def status() -> int:
    cfg, led = load_config(), load_ledger()
    mode = resolve_mode(cfg)
    print(f"mode: {mode}" + (f" (headless schedule: {installed()})" if mode == "headless" else
                            " (scheduled task lives in the desktop app)"))
    if led.get("desktop_pending"):
        p = led["desktop_pending"]
        print(f"in progress: {p['action']} on {p['target'].get('theorem_name')}")
    r = budget.current_reading(cfg, led, allow_probe=False)
    budget.roll_windows(led, r)
    print(budget.status_text(cfg, led, r))
    c = led.get("credits", {})
    print(f"credits: {c.get('alternative_proofs', 0)} alternative proofs accepted, "
          f"{c.get('proofs', 0)} proofs, {c.get('sketches', 0)} sketches")
    print("recent actions:")
    for a in led["actions"][-8:]:
        when = dt.datetime.fromtimestamp(a["ts"]).strftime("%m-%d %H:%M")
        subs = ",".join(s[:8] for s in a.get("submission_ids") or [])
        print(f"  {when} {a['action']:<12} {a.get('outcome') or '':<9} {a.get('theorem_name')} {subs}")
    last = next((a for a in reversed(led["actions"]) if a.get("session_id")), None)
    if last:
        print(f"latest session ({last['action']} on {last.get('theorem_name')}):")
        print("  " + sessions.resume_hint(cfg["agent"]["provider"], last["session_id"],
                                          last.get("transcript")).replace("\n", "\n  "))
    save_ledger(led)
    return 0


def list_sessions(n: int) -> int:
    cfg, led = load_config(), load_ledger()
    rows = [a for a in led["actions"] if a.get("session_id")][-n:]
    if not rows:
        print("no sessions recorded yet")
    for a in rows:
        when = dt.datetime.fromtimestamp(a["ts"]).strftime("%m-%d %H:%M")
        print(f"{when} {a['action']} on {a.get('theorem_name')} — {a.get('outcome')}")
        print("  " + sessions.resume_hint(cfg["agent"]["provider"], a["session_id"],
                                          a.get("transcript")).replace("\n", "\n  "))
    return 0


def pause(days: float) -> int:
    led = load_ledger()
    led["paused_until"] = now() + days * 86400
    save_ledger(led)
    print(f"paused until {dt.datetime.fromtimestamp(led['paused_until']):%a %b %d %H:%M}")
    return 0


def resume() -> int:
    led = load_ledger()
    led["paused_until"] = None
    save_ledger(led)
    print("resumed; the next scheduled run will check the budget")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    i = sub.add_parser("install")
    i.add_argument("--dry-run", action="store_true", help="schedule dry runs (no agent, no submissions)")
    i.add_argument("--print", action="store_true", help="show what would be installed")
    g = i.add_mutually_exclusive_group()
    g.add_argument("--headless", action="store_const", const="headless", dest="mode")
    g.add_argument("--desktop", action="store_const", const="desktop", dest="mode")
    sv = sub.add_parser("sessions")
    sv.add_argument("-n", type=int, default=10)
    sub.add_parser("uninstall")
    sub.add_parser("status")
    p = sub.add_parser("pause")
    p.add_argument("--days", type=float, default=7)
    sub.add_parser("resume")
    a = ap.parse_args()
    if a.cmd == "install":
        return install(a.dry_run, a.print, a.mode or "")
    if a.cmd == "sessions":
        return list_sessions(a.n)
    return {"uninstall": uninstall, "status": status, "resume": resume}.get(a.cmd, lambda: pause(a.days))()


if __name__ == "__main__":
    sys.exit(main())
