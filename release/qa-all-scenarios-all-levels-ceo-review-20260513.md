# AI Level Full Matrix QA + CEO Review

Date: 2026-05-13
Scope: expanded scenario bank in `ai-level/references/scenario-bank.md`
Modes used: `$qa` + `$plan-ceo-review`

## Executive Verdict

DONE_WITH_CONCERNS.

The expanded bank is now broad enough to support a real diagnostic. But the important product truth is this:

> A good diagnostic does not try to make every scenario confirm every level. It routes users into the right pressure test, then uses evidence gates to avoid inflated scores.

The bank now covers all levels as a system. It does not mean every scenario can fairly test every level.

CEO call: **SELECTIVE EXPANSION**.

- Do not add more scenarios right now.
- Do add scenario-specific anchors and a regression eval harness.
- Keep Lv.8-Lv.10 rare and evidence-gated, otherwise the product becomes a "make users feel advanced" toy.

## QA Method

I simulated:

- 11 scenario prompts.
- 11 level archetypes from Lv.0 to Lv.10.
- Harsh scoring using `rubric.md` evidence gates.
- CEO/product review: is the scenario useful, motivating, and hard to game?

I used this pass/fail logic:

- PASS: scenario naturally exposes the level without awkward prompting.
- WEAK: scenario can show a signal but needs routing, anchor, or evidence.
- BAD: scenario should not be used for that level.

## Level Archetypes I Used To Answer

These are the self-answer personas used across scenarios.

| Level | Simulated answer pattern | Expected result |
| --- | --- | --- |
| Lv.0 | "I probably would not use AI. I might ask someone else." | Confirm Lv.0-Lv.1 |
| Lv.1 | "I ask AI once: help me do this." | Confirm Lv.1 |
| Lv.2 | "I ask again and tell it what I disliked." | Confirm Lv.2 |
| Lv.3 | "I give context, constraints, examples, format, and ask for options." | Confirm Lv.3 |
| Lv.4 | "I use AI to understand an unfamiliar area and compare tradeoffs." | Confirm Lv.4 |
| Lv.5 | "I split the task into stages with a checklist and review step." | Confirm Lv.5 |
| Lv.6 | "I use agents/tools/sources to execute multi-step work and check key facts." | Confirm Lv.6 if validation is concrete |
| Lv.7 | "I design a reusable workflow with inputs, steps, source rules, checks, outputs, and failure handling." | Confirm weak Lv.7 if concrete |
| Lv.8 | "I have run it multiple times, produced artifacts, and changed the workflow after failure." | Confirm Lv.8 only with E4 |
| Lv.9 | "I have a transferable human/AI collaboration method and know what AI must not decide." | Signal Lv.9; confirm only with strong examples |
| Lv.10 | "I maintain a multi-domain AI operating system other people can use." | Confirm only with E5 and multiple domains |

## Full Scenario x Level Fit Matrix

Legend:

- PASS: reasonable to test or confirm this level.
- WEAK: can produce signal but not confirmation.
- BAD: wrong pressure level; do not use.

| Scenario | Lv0 | Lv1 | Lv2 | Lv3 | Lv4 | Lv5 | Lv6 | Lv7 | Lv8 | Lv9 | Lv10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| First Real Ask | PASS | PASS | PASS | PASS | WEAK | BAD | BAD | BAD | BAD | BAD | BAD |
| Family Travel 2.0 | WEAK | WEAK | PASS | PASS | PASS | PASS | PASS | PASS | WEAK | BAD | BAD |
| Home Move And New Setup | BAD | WEAK | WEAK | PASS | PASS | PASS | PASS | PASS | WEAK | BAD | BAD |
| Expensive Family Purchase | WEAK | PASS | PASS | PASS | PASS | PASS | PASS | WEAK | BAD | BAD | BAD |
| Weekend Plan With Mixed Preferences | PASS | PASS | PASS | PASS | PASS | PASS | WEAK | BAD | BAD | BAD | BAD |
| Eight-Week Learning Sprint | WEAK | PASS | PASS | PASS | PASS | PASS | PASS | WEAK | WEAK | BAD | BAD |
| Messy Work Rescue | BAD | BAD | WEAK | WEAK | PASS | PASS | PASS | PASS | WEAK | WEAK | BAD |
| Knowledge Product Launch | BAD | BAD | WEAK | PASS | PASS | PASS | PASS | PASS | PASS | WEAK | BAD |
| Personal Workflow Automation | BAD | BAD | BAD | WEAK | WEAK | PASS | PASS | PASS | PASS | WEAK | WEAK |
| Plan Breakdown Crisis | BAD | BAD | WEAK | WEAK | PASS | PASS | PASS | PASS | WEAK | PASS signal | BAD |
| Personal AI Operating System | BAD | BAD | BAD | BAD | BAD | WEAK | WEAK | WEAK | PASS | PASS | PASS signal |

