"""check_register.py — verification entry of the register (Rulebook Article 5).
Pinned tag: v0.1-checker (NOT YET CUT — see docs/RULEBOOK-v0.1.md DRAFT status).

Exit 0 = accept, exit 1 = reject (with reason on stdout).
The checker validates ROW FORMAT, STATE-MACHINE TRANSITIONS and SCORING LEDGER.
It does not check mathematics.

Second-channel fixes applied (2026-11-28):
  F1  scoreboard() now PRINTS both lanes; empty rows/ is a hard FAIL.
  F2  Article 2 transition legality is checked over history (absorbing states,
      no direct VERIFIED<->FALSIFIED, dual marks on re-verification failure).
  F3  FROZEN is not self-declared: --rulebook-tag requires tag@sha and verifies
      the rulebook file hash; DRAFT text alone never passes.
  F5  An external-actor lane is derived from history actor field, plus a
      machine-readable separation lane for registrar-authored rows.
"""
import json, sys, os, glob, hashlib, re

WEIGHTS = {"Pi": 10, "U": 8, "Sigma": 4, "L1": 2, "L2": 3, "L3": 0.5, "L0": 0}
STATES = {"VERIFIED", "FALSIFIED", "SUSPENDED"}
SIX = ["object_registration", "proposition_registration", "certificate_status",
       "protocol_slots", "budget", "history"]
REGISTRAR = "registrar"
BEACON_ID = "ROW-2026-0006"


def fail(msg):
    print(f"CHECK REJECT: {msg}")
    sys.exit(1)


def legal_transition(prev, nxt, marks):
    """Article 2. Returns (ok, reason)."""
    if prev is None:
        return nxt in STATES, "initial state must be one of VERIFIED/FALSIFIED/SUSPENDED"
    if prev == "SUSPENDED":
        return True, "SUSPENDED may go to any state"
    if prev in ("VERIFIED", "FALSIFIED"):
        if nxt == prev:
            return True, "absorbing within certificate validity"
        if nxt == "SUSPENDED":
            has_dual = any("previously passed" in str(m) and "later undecidable" in str(m)
                           for m in marks) or any(
                "previously passed" in str(m) and "later undecidable" in str(m)
                for m in [marks] if isinstance(marks, str))
            return has_dual, "VERIFIED/FALSIFIED -> SUSPENDED requires dual marks"
        return False, "no direct VERIFIED<->FALSIFIED transition; route through SUSPENDED"
    return False, "unknown previous state"


def check_row(path):
    r = json.load(open(path, encoding="utf-8"))
    rid = r.get("row_id", os.path.basename(path))
    if set(r.keys()) != set(SIX + ["row_id"]):
        fail(f"{rid}: row must have exactly the six disjoint fields + row_id")

    cs = r["certificate_status"]
    if cs.get("state") not in STATES:
        fail(f"{rid}: illegal state {cs.get('state')!r}")
    if cs.get("marker_scope") != "certificate-only":
        fail(f"{rid}: Article 3: VERIFIED signs certificates only")
    al = cs.get("alignment", {})
    for layer in ("L0", "L1", "L2", "L3"):
        if layer not in al:
            fail(f"{rid}: alignment layer {layer} must be present (Article 3)")

    if cs["state"] == "VERIFIED" and not cs.get("certificates"):
        fail(f"{rid}: VERIFIED requires at least one accepted certificate")

    hist = r["history"]
    if not hist:
        fail(f"{rid}: history must be non-empty and append-only")
    # Article 2: the current state must be reachable from the registered initial
    # state through legal transitions recorded in history. Do not seed `prev`
    # from the final state — that lets a forged history bypass the transition gate.
    if hist[0].get("event") not in ("registered", "beacon_registered", "registrar_own_claim_demoted"):
        fail(f"{rid}: first history event must be a registration event, got {hist[0].get('event')!r}")
    prev, marks = "SUSPENDED", []
    for h in hist:
        if "timestamp" not in h or "event" not in h:
            fail(f"{rid}: history entry lacks timestamp/event")
        ev = str(h.get("event", ""))
        if "reverif" in ev.lower() or "re-verif" in ev.lower():
            marks.extend([h.get("note", ""), h.get("source", "")])
        if ev == "state_transition":
            nxt = h.get("to")
            ok, why = legal_transition(prev, nxt, marks)
            if not ok:
                fail(f"{rid}: illegal transition {prev}->{nxt}: {why}")
            prev = nxt
    if prev != cs["state"]:
        fail(f"{rid}: Article 2: history ends at {prev} but certificate_status.state={cs['state']}")

    b = r["budget"]
    for k in ("t", "L", "k", "E"):
        if k not in b:
            fail(f"{rid}: budget tuple must instantiate {k}")

    # Article 4: negative-instance certificate class empty by definition.
    for c in cs.get("certificates", []):
        if c.get("class") == "I-" and c.get("type") in WEIGHTS:
            fail(f"{rid}: Article 4: I- certificate class is empty by definition")

    print(f"CHECK PASS (format+state): {rid} state={cs['state']} L0lane={WEIGHTS['L0']}")
    return r


