"""Budget accounting for agent mode.

Usage is measured as the share of the provider's own rate-limit windows that the
agent's runs consume:

* weekly window  (Codex `secondary`, Claude `seven_day`)
* 5-hour window  (Codex `primary`; not limited for Claude)

All quantities are fractions in [0, 1]. A window's id is its `resets_at`
timestamp; when it changes the window has rolled over and its spend resets.

    python3 scripts/agent_mode/budget.py status
    python3 scripts/agent_mode/budget.py probe     # claude: refresh the reading
"""
from __future__ import annotations

import datetime as dt
import glob
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import load_config, load_ledger, log, now, save_ledger  # noqa: E402

WINDOWS = ("weekly", "five_hour")
SAME_WINDOW_TOLERANCE_S = 900  # resets_at can jitter slightly between readings

Reading = Dict[str, Any]


# ---------------------------------------------------------------- readings


def _iso_to_epoch(ts: str) -> float:
    return dt.datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp()


def codex_reading(files: Optional[Iterable[str]] = None, since: float = 0.0) -> Optional[Reading]:
    """Latest Codex rate-limit record from ~/.codex/sessions rollouts.

    Codex logs `rate_limits` on token_count events; records for other limit ids
    (e.g. "premium") can carry nulls, so keep the latest non-null one.
    """
    if files is None:
        home = os.environ.get("CODEX_HOME", os.path.expanduser("~/.codex"))
        files = sorted(
            glob.glob(os.path.join(home, "sessions", "**", "rollout-*.jsonl"), recursive=True),
            key=os.path.getmtime,
        )[-15:]
    best: Optional[Reading] = None
    for f in files:
        try:
            if os.path.getmtime(f) < since:
                continue
            fh = open(f, encoding="utf-8")
        except OSError:
            continue
        with fh:
            for line in fh:
                if '"rate_limits"' not in line:
                    continue
                try:
                    d = json.loads(line)
                    rl = (d.get("payload") or {}).get("rate_limits") or {}
                except ValueError:
                    continue
                prim, sec = rl.get("primary"), rl.get("secondary")
                if not (prim or sec):
                    continue
                at = _iso_to_epoch(d["timestamp"])
                if best and at <= best["at"]:
                    continue
                best = {
                    "provider": "codex",
                    "at": at,
                    "plan": rl.get("plan_type"),
                    "weekly": _codex_window(sec),
                    "five_hour": _codex_window(prim),
                }
    return best


def _codex_window(w: Optional[Dict[str, Any]]) -> Optional[Dict[str, float]]:
    if not w or w.get("used_percent") is None:
        return None
    return {"used": float(w["used_percent"]) / 100.0, "resets_at": float(w["resets_at"])}


_CLAUDE_KEYS = {"seven_day": "weekly"}  # no 5-hour budget for Claude


def claude_readings_from_stream(lines: Iterable[str]) -> List[Reading]:
    """All usage readings in a `claude -p --output-format stream-json` log.

    Each `rate_limit_event` carries `rate_limit_info.unifiedWindows`, e.g.
    {"seven_day": {"utilization": 0.4, "resetsAt": 1794823200}}.
    """
    out: List[Reading] = []
    for line in lines:
        if "rate_limit_event" not in line:
            continue
        try:
            d = json.loads(line)
        except ValueError:
            continue
        if d.get("type") != "rate_limit_event":
            continue
        info = d.get("rate_limit_info") or {}
        r: Reading = {"provider": "claude", "at": now(), "weekly": None, "five_hour": None,
                      "status": info.get("status")}
        for key, w in (info.get("unifiedWindows") or {}).items():
            name = _CLAUDE_KEYS.get(key)
            if name and w and w.get("utilization") is not None:
                r[name] = {"used": float(w["utilization"]), "resets_at": float(w["resetsAt"])}
        # older payloads: single window described at the top level
        name = _CLAUDE_KEYS.get(info.get("rateLimitType", ""))
        if name and r[name] is None and info.get("utilization") is not None:
            r[name] = {"used": float(info["utilization"]), "resets_at": float(info["resetsAt"])}
        out.append(r)
    return out


def claude_probe(model: str = "haiku") -> Optional[Reading]:
    """Cheapest way to read Claude usage: a one-turn headless call."""
    with tempfile.TemporaryDirectory() as d:
        cmd = ["claude", "-p", "Reply with: ok", "--max-turns", "1",
               "--output-format", "stream-json", "--verbose"]
        if model:
            cmd += ["--model", model]
        try:
            p = subprocess.run(cmd, cwd=d, capture_output=True, text=True, timeout=180)
        except (OSError, subprocess.TimeoutExpired) as e:
            log(f"claude probe failed: {e}")
            return None
    rs = claude_readings_from_stream(p.stdout.splitlines())
    return rs[-1] if rs else None