Harsh conclusion:

- The bank is not a 121-cell universal test. It is a routed test.
- Trying to use Personal AI Operating System on a Lv.3 user is hostile.
- Trying to confirm Lv.10 from Weekend Plan is nonsense.
- Trying to confirm Lv.8 from Family Purchase is almost always inflation.

## Scenario-By-Scenario Self Answers And Review

### 1. First Real Ask

Best route: basic.

Representative self-answers:

- Lv.0: "我不太会用 AI，可能不会用。"
- Lv.1: "我会问：帮我写一下。"
- Lv.2: "不好我会说太长了、语气不对，让它改。"
- Lv.3: "我会告诉它对象、语气、限制、例子，让它给 3 个版本。"

Harsh review:

- This scenario is necessary and humane.
- It should never be used for serious high-level scoring.
- It is not "too simple"; it solves the old problem where the test assumed everyone already knows how to use AI.

Verdict: PASS for Lv.0-Lv.3. BAD for Lv.6+.

### 2. Family Travel 2.0

Best route: workflow/system.

Representative self-answers:

- Lv.3: "我给预算、人数、时间、偏好，让 AI 出表格和 3 个方案。"
- Lv.5: "我先收集约束，再让 AI 做路线、预算、风险、备选方案。"
- Lv.6: "我让 AI 查交通、天气、酒店评价和地图，再人工核对关键事实。"
- Lv.7: "我把它做成旅行规划 Skill：输入、来源、取舍规则、输出页、检查项。"
- Lv.8: "我跑过两次，第二次加了来源时间、老人步行强度和失败复盘字段。"

Harsh review:

- Still the best default because人人都能懂。
- But it已经被你反复测试过，有熟题风险。
- Lv.8 只能靠"跑过几次、改过什么"确认，不能靠"我会做 Skill"确认。

Verdict: PASS for Lv.3-Lv.7, WEAK for Lv.8, BAD for Lv.9-Lv.10.

### 3. Home Move And New Setup

Best route: workflow.

Representative self-answers:

- Lv.3: "我告诉 AI 预算、户型、人数，让它列采购清单。"
- Lv.5: "我分成搬家前、搬家当天、安装验收、补漏四个阶段。"
- Lv.6: "我让 AI 对比平台价格、配送时间、售后政策，再核对订单和日程。"
- Lv.7: "我做成搬家作战模板，含输入表、采购优先级、延迟预案。"

Harsh review:

- 这是非常好的生活运营场景，比旅行更能测执行力。
- 缺点是它容易变成项目管理空话。
- 必须追问"哪个日期必须确认、哪个采购不能让 AI 拍板、延迟怎么办"。

Verdict: PASS for Lv.3-Lv.7, WEAK for Lv.8, BAD for Lv.9-Lv.10.

### 4. Expensive Family Purchase

Best route: basic/workflow.

Representative self-answers:

- Lv.2: "我会让 AI 推荐，不满意再说预算不对。"
- Lv.3: "我给预算、用途、品牌偏好，让它做对比表。"
- Lv.4: "我不懂参数，所以让 AI 解释参数和坑。"
- Lv.5: "我先定评价标准，再筛选、对比、查风险、做最终清单。"
- Lv.6: "我让 AI 查官网参数、价格趋势、真实评测，再人工确认。"

Harsh review:

- 这是中阶最佳场景之一，生活感强，也不尴尬。
- 但它不是高阶系统题。
- 如果有人在这里说到 Lv.8，大概率是在借题发挥，需要换到 Workflow Automation 追证据。

Verdict: PASS for Lv.2-Lv.6, WEAK for Lv.7, BAD for Lv.8+.

### 5. Weekend Plan With Mixed Preferences

Best route: basic/workflow.

Representative self-answers:

- Lv.1: "我让 AI 推荐一个活动。"
- Lv.2: "有人不满意，我再让 AI 换轻松一点的。"
- Lv.3: "我给人数、预算、地点、时间，让它给几个方案。"
- Lv.5: "我收集偏好、让 AI 聚类、出候选，再让大家投票确认。"

