# Scenario Bank

This bank is for selecting one practical scenario per run. Do not show all scenarios to the user.

Design stance: scenarios should feel like real life, not a school exam. A top AI user is not just "using more tools"; they can turn messy human situations into clear inputs, tradeoff rules, tool chains, validation checks, artifacts, and reusable loops.

## Scenario Selection

Use the baseline gate to choose a diagnostic lane. The lane is not the final grade.

| Lane | Target range | Use when |
| --- | --- | --- |
| basic | Lv.0-Lv.3 | User has little recent AI usage or mostly retries/simple asks |
| workflow | Lv.3-Lv.6 | User uses AI for real tasks and can add context or checks |
| system | Lv.6-Lv.8 | User mentions tools, agents, MCP, automation, templates, or reusable workflows |
| method | Lv.8-Lv.10 signal | User has real reuse, artifacts, cross-domain practice, team use, or explicit human/AI boundary thinking |

Guardrails:

- Baseline selects the lane; practical evidence confirms the level.
- Never confirm Lv.8+ without reuse, iteration, artifact, or real-case evidence.
- Never confirm Lv.9-Lv.10 from one scenario alone.
- If a high-lane answer is vague, downshift confirmed level.
- If a low-lane user gives a strong practical answer, allow upgrade.

## Shared Scoring Pressure

Across all scenarios, look for:

- Context: what inputs and constraints the user collects.
- Decomposition: whether they split work into stages.
- Verification: whether they check facts, sources, uncertainty, and failure modes.
- Tooling: whether tools are used with roles and proof, not just name-dropped.
- Reuse: whether the process can be rerun.
- Judgment: which decisions stay human.

## Scenario Diagnostic Contracts

Use these contracts to keep scoring consistent. A scenario's default confirmed ceiling is the normal maximum for a casual 3-5 minute run. Strong evidence can exceed it only when the override gate is explicitly met. Signal ceiling means the highest level the scenario can suggest, not confirm.

| Scenario | Best for | Default confirmed ceiling | Signal ceiling | Override gate |
| --- | --- | --- | --- | --- |
| First Real Ask | Lv.0-Lv.3 | Lv.3 | Lv.4 | Low-baseline user gives unusually structured context, constraints, examples, and follow-up logic |
| Weekend Plan With Mixed Preferences | Lv.1-Lv.5 | Lv.5 | Lv.6 | User describes tool-assisted preference collection plus concrete conflict and fallback rules |
| Expensive Family Purchase | Lv.2-Lv.6 | Lv.6 | Lv.7 | User has a repeated purchase-decision workflow with source rules, reversibility checks, and artifacts |
| Home Move And New Setup | Lv.3-Lv.7 | Lv.7 | Lv.8 signal | Real run evidence: reusable checklist or artifact, delay handling, and post-run improvement |
| Eight-Week Learning Sprint | Lv.2-Lv.7 | Lv.7 | Lv.8 signal | Real repeated coaching flow with metrics, missed-week adjustment, and revised rules |
| Family Travel 2.0 | Lv.3-Lv.7 | Lv.7 | Lv.8 signal | Real repeated run, shareable artifact, and failure-based rule changes |
| Messy Work Rescue | Lv.5-Lv.7 | Lv.7 | Lv.8 signal | Multiple real projects, concrete artifacts, source authority rules, and improved intake protocol |
| Knowledge Product Launch | Lv.5-Lv.7 | Lv.7 | Lv.9 signal | Published artifact plus audience feedback and workflow revision; cross-domain publishing method for Lv.9 signal |
| Personal Workflow Automation | Lv.6-Lv.8 | Lv.8 | Lv.9 signal | At least two runs, one failure-based rule change, reusable artifact, and clear human decision boundary |
| Plan Breakdown Crisis | Lv.5-Lv.7 | Lv.7 | Lv.9 signal | Reused replanning protocol plus human risk-communication principles across cases |
| Personal AI Operating System | Lv.8-Lv.9 | Lv.9 | Lv.10 signal | E5 evidence: multi-domain system, artifacts, other-user adoption, and sustained practice |

Hard downgrade triggers:

- Tool names only (`Agent`, `MCP`, `Skill`, browser, plugins) without input rules, validation, output shape, or human decision boundary: confirmed level should not exceed Lv.6.
- "I would make a Skill/workflow" without concrete inputs, steps, checks, and failure handling: treat as Lv.7 signal, not confirmation.
- No real run, artifact, reuse, or failure-based iteration: do not confirm Lv.8.
- No cross-domain evidence or human/AI method: do not confirm Lv.9.
- No other-user adoption or multi-domain operating system: do not confirm Lv.10.
- Workplace fluency without artifacts (`align stakeholders`, `close the loop`, `form consensus`) should be downgraded unless the answer names inputs, conflict representation, review artifact, and decision owner.

