"""Find agent sessions after the fact, so a human can resume or side-chat with them.

Every agent-mode action runs as an ordinary Claude Code or Codex session. Its
transcript stays on disk, so you can

* resume it:            claude --resume <id>   /  codex resume <id>
* branch a side chat:   claude --resume <id> --fork-session
* or point any other session at the transcript file and ask about it.
"""
from __future__ import annotations

import glob
import json
import os
import platform
import plistlib
import re
import shutil
import subprocess
from pathlib import Path
from typing import Dict, Optional

from common import WORKSPACE

UUID = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"


def claude_session_id(stream_text: str) -> Optional[str]:
    for line in stream_text.splitlines():
        if '"session_id"' in line:
            try:
                sid = json.loads(line).get("session_id")
            except ValueError:
                continue
            if sid:
                return sid
    return None


def claude_transcript(session_id: str) -> Optional[str]:
    hits = glob.glob(os.path.expanduser(f"~/.claude/projects/*/{session_id}.jsonl"))
    return hits[0] if hits else None


def codex_session_since(t: float) -> Dict[str, Optional[str]]:
    """The Codex rollout created at or after t (the action's own session)."""
    home = os.environ.get("CODEX_HOME", os.path.expanduser("~/.codex"))
    files = [f for f in glob.glob(os.path.join(home, "sessions", "**", "rollout-*.jsonl"), recursive=True)
             if os.path.getctime(f) >= t - 5]
    if not files:
        return {"session_id": None, "transcript": None}
    f = min(files, key=os.path.getctime)
    m = re.search(f"({UUID})\\.jsonl$", f)
    return {"session_id": m.group(1) if m else None, "transcript": f}


def resume_hint(provider: str, session_id: Optional[str], transcript: Optional[str]) -> str:
    if not session_id:
        return "no session id recorded"
    if provider == "claude":
        return (f"cd {WORKSPACE} && claude --resume {session_id}            # continue it\n"
                f"cd {WORKSPACE} && claude --resume {session_id} --fork-session   # side chat\n"
                f"transcript: {transcript or '?'}")
    return (f"codex resume {session_id}            # continue it\n"
            f"transcript: {transcript or '?'}")


# ---------------------------------------------------------------- desktop apps

BUNDLE_IDS = {"claude": "com.anthropic.claudefordesktop", "codex": "com.openai.codex"}
APP_PATHS = {"claude": ["Claude.app"], "codex": ["Codex.app", "ChatGPT.app"]}


def desktop_app(provider: str) -> Optional[str]:
    """Path of the provider's desktop app on macOS, or None."""
    if platform.system() != "Darwin":
        return None
    if shutil.which("mdfind"):
        try:
            out = subprocess.run(["mdfind", f'kMDItemCFBundleIdentifier == "{BUNDLE_IDS[provider]}"'],
                                 capture_output=True, text=True, timeout=10).stdout.split("\n")
            hit = next((p for p in out if p.endswith(".app")), None)
            if hit:
                return hit
        except (OSError, subprocess.TimeoutExpired):
            pass
    for base in ("/Applications", str(Path.home() / "Applications")):
        for name in APP_PATHS[provider]:
            p = Path(base) / name / "Contents" / "Info.plist"
            try:
                if plistlib.loads(p.read_bytes()).get("CFBundleIdentifier") == BUNDLE_IDS[provider]:
                    return str(p.parents[1])
            except (OSError, ValueError):
                continue
    return None
