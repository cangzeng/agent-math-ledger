# Release note — v0.2-rulebook

**Tag:** `v0.2-rulebook` → commit `545160707e7acc34c2fdd64da622721a055a739b`
**Tagged:** 2026-11-28
**Effective: 2026-12-05** (tag + 7 days)

## Article 5 cooling-off (single-registrar structural equivalent)

Article 5 requires a checker-code change to have a second account's merge PLUS a 7-day delay
before taking effect. Under a single-honest-party registrar, the structural equivalent is:

- tag now (2026-11-28) — the content is frozen and cannot be retroactively edited;
- **effective 2026-12-05** — the repaired lane definition governs scoring only from this date.

Between tag and effective date, the v0.1 defective reading and the v0.2 repaired reading are
both printed, as already disclosed in `docs/PROBE-VERDICT.md`. The early verdict (H confirmed at
t0+0d, external weighted closure 4.0 ≥ 4.0) does not depend on the repaired lane rule: the
closure itself is a fact in the merged PR; the v0.2 repair only makes the instrument report it
correctly. The threshold 4.0, t0, day-45 and day-90 are unchanged.

## What changed

Exactly one thing: lane assignment in `checker/check_register.py`. v0.1 assigned a row to the
registrar lane if ANY history entry had `actor=registrar` — every row carries the registrar's
registration entry, so no external closure of an existing row could ever enter the demand lane.
v0.2 assigns the lane by the actor of the CLOSURE EVENT. Article 9 of the FROZEN v0.1 text
already specified external-closure scoring; this repair returns the instrument to that spec.

Defect found and isolated in simulation by **zambodotdev**, 2026-11-28T01:05:01Z,
arc-open-governance/agent-consequence-challenge#6 comment 7231407899 — filed as a raw negative
result, with no request to change the frozen thresholds.

## What did not change

epsilon (4.0), t0 (2026-11-28T00:57:51Z), day-45 (2027-01-12), day-90 (2027-02-26),
the six-field row schema, the four certificate classes and weights (Π10/U8/Σ4),
and the single-honest-party trust ceiling declared in Article 10.

## Dual reading (permanent)

Both readings are printed on every checker run:

- v0.1 defective reading: ROW-2026-0006 booked as registrar-authored, EXTERNAL DEMAND TOTAL 0.0
- v0.2 repaired reading: ROW-2026-0006 booked as external demand, EXTERNAL DEMAND TOTAL 4.0

The defect stays in the record. No silent edit to the original case post.