def fresh(r: Optional[Reading]) -> Optional[Reading]:
    """Drop windows whose reset time has passed: their usage is no longer current."""
    if not r:
        return r
    out = dict(r)
    for name in WINDOWS:
        w = out.get(name)
        if w and w["resets_at"] <= now():
            out[name] = None
    return out


def current_reading(cfg: Dict[str, Any], led: Dict[str, Any], allow_probe: bool = True) -> Optional[Reading]:
    return fresh(_current_reading(cfg, led, allow_probe))


def _current_reading(cfg: Dict[str, Any], led: Dict[str, Any], allow_probe: bool) -> Optional[Reading]:
    provider = cfg["agent"]["provider"]
    max_age = 60 * float(cfg["budget"]["max_reading_age_min"])
    if provider == "codex":
        r = codex_reading()
        if r:
            return r
        # Codex logs nothing between sessions; fall back to our last reading
        return led.get("last_reading")
    last = led.get("last_reading")
    if last and last.get("provider") == "claude" and now() - last["at"] < max_age:
        return last
    if allow_probe:
        r = claude_probe(cfg["budget"].get("probe_model", "haiku"))
        if r:
            return r
    return last


# ---------------------------------------------------------------- accounting


def same_window(a: Optional[float], b: Optional[float]) -> bool:
    return a is not None and b is not None and abs(a - b) < SAME_WINDOW_TOLERANCE_S


def roll_windows(led: Dict[str, Any], reading: Optional[Reading]) -> List[Tuple[str, Dict[str, Any]]]:
    """Reset spend for any window whose resets_at changed. Returns the closed windows."""
    closed = []
    if not reading:
        return closed
    for name in WINDOWS:
        w = reading.get(name)
        lw = led["windows"][name]
        if not w:
            continue
        if lw["id"] is None:
            lw["id"] = w["resets_at"]
            continue
        elif not same_window(lw["id"], w["resets_at"]):
            # a reading from an *older* window (stale log) must not roll us back
            if w["resets_at"] < lw["id"]:
                continue
            closed.append((name, dict(lw)))
            led["windows"][name] = {"id": w["resets_at"], "spent": 0.0, "usd": 0.0}
    led["last_reading"] = reading
    return closed


def measure_delta(before: Optional[Reading], after: Optional[Reading], window: str) -> Optional[float]:
    b = (before or {}).get(window)
    a = (after or {}).get(window)
    if not a:
        return None
    if not b:
        return a["used"]  # previous window expired: count everything in the new one
    if same_window(b["resets_at"], a["resets_at"]):
        return max(0.0, a["used"] - b["used"])
    if a["resets_at"] > b["resets_at"]:
        return a["used"]  # window rolled over mid-action: count everything in the new one
    return None


def charge(led: Dict[str, Any], before: Optional[Reading], after: Optional[Reading],
           usd: float = 0.0) -> Dict[str, Optional[float]]:
    """Add one action's usage to the open windows. Returns what was charged.

    When a window's reading is missing (e.g. Claude did not report its 5-hour
    window) or too coarse to move, fall back to the USD cost scaled by the
    observed points-per-dollar for that window, so spend is never under-counted.
    """
    before, after = fresh(before), fresh(after)
    roll_windows(led, after)
    charged: Dict[str, Optional[float]] = {}
    cal = led.setdefault("calibration", {})
    for name in WINDOWS:
        d = measure_delta(before, after, name)
        c = cal.setdefault(name, {"usd": 0.0, "points": 0.0})
        if d is not None and usd > 0:
            c["usd"] += usd
            c["points"] += d
        ratio = c["points"] / c["usd"] if c["usd"] > 0 and c["points"] > 0 else None
        if ratio is not None and usd > 0:
            est = usd * ratio
            d = est if d is None else max(d, est)
        charged[name] = d
        if d:
            led["windows"][name]["spent"] += d
        led["windows"][name]["usd"] = led["windows"][name].get("usd", 0.0) + usd
    return charged


# ---------------------------------------------------------------- go / no-go


