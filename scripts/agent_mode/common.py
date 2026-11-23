"""Shared helpers for Prove2Me agent mode: paths, config, ledger, API client.

Standard library only; runs on Python 3.9+.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, Optional

API_BASE = "https://prove2.me/api/v1"
WORKSPACE = Path(__file__).resolve().parents[2]
HOME_DIR = Path(os.environ.get("PROVE2ME_HOME", Path.home() / ".prove2me"))
STATE_DIR = HOME_DIR / "agent_mode"
CONFIG_PATH = HOME_DIR / "agent_mode.toml"
LEDGER_PATH = STATE_DIR / "ledger.json"
EXAMPLE_CONFIG = WORKSPACE / "agent_mode.example.toml"

# ---------------------------------------------------------------- config

DEFAULTS: Dict[str, Dict[str, Any]] = {
    "agent": {
        "provider": "claude",  # claude | codex
        "mode": "auto",  # auto (desktop app if installed, else headless) | desktop | headless
        "model": "",
        "max_turns": 80,
        "action_usd_cap": 5.0,  # claude only: --max-budget-usd per action
        "action_timeout_min": 60,
        "allowed_tools": [
            "Bash(curl:*)", "Bash(lake:*)", "Bash(python3:*)", "Bash(jq:*)",
            "Bash(mkdir:*)", "Bash(ls:*)", "Bash(cat:*)", "Bash(grep:*)",
            "Read", "Write", "Edit", "Glob", "Grep", "WebFetch", "WebSearch",
        ],
    },
    "budget": {
        "weekly_fraction": 0.10,
        "five_hour_fraction": 0.10,
        "per_run_cap": 0.02,
        "reserve_ceiling": 0.85,
        "five_hour_ceiling": 0.60,
        "probe_model": "haiku",  # claude: cheap call to read usage when no recent reading exists
        "max_reading_age_min": 30,
    },
    "schedule": {
        "every_hours": 3,
        "quiet_hours": "",  # e.g. "09:00-18:00": do not start runs in this window
        "max_actions_per_run": 4,
        "max_submissions_per_day": 10,
    },
    "actions": {
        "prove_open": 0.35,
        "reformalize": 0.30,
        "formalize_new": 0.10,
        "sketch": 0.10,
        "review": 0.10,
        "discuss": 0.05,
    },
    "targets": {
        "collections": ["oai-math"],
        "missions": [],
        "fields": [],
        "top_k": 8,
        "temperature": 1.0,
        "epsilon": 0.1,
        "retry_cooldown_days": 14,
        "pool_ttl_hours": 24,
    },
}


def _parse_toml_value(raw: str) -> Any:
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        return [_parse_toml_value(p) for p in _split_top(inner)]
    if raw.startswith('"') and raw.endswith('"'):
        return bytes(raw[1:-1], "utf-8").decode("unicode_escape")
    if raw.startswith("'") and raw.endswith("'"):
        return raw[1:-1]
    if raw in ("true", "false"):
        return raw == "true"
    try:
        return int(raw)
    except ValueError:
        return float(raw)


def _split_top(s: str) -> list:
    out, cur, q = [], "", None
    for ch in s:
        if q:
            cur += ch
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
            cur += ch
        elif ch == ",":
            if cur.strip():
                out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur)
    return out


def _strip_comment(line: str) -> str:
    q = None
    for i, ch in enumerate(line):
        if q:
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
        elif ch == "#":
            return line[:i]
    return line


def parse_toml(text: str) -> Dict[str, Any]:
    """Load TOML with tomllib when available; otherwise a minimal parser that
    covers this config (sections, scalars, single-line arrays)."""
    try:
        import tomllib  # type: ignore

        return tomllib.loads(text)
    except ImportError:
        pass
    data: Dict[str, Any] = {}
    section = data
    for line in text.splitlines():
        line = _strip_comment(line).strip()
        if not line:
            continue
        m = re.fullmatch(r"\[([A-Za-z0-9_.-]+)\]", line)
        if m:
            section = data.setdefault(m.group(1), {})
            continue
        key, _, val = line.partition("=")
        section[key.strip()] = _parse_toml_value(val)
    return data


def load_config(path: Optional[Path] = None) -> Dict[str, Dict[str, Any]]:
    path = path or CONFIG_PATH
    user: Dict[str, Any] = {}
    if path.exists():
        user = parse_toml(path.read_text())
    cfg: Dict[str, Dict[str, Any]] = {}
    for sec, vals in DEFAULTS.items():
        merged = dict(vals)
        merged.update(user.get(sec, {}))
        cfg[sec] = merged
    total = sum(max(0.0, float(v)) for v in cfg["actions"].values())
    if total <= 0:
        raise SystemExit("config: all action weights are 0")
    cfg["actions"] = {k: max(0.0, float(v)) / total for k, v in cfg["actions"].items()}
    if cfg["agent"]["provider"] not in ("claude", "codex"):
        raise SystemExit("config: agent.provider must be 'claude' or 'codex'")
    return cfg


# ---------------------------------------------------------------- ledger


def empty_ledger() -> Dict[str, Any]:
    return {
        "windows": {
            "weekly": {"id": None, "spent": 0.0, "usd": 0.0},
            "five_hour": {"id": None, "spent": 0.0, "usd": 0.0},
        },
        "last_reading": None,  # latest provider usage reading
        "paused_until": None,
        "runs": [],
        "actions": [],
        "attempted": {},  # theorem_id -> {"ts": ..., "action": ..., "outcome": ...}
        "calibration": {"usd": 0.0, "points": 0.0},
        "cache": {},
    }


def load_ledger() -> Dict[str, Any]:
    if LEDGER_PATH.exists():
        led = json.loads(LEDGER_PATH.read_text())
        base = empty_ledger()
        for k, v in base.items():
            led.setdefault(k, v)
        return led
    return empty_ledger()


def save_ledger(led: Dict[str, Any]) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    # keep the ledger bounded
    led["runs"] = led["runs"][-500:]
    led["actions"] = led["actions"][-2000:]
    tmp = LEDGER_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(led, indent=1, sort_keys=True))
    tmp.replace(LEDGER_PATH)


def now() -> float:
    return time.time()


def log(msg: str) -> None:
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{stamp}] {msg}", file=sys.stderr, flush=True)


# ---------------------------------------------------------------- API client


class P2M:
    """Minimal Prove2Me REST client using the workspace's credentials.json."""

    def __init__(self, workspace: Path = WORKSPACE):
        self.cred_path = workspace / "credentials.json"
        if not self.cred_path.exists():
            raise SystemExit(
                f"{self.cred_path} not found. Set up an API key first (references/setup.md)."
            )
        self.cred = json.loads(self.cred_path.read_text())
        self.server_version: Optional[str] = None

    def _token(self) -> str:
        exp = float(self.cred.get("expires_at") or 0)
        if self.cred.get("access_token") and exp - now() > 120:
            return self.cred["access_token"]
        if not self.cred.get("api_key"):
            raise SystemExit("credentials.json has no api_key")
        r = self._raw("POST", "/agent/refresh", {"api_key": self.cred["api_key"]}, auth=False)
        self.cred["access_token"] = r["access_token"]
        self.cred["expires_at"] = r.get("expires_at") or now() + 3600
        self.server_version = r.get("version")
        tmp = self.cred_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.cred, indent=1))
        os.chmod(tmp, 0o600)
        tmp.replace(self.cred_path)
        return self.cred["access_token"]

    def _raw(self, method: str, path: str, body: Any = None, auth: bool = True,
             params: Optional[Dict[str, Any]] = None) -> Any:
        url = API_BASE + path
        if params:
            url += "?" + urllib.parse.urlencode(
                {k: v for k, v in params.items() if v is not None}, doseq=True
            )
        headers = {"Content-Type": "application/json", "User-Agent": "prove2me-agent-mode"}
        if auth:
            headers["Authorization"] = "Bearer " + self._token()
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(url, data=data, method=method, headers=headers)
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    raw = resp.read()
                    return json.loads(raw) if raw else None
            except urllib.error.HTTPError as e:
                if e.code in (429, 502, 503, 504) and attempt < 2:
                    time.sleep(5 * (attempt + 1))
                    continue
                raise
            except urllib.error.URLError:
                if attempt < 2:
                    time.sleep(5 * (attempt + 1))
                    continue
                raise

    def get(self, path: str, **params: Any) -> Any:
        return self._raw("GET", path, params=params)


def skill_version() -> Optional[str]:
    m = re.search(r'version:\s*"([^"]+)"', (WORKSPACE / "SKILL.md").read_text())
    return m.group(1) if m else None
