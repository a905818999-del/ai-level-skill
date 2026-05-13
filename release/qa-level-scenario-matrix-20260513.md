# AI Level Scenario Matrix QA

Date: 2026-05-13
Scope: current `ai-level` skill v0.1.1
Mode: self-question / self-answer simulation plus strict reviewer pass

## QA Goal

Test whether the current diagnostic design can distinguish every level from Lv.0 to Lv.10 across every currently implemented scenario bank.

Current scenario banks in `ai-level/references/diagnostic-flow.md`:

- Scenario A: Family Travel
- Scenario B: Home Move / Setup
- Scenario C: Learning / Exam Plan
- Scenario D: Messy Work Problem

Historical caveat:

- This report was written before the expanded `scenario-bank.md` implementation.
- It tests the v0.1.1 shipped scenario set. See `release/scenario-bank-full-review-20260513.md` for the expanded bank review.

## Overall Verdict

DONE_WITH_CONCERNS.

The current skill can reasonably separate Lv.3-Lv.7 and can avoid obvious Lv.8 inflation when the anchor follow-up is used well.

It is weak for:

- Lv.0-Lv.2: the scenarios are too heavy and assume the user can imagine practical AI usage.
- Lv.8-Lv.10: one practical scenario cannot confirm repeated artifact creation, method ownership, or team-level operating systems.
- Scenario diversity: all four current prompts use the same "你会怎么做" shape, so answers may look similar across banks.
- Baseline routing: current implementation has baseline questions, but no explicit route band or difficulty selection yet.

## Test Matrix Summary

Legend:

- OK: scenario can expose this level.
- WEAK: scenario can approximate this level but needs better routing or follow-up.
- POOR: scenario is not appropriate for this level.

| Level | Family Travel | Home Move | Learning Plan | Messy Work | Reviewer Note |
| --- | --- | --- | --- | --- | --- |
| Lv.0 | WEAK | POOR | WEAK | POOR | Too much task framing for non-users. Needs a "how would you even start" lane. |
| Lv.1 | WEAK | WEAK | WEAK | POOR | Can answer "ask AI directly", but work scenario feels unnatural. |
| Lv.2 | OK | WEAK | OK | WEAK | Follow-up behavior can be seen, but prompts do not explicitly invite iteration. |
| Lv.3 | OK | OK | OK | OK | Constraints, formats, and examples are easy to observe. |
| Lv.4 | OK | OK | OK | OK | Good for seeing unfamiliar-domain exploration. |
| Lv.5 | OK | OK | OK | OK | Staged workflows show clearly in all scenarios. |
| Lv.6 | OK | OK | OK | OK | Tool/source/agent use can appear naturally. |
| Lv.7 | OK | OK | WEAK | OK | Reusable system design is strongest in travel/work, weaker in learning unless prompt nudges repeatability. |
| Lv.8 | WEAK | WEAK | WEAK | WEAK | Needs real artifact/reuse evidence; scenario alone cannot confirm. |
| Lv.9 | POOR | POOR | WEAK | WEAK | Needs cross-domain method and human/AI boundary evidence. |
| Lv.10 | POOR | POOR | POOR | POOR | Cannot confirm from one scenario. Needs portfolio/system evidence. |

## Self-Question / Self-Answer Samples By Level

These are compact simulations. Each sample was mentally run across the four scenarios; scenario-specific notes are below.

### Lv.0: Observer

Baseline:

```text
1A 2A 3A
```

Typical answer:

```text
我可能不会用 AI，或者让别人帮我查一下。最多问一句“帮我做个计划”。
```

Expected judgment:

- Signal: Lv.0-Lv.1
- Confirmed: Lv.0 or Lv.1
- Evidence: E0

Strict review:

- Current scenarios are too elaborate for this user.
- The skill may make them feel like the test is not for them.
- Need a basic lane: "如果你只会问一句，你会怎么问？拿到回答后你会不会改？"

### Lv.1: Fresh Tryer

Baseline:

```text
1B 2A 3A
```

Typical answer:

```text
我会问 AI：帮我安排一下。不好就换个说法再问一次。
```

Expected judgment:

- Signal: Lv.1-Lv.2
- Confirmed: Lv.1
- Evidence: E1

Strict review:

- Travel and learning scenarios can show this.
- Home move and messy work are too loaded; user may answer with social desirability instead of real behavior.

### Lv.2: Conversational Improver

Baseline:

```text
1B 2B 3A
```

Typical answer:

```text
我会先让 AI 出一个方案，如果不满意就告诉它太累、太贵、太笼统，让它重新改。
```

Expected judgment:

- Signal: Lv.2
- Confirmed: Lv.2
- Evidence: E1

Strict review:

- Current scenarios can catch "follow-up correction".
- But scoring guide starts visible mapping at Lv.3; low-level reporting needs clearer wording for Lv.0-Lv.2.

### Lv.3: Prompt Controller

Baseline:

```text
1B 2C 3B
```

Typical answer:

```text
我会告诉 AI 预算、人数、时间、偏好，让它用表格输出，给我 3 个方案，每个方案列优缺点。
```

Expected judgment:

- Signal: Lv.3
- Confirmed: Lv.3
- Evidence: E1

Strict review:

- All four scenarios can identify Lv.3.
- Risk: if the user says "三个方案 + 表格" in every scenario, reports may sound repetitive unless scenario-specific examples are used.

### Lv.4: Boundary Crosser

Baseline:

```text
1C 2C 3B
```

Typical answer:

```text
这事我不熟，所以会让 AI 先解释有哪些选择、风险和常见坑，再帮我比较方案。
```

Expected judgment:

- Signal: Lv.4
- Confirmed: Lv.4
- Evidence: E1

Strict review:

- Learning and home move are good Lv.4 tests.
- Messy work can overstate capability because workplace language sounds more advanced than actual AI behavior.

### Lv.5: Workflow Builder

Baseline:

```text
1C 2CD 3C
```

Typical answer:

```text
我会先让 AI 问我缺哪些信息，再分成信息收集、方案比较、执行清单、风险检查四步。最后用一个检查表看有没有遗漏。
```

Expected judgment:

- Signal: Lv.5
- Confirmed: Lv.5
- Evidence: E1-E2

Strict review:

- Current scenarios are strongest at Lv.5.
- This is the cleanest level for the existing design.
- Need avoid accidentally calling Lv.5 "Lv.6" just because user says "找资料".

### Lv.6: Agent / Tool User

Baseline:

```text
1C 2D 3C
```

Typical answer:

```text
我会让 AI 搜网页、查资料、读表格或调用工具，把路线、价格、评论、资料都整理出来，再让我确认。
```

Expected judgment:

- Signal: Lv.6
- Confirmed: Lv.6 if validation is concrete
- Evidence: E2

Strict review:

- All scenarios can expose Lv.6.
- Main risk: tool names can inflate score.
- The anchor should ask "怎么确认工具真的被调用" whenever Agent/MCP/browser is mentioned.

### Lv.7: Skill / System Designer

Baseline:

```text
1D 2CD 3D
```

Typical answer:

```text
我会把这件事做成一个流程：先收集输入，再调用信息源，再出候选方案，再按规则校验，最后输出 HTML 或模板，下次复用。
```

Expected judgment:

- Signal: Lv.7-Lv.8
- Confirmed: Lv.7 if inputs/checks/failure handling are clear
- Evidence: E2-E3 depending on artifact

Strict review:

- Current anchor follow-up handles this level best.
- But only travel has a concrete tuned follow-up. Home move, learning, and messy work need equivalent domain-specific anchors.

### Lv.8: Creator

Baseline:

```text
1D 2D 3D
```

Typical answer:

```text
我已经跑过这个流程两次。第一次生成了方案，第二次我加了来源时间、风险项和复盘字段。现在同类任务我会直接套这个模板。
```

Expected judgment:

- Signal: Lv.8
- Confirmed: Lv.8 only if artifact/reuse evidence is specific
- Evidence: E4

Strict review:

- Current practical scenarios can invite Lv.8 evidence but cannot force it.
- Need a "show me the second run" style follow-up:
  - 第一次跑出了什么？
  - 第二次改了什么？
  - 哪个字段或检查项是失败后加进去的？

### Lv.9: Method Owner

Baseline:

```text
1D 2D 3D
```

Typical answer:

```text
我有一套原则：AI 负责扩展选项、整理信息、提出反方意见；我负责定目标、排序冲突、做最终判断。旅行、采购、学习和工作推进我都会用类似结构。
```

Expected judgment:

- Signal: Lv.9
- Confirmed: Lv.8-Lv.9 only with cross-domain evidence
- Evidence: E5 or strong real-case set

Strict review:

- Existing scenarios are not enough.
- Need a method lane that explicitly asks cross-domain transfer and human/AI boundary.

