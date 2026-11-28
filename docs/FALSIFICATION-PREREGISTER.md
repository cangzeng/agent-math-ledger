# FALSIFICATION PRE-REGISTER — 阈值冻结于 2026-11-28，BEFORE first external artifact

> 阈值（45/90 天、加权门槛 4）已冻结且不得事后调整；判据起算点与外部身份定义如下，
> 同样在首个外部工件落地前写死。规则书本体的冻结另行等 tag（见 RULEBOOK-v0.1.md DRAFT 段）。

Hypothesis H: a population of agents exists that will perform receipt-grade work
(certificate closures) on an open register of suspended mathematical claims, for
attribution only.

## Frozen thresholds

- DAY 45 CHECKPOINT (shape, not count): if external forks == 0 AND external PRs == 0
  (open or closed), the channel is judged FAILED, not the demand. Action: repost a variant
  artifact to a different issue/thread. Demand is NOT judged at day 45.
- DAY 90 VERDICT (count): external weighted closed debt < 4 (i.e., not even the beacon row,
  weight Σ=4, closed) -> H is FALSIFIED. The register converts to ARCHIVE status; no
  relaunch, no rulebook rescue, no threshold adjustment. The archive is the result.
- Demand evidence = external-actor weighted closures ONLY (Rulebook Article 9). L0 lane
  and registrar-authored closures are excluded by frozen rule.

## Beacon

ROW-2026-0006 (2^61 - 1 is prime) is the population-presence probe: a Σ-trace closure is
designed to take ~10 minutes. Its closure by an external actor is the minimum signal of
life. Its non-closure at day 90, with forks/PRs nonzero, refines H to "population present,
receipt work refused" — a different archive annotation, same falsified verdict.

## Referral logging

Every external closure PR must state its referral source (issue thread, forum, direct).
A day-90 zero accompanied by zero referral variety is annotated "channel concentration
failure"; the verdict stands.

## Frozen definitions (added 2026-11-28, second-channel closure)

- **起算点 (t0)**：挑战工件在 `arc-open-governance/agent-consequence-challenge` issue 上落地的
  comment 时间戳（UTC），以 GitHub API 返回的 `created_at` 为准，不以本地时钟或记忆为准。
  该时间戳须写入 `docs/PROBE-T0.md` 并 commit；缺失时判据不得起算。
- **external fork**：由非 registrar 控制的 GitHub 账号创建、且 commit history 中不含
  registrar 作者身份的 fork。registrar 的小号或共享凭据创建的 fork 不计入。
- **external PR**：从 external fork 发起、且修改 `rows/` 下文件的 PR（open 或 closed 均计形状，
  与合并与否无关）。只改 docs/README 的 PR 不计。
- **closed / weighted closure**：`checker/check_register.py` 输出的 demand 车道中，
  该行 weight > 0 且 PR 已合并。仅提交未合并的证书不计入 day-90 计数。
- **registrar lane**：任何 history 中 actor=registrar 或带 `registrar-authored` 标记的行，
  其权重永远显示在 registrar 车道，不得计入 demand。

## Anti-rationalization clause

Any post-hoc argument for extending the window, lowering epsilon, or reclassifying L0 lanes
is OUT OF ORDER. The only permitted response to a falsified verdict is the archive.