High-score evidence must be concrete:

- Artifact means a page, template, Skill, checklist, table, script, document, or other inspectable output.
- Repeated use means at least two real runs, not "I could reuse it".
- Failure-based improvement means a named rule, field, or check was added because a real run failed or disappointed.
- Other-user evidence means someone can use the workflow without the user explaining every step live.

## Scenario-Specific Anchor Examples

Use these as starting points for the adaptive anchor. Delete questions that the user already answered. Ask only 2-3 missing gaps.

### Family Travel 2.0

```text
你已经说清楚了【用户已覆盖内容】。

我只追几个还没看清的点：

1. 如果老人不累、小孩开心、预算不爆、你自己也想玩发生冲突，你会让 AI 按什么顺序取舍？
2. 你怎么确认交通、酒店、天气、人流这类信息不是过期或编出来的？
3. 如果这套流程跑第二次，你会保留或改掉哪条规则？
```

### Home Move And New Setup

```text
你已经说了会用 AI 帮你排搬家和新家配置流程。

我只追几个还没看清的点：

1. 哪些日期必须人工确认，比如配送、安装、水电网络开通？你会怎么让 AI 标出来？
2. 哪些采购决定不能让 AI 直接拍板，必须你自己判断？
3. 如果关键家具或安装延期，你的流程会怎么自动改计划？
```

### Expensive Family Purchase

```text
你已经说了会用 AI 帮你比较和筛选大件购买选项。

我只追几个还没看清的点：

1. 你怎么区分官方参数、真实评测、带货内容和过期信息？
2. 哪些标准可以让 AI 算分，哪些偏好必须由人决定？
3. 如果买错成本很高，你会让方案里保留什么安全阀，比如退换、试用、保修或备选？
```

### Weekend Plan With Mixed Preferences

```text
你已经说了会让 AI 帮你整理大家的时间、预算和偏好。

我只追几个还没看清的点：

1. 如果大家偏好冲突，你会让 AI 按什么规则缩小选择，而不是谁声音大听谁的？
2. 你怎么收集反馈，避免最后还是你一个人拍脑袋？
3. 如果天气或时间临时变化，有没有备用方案？
```

### Eight-Week Learning Sprint

```text
你已经说了会用 AI 帮忙制定和调整学习计划。

我只追几个还没看清的点：

1. 一开始你怎么判断真实水平，而不是让 AI 直接排一个看起来很满的计划？
2. 每周用什么指标判断计划有效，比如正确率、完成率、错题类型，还是实际输出？
3. 如果有一周没执行，AI 应该怎么改下一周，而不是简单把任务往后挪？
```

### Messy Work Rescue

```text
你已经说了会用 AI 帮你整理混乱信息并形成推进方案。

我只追几个还没看清的点：

1. 聊天记录、文档、表格和口头说法冲突时，哪个来源更权威？
2. AI 最终产出的中间件是什么：事实表、争议表、行动表，还是决策页？
3. 哪些结论 AI 可以草拟，哪些必须由负责人或相关人确认？
```

### Knowledge Product Launch

```text
你已经说了会用 AI 把零散材料做成一个可发布产物。

我只追几个还没看清的点：

1. 这个产物到底给谁看？什么标准算“能发布”？
2. 你会用什么检查项抓 AI 味、空话、重复和不可信内容？
3. 如果真实读者反馈不好，下一版流程会改什么？
```

### Personal Workflow Automation

```text
你已经说了想把重复劳动做成稳定流程。

我只追几个还没看清的点：

1. 每次运行固定要输入什么？哪些输入缺了就不能开始？
2. 输出前必须检查什么，才能防止 Agent 看起来跑了但实际在编？
3. 这个流程从 v1 到 v2 会因为哪类失败而改变？
```

### Plan Breakdown Crisis

```text
你已经说了会用 AI 帮你快速重排崩掉的计划。

我只追几个还没看清的点：

1. 哪些事实必须实时确认，不能靠 AI 推测？
2. 什么叫“最低可接受方案”？你会怎么让 AI 不只追求表面最优？
3. 风险要怎么告诉受影响的人，哪些话不能让 AI 自己决定？
```

### Personal AI Operating System

