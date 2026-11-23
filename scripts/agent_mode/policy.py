"""Action and target selection for agent mode.

1. Draw an action from the configured weights (re-roll up to 5 times when the
   drawn action has no viable target, as in flamebird's proactive engine).
2. Build that action's candidate pool from the public API, score each candidate
   with a few cheap features, enrich the best ones with extra API calls, then
   sample one by softmax over the top K (with ε-uniform exploration).

    python3 scripts/agent_mode/policy.py [--action reformalize] [--seed 1]
"""
from __future__ import annotations

import argparse
import json
import math
import random
import sys
import urllib.error
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import P2M, load_config, load_ledger, log, now, save_ledger  # noqa: E402

PHASE1_ACTIONS = {"prove_open", "reformalize", "sketch", "review"}
FALLBACK_ACTION = "prove_open"
MAX_REROLLS = 5
ACCEPTED = "ACCEPTED,SKETCH_ACCEPTED"
FAILED = "FAILED,CE,WA,ERROR"

Candidate = Dict[str, Any]


# ---------------------------------------------------------------- cached fetches


class Source:
    """API reads with a TTL cache stored in the ledger."""

    def __init__(self, api: P2M, led: Dict[str, Any], cfg: Dict[str, Any]):
        self.api, self.led, self.cfg = api, led, cfg
        self.ttl = 3600 * float(cfg["targets"]["pool_ttl_hours"])
        self.calls = 0

    def cached(self, key: str, fetch: Callable[[], Any], ttl: Optional[float] = None) -> Any:
        cache = self.led.setdefault("cache", {})
        hit = cache.get(key)
        ttl = self.ttl if ttl is None else ttl
        if hit and hit.get("failed"):
            ttl = 600  # retry failed reads after 10 minutes
        if hit and now() - hit["ts"] < ttl:
            return hit["data"]
        self.calls += 1
        try:
            data, failed = fetch(), False
        except (urllib.error.URLError, OSError, ValueError) as e:
            log(f"read {key} failed: {e}")
            data, failed = None, True
        cache[key] = {"ts": now(), "data": data, "failed": failed}
        return data

    # collections / missions ---------------------------------------------

    def collection_missions(self, slug: str) -> List[Dict[str, Any]]:
        def fetch() -> List[Dict[str, Any]]:
            out, off = [], 0
            while True:
                r = self.api.get(f"/collections/{slug}/missions", limit=100, offset=off)
                rows = r.get("missions", [])
                out += [{"id": x["mission_id"], "name": (x.get("missions") or {}).get("name")} for x in rows]
                off += len(rows)
                if not rows or off >= r.get("total", 0):
                    return out
        return self.cached(f"collection:{slug}", fetch) or []

    def mission(self, mission_id: str, name: Optional[str]) -> Optional[Dict[str, Any]]:
        """Full mission row (with main_theorem). There is no GET /missions/:id, so search by name."""
        def fetch() -> Optional[Dict[str, Any]]:
            if not name:
                return None
            r = self.api.get("/missions", q=name[:160], limit=10)
            for m in r.get("missions", []):
                if m["id"] == mission_id:
                    return _slim_mission(m)
            return None
        return self.cached(f"mission:{mission_id}", fetch, ttl=3 * 86400)

    def featured_missions(self) -> List[Dict[str, Any]]:
        r = self.cached("missions:first_page", lambda: self.api.get("/missions", limit=100))
        return [_slim_mission(m) for m in (r or {}).get("missions", [])]

    def named_missions(self, names: List[str]) -> List[Dict[str, Any]]:
        out = []
        for n in names:
            r = self.cached(f"missions:q:{n}", lambda n=n: self.api.get("/missions", q=n[:160], limit=1))
            out += [_slim_mission(m) for m in (r or {}).get("missions", [])[:1]]
        return out

    def milestones(self, mission_id: str) -> List[Dict[str, Any]]:
        r = self.cached(f"milestones:{mission_id}",
                        lambda: self.api.get(f"/missions/{mission_id}/milestones", limit=100))
        return (r or {}).get("milestones", [])

    # theorems ------------------------------------------------------------

    def open_leaves(self, theorem_id: str) -> List[Dict[str, Any]]:
        r = self.cached(f"leaves:{theorem_id}",
                        lambda: self.api.get(f"/theorems/{theorem_id}/open-leaves", limit=15), ttl=6 * 3600)
        return (r or {}).get("open_leaves", [])

    def theorem(self, theorem_id: str) -> Optional[Dict[str, Any]]:
        def fetch() -> Dict[str, Any]:
            t = self.api.get(f"/theorems/{theorem_id}")
            return {k: t.get(k) for k in ("theorem_id", "theorem_name", "theorem_title", "status",
                                          "vote_count", "source", "tags", "audits", "deprecated_at")} | {
                "has_nl": bool(t.get("natural_language_statement"))}
        return self.cached(f"theorem:{theorem_id}", fetch)

    def submissions(self, theorem_id: str, status: str) -> Dict[str, Any]:
        def fetch() -> Dict[str, Any]:
            r = self.api.get(f"/theorems/{theorem_id}/submissions", status=status, limit=20)
            subs = r.get("submissions", [])
            return {"total": r.get("total", len(subs)),
                    "ids": [s["id"] for s in subs],
                    "users": [s.get("username") for s in subs]}
        return self.cached(f"subs:{status}:{theorem_id}", fetch) or {"total": 0, "ids": [], "users": []}

    def solution_lines(self, submission_id: str) -> int:
        r = self.cached(f"solution_len:{submission_id}",
                        lambda: {"lines": self.api.get(f"/submissions/{submission_id}/solution")
                                 .get("content", "").count("\n") + 1}, ttl=30 * 86400)
        return int((r or {}).get("lines", 0))

    def proved_by_votes(self) -> List[Dict[str, Any]]:
        r = self.cached("theorems:proved:votes",
                        lambda: self.api.get("/theorems", status="Proved", sort="votes", limit=100))
        return (r or {}).get("theorems", [])


