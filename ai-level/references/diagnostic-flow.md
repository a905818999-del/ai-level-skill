# Diagnostic Flow

## Welcome Page

Show this before asking any questions.

```text
欢迎来到 AI 应用等级测试。

这个测试不是让你自评“我有多会用 AI”，而是通过一个简单场景，看你会如何把 AI 用到真实问题里。

等级大致分成 10 级：

Lv.0 旁观者：知道 AI，但基本没用过。
Lv.1 尝鲜者：偶尔问 AI，要什么给什么。
Lv.2 对话者：会追问、补充背景，让回答变好。
Lv.3 驯化师：会给约束、格式、例子，能控制输出质量。
Lv.4 越境者：开始用 AI 做自己不熟悉领域的事。
Lv.5 织网者：把 AI 嵌入固定流程，有模板和检查清单。
Lv.6 召唤师：会用 Agent、工具或外部资料完成多步任务。
Lv.7 铸造师：会设计自己的 Skill、Agent 流程或复用系统。
Lv.8 造物主：能持续产出可用作品、工具或系统，并不断复用改进。
Lv.9 觉醒者：形成自己的人机协作方法论，知道哪些交给 AI，哪些必须自己判断。
Lv.10 一人军团：有成熟的 AI 工作系统，一个人能完成过去一个小团队的产出。

测试怎么进行：
1. 先用 3 个小问题了解你的基础使用情况。
2. 再给你一个生活综合场景，看你会怎么用 AI 解决。
3. 如果有些地方需要看得更清楚，会补一个追问。
4. 最后给出等级区间、确认等级、判断依据和下一步建议。

选择题说明：
- 第 1 题单选。
- 第 2 题可以选 1-2 个最符合你的做法。
- 第 3 题单选，选你已经稳定做到的最高一项。

没有标准答案。请按你真实会做的方式回答。
```

## Baseline Gate Questions

Ask these quickly before the practical scenario. They are not the main test; they provide ceilings and context.

Tell the user: "直接写选项即可，例如 `1C 2CD 3D`。第 2 题可以多选，其余题单选。"

1. In the past 30 days, have you used AI for a real task? Single-select.
   - A. Rarely or not at all
   - B. Yes, mostly for writing, summarizing, translation, or search-like help
   - C. Yes, for real work or life decisions where the output was used
   - D. Yes, repeatedly, with templates, tools, workflows, or agents

2. When AI gives a weak or unreliable answer, what do you usually do? Choose up to two.
   - A. Ask again or switch tools
   - B. Ask it to be more detailed
   - C. Add context, constraints, examples, or output format
   - D. Split the task, require sources, mark uncertainty, and verify key facts

3. Have you ever turned an AI usage pattern into something reusable? Single-select; choose the highest option you have actually done.
   - A. No
   - B. I have saved prompts or examples
   - C. I have a checklist, template, or repeated workflow
   - D. I have built or used Agent/Skill/MCP/tool workflows for repeated tasks

## Main Practical Scenario

Do not hard-code one question forever. Use the travel scenario as the default because it is easy for most people to answer, but rotate scenarios when the same group is testing repeatedly, when the user asks whether there are other cases, or when the user's context clearly fits another scenario.

Pick one scenario. Do not ask all of them.

### Scenario A: Family Travel

```text
你要安排一次 5 天家庭旅行。

基本情况：
- 同行人包括老人、小孩和成年人，大家体力和兴趣不同。
- 预算有限，希望兼顾舒适度和性价比。
- 时间在下个月，天气、人流、交通住宿都有不确定性。
- 你希望最后得到一份能直接执行的旅行方案。

如果你准备用 AI 帮你把这件事做好，你会怎么做？
```

### Scenario B: Home Move / Setup

```text
你要在 3 周内完成一次搬家和新家配置。

基本情况：
- 家里有老人或小孩，搬家当天不能太混乱。
- 预算有限，但希望家具、电器、网络、水电、收纳都尽快到位。
- 需要比较平台、价格、配送时间、安装风险和售后。
- 你希望最后得到一份能执行的搬家计划、采购清单和风险预案。

如果你准备用 AI 帮你把这件事做好，你会怎么做？
```

