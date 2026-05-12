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

Ask the scenario exactly or lightly adapt it to the user's context.

```text
你要安排一次 5 天家庭旅行。

基本情况：
- 同行人包括老人、小孩和成年人，大家体力和兴趣不同。
- 预算有限，希望兼顾舒适度和性价比。
- 时间在下个月，天气、人流、交通住宿都有不确定性。
- 你希望最后得到一份能直接执行的旅行方案。

如果你准备用 AI 帮你把这件事做好，你会怎么做？
```

Do not add hints such as "how would you verify" or "what tools would you use" unless the user asks for clarification. The purpose is to see what the user brings up unprompted.

## Adaptive Anchor Follow-Up

Ask one anchor follow-up when the main answer shows Lv.7+ signals, especially if the user mentions Agent, Skill, workflow, MCP, automation, scripts, or reusable systems.

Do not preface the follow-up with internal evaluation like "your answer has advanced signals" or "I need to verify whether this is bluffing." Ask the anchor directly.

Construct the follow-up from the user's own claim:

```text
你刚才提到【用户的高阶做法】。

请把它落成一个别人可以复用的执行说明：

- 输入是什么？
- 处理步骤是什么？
- 需要哪些外部资料或工具？
- 哪些地方最容易出错？
- 你怎么验证？
- 最后产物长什么样？
- 下次如何复用或改进？
```

For travel-planning answers that mention skills or agents, use:

```text
你提到会把这件事做成 skill / Agent 流程，并调用外部信息源。

我想看一下你会怎么把它真正落地。请具体说明这个流程：

- 需要哪些输入？
- 会调用哪些信息源？每个信息源解决什么问题？
- 哪些信息必须标注来源和查询时间？
- 生成方案前，要先做哪几个判断？
- 方案完成后，你会用什么规则检查它是否靠谱？
- 如果老人觉得太累、小孩觉得无聊、预算超支，你会如何让 AI 调整？
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