```text
你已经说了自己有反复运行的 AI 流程或系统。

我只追几个还没看清的点：

1. 除了这个例子，还有没有第二个领域也用同一套方法？
2. 如果你不在场，别人能直接使用哪部分：模板、Skill、检查表、案例，还是操作说明？
3. 哪条规则是因为真实失败才加进去的？
```

## Scenario 1: First Real Ask

Category: basic life task
Diagnostic lane: basic
Best for: Lv.0-Lv.3

User-facing prompt:

```text
你有一件小事想让 AI 帮忙，比如写一条消息、整理一个购物清单、做一个简单安排，或者把一段乱糟糟的话改清楚。

如果你现在要开始用 AI，你会怎么问？
如果它第一次回答不太满意，你会怎么继续？
```

Do not hint:

- Do not mention validation, tools, or workflows.

Lv signals:

- Lv.0-Lv.1: asks one generic question or says they would not use AI.
- Lv.2: can follow up and correct the answer.
- Lv.3: adds context, constraints, examples, tone, and output format.

Anchor gaps:

- What information would you add after the first bad answer?
- What would make the answer "usable"?

Reviewer verdict:

- This scenario is necessary. Without it, the test starts too high for beginners.

## Scenario 2: Family Travel 2.0

Category: life logistics
Diagnostic lane: workflow or system
Best for: Lv.3-Lv.8 signal

User-facing prompt:

```text
你要安排一次 5 天家庭旅行。同行里有老人、小孩和成年人，大家体力、兴趣和耐心都不一样。预算不能乱花，时间在下个月，交通、天气、人流、住宿评价都可能变化。

你希望最后不是一份漂亮攻略，而是一份同行人真的能照着走、也知道为什么这么安排的方案。

如果你准备用 AI 帮你把这件事做好，你会怎么做？
```

Do not hint:

- Do not ask upfront about 12306, Xiaohongshu, browser, sources, or verification.

Lv signals:

- Lv.3: gives constraints and asks for tables/options.
- Lv.5: splits into input collection, options, itinerary, budget, risk checks.
- Lv.6: uses travel sites, maps, weather, agents, or external sources.
- Lv.7: designs a reusable travel-planning workflow or skill.
- Lv.8: has run and reused the workflow, with changes after real failures.

Anchor gaps:

- Tradeoff order when elderly comfort, child interest, budget, and personal preference conflict.
- Proof that tools/sources were really used.
- Source freshness and human confirmation rules.
- What changed after the first real run.

Reviewer verdict:

- Still the best default scenario, but should not be the only high-lane test.

## Scenario 3: Home Move And New Setup

Category: life operations
Diagnostic lane: workflow
Best for: Lv.3-Lv.7

User-facing prompt:

```text
你要在 3 周内完成一次搬家和新家配置。东西很多，家里有老人或小孩，搬家当天不能乱成一团。家具、电器、网络、水电、收纳、配送和安装都要排上，而且预算有限。

你希望最后拿到的不是一堆建议，而是一张能执行的搬家作战图：先做什么、谁来做、什么时候确认、哪里容易出问题。

如果你准备用 AI 帮你推进，你会怎么做？
```

Do not hint:

- Do not list platforms, return policies, or installation risk upfront.

Lv signals:

- Lv.4: asks AI解释搬家常见坑和采购顺序。
- Lv.5: turns it into timeline, purchase list, risk list, and day-of checklist.
- Lv.6: uses shopping platforms, calendar, maps, files, or agents.
- Lv.7: creates a reusable move/procurement template.

Anchor gaps:

- How delivery/installation dates are verified.
- What must be human-confirmed before purchase.
- What happens if a key item is delayed.
- Whether the checklist is reusable for another move.

Reviewer verdict:

- Strong for operational thinking. Needs tone to feel like real life rather than a project brief.

## Scenario 4: Expensive Family Purchase

Category: decision comparison
Diagnostic lane: basic or workflow
Best for: Lv.2-Lv.6

User-facing prompt:

```text
家里准备买一件不便宜、也不能随便退换的大件，比如电脑、冰箱、洗烘套装、儿童座椅、相机或人体工学椅。每个人在意的点不一样：有人看价格，有人看安全，有人看品牌，有人怕售后麻烦。

你想用 AI 帮你做选择，但又不想被带货软文、过期测评或参数堆砌骗到。

你会怎么用 AI 做这个决策？
```

Do not hint:

- Do not directly say "require source and timestamp".

Lv signals:

- Lv.3: lists budget,需求, asks for comparison table.
- Lv.4: uses AI理解陌生参数 and tradeoffs.
- Lv.5: defines criteria, weights, shortlist, and review checklist.
- Lv.6: checks reviews, price history, official specs, or forums.