### Scenario C: Learning / Exam Plan

```text
你要帮一个人制定 8 周学习计划。

基本情况：
- 他时间不稳定，基础也不均衡。
- 目标比较明确，但不知道从哪里开始。
- 需要找资料、安排练习、检查进度，还要避免计划太理想化。
- 你希望最后得到一套能每周执行和复盘的学习方案。

如果你准备用 AI 帮你把这件事做好，你会怎么做？
```

### Scenario D: Messy Work Problem

```text
你要把一件混乱的工作推进清楚。

基本情况：
- 相关信息散在聊天记录、文档、表格和网页里。
- 多个人有不同诉求，优先级不完全一致。
- 你需要先理清现状，再形成方案、行动清单和对外说明。
- 你希望最后得到一份别人看得懂、能继续协作的交付物。

如果你准备用 AI 帮你把这件事做好，你会怎么做？
```

Do not add hints such as "how would you verify" or "what tools would you use" unless the user asks for clarification. The purpose is to see what the user brings up unprompted.

## Adaptive Anchor Follow-Up

Ask one anchor follow-up when the main answer shows Lv.7+ signals, especially if the user mentions Agent, Skill, workflow, MCP, automation, scripts, or reusable systems.

Do not preface the follow-up with internal evaluation like "your answer has advanced signals" or "I need to verify whether this is bluffing." Ask the anchor directly.

Construct the follow-up from the user's own claim. The follow-up is not a fixed checklist. It should prove that you read the first answer.

### Follow-Up Composer

1. Start with one sentence naming what the user already covered.
2. Identify the missing evidence gaps from this list:
   - Success standard: what counts as a good result, and what tradeoff wins when goals conflict.
   - Source rules: which facts need source, timestamp, or human confirmation.
   - Tool-use proof: how to detect whether an agent really called a tool instead of pretending.
   - Validation rules: how the user checks hallucination, stale data, route/budget conflicts, or bad recommendations.
   - Feedback loop: how feedback is structured so the next version gets better, not just "try again".
   - Reuse evidence: whether the flow becomes a template, skill, artifact, or improved second run.
3. Ask only the top 2-3 missing gaps. Do not re-ask about things already answered.
4. If the user already described many tools, do not ask "which tools" again. Ask how those tools are verified and orchestrated.
5. If the user already described validation, ask for the exact rule or threshold, not "how do you validate?"

Generic shape:

```text
你刚才已经说清楚了【用户已覆盖内容】。

我只追问几个还没看清的点：

1. 【缺口 1】
2. 【缺口 2】
3. 【缺口 3】

不用写长，按你真实会怎么做回答就行。
```

For travel-planning answers that mention skills or agents, adapt from this, but delete bullets already covered:

```text
你已经说了会用 workbuddy / openclaw 调用 12306、小红书、浏览器等信息源，最后生成 HTML，也可能沉淀成 skill。

我只追三个还没看清的点：

1. 如果“老人不累、小孩开心、预算不爆、你自己也想玩”发生冲突，你会让 AI 按什么顺序取舍？
2. 你会怎么确认 Agent 真的调用了 12306 / 携程 / 浏览器，而不是只编了一个看起来像真的结果？
3. 你说会反馈微调。这个反馈是随口说“再改改”，还是有固定检查项，比如步行强度、预算偏差、来源新鲜度、每天兴趣点？
```

## When To Skip The Anchor

Skip the anchor if:

- The answer is clearly Lv.3-Lv.5.
- The user only wants a quick estimate.
- The baseline answers already cap the user below Lv.6.

## Minimal Run

If time is short:

1. Ask only the main scenario.
2. If the answer has Lv.7+ signals, ask one anchor follow-up.
3. Output range, confirmed level, evidence strength, and next advice.
