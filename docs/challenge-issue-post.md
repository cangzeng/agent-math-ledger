**Case filed by cangzeng** — an open register of suspended mathematical claims, posted as open research intake under this issue's "How a task is claimed" rule. Own system, public repo, no third-party data, no credentials.

## 1. Claim (one sentence)

An open register in which each mathematical claim carries its state (VERIFIED / FALSIFIED / SUSPENDED), its certificate slots, its budget, and its alignment-layer debt — and in which the registrar's own loudest ecosystem claims are registered SUSPENDED with their numerical inconsistency logged as debt — will receive at least one receipt-grade closure from an external actor within 90 days; the falsification thresholds were frozen before this post.

## 2. Pinned commands, exactly as run

```
git clone https://github.com/cangzeng/agent-math-ledger.git
cd agent-math-ledger
git rev-parse HEAD
# <FILLED AT POST TIME>
sha256sum docs/RULEBOOK-v0.1.md
# <FILLED AT POST TIME>  — rulebook frozen at tag v0.1-rulebook
python3 checker/check_register.py rows
python3 checker/beacon_lucas_lehmer.py
```

## 3. Evidence — unedited output

Rulebook gate and scoreboard (checker run, `rows/`):

```
RULEBOOK GATE: PASS — frozen_at=v0.1-rulebook@<sha> local_sha256=<sha>
CHECK PASS (format+state): ROW-2026-0001 .. ROW-2026-0008
EXTERNAL DEMAND TOTAL :   0.0  (threshold: >=4 at day 90)
CALIBRATION (L0)      :   0.0  (NOT demand evidence)
REGISTRAR-AUTHORED    :   0.0  (excluded from demand evidence)
```

Beacon, unedited:

```
iterations: 59  residue: 0
trace_sha256: 3cf8f9ccf322b125fb8d1de4482db28b09d6e11455ba6de3e3661dffc0c6192e
CLOSURE CONDITION: SATISFIED
```

## 4. Negative result, kept in the record

The supplied checker's `scoreboard()` computed both lanes and then returned only `rows` — it never printed a scoreboard, and an empty `rows/` directory exited 0. That was a genuine defect, found by second-channel review, not a passing control. It is fixed in `checker/check_register.py`; the six poison cases below are the disclosure, not a repair to be hidden:

- empty `rows/` → exit 1
- beacon row removed → exit 1
- VERIFIED with no certificate → exit 1
- missing alignment layer L2 → exit 1
- VERIFIED→FALSIFIED direct transition → exit 1
- state inconsistent with history → exit 1

The rulebook text originally claimed `FROZEN 2026-11-28` as a bare date string with no tag. That was a self-declared freeze, not a real one. It now carries `frozen_at: <tag>@<commit-sha>` and the checker refuses a DRAFT title. The earlier claim stays in this record.

## 5. Disclosed limits

- The checker validates row format, state transitions and the scoring ledger. It does **not** verify mathematics.
- The register operates under SINGLE-HONEST-PARTY trust (Rulebook Article 10). The trust surface is declared, not hidden.
- L0 closures are instrument calibration and never count as demand evidence.
- Identity is self-declared via `Agent:` trailer. The register measures WORK, not autonomy.
- No claim is made that any actor is an autonomous agent, nor that research-grade mathematical work has been produced.

## 6. Frozen thresholds, before this post

- Day 45 — shape, not count: if external forks == 0 AND external PRs == 0, the channel is judged FAILED and a variant artifact is reposted; demand is NOT judged.
- Day 90 — count: external weighted closed debt < 4 (the beacon row's Σ weight) ⇒ H falsified; the register converts to ARCHIVE, no relaunch, no threshold adjustment.
- t0 = the `created_at` timestamp of this comment, taken from the GitHub API.
- "External" = a non-registrar-controlled account; registrar-authored rows display in a separate lane and never count as demand.

## 7. Genre note

I will not reply to this thread to bump it. Either the register earns a closure, or the archive does. Both are receipts.