def _in_quiet_hours(spec: str) -> bool:
    if not spec:
        return False
    try:
        a, b = spec.split("-")
        ha, ma = map(int, a.split(":"))
        hb, mb = map(int, b.split(":"))
    except ValueError:
        log(f"config: bad quiet_hours '{spec}', ignoring")
        return False
    t = dt.datetime.now()
    cur = t.hour * 60 + t.minute
    start, end = ha * 60 + ma, hb * 60 + mb
    return start <= cur < end if start <= end else (cur >= start or cur < end)


def submissions_today(led: Dict[str, Any]) -> int:
    cutoff = now() - 86400
    return sum(len(a.get("submission_ids") or []) for a in led["actions"] if a.get("ts", 0) > cutoff)


def check_go(cfg: Dict[str, Any], led: Dict[str, Any], reading: Optional[Reading],
             run_spent: float = 0.0, ignore_schedule: bool = False) -> Tuple[bool, List[str]]:
    b, s = cfg["budget"], cfg["schedule"]
    why: List[str] = []
    pu = led.get("paused_until")
    if pu and now() < pu:
        why.append(f"paused until {_fmt(pu)}")
    if not ignore_schedule and _in_quiet_hours(s.get("quiet_hours", "")):
        why.append(f"inside quiet hours {s['quiet_hours']}")
    if reading is None:
        why.append("no usage reading available")
        return False, why
    w, f = led["windows"]["weekly"], led["windows"]["five_hour"]
    if w["spent"] >= b["weekly_fraction"]:
        why.append(f"weekly budget used ({w['spent']:.1%} of {b['weekly_fraction']:.0%}); "
                   f"resumes {_fmt(w['id'])}")
    if f["spent"] >= b["five_hour_fraction"]:
        why.append(f"5-hour budget used ({f['spent']:.1%} of {b['five_hour_fraction']:.0%}); "
                   f"resumes {_fmt(f['id'])}")
    rw, rf = reading.get("weekly"), reading.get("five_hour")
    if rw and rw["used"] >= b["reserve_ceiling"]:
        why.append(f"your weekly usage is {rw['used']:.0%} ≥ reserve ceiling {b['reserve_ceiling']:.0%}")
    if rf and rf["used"] >= b["five_hour_ceiling"]:
        why.append(f"your 5-hour usage is {rf['used']:.0%} ≥ ceiling {b['five_hour_ceiling']:.0%}")
    if run_spent >= b["per_run_cap"]:
        why.append(f"per-run cap reached ({run_spent:.1%})")
    if submissions_today(led) >= int(s["max_submissions_per_day"]):
        why.append("daily submission cap reached")
    return not why, why


def _fmt(ts: Optional[float]) -> str:
    if not ts:
        return "?"
    return dt.datetime.fromtimestamp(ts).strftime("%a %b %d %H:%M")


def status_text(cfg: Dict[str, Any], led: Dict[str, Any], reading: Optional[Reading]) -> str:
    b = cfg["budget"]
    lines = [f"provider: {cfg['agent']['provider']}"]
    n = 1 if cfg["agent"]["provider"] == "claude" else 2  # Claude has no 5-hour budget
    if reading:
        for name, label in (("weekly", "weekly"), ("five_hour", "5-hour"))[:n]:
            r = reading.get(name)
            lines.append(
                f"  your {label} usage: " + (f"{r['used']:.0%} (resets {_fmt(r['resets_at'])})" if r else "not reported")
            )
        lines.append(f"  reading taken {_fmt(reading['at'])}")
    else:
        lines.append("  no usage reading")
    for name, frac, label in (("weekly", b["weekly_fraction"], "weekly"),
                              ("five_hour", b["five_hour_fraction"], "5-hour"))[:n]:
        w = led["windows"][name]
        lines.append(f"agent {label} spend: {w['spent']:.2%} of {frac:.0%} budget"
                     f" (${w.get('usd', 0):.2f}; window resets {_fmt(w['id'])})")
    ok, why = check_go(cfg, led, reading)
    lines.append("next run: " + ("GO" if ok else "WAIT — " + "; ".join(why)))
    return "\n".join(lines)


def main(argv: List[str]) -> int:
    cfg, led = load_config(), load_ledger()
    cmd = argv[0] if argv else "status"
    if cmd == "probe":
        r = claude_probe(cfg["budget"].get("probe_model", "haiku")) if cfg["agent"]["provider"] == "claude" else codex_reading()
        print(json.dumps(r, indent=1))
        if r:
            roll_windows(led, r)
            save_ledger(led)
        return 0
    if cmd == "status":
        r = current_reading(cfg, led, allow_probe=False)
        roll_windows(led, r)
        save_ledger(led)
        print(status_text(cfg, led, r))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
