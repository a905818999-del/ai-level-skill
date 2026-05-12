# AI Level Simulated Colleague Trial

Date: 2026-05-12

Goal: simulate likely colleague responses before sharing the skill in a group. This checks whether the flow separates one-shot prompting, workflow thinking, tool use, and reusable-system thinking without asking a long questionnaire.

## Sample A: content/ops colleague

Baseline: `1B 2C 3B`

Scenario answer:

> 我会把人数、预算、老人和小孩的情况告诉 AI，让它做一个 5 天行程表。最好每天不要太累，景点和吃饭都列出来，再给一个预算表。如果不满意，我会让它改得轻松一点。

Expected report:

- Signal: Lv.3-Lv.4
- Confirmed: Lv.3
- Evidence strength: E1
- Anchor follow-up: no

Why:

- 有约束和输出格式，能控制回答质量。
- 还没有明显的分阶段流程、外部信息校验或复用结构。
- 下一步建议应该引导 TA 把“行程表”升级成“可检查的方案”：先补缺失输入，再让 AI 给候选方案和取舍理由。

Wording risk:

- 不要说“你只是基础用户”。更好的说法是：“你已经会让 AI 按要求出东西，下一步是让它帮你比较和验证。”

## Sample B: project/product colleague

Baseline: `1C 2CD 3C`

Scenario answer:

> 我会先让 AI 问我还缺哪些信息，比如出发城市、预算上限、老人能走多久、小孩喜欢什么。然后让它先给 3 个旅行方向，列优缺点和风险。选定方向后再拆交通、住宿、每天路线和预算。我会自己核对火车票、酒店价格、景点开放时间，最后让 AI 整理成一个表格。

Expected report:

- Signal: Lv.5-Lv.6
- Confirmed: Lv.5
- Evidence strength: E2
- Anchor follow-up: maybe no, unless TA later mentions tools/agent

Why:

- 有缺失信息收集、候选方案、分阶段执行和人工校验。
- 主要还是人在驱动流程，AI 是协助整理和比较。
- 下一步建议应该是把这个流程写成模板或 checklist，并让工具承担一部分信息收集。

Wording risk:

- 不要强行拔高到 Lv.6。没有明确外部工具/Agent 执行，最多是 Lv.6 信号。

## Sample C: tool-name heavy colleague

Baseline: `1D 2C 3D`

Scenario answer:

> 我会直接让 Agent 做。它可以搜小红书、携程、地图、天气，然后生成一个 HTML 页面。这样效率最高，我基本只要看结果就行。

Anchor answer:

> 输入就是目的地、时间、预算和人数。信息源就让 Agent 自己搜，最后我看一下页面有没有明显问题。不满意就让它重做。

Expected report:

- Signal: Lv.6
- Confirmed: Lv.5-Lv.6
- Evidence strength: E1
- Anchor follow-up: yes, and it should lower confidence

Why:

- 有 Agent 和 HTML 产物信号，但输入设计、来源规则、校验规则都很弱。
- 这类回答最容易“口嗨”，追问后应该明确指出：工具名不等于系统能力。
- 下一步建议应该让 TA 写清楚三个东西：输入清单、来源标注规则、失败时如何调整。

Wording risk:

- 不要用“口嗨”评价本人。可以说：“你已经有工具方向，但证据还不足以确认到 Lv.7。”

## Sample D: advanced builder colleague

Baseline: `1D 2D 3D`

Scenario answer:

> 我会做成一个可复用的 Travel Decision Skill。先收集家庭成员、预算、体力、兴趣、不能接受项，再调用 12306、地图、天气、酒店和内容平台。输出前先做候选方案对比，不直接排行程。每个关键事实都要带来源和查询时间，最后输出一个给同行人看的 HTML 决策页。

Anchor answer:

> 输入会分必填和可选：日期、出发地、人数、年龄、预算、体力、兴趣、住宿偏好、不能接受项。信息源分别解决交通、住宿、天气、玩法和风险。我会要求交通班次、酒店价格、开放时间、天气都标来源和查询时间。生成前先判断预算是否够、老人小孩是否冲突、每天步行强度是否合理。完成后检查来源、时间、预算、路线折返和备选方案。如果老人累，就减少景点和增加休息；小孩无聊，就替换成互动项目；预算超支，就先动酒店档位或景点组合。

Expected report:

- Signal: Lv.7-Lv.8
- Confirmed: Lv.7
- Evidence strength: E2
- Anchor follow-up: yes

Why:

- 有可复用 Skill、外部信息源、来源规则、生成前判断、失败调整机制。
- 还没有真实跑过、复用过、改进过的证据，所以不确认 Lv.8。
- 下一步建议应该集中在“真实跑完一次并留下结构”，而不是继续加工具。

Wording risk:

- 这类用户不需要鼓励“多学习 AI”。要直接指出 Lv.8 的核心：稳定产出、复用、迭代。

## Trial verdict

The diagnostic is ready for a small colleague-group release.

Pass:

- Differentiates Lv.3, Lv.5, Lv.6, and Lv.7 signals.
- The anchor follow-up catches inflated Agent/tool-name answers.
- Advice can be tailored without becoming a long questionnaire.
- The family-travel scenario feels broad enough for non-business testing.

Watch:

- Lv.8+ still needs real artifact evidence. The report should keep saying "signal" unless the user shows reuse or iteration.
- If many colleagues answer very briefly, the skill should ask one broad follow-up instead of over-scoring.