Harsh review:

- 非常适合同事群，轻松，不像考试。
- 但高级别压力不够。Lv.6 以上很容易变成硬凹。
- 这是 warming-up 场景，不是系统能力场景。

Verdict: PASS for Lv.1-Lv.5, WEAK for Lv.6, BAD for Lv.7+.

### 6. Eight-Week Learning Sprint

Best route: workflow.

Representative self-answers:

- Lv.2: "学不下去就让 AI 改轻一点。"
- Lv.3: "告诉 AI 目标、时间、基础，让它做周计划。"
- Lv.5: "先诊断基础，再按周安排练习、测验、复盘和调整。"
- Lv.6: "让 AI 找资料、生成练习题、分析错题、追踪进度。"
- Lv.7: "做成学习教练流程，有诊断、计划、测验、复盘和调整规则。"

Harsh review:

- 很适合发现"AI 生成幻想计划"的问题。
- 但它的工具压力不如旅行/工作强。
- 高阶必须追问：指标是什么？错过一周怎么办？反馈如何进入下周？

Verdict: PASS for Lv.2-Lv.6, WEAK for Lv.7-Lv.8.

### 7. Messy Work Rescue

Best route: workflow/system.

Representative self-answers:

- Lv.4 bluff: "我会让 AI 对齐认知、推进闭环。"
- Lv.5: "我汇总信息、分类问题、列行动清单、让相关人确认。"
- Lv.6: "我让 AI 读文档、表格、聊天记录和网页，整理冲突点。"
- Lv.7: "我做成混乱项目 intake 流程：输入、事实表、争议表、行动表、决策页。"
- Lv.8: "我在三个项目里用过，第二次加了权威来源和决策 owner 字段。"

Harsh review:

- 这是最有价值也最危险的场景。
- 它会奖励会说职场黑话的人，除非评分非常严。
- 没有具体输入、产物、验证、决策边界，一律不要给高分。

Verdict: PASS for Lv.5-Lv.7, WEAK for Lv.8-Lv.9, BAD for beginners.

### 8. Knowledge Product Launch

Best route: system.

Representative self-answers:

- Lv.5: "我整理材料、让 AI 出结构和初稿，再人工改。"
- Lv.6: "我让 AI 读链接、截图、笔记，生成页面或 slides。"
- Lv.7: "我做成内容生产流程：输入池、受众、结构、反 slop review、发布检查。"
- Lv.8: "我发过几次，发现读者不买账后加了受众问题、反方评审和标题测试。"

Harsh review:

- 这是最像真实高阶 AI 使用的场景之一，因为它同时考产物、审美、交付。
- 风险是用户说一堆内容策略，但没有交付证据。
- 必须问"谁用、什么叫可发布、真实反馈改了什么"。

Verdict: PASS for Lv.5-Lv.8, WEAK for Lv.9, BAD for Lv.10 confirmation.

### 9. Personal Workflow Automation

Best route: system/method.

Representative self-answers:

- Lv.6: "我用 Agent 每周收集信息、整理摘要。"
- Lv.7: "我定义固定输入、处理步骤、校验规则、输出模板和失败处理。"
- Lv.8: "这个流程跑了四周，第二周因为误报加了来源时间和 reject reason。"
- Lv.9: "这套方法也迁移到周报、阅读、项目复盘；AI 做处理，我做人类判断。"

Harsh review:

- 这是目前最强的 Lv.6/Lv.7/Lv.8 分层题。
- 如果只能保留一个高阶场景，保留它。
- 但它不能独立确认 Lv.10，除非有别人使用和多领域系统证据。

Verdict: PASS for Lv.6-Lv.8, WEAK for Lv.9-Lv.10 signal.

### 10. Plan Breakdown Crisis

Best route: workflow/method stress test.

Representative self-answers:

- Lv.5: "我列备选方案和风险清单。"
- Lv.6: "我实时查票、酒店、日程，确认哪些事实变了。"
- Lv.7: "我有危机重排协议：事实变更、最低可接受方案、通知模板、复盘。"
- Lv.9: "AI 负责找备选和风险，我决定风险是否可接受以及怎么对人沟通。"

Harsh review:

- 这是压力测试，不是默认题。
- 它能暴露一个人的判断边界，这是高阶能力的核心。
- 但给低阶用户会很糟，像突击考试。

Verdict: PASS for Lv.5-Lv.7, PASS signal for Lv.9, BAD for beginners.

