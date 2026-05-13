# Scoring Guide

## Dimensions

Score each dimension from 0 to 3.

| Dimension | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| Context | Generic ask | Adds basic constraints | Specifies missing inputs | Designs input collection |
| Decomposition | One-shot prompt | Requests sections | Breaks into stages | Designs repeatable pipeline |
| Verification | Trusts output | Checks obvious facts | Requires sources/uncertainty | Builds explicit validation rules |
| Tooling | Chat only | Uses AI app features | Uses tools/agents/sources | Designs tool chain with roles |
| Reuse | One-off | Saves prompt | Uses template/checklist | Builds skill/workflow/system |
| Judgment | Lets AI decide | Picks among options | Defines tradeoffs | States human decision principles |

## Level Mapping

Use the table as a guide, then apply evidence gates from `rubric.md`.

| Pattern | Signal level |
| --- | --- |
| No practical AI use, or only awareness | Lv.0-Lv.1 |
| One-shot asks and simple retries | Lv.1-Lv.2 |
| Follow-up correction without much structure | Lv.2 |
| Mostly generic prompt, some constraints | Lv.3 |
| Uses AI to explore unfamiliar options | Lv.4 |
| Breaks task into stages and templates | Lv.5 |
| Uses external tools, sources, or agents | Lv.6 |
| Designs reusable skill/workflow with validation | Lv.7 |
| Shows real artifact, reuse, iteration | Lv.8 |
| Explains method, human/AI boundaries, transfer across domains | Lv.9 |
| Mature multi-domain personal/team operating system | Lv.10 |

## Baseline Routing

Baseline choices are for scenario selection, not grading.

- `basic`: use when the user has little recent AI usage or mostly retries/simple asks.
- `workflow`: use when the user uses AI for real tasks and can add context, steps, or checks.
- `system`: use when the user mentions tools, agents, MCP, automation, templates, or reusable workflows.
- `method`: use only when the user has real reuse, artifacts, cross-domain examples, team use, or explicit human/AI boundary thinking.

The final report should not say "your baseline route is system". It should only report signal level, confirmed level, and evidence strength.

## Ceilings

- If there is no real AI usage in the past 30 days, confirmed level should not exceed Lv.4.
- If the user cannot explain validation, confirmed level should not exceed Lv.6.
- If the user cannot explain reuse, confirmed level should not exceed Lv.7.
- If the user explains a reusable workflow in concrete inputs, steps, checks, and failure handling, confirmed weak Lv.7 is acceptable even before an artifact exists.
- If there is no real artifact or case evidence, confirmed level should not exceed Lv.7.
- If there is no reuse/iteration evidence, confirmed level should not exceed Lv.8 signal.
- If there is no method or influence evidence, do not confirm Lv.9-Lv.10.

## Report Style

Use plain language with a light Weibo/Xiaohongshu feel:

- Lead with a clean conclusion.
- Use short paragraphs and crisp bullets.
- Make the user feel "this is about me" without flattery.
- Avoid internal scoring narration.
- Avoid stiff labels unless they help clarity.
- Do not use mystical, grandiose, or status-heavy language.

## Report Template

```text
你的 AI 应用等级：Lv.X-Lv.Y｜确认 Lv.X
证据强度：E_

一句话：
……

为什么这么判：
- ……
- ……
- ……

离下一级差在哪：
……

下一步怎么升：
……

一个小挑战：
……
```

## Lane-Specific Report Guidance

Use the same final report structure, but adjust the gap diagnosis by route. Do not expose route labels to the user.

### Basic Users

Use when the user is around Lv.0-Lv.3.

Tone:

- Gentle and practical.
- No shame, no "you are behind".
- Do not recommend Agent, MCP, Skill, automation, or complex workflows.

Core message:

```text
你现在最值得练的不是工具，而是把问题说清楚：对象、背景、限制、例子、想要的格式。
```

Good next challenge:

```text
找一个低风险小任务，连续改问 3 次：第一次直接问，第二次补背景，第三次加格式和例子。比较三次答案差在哪里。
```

### Workflow Users

Use when the user is around Lv.3-Lv.6.

Tone:

- Encourage real task use, but push toward structure.
- Name the user's ability to turn a vague task into stages.

Core message:

```text
你已经不只是会问了，开始会把任务拆开。下一步是把拆法固定下来：输入清单、步骤、输出格式、检查项。
```

Good next challenge:

```text
把一个重复任务写成一页流程：开始前需要什么、AI 做哪几步、你检查什么、最后产出什么。
```

### System Users

Use when the user is around Lv.6-Lv.8 signal.

Tone:

- Be stricter.
- Distinguish tool use from system design.
- Do not flatter tool-name dropping.

Core message:

```text
会调用工具是 Lv.6 信号；能规定工具怎么协作、怎么校验、失败后怎么改，才接近 Lv.7。
```

Lv.8 gate:

```text
Lv.8 看的不是你会不会设计流程，而是这个流程有没有真实跑过、复用过、失败后改过。
```

Good next challenge:

```text
把同一个流程跑两次。第二次必须记录：哪条规则是第一次踩坑后加的，哪个字段让结果更可靠。
```

### Method Users

Use when the user shows Lv.8-Lv.10 signals.

Tone:

- Respectful but strict.
- Treat method language as signal, not proof.
- Ask for cross-domain evidence and other-user evidence.

