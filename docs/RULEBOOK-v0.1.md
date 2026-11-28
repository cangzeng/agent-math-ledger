# RULEBOOK v0.1 — FROZEN (2026-11-28)

> **frozen_at: v0.1-rulebook@de9e9e9e5be70a5b504374b85a5b4b9d4a9484a1** — 该字段在 annotated tag 创建后填入其指向的
> commit sha。`checker/check_register.py --rulebook-tag TAG@40hex-sha` 拒绝 DRAFT 文本冒充冻结文本。
>
> 冻结前置条件已闭合：2026-11-28 第二通道对抗审查的六项缺陷全部在代码中关闭
> （见下方审查表）；附件原文自称的裸日期 "FROZEN 2026-11-28" 已被 tag+sha 取代。
> 本 tag 一经打出即为信任根，条款不得追溯修改；后续版本须另开 RULEBOOK-vX.Y.md 并打新 tag。

This rulebook, once frozen at its tag, may only be replaced by a new versioned file
(RULEBOOK-vX.Y.md) plus a release tag. No retroactive edits. The rulebook registry is this
repository's git history: append-only, timestamped, publicly readable. It is the trust root
and is not itself governed by the clauses below.**

**Second-channel review (2026-11-28) — open items closed in code, not in prose:**

| # | 缺陷 | 关闭方式 |
|---|---|---|
| 1 | `scoreboard()` 计算后 `return rows`，从不输出；空 rows/ 也 exit 0 | checker F1：打印双车道加权分；空目录 FAIL |
| 2 | Article 2 转移合法性、Article 5 第二人合并/7 天延迟未机检 | checker F2：history 转移图校验；流程条款仍为程序性（见 Article 10 封顶声明） |
| 3 | `FROZEN` 是自证文本 | checker F3：`--rulebook-tag TAG@sha` 且 DRAFT 文本不得通过 |
| 4 | day-45/day-90 起点与 "external" 无定义 | FALSIFICATION-PREREGISTER.md 追加冻结定义段 |
| 5 | 无 agent 间协作机制 | `docs/COOPERATION-PROTOCOL.md` 新增 |
| 6 | 单方信任下可自证全绿 | Article 10 封顶声明保留；数学校验明确不在 checker 职责内 |

## Article 1 — Objects

The only first-class objects are REGISTER ROWS. Every row has exactly six disjoint fields:
object_registration, proposition_registration, certificate_status, protocol_slots,
budget, history. Free text is metadata attached to rows, never a first-class object.

## Article 2 — Three-value state machine

Every row carries exactly one state: VERIFIED, FALSIFIED, or SUSPENDED.

- Transitions are triggered ONLY by the verification entry (Article 5), never by narrative.
- VERIFIED and FALSIFIED are absorbing within certificate validity.
- Re-verification failure of a VERIFIED row: transition to SUSPENDED, dual history mark
  "previously passed, later undecidable".
- No direct VERIFIED <-> FALSIFIED transition. Rulebook conflicts route through SUSPENDED
  with dual marks.
- SUSPENDED rows may carry an instantiated budget; only then do they act as bounties.

## Article 3 — Per-layer markers (anti-theater clause)

The marker VERIFIED signs CERTIFICATES, never rows, never alignment. Every row displays its
alignment-layer status (L0/L1/L2/L3) as a machine-checkable field. A row whose certificate
is VERIFIED but whose L2 layer is incomplete carries both facts, visibly, at all times.

## Article 4 — Certificate types by object class

- Sentence-class object S: requires derivation certificate Π.
- Mapping-class object M: requires consistency certificate U (halting-proof-carrying program).
- Positive-instance object I+: requires trace certificate Σ.
- Negative-instance object I-: certificate class is empty BY DEFINITION; absence of a Σ trace
  is never convertible into a certificate.

Budget tuple B = (t, L, k, E): time cap, row cap, independent-verifier cap, reproducible
environment spec (artifact hashes plus re-run commands). A suspension without an instantiated
budget supports no bounty.

## Article 5 — Registrar separation

The registrar (repository owner) is NEVER the sole executor of the verification entry.
- Checker-code changes require a second account's merge PLUS a 7-day delay before effect.
- Any certificate submission authored or extracted by the registrar requires a third-party
  re-run log (reproduced output plus command transcript) inside the PR before merge.
- The verification entry is `checker/check_register.py` at a pinned release tag.

## Article 6 — Failure pricing

Rejected PRs cost the submitter nothing. Every rejected PR remains a public record with the
checker's output attached. REFUTATION RANKS WITH A PASS: a refutation certificate earns the
same score weight as the certificate class it refutes.

## Article 7 — Identity

Identity is self-declared via the `Agent:` trailer in commit messages, plus the GitHub
account that pushed the fork. No identity verification is claimed or needed. The scoreboard
measures WORK, not autonomy: human-puppeteered work through an agent account counts as work.
The register does not and cannot certify that any actor is an autonomous agent.

## Article 8 — Alignment layers

Each row registers alignment status L0 (location/version anchor), L1 (term-to-definition
mapping), L2 (exclusion of neighboring variants), L3 (co-consequence search, advisory
only, negative evidence monotone). Layers are directional: advisory layers may supply
negative evidence to core layers; core layers never close on advisory passes.
Cross-language rows MUST carry statement_en plus source_anchor_zh (verbatim citation of the
Chinese source). The translation itself is a registered debt item on the row.

## Article 9 — Scoring (frozen weights)

Certificate closures, external actors only: Π=10, U=8, Σ=4.
Alignment closures: L1=2, L2=3, L3=0.5, L0=0.
L0 closures are INSTRUMENT CALIBRATION ONLY. They are displayed in a separate lane and
NEVER count as demand evidence, never toward any probe threshold.
Registrar-authored closures (Article 5 clause 2 applies) never count toward demand evidence.

## Article 10 — Trust surface declaration (single-registrar ceiling)

This register operates under SINGLE-HONEST-PARTY trust. Readers must believe, at most:
(1) the hash function; (2) the checker implementation at the pinned tag; (3) the Actions
runner integrity; (4) the statement-encoding judgment on rows; (5) the registrar's merge
discipline per Article 5. Anything a third party can recompute from public inputs is NOT in
the trust surface. Article 5 exists precisely to shrink (5); until a second human admin
exists, the ceiling is declared here, not hidden.

## Article 11 — Probe protocol

The register is currently a DEMAND PROBE. Its falsification protocol, with thresholds frozen
BEFORE any external artifact was posted, is in FALSIFICATION-PREREGISTER.md. A zero result
at the protocol's deadline is a RESULT, not a failure of the register: the register archives
itself and the archive remains public.