# Python 3.9 has no dict | dict on all builds we care about; keep a helper.
def _merge(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    out = dict(a)
    out.update(b)
    return out


def _slim_mission(m: Dict[str, Any]) -> Dict[str, Any]:
    mt = m.get("main_theorem") or {}
    return {
        "id": m["id"],
        "name": m.get("name"),
        "fields": [f.get("slug") for f in m.get("fields") or []],
        "main_theorem_id": mt.get("theorem_id"),
        "main_theorem_name": mt.get("theorem_name"),
        "main_status": mt.get("status"),
        "main_has_nl": bool(mt.get("natural_language_statement")),
        "deprecated": bool(mt.get("deprecated_at")),
    }


# ---------------------------------------------------------------- pools


def preferred_missions(src: Source, rng: random.Random, want: str, k: int = 12) -> List[Dict[str, Any]]:
    """Missions from the user's preferred collections/missions, filtered by goal status.

    want: "open" or "completed". Resolves mission rows lazily (one search per
    mission, cached for days), sampling at most k unresolved missions per call.
    """
    t = src.cfg["targets"]
    rows: List[Dict[str, Any]] = []
    rows += src.named_missions(list(t.get("missions") or []))
    stubs: List[Dict[str, Any]] = []
    for slug in t.get("collections") or []:
        stubs += [_merge(s, {"collection": slug}) for s in src.collection_missions(slug)]
    rng.shuffle(stubs)
    resolved = 0
    for s in stubs:
        key = f"mission:{s['id']}"
        if key not in src.led["cache"]:
            if resolved >= k:
                continue
            resolved += 1
        m = src.mission(s["id"], s["name"])
        if m:
            rows.append(_merge(m, {"collection": s["collection"]}))
    if not rows:
        rows = src.featured_missions()
    done = {"Proved", "Disproved"}
    keep = [m for m in rows if m.get("main_theorem_id") and not m.get("deprecated")]
    if want == "open":
        open_ = [m for m in keep if m.get("main_status") not in done]
        if len(open_) < 5:  # preferred collections nearly finished: widen to featured missions
            seen = {m["id"] for m in open_}
            open_ += [m for m in src.featured_missions() if m["id"] not in seen
                      and m.get("main_theorem_id") and m.get("main_status") not in done]
        return open_
    return [m for m in keep if m.get("main_status") == "Proved"]


def recently_attempted(led: Dict[str, Any], cfg: Dict[str, Any]) -> set:
    cutoff = now() - 86400 * float(cfg["targets"]["retry_cooldown_days"])
    return {tid for tid, a in led.get("attempted", {}).items() if a.get("ts", 0) > cutoff}


def flagged(th: Optional[Dict[str, Any]]) -> bool:
    return bool(th) and any(a.get("decision") == "flag" for a in th.get("audits") or [])


def pool_open(src: Source, rng: random.Random, sketch: bool) -> List[Candidate]:
    fields = set(src.cfg["targets"].get("fields") or [])
    skip = recently_attempted(src.led, src.cfg)
    missions = preferred_missions(src, rng, "open")
    rng.shuffle(missions)
    cands: List[Candidate] = []
    for m in missions[:10]:
        ms_ids = {(x.get("theorem") or {}).get("id") for x in src.milestones(m["id"]) if not x.get("completed")}
        for leaf in src.open_leaves(m["main_theorem_id"]):
            if leaf["theorem_id"] in skip:
                continue
            cands.append({
                "theorem_id": leaf["theorem_id"], "theorem_name": leaf.get("theorem_name"),
                "mission_id": m["id"], "mission_name": m["name"],
                "f": {"closability": leaf.get("closability", 0),
                      "milestone": leaf["theorem_id"] in ms_ids,
                      "pref_field": bool(fields & set(m.get("fields") or [])),
                      "preferred": "collection" in m},
            })

    def cheap(c: Candidate) -> float:
        f = c["f"]
        if sketch:
            return (1.0 * f["milestone"] + 0.3 * f["pref_field"] + 0.7 * f["preferred"]
                    - 0.3 * math.log1p(f["closability"]))
        return (1.0 * math.log1p(f["closability"]) + 1.0 * f["milestone"] + 0.5 * f["pref_field"]
                + 0.7 * f["preferred"])

    def enrich(c: Candidate) -> Optional[float]:
        th = src.theorem(c["theorem_id"])
        if not th or th.get("status") != "Open" or th.get("deprecated_at") or flagged(th):
            return None
        failed = src.submissions(c["theorem_id"], FAILED)["total"]
        c["f"]["failed_attempts"] = failed
        c["f"]["votes"] = th.get("vote_count") or 0
        base = cheap(c) + 0.2 * math.log1p(max(0, c["f"]["votes"]))
        # many failures: a poor fit for a direct attempt, a good fit for decomposition
        return base + (0.5 if sketch else -0.4) * math.log1p(failed)

    return rank(cands, cheap, enrich, src.cfg)


def pool_reformalize(src: Source, rng: random.Random) -> List[Candidate]:
    skip = recently_attempted(src.led, src.cfg)
    cands: Dict[str, Candidate] = {}
    missions = preferred_missions(src, rng, "completed")
    for m in missions:
        cands[m["main_theorem_id"]] = {
            "theorem_id": m["main_theorem_id"], "theorem_name": m.get("main_theorem_name"),
            "mission_id": m["id"], "mission_name": m["name"],
            "f": {"preferred": True, "has_nl": m.get("main_has_nl", False)},
        }
    for t in src.proved_by_votes():
        cands.setdefault(t["theorem_id"], {
            "theorem_id": t["theorem_id"], "theorem_name": t.get("theorem_name"),
            "f": {"preferred": False, "votes": t.get("vote_count") or 0,
                  "has_nl": bool(t.get("natural_language_statement"))},
        })
    # Completed milestones are fair game: agent mode overrides missions.md's
    # "do not re-formalize or re-prove" rule for tagged alternative formalizations.
    rng.shuffle(missions)
    for m in missions[:10]:
        for x in src.milestones(m["id"]):
            th = x.get("theorem") or {}
            if x.get("completed") and th.get("id"):
                cands.setdefault(th["id"], {
                    "theorem_id": th["id"], "theorem_name": th.get("theorem_name"),
                    "mission_id": m["id"], "mission_name": m["name"],
                    "f": {"preferred": True, "has_nl": True, "milestone": True},
                })
    pool = [c for tid, c in cands.items() if tid not in skip]

    def cheap(c: Candidate) -> float:
        f = c["f"]
        return 1.0 * f["preferred"] + 0.5 * f["has_nl"] + 0.3 * math.log1p(f.get("votes", 0))

    me = src.led.get("me")

    def enrich(c: Candidate) -> Optional[float]:
        th = src.theorem(c["theorem_id"])
        if not th or th.get("status") != "Proved" or th.get("deprecated_at") or flagged(th):
            return None
        acc = src.submissions(c["theorem_id"], ACCEPTED)
        n = acc["total"]
        if n == 0 or (me and me in acc["users"]):
            return None  # nothing to compare against, or we already have a version
        lines = src.solution_lines(acc["ids"][-1]) if acc["ids"] else 0
        f = c["f"]
        f.update(accepted=n, votes=th.get("vote_count") or 0, proof_lines=lines,
                 has_source=bool(th.get("source")))
        c["existing_submission_ids"] = acc["ids"][:5]
        diversity = {1: 1.5, 2: 0.6}.get(n, 0.0)  # few versions → most to gain
        return (diversity + 1.0 * f["preferred"] + 0.5 * f["has_nl"] + 0.3 * f["has_source"]
                + 0.3 * f.get("milestone", False)  # canonical statement, captain-endorsed
                + 0.3 * math.log1p(f["votes"]) + 0.25 * math.log10(1 + lines))

    return rank(pool, cheap, enrich, src.cfg)


def pool_review(src: Source, rng: random.Random) -> List[Candidate]:
    """Proved theorems that already have ≥2 accepted versions (from the cache)."""
    skip = recently_attempted(src.led, src.cfg)
    cands = []
    for key, hit in list(src.led.get("cache", {}).items()):
        if not key.startswith(f"subs:{ACCEPTED}:") or not hit.get("data"):
            continue
        tid = key.split(":", 2)[2]
        if tid in skip or hit["data"]["total"] < 2:
            continue
        cands.append({"theorem_id": tid, "existing_submission_ids": hit["data"]["ids"][:5],
                      "f": {"accepted": hit["data"]["total"]}})
    for tid, a in src.led.get("attempted", {}).items():
        if a.get("action") == "reformalize" and a.get("outcome") == "submitted" and tid not in skip:
            cands.append({"theorem_id": tid, "f": {"accepted": 2, "mine": True}})

    def cheap(c: Candidate) -> float:
        return math.log(c["f"]["accepted"]) + 0.5 * c["f"].get("mine", False)

    def enrich(c: Candidate) -> Optional[float]:
        th = src.theorem(c["theorem_id"])
        if not th:
            return None
        c["theorem_name"] = th.get("theorem_name")
        c["f"]["votes"] = th.get("vote_count") or 0
        return cheap(c) - 0.2 * math.log1p(c["f"]["votes"])  # fewer votes → more useful review

    return rank(cands, cheap, enrich, src.cfg)


def rank(cands: List[Candidate], cheap: Callable[[Candidate], float],
         enrich: Callable[[Candidate], Optional[float]], cfg: Dict[str, Any]) -> List[Candidate]:
    """Cheap pre-score → enrich the top 3K → return the finalists sorted by score."""
    k = int(cfg["targets"]["top_k"])
    cands = sorted(cands, key=cheap, reverse=True)[: 3 * k]
    out = []
    for c in cands:
        s = enrich(c)
        if s is not None:
            c["score"] = round(s, 3)
            out.append(c)
    return sorted(out, key=lambda c: c["score"], reverse=True)


POOLS: Dict[str, Callable[[Source, random.Random], List[Candidate]]] = {
    "prove_open": lambda s, r: pool_open(s, r, sketch=False),
    "sketch": lambda s, r: pool_open(s, r, sketch=True),
    "reformalize": pool_reformalize,
    "review": pool_review,
    # Phase 2+: formalize_new (needs a paper index), discuss (follow-ups on our own work)
}


# ---------------------------------------------------------------- sampling


def sample_target(cands: List[Candidate], cfg: Dict[str, Any], rng: random.Random) -> Optional[Candidate]:
    if not cands:
        return None
    t = cfg["targets"]
    if rng.random() < float(t["epsilon"]):
        return rng.choice(cands)
    top = cands[: int(t["top_k"])]
    temp = max(1e-6, float(t["temperature"]))
    mx = max(c["score"] for c in top)
    ws = [math.exp((c["score"] - mx) / temp) for c in top]
    return rng.choices(top, weights=ws)[0]


def pick(cfg: Dict[str, Any], led: Dict[str, Any], api: P2M, rng: random.Random,
         force_action: Optional[str] = None) -> Tuple[Optional[str], Optional[Candidate], List[str]]:
    """Returns (action, target, trace). target is None only if nothing is viable."""
    src = Source(api, led, cfg)
    if "me" not in led:
        try:
            led["me"] = api.get("/me").get("username")
        except Exception:  # noqa: BLE001
            led["me"] = None
    weights = {a: w for a, w in cfg["actions"].items() if a in POOLS and w > 0}
    trace: List[str] = []
    pools: Dict[str, List[Candidate]] = {}
    for i in range(1 if force_action else MAX_REROLLS + 1):
        if force_action:
            a = force_action
        elif weights:
            a = rng.choices(list(weights), weights=list(weights.values()))[0]
        elif FALLBACK_ACTION not in pools:
            a = FALLBACK_ACTION
        else:
            break
        if a not in pools:
            pools[a] = POOLS[a](src, rng)
        tgt = sample_target(pools[a], cfg, rng)
        trace.append(f"{a}: {len(pools[a])} candidates" + (f" → {tgt['theorem_name']} ({tgt['score']})" if tgt else ""))
        if tgt:
            return a, tgt, trace
        weights.pop(a, None)  # re-roll among the actions not yet found empty
    return None, None, trace


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--action", choices=sorted(POOLS))
    ap.add_argument("--seed", type=int)
    args = ap.parse_args()
    cfg, led = load_config(), load_ledger()
    api = P2M()
    action, tgt, trace = pick(cfg, led, api, random.Random(args.seed), args.action)
    save_ledger(led)
    print("\n".join(trace))
    print(json.dumps({"action": action, "target": tgt}, indent=1, ensure_ascii=False))
    return 0 if tgt else 1


if __name__ == "__main__":
    sys.exit(main())