Core message:

```text
你已经在谈方法了，但方法要靠证据站住：跨场景案例、真实产物、复用记录、别人能不能照着用。
```

Lv.9/Lv.10 gate:

```text
Lv.9 要看到稳定的人机分工原则；Lv.10 要看到多领域系统和他人可用性。一个漂亮案例不够。
```

Good next challenge:

```text
选两个不同领域的 AI 流程，各写一张操作卡：AI 负责什么、人负责什么、校验什么、失败后改过什么。能被别人照着跑，才继续看 Lv.10。
```

## Next-Level Advice

### Lv.3 -> Lv.4

Advice: Pick a low-risk task outside your usual domain and use AI to produce a real artifact. The goal is not a perfect answer; the goal is to cross a boundary.

### Lv.4 -> Lv.5

Advice: Turn one repeated task into a simple workflow: input list, AI steps, output format, and check list.

### Lv.5 -> Lv.6

Advice: Give one multi-step task to an AI tool or agent that can read files, browse, search, or manipulate a document/table. Keep human review at the end.

### Lv.6 -> Lv.7

Advice: Stop treating the agent run as a one-off. Write the process down so another person or future you can run it again.

### Lv.7 -> Lv.8

Plain-language advice:

```text
你离 Lv.8 差的不是工具，而是“稳定产出”。

Lv.7 的核心是：我能搭一个 AI 流程。
Lv.8 的核心是：这个流程真的跑过、产出过、复用过，而且第二次会比第一次更稳。

你现在已经会想到 Agent、Skill、MCP、外部信息源和 HTML 交付，这很像 Lv.7。
但 Lv.8 要看的不是“我会搭”，而是：

- 这套流程有没有真的跑完一次？
- 跑完之后有没有留下可复用的结构？
- 下次再做类似任务时，是不是可以少想很多？
- 信息错误、偏好冲突、预算超支时，它有没有调整机制？

推荐你做一个更有意思的小挑战：

把这次旅行规划做成一个“可分享的旅行决策页”，而不是普通攻略。

它不需要很复杂，只要包含：
- 2-3 个候选方案，让同行人可以比较。
- 每个方案的适合人群、风险点和放弃理由。
- 关键事实的来源和查询时间。
- 一个“如果老人累 / 小孩无聊 / 预算超支”的备用按钮或备用段落。
- 跑完后记录一句：下次这个流程哪里可以直接复用。

做到这里，你就不是“会用 AI 做旅行规划”，而是开始拥有一个能反复生长的小系统。
```

Authority framing:

```text
大佬视角会这么看：你现在不缺执行力，缺的是决策标准。

Agent 能帮你跑资料、出方案、做页面，但它不知道你真正认为什么叫“好”。这个标准如果不写进去，系统跑得越快，只是越快地产出一堆看起来不错、但不一定适合你的东西。

往 Lv.8 走，重点不是再接一个工具，而是把三件事钉住：

1. 先定取舍顺序。
老人不累、小孩开心、预算不爆、路线顺，这些都对，但不能并列第一。你要先给系统一个排序，否则它只会做平均分方案。

2. 把校验前置。
不要等方案出来以后再人工挑错。直接要求每个关键结论带来源、查询时间、风险标记和待确认项。好系统不是少犯错，而是让错误更容易被抓住。

3. 留下结构，不要只留下结果。
一次旅行攻略没什么价值。真正有价值的是：下次任何“多人、多偏好、多约束”的决策，都能复用这套输入、排序、校验、输出结构。

一句话：Lv.8 不是让 AI 多干活，是让 AI 按你的标准干活。

大佬的实际操作会更像这样：

1. 先写一条决策原则，而不是先搜攻略。
示例：这次旅行宁可少玩两个点，也不能让老人累崩；孩子每天必须有一个期待点；预算可以浮动 10%，但不能靠牺牲住宿安全感来省钱。

2. 让 Agent 先出“决策表”，不是直接出行程。
表里至少有：方案、适合谁、不适合谁、最大风险、证据来源、需要人工确认的地方。先选方向，再排行程。

3. 给每个方案加一个反方评审。
让 AI 专门挑刺：这个方案为什么可能失败？老人会在哪里累？孩子会在哪里无聊？预算最容易在哪里失控？

4. 最后再生成分享页。
分享页不是展示“攻略多丰富”，而是让同行人快速确认：我们为什么选这个方案，放弃了什么，风险在哪里，备选是什么。
```

### Lv.8 -> Lv.9

Advice: Write down your AI collaboration principles. What do you always delegate? What do you never delegate? How do you verify? Where must your own judgment enter?

### Lv.9 -> Lv.10

Advice: Make your method usable by others. Turn your workflows, standards, and review principles into a small operating system: templates, skills, examples, review rules, and onboarding notes.

## Tone Rules

- Say "confirmed level" instead of "true level".
- Say "signal" when evidence is promising but incomplete.
- Avoid status language like "advanced user" unless necessary.
- Do not embarrass the user. The report should make improvement feel reachable.
- For Lv.7+ users, explain the next level's core criterion before giving advice.
- Make recommended actions feel like an interesting challenge or artifact, not homework.
- When explaining gaps, avoid making it sound like a deduction. Prefer "the next upgrade point is..." and pair each observation with a concrete move.