### Lv.10: One-Person Team

Baseline:

```text
1D 2D 3D
```

Typical answer:

```text
我维护一组 Skill、模板、知识库和检查标准，覆盖研究、写作、分析、自动化和交付。团队里其他人也能直接用，我会持续更新。
```

Expected judgment:

- Signal: Lv.10
- Confirmed: Lv.10 only with multiple artifacts, team use, or repeatable operating system evidence
- Evidence: E5

Strict review:

- Current test should almost never confirm Lv.10.
- If it confirms Lv.10 from one场景回答，就是严重虚高。

## Scenario-by-Scenario Review

### Scenario A: Family Travel

Strengths:

- Very accessible.
- Good for Lv.3-Lv.7.
- Naturally exposes sources, tool use, tradeoffs, output artifacts, and human preferences.

Weaknesses:

- Overused. Same group testing multiple times会显得固定。
- Tuned anchor is travel-specific, which makes other scenarios look less polished.
- For Lv.8+, travel alone cannot prove repeated system creation.

Best levels:

- Lv.3-Lv.7.

Worst levels:

- Lv.0, Lv.9, Lv.10.

Reviewer demand:

- Keep it as default, but stop treating it as the whole test.

### Scenario B: Home Move / Setup

Strengths:

- Good practical pressure: budget, procurement, schedule, installation risk, family constraints.
- Better than travel for testing operational planning.

Weaknesses:

- Current wording still feels like a task assignment.
- It does not naturally ask for reuse unless the user is already high-level.
- Needs a domain-specific anchor around delivery times, installation risk, return policy, and "day-of chaos" fallback.

Best levels:

- Lv.4-Lv.6.

Potential Lv.7:

- If user turns it into a reusable procurement / move checklist.

Reviewer demand:

- Rewrite the prompt to feel more like "我真的要搬家，脑子已经乱了" instead of a requirements doc.

### Scenario C: Learning / Exam Plan

Strengths:

- Good for Lv.2-Lv.5 because users can describe feedback, revision, and weekly review.
- Good for testing whether the user avoids unrealistic AI-generated plans.

Weaknesses:

- Weak for Lv.6 because external source/tool pressure is lower unless the user brings it up.
- Weak for Lv.7 unless framed as a reusable learning coach workflow.
- High-level users may answer in generic productivity language, making scoring fuzzy.

Best levels:

- Lv.2-Lv.5.

Potential Lv.7:

- If redesigned as "create a reusable 8-week learning coach flow."

Reviewer demand:

- Add a high-lane variant that asks for diagnosis, weekly instrumentation, test feedback, and plan adjustment.

### Scenario D: Messy Work Problem

Strengths:

- Best current scenario for high-level workplace AI use.
- Naturally exposes file reading, synthesis, stakeholder conflict, output artifacts, and collaboration.

Weaknesses:

- Too abstract for lower-level users.
- It can reward corporate-sounding answers that are not actually AI-capable.
- Needs stronger anti-bluff follow-up: "which inputs, what artifact, what decision owner, what changes after stakeholder feedback."

Best levels:

- Lv.5-Lv.8 signal.

Worst levels:

- Lv.0-Lv.2.

Reviewer demand:

- Use only after baseline suggests workflow/tool maturity, not as a universal default.

## Cross-Level Failure Modes

### Issue 1: No Explicit Baseline Routing

Severity: High.

The baseline questions currently provide "ceilings and context", but they do not explicitly select a diagnostic lane.

Impact:

- Low-level users may get scenarios that feel too hard.
- High-level users may get a generic scenario that does not pressure Lv.8-Lv.10 evidence.

Fix:

- Implement the route bands from `.omx/plans/plan-scenario-bank-ab.md`:
  - basic
  - workflow
  - system
  - method

### Issue 2: Lv.0-Lv.2 Are Under-Designed

Severity: Medium.

The welcome page names Lv.0-Lv.2, but the scenario design mostly starts at Lv.3.

Impact:

- Reports may be awkward for non-users.
- The test may feel alienating to people who are just starting.

Fix:

- Add one basic-lane prompt:

```text
你现在有一件小事想让 AI 帮忙，但你还不太会用。
你会怎么问？拿到一个不满意的回答后，你会怎么改问？
```

### Issue 3: Lv.8 Confirmation Needs Artifact / Reuse Probe

Severity: High.