### 11. Personal AI Operating System

Best route: method only.

Representative self-answers:

- Lv.8: "我跑过真实流程，版本 2 比版本 1 增加了失败后新增的检查项。"
- Lv.9: "我有跨场景原则：AI 负责扩展、整理、反方；我负责目标、取舍、最终判断。"
- Lv.10: "我维护 skill library、review rules、知识库和 onboarding，别人能直接用。"

Harsh review:

- 这是唯一能接近 Lv.9/Lv.10 的题。
- 它不是场景题，是证据审计题。
- 如果普通用户看到这个，会觉得被审问。只能在高证据用户身上使用。

Verdict: PASS for Lv.8-Lv.10 signal. BAD as default.

## Cross-Level Sharp Findings

### Finding 1: The bank is strong enough. The scoring engine is the weak point.

Adding more scenes now收益很低。真正容易出错的是：

- follow-up 不够贴回答；
- report 忘记 evidence gate；
- tool-name dropping 被抬高；
- 职场黑话被当成高级能力。

Priority: build eval harness, not more prompts.

### Finding 2: Lv.8 is the product's danger zone.

Most users will want to hear "你已经 Lv.8 了". The skill must resist that.

Lv.8 should require:

- at least two runs;
- changed rule after failure;
- usable artifact;
- proof that second run was easier or better.

No reuse means no confirmed Lv.8.

### Finding 3: Lv.9/Lv.10 should almost never be "confirmed" in casual group tests.

In a 3-5 minute colleague test:

- Lv.9 should usually be "signal".
- Lv.10 should almost never be confirmed.

If the product confirms Lv.10 casually, it loses credibility with serious users.

### Finding 4: The current best product flow is not a quiz. It is a challenger.

The value is not "your score is 7".

The value is:

> 你以为你会用 AI，但我能精准指出你下一层缺哪根骨头。

That means the report must be sharper than the score.

## CEO Review

### What is the 10-star product?

Not "AI level quiz".

The 10-star version is:

> A short AI capability mirror that gives people a painfully accurate diagnosis of how they actually use AI, then shows the smallest next upgrade that would change their work.

This means the product should optimize for:

- uncomfortable accuracy;
- fast challenge;
- evidence-based humility;
- next action that feels worth doing.

### What should be cut?

Cut the ambition to make every scenario cover every level.

That is fake completeness. It makes the system harder to reason about and increases scoring inconsistency.

### What should be expanded?

Expand only three things:

1. Scenario-specific anchors.
2. Regression evals with high-baseline weak answers and low-baseline strong answers.
3. Report quality: sharper gap diagnosis and more motivating next challenge.

### Scope decision

SELECTIVE EXPANSION:

- Keep the 11 scenarios.
- Do not add more scenarios for v0.1.2.
- Add anchor examples and automated/structured QA cases.
- Treat Lv.9/Lv.10 as premium evidence modes, not normal group-test outcomes.

## Required Fixes Before Calling This "Robust"

### P0: Add scenario-specific anchors

Need tuned anchors for:

- Home Move
- Expensive Purchase
- Learning Sprint
- Messy Work
- Knowledge Product
- Workflow Automation
- Plan Breakdown Crisis
- Personal AI Operating System

Without this, the bank is broad but the interrogation quality is uneven.

### P0: Add regression cases to sample script

Current `sample_run.py` still mostly validates one high-travel path.

Need at least:

- beginner route;
- mid workflow route;
- high baseline weak answer;
- real Lv.8 evidence answer;
- Lv.9 signal but not confirmation.

### P1: Add scoring examples per lane

Each lane needs example reports:

- basic report,
- workflow report,
- system report,
- method report.

Otherwise report tone will be overfit to Lv.7 travel planning.

### P1: Tighten wording around "匹配难度"

It is acceptable in sample output, but live UX should avoid making users feel routed into a "harder exam".

Better:

```text
我会给你一个更适合你当前用法的场景。
```

## Final Decision

The scenario bank is conceptually right.

It is not yet robust enough to call the diagnostic "fully tested", because the live flow lacks:

- per-scenario anchors;
- multi-route sample tests;
- automated checks for over-confirming Lv.8+;
- report examples below Lv.7.

Ship-readiness after this review:

- Good enough for internal iteration.
- Not yet good enough to claim "all levels all scenarios are rigorously validated."

Next best move:

> Stop adding scenes. Add anchors and evals.
