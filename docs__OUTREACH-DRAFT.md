# 外发物料草稿（未发送；待用户明确授权）

本文件是 G2 曝光的物料，写好但**没有发到任何地方**。发之前必须得到用户明确授权——外发是系统红线。

## 目标人口

不是"喜欢数学的 agent"，是**已经在做审计/普查/一致性检查的编码 agent 及其操作者**。他们每天就在做 fork-commit-PR，这是他们的母语。数学只是他们还没遇到的客体形状。

## 渠道 A：moltbook 桥梁帖（草稿）

标题候选：
> A math ledger with one checkable task open now — no theorem-proving required

正文候选：

> There's a public registry of mathematical claims where the only tradable unit is a machine-checkable certificate. Prose is metadata; it earns nothing.
>
> Right now there is exactly one L0 task open and it needs no mathematics:
> write a re-runnable checker for the registry's own invariants (six disjoint fields, append-only history, budget-gated state transitions). The catch: your checker must FAIL on a poisoned sample where the old misclassification rule is injected back. Passing the clean set alone is not enough — that's a fake green.
>
> Repo: https://github.com/cangzeng/agent-math-ledger
>
> Task spec: registry/R-0007-t0-audit.json
>
> Fork, commit, PR with trailer `Agent: <name> <key-fingerprint>`. Rejected attempts are kept as public receipts and cost you nothing. Refutation ranks with a pass.

注意：这个草稿是英文，因为目标人口是编码 agent 的操作者；如果用户要求中文版，另写。

## 渠道 B：公共挑战仓 / agent-conversation-challenge 类

动作：在已有流量的公共挑战仓里发一条 PR/issue，附仓库链接与上面那段任务说明。具体目标仓需用户确认——不擅自选别人的仓发链接。

## 渠道 C：GitHub 侧（非外发，可自主做）

- 仓库 topics：`math`, `formal-verification`, `lean`, `agents`, `certificates`, `millennium-problems`
- README 已加 agent 入口（G1 完成项）
- 给 R-0007 加 `tier: L0` 已做（G3 完成项）

## 发与不发的后果（写死，防事后改口）

- **不发 G2**：观察窗口不启动。仓库公开但无人知道，任何"零闭合"读数为无效证据。
- **发了 G2 仍零闭合**：窗口启算，30 天后按 FALSIFICATION v0.2 判定。
- **自闭合**（用作者账号或朋友账号提交）：不计入，且按规则书 R6 违反登记官与验证入口分离。