Anchor gaps:

- Which criteria can be delegated to AI and which stay human.
- How to reject fake reviews or stale recommendations.
- What would make the decision reversible or safer.

Reviewer verdict:

- Great for middle levels. It feels everyday and naturally tests judgment.

## Scenario 5: Weekend Plan With Mixed Preferences

Category: social coordination
Diagnostic lane: basic or workflow
Best for: Lv.1-Lv.5

User-facing prompt:

```text
你要组织一个周末活动，可能是朋友聚会、亲子活动、团队小 outing 或生日安排。大家时间不完全一致，预算不同，口味也不一样。你不想最后变成你一个人拍脑袋。

如果你准备用 AI 帮你把这个活动安排得更顺一点，你会怎么做？
```

Do not hint:

- Do not ask for voting, forms, or backup plans upfront.

Lv signals:

- Lv.2: iterates based on people's objections.
- Lv.3: adds人数,预算,地点,时间,偏好 and output format.
- Lv.5: collects preferences, clusters options, creates shortlist, confirms final plan.

Anchor gaps:

- How conflicting preferences are resolved.
- How feedback is collected.
- What fallback exists if weather/time changes.

Reviewer verdict:

- Useful for friendly group testing because it feels low-pressure.

## Scenario 6: Eight-Week Learning Sprint

Category: personal growth
Diagnostic lane: workflow or system
Best for: Lv.2-Lv.7

User-facing prompt:

```text
你要帮一个人制定 8 周学习计划。他的基础不均衡，时间也不稳定，目标比较明确，但很容易三分钟热度。你不想要一张看起来很满、实际执行不了的计划表。

如果你准备用 AI 帮他真的学起来，你会怎么做？
```

Do not hint:

- Do not mention weekly review, diagnostic test, or progress metrics upfront.

Lv signals:

- Lv.3: adds goal,时间,基础,输出格式。
- Lv.5: starts with diagnosis, weekly plan, practice, review, adjustment.
- Lv.6: uses external materials, quizzes, documents, spaced repetition tools, or agents.
- Lv.7: creates a reusable learning-coach workflow.

Anchor gaps:

- How the starting level is diagnosed.
- What metric shows the plan is working.
- How missed weeks are handled.
- How feedback changes the next week's plan.

Reviewer verdict:

- Strong for seeing whether the user can prevent AI from making fantasy plans.

## Scenario 7: Messy Work Rescue

Category: work collaboration
Diagnostic lane: workflow or system
Best for: Lv.5-Lv.8 signal

User-facing prompt:

```text
你接手了一件已经有点乱的工作。信息散在聊天记录、文档、表格、网页和几个人的口头说法里。每个人都觉得自己说得对，但优先级并不一致。

你需要先把局面理清楚，再产出一份别人能看懂、能继续协作的说明、行动清单或决策页。

如果你准备用 AI 帮你推进，你会怎么做？
```

Do not hint:

- Do not ask directly about stakeholders, source files, or decision owners.

Lv signals:

- Lv.5: collects info, summarizes, creates action list.
- Lv.6: lets AI read files, tables, chats, and links.
- Lv.7: builds a repeatable messy-project intake and synthesis flow.
- Lv.8: has used the flow across real projects and improved it.

Anchor gaps:

- Which inputs are authoritative.
- How stakeholder conflicts are represented.
- What artifact gets reviewed by humans.
- Which decision AI cannot make.

Reviewer verdict:

- Powerful but dangerous: fluent workplace language can fake competence. Require concrete artifacts.

## Scenario 8: Knowledge Product Launch

Category: creation and delivery
Diagnostic lane: system
Best for: Lv.5-Lv.8

User-facing prompt:

```text
你手里有一堆零散材料：笔记、链接、聊天记录、截图、想法和几个半成品。你想把它做成一个别人能看懂、愿意转发或愿意使用的东西，比如分享页、小课程、内部指南、工具清单或一篇系列文章。

如果你准备用 AI 帮你从一堆材料走到一个可发布产物，你会怎么做？
```

Do not hint:

- Do not ask for content pipeline, audience, or review loop upfront.

Lv signals:

- Lv.5:整理材料,定结构,出初稿,人工改。
- Lv.6: uses files, web, images, slides, HTML, or agents.
- Lv.7: creates a reusable content production workflow.
- Lv.8: has shipped artifacts and revised the pipeline after audience feedback.

Anchor gaps:

- Who the artifact is for.
- What "publishable" means.
- What review pass catches AI slop.
- What changes after real readers use it.