The rubric correctly says Lv.8 needs reuse or iteration evidence, but the flow does not force that evidence unless the model remembers to ask.

Impact:

- A polished Lv.7 answer can be mistaken for Lv.8.

Fix:

- For any Lv.8 signal, ask one of:
  - "这套流程跑过几次？第二次比第一次改了什么？"
  - "有没有一个别人能打开使用的产物？"
  - "哪条规则是踩坑后加进去的？"

### Issue 4: Scenario Anchors Are Uneven

Severity: Medium.

Travel has a strong tuned anchor. The other three scenarios rely on generic composer logic.

Impact:

- The user experience quality varies by scenario.

Fix:

- Add tuned anchor examples for:
  - Home Move
  - Learning Plan
  - Messy Work

### Issue 5: Work Scenario Can Over-Reward Fluent Talk

Severity: Medium.

"整理信息、对齐诉求、形成方案" sounds advanced even when the user has no concrete AI workflow.

Impact:

- Messy Work may inflate Lv.5-Lv.6 answers.

Fix:

- Require concrete evidence:
  - What files or inputs?
  - What intermediate artifact?
  - How are conflicts resolved?
  - What does AI draft, and what must human decide?

## Required QA Cases For Next Version

Add these to `calibration-cases.md` after scenario-bank implementation.

### Case A: High Baseline, Weak Practical Answer

Baseline:

```text
1D 2D 3D
```

Answer:

```text
我会让 Agent 搜资料，然后生成结果。不行就再改。以后做成 Skill。
```

Expected:

- Signal: Lv.6-Lv.7
- Confirmed: Lv.6
- Reason: tool names and Skill claim without concrete workflow design.

### Case B: Low Baseline, Strong Practical Answer

Baseline:

```text
1B 2C 3A
```

Answer:

```text
我不常用 AI，但这次我会先整理目标、限制和已有资料，让 AI 问我还缺什么。然后分三步做：找选项、比较优缺点、生成执行清单。我会自己核对价格和时间。
```

Expected:

- Signal: Lv.5
- Confirmed: Lv.4-Lv.5
- Reason: baseline modest but practical structure is real. Allow upgrade.

### Case C: Lv.8 Claim Without Reuse

Answer:

```text
我会设计一个完整系统，有输入、检查、输出和 HTML 页面。
```

Expected:

- Signal: Lv.7-Lv.8
- Confirmed: Lv.7 max
- Reason: no evidence it has run, reused, or improved.

### Case D: Real Lv.8 Evidence

Answer:

```text
我跑过两次。第一次只是输出方案，后来发现酒店评论过期，所以第二版加了来源时间和人工确认字段。第三次别人直接拿模板填输入就能用。
```

Expected:

- Signal: Lv.8
- Confirmed: Lv.8 if details are credible
- Evidence: E4-E5 depending on artifact/team use.

### Case E: Lv.9 Signal But Not Confirmed

Answer:

```text
我的方法是 AI 做研究、反方和整理，我做人类判断。旅行、采购、学习、项目推进都用这一套。
```

Expected:

- Signal: Lv.9
- Confirmed: Lv.8-Lv.9 depending on real examples
- Reason: method language is promising, but needs cross-domain evidence.

### Case F: Messy Work Fluent Bluff

Answer:

```text
我会让 AI 对齐各方诉求，形成统一认知，沉淀行动方案，推进闭环。
```

Expected:

- Signal: Lv.4-Lv.5
- Confirmed: Lv.4
- Reason: no inputs, no tools, no validation, no artifact details.

## Ship Readiness For Scenario Expansion

Before implementing expanded scenario library:

- Add baseline route bands.
- Add `scenario-bank.md`.
- Add per-lane scenario prompts.
- Add tuned anchor examples for non-travel scenarios.
- Add anti-inflation calibration cases.
- Extend `sample_run.py` beyond the single travel Lv.7 case.

Suggested release target:

- v0.1.2 should not try to support perfect Lv.10 confirmation.
- v0.1.2 should target accurate Lv.3-Lv.8 separation and explicitly treat Lv.9-Lv.10 as "signal only unless evidence is strong."

## Final Reviewer Verdict

The current skill is good enough for a first public share among colleagues, but the next quality jump is not "more examples" alone.

The next quality jump is:

```text
baseline route band -> lane-specific scenario -> adaptive anchor -> evidence-gated report
```

Without that, adding more scenes will make the skill feel richer but not necessarily more accurate.