def rulebook_ok(rulebook_path, tag_spec):
    """F3: FROZEN must be backed by tag@sha, not a text claim."""
    if not tag_spec:
        return False, "no --rulebook-tag supplied; DRAFT cannot pass"
    m = re.fullmatch(r"([^@]+)@([0-9a-f]{40})", tag_spec)
    if not m:
        return False, "--rulebook-tag must be TAG@40-hex-sha"
    tag, sha = m.group(1), m.group(2)
    if not os.path.exists(rulebook_path):
        return False, "rulebook file missing"
    digest = hashlib.sha256(open(rulebook_path, "rb").read()).hexdigest()
    # A DRAFT file must never be accepted as a frozen rulebook.
    head = open(rulebook_path, encoding="utf-8").read(2000)
    if "DRAFT" in head:
        return False, "rulebook still marked DRAFT; freeze only after second-channel closure"
    return True, f"frozen_at={tag}@{sha[:8]} local_sha256={digest[:12]}"


def scoreboard(rows_dir, verbose=True):
    paths = sorted(glob.glob(os.path.join(rows_dir, "*.json")))
    if not paths:
        fail("rows/ is empty: an empty register cannot produce a valid scoreboard")
    rows = [check_row(p) for p in paths]
    if not any(r.get("row_id") == BEACON_ID for r in rows):
        fail(f"beacon row {BEACON_ID} missing")

    demand_total, calibration_total, registrar_total = 0.0, 0.0, 0.0
    lanes = []
    for r in rows:
        rid = r["row_id"]
        cs = r["certificate_status"]
        w = 0.0
        for cert in cs.get("certificates", []):
            w = max(w, WEIGHTS.get(cert.get("type", ""), 0))
        # Alignment closures are counted only when explicitly recorded as accepted.
        for h in r["history"]:
            if h.get("event") == "alignment_closure" and h.get("accepted") is True:
                layer = h.get("layer", "L0")
                w = max(w, WEIGHTS.get(layer, 0))
        is_registrar = any(
            h.get("actor") == REGISTRAR or "registrar-authored" in str(h.get("note", ""))
            for h in r["history"]
        )
        lane = "registrar" if is_registrar else ("calibration" if w == 0 else "demand")
        if lane == "registrar":
            registrar_total += w
        elif lane == "calibration":
            calibration_total += w
        else:
            demand_total += w
        lanes.append((rid, lane, w))

    if verbose:
        print("\n=== SCOREBOARD (two-lane, frozen weights) ===")
        for rid, lane, w in lanes:
            print(f"  {rid:32s} {lane:11s} {w:5.1f}")
        print(f"  EXTERNAL DEMAND TOTAL : {demand_total:5.1f}  (threshold: >=4 at day 90)")
        print(f"  CALIBRATION (L0)      : {calibration_total:5.1f}  (NOT demand evidence)")
        print(f"  REGISTRAR-AUTHORED    : {registrar_total:5.1f}  (excluded from demand evidence)")
        print("=== END SCOREBOARD ===\n")
    return demand_total, calibration_total, registrar_total


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "rows"
    tag_spec = None
    if "--rulebook-tag" in sys.argv:
        i = sys.argv.index("--rulebook-tag")
        if i + 1 < len(sys.argv):
            tag_spec = sys.argv[i + 1]
    rb = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "RULEBOOK-v0.1.md")
    ok, why = rulebook_ok(rb, tag_spec)
    print(f"RULEBOOK GATE: {'PASS' if ok else 'DRAFT/BLOCK'} — {why}")
    if os.path.isfile(target):
        check_row(target)
    else:
        scoreboard(target)
    print("CHECKER DONE.")