Reviewer verdict:

- Excellent for high-level creative operators. It tests taste plus process.

## Scenario 9: Personal Workflow Automation

Category: recurring operations
Diagnostic lane: system or method
Best for: Lv.6-Lv.9 signal

User-facing prompt:

```text
你发现自己每周都有一类重复劳动：整理周报、筛选信息、复盘项目、处理票据、做阅读摘要、更新任务清单，或者把多个来源的信息合成一个交付物。

你不想每周从零开始问 AI，而是想让它慢慢变成一个稳定流程。

你会怎么设计这个流程？
```

Do not hint:

- Do not mention Skill, MCP, cron, or agent unless the user brings it up.

Lv signals:

- Lv.6: uses tools/agents to collect and process recurring inputs.
- Lv.7: defines input schema, steps, checks, output format, and failure handling.
- Lv.8: has run it multiple times and improved it.
- Lv.9: can explain broader human/AI operating principles.

Anchor gaps:

- What stays constant each run.
- What gets checked before output.
- What changed between v1 and v2.
- What humans still decide.

Reviewer verdict:

- Best current candidate for separating Lv.6, Lv.7, and Lv.8.

## Scenario 10: Plan Breakdown Crisis

Category: dynamic replanning
Diagnostic lane: workflow or method
Best for: Lv.5-Lv.9 signal

User-facing prompt:

```text
一个原本安排好的计划突然崩了：车票没了、酒店出问题、关键人临时没空、供应商延期、考试安排改变，或者项目 deadline 提前。

你现在需要用 AI 快速重排方案，但不能只追求看起来快，还要知道哪些信息是真的、哪些风险需要人来判断。

你会怎么做？
```

Do not hint:

- Do not directly ask for fallback plans or decision boundaries.

Lv signals:

- Lv.5: lists options and fallback checklist.
- Lv.6: checks live sources and constraints.
- Lv.7: has a replanning protocol.
- Lv.8-Lv.9: explains human decision boundary and postmortem learning.

Anchor gaps:

- Which facts must be live-checked.
- What is the minimum acceptable option.
- How risk is communicated to affected people.
- What gets added to the workflow after the crisis.

Reviewer verdict:

- Strong stress test. Use after a user has enough maturity; it may overwhelm beginners.

## Scenario 11: Personal AI Operating System

Category: method evidence
Diagnostic lane: method
Best for: Lv.8-Lv.10 signal

User-facing prompt:

```text
挑一个你已经反复用 AI 跑过的真实流程。不要讲理想方案，讲真实发生过的。

它第一次是怎么跑的？
现在是怎么跑的？
中间你因为失败或不满意改过什么？
哪些事情你会交给 AI，哪些判断你一定自己做？
有没有别人能直接使用你沉淀下来的流程、模板或 Skill？
```

Do not hint:

- This is already an evidence probe. Do not soften it into a generic scenario.

Lv signals:

- Lv.8: repeated artifact creation and iteration.
- Lv.9: clear transferable method and human judgment boundary.
- Lv.10: multi-domain operating system used by self or others.

Anchor gaps:

- Ask for a second domain if only one domain is described.
- Ask what others can use without the user present.
- Ask which rule was added after a real failure.

Reviewer verdict:

- This is not a default scenario. Use only when the baseline and answer already show high-level evidence.

## Strict Reviewer Notes

### Coverage by level

| Level | Best scenario |
| --- | --- |
| Lv.0-Lv.1 | First Real Ask |
| Lv.2-Lv.3 | First Real Ask, Weekend Plan, Family Purchase |
| Lv.4-Lv.5 | Family Purchase, Home Move, Learning Sprint |
| Lv.6 | Family Travel, Home Move, Messy Work, Workflow Automation |
| Lv.7 | Family Travel, Messy Work, Knowledge Product, Workflow Automation |
| Lv.8 | Workflow Automation, Knowledge Product, Personal AI Operating System |
| Lv.9-Lv.10 | Personal AI Operating System only, with cross-domain evidence |

### Current risk after expansion

- More scenarios can create inconsistent scoring if the report forgets the shared evidence gates.
- The model must not show scenario-selection mechanics to the user.
- The method scenario is strong but should not be used too early. It will feel like an audit if given to ordinary users.

### Pass condition

The expanded bank is good enough when:

- A beginner gets a humane basic scenario.
- A Lv.6 tool user does not get inflated to Lv.7 without workflow design.
- A Lv.7 designer does not get inflated to Lv.8 without reuse.
- A Lv.9-sounding answer is treated as signal unless backed by real examples.
