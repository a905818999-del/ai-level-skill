# Scenario Bank Full Review

Date: 2026-05-13
Scope: expanded `ai-level/references/scenario-bank.md`
Reviewer stance: life-rich, top-tier AI operator, strict anti-inflation

## Verdict

DONE_WITH_CONCERNS.

The expanded bank now covers Lv.0-Lv.10 signals, but it should be used as a routed diagnostic, not a flat list.

The strongest shape is:

```text
baseline route -> one matching scenario -> adaptive anchor -> evidence-gated report
```

## Coverage Matrix

| Level | Best scenarios | Review |
| --- | --- | --- |
| Lv.0 | First Real Ask | Good. This finally gives non-users a humane entry point. |
| Lv.1 | First Real Ask, Weekend Plan | Good. Can show one-shot asking and simple retry. |
| Lv.2 | First Real Ask, Weekend Plan, Learning Sprint | Good. Can show follow-up correction. |
| Lv.3 | Family Purchase, Weekend Plan, Family Travel | Good. Constraints, formats, and examples are visible. |
| Lv.4 | Family Purchase, Home Move, Learning Sprint | Good. Tests unfamiliar-domain exploration. |
| Lv.5 | Home Move, Learning Sprint, Messy Work | Strong. Workflow thinking shows clearly. |
| Lv.6 | Family Travel, Messy Work, Workflow Automation | Strong, but tool-name inflation must be watched. |
| Lv.7 | Workflow Automation, Knowledge Product, Messy Work | Strong. Best tested by reusable structure and validation. |
| Lv.8 | Workflow Automation, Knowledge Product, Personal AI Operating System | Usable only with artifact/reuse/iteration evidence. |
| Lv.9 | Personal AI Operating System, Plan Breakdown Crisis | Signal only unless cross-domain method evidence appears. |
| Lv.10 | Personal AI Operating System | Very strict. Requires multi-domain operating system and other-user evidence. |

## Scenario Reviews

### 1. First Real Ask

Good for: Lv.0-Lv.3.

Why it works:

- It does not assume the user already understands workflows.
- It tests whether the user can move from one-shot asking to iterative correction.

Main risk:

- Too easy for middle users. Do not use when baseline shows Q2 C/D or Q3 C/D unless the user explicitly says they are a beginner.

Reviewer call:

- Keep. This fixes the old beginner blind spot.

### 2. Family Travel 2.0

Good for: Lv.3-Lv.8 signal.

Why it works:

- Real constraints are emotionally legible: elderly comfort, child interest, budget, weather, transport.
- It naturally exposes tradeoff standards and source freshness.

Main risk:

- It is now familiar from previous testing. Repeated use in the same group will feel fixed.

Reviewer call:

- Keep as default, but rotate after first use.

### 3. Home Move And New Setup

Good for: Lv.3-Lv.7.

Why it works:

- Tests operations: procurement, sequence, installation, delivery, day-of chaos.
- It is less "tourism tool" biased than travel.

Main risk:

- Can become a generic project-management answer.

Reviewer call:

- Good workflow lane scenario. Anchor should ask about date verification, purchase risk, and fallback.

### 4. Expensive Family Purchase

Good for: Lv.2-Lv.6.

Why it works:

- Almost everyone understands the stakes.
- Great for testing criteria design, stale reviews, fake recommendations, and human judgment.

Main risk:

- Advanced users may find it too narrow unless pushed into reusable decision template territory.

Reviewer call:

- Strong mid-level scenario. Do not use for Lv.8+ confirmation.

### 5. Weekend Plan With Mixed Preferences

Good for: Lv.1-Lv.5.

Why it works:

- Friendly, low-pressure, good for colleague groups.
- Tests preference gathering and conflict resolution without sounding like work.

Main risk:

- Too soft for high-level users.

Reviewer call:

- Use for basic/workflow lane, not system lane.

### 6. Eight-Week Learning Sprint

Good for: Lv.2-Lv.7.

Why it works:

- Exposes whether the user can avoid fantasy plans.
- Strong for diagnosing feedback loops and progress checks.

Main risk:

- Tooling pressure is weaker unless the user brings external materials, quizzes, or tracking.

Reviewer call:

- Good, but high-lane answer needs an anchor around measurement and adaptation.

### 7. Messy Work Rescue

Good for: Lv.5-Lv.8 signal.

Why it works:

- Best work scenario for real AI leverage: scattered inputs, conflicting stakeholders, artifact production.

Main risk:

- Biggest bluff risk. Fluent phrases like "align stakeholders" can sound senior without proving AI capability.

Reviewer call:

- Use only after baseline shows maturity. Require concrete inputs, intermediate artifact, decision owner, and human review.

### 8. Knowledge Product Launch

Good for: Lv.5-Lv.8.

Why it works:

- Tests creation, taste, anti-slop review, audience fit, and real artifact delivery.
- More "life-rich" than pure business operations because many people have notes, links, ideas, and unfinished drafts.

Main risk:

- User may talk in content strategy abstractions.

Reviewer call:

- Strong high-lane scenario. Anchor should ask what "publishable" means and what real reader feedback changed.

### 9. Personal Workflow Automation

Good for: Lv.6-Lv.9 signal.

Why it works:

- Best separator for Lv.6/Lv.7/Lv.8.
- Tool user says "agent runs it"; system designer defines inputs/checks/outputs; creator shows repeated runs.

Main risk:

- Users may name automation without explaining validation.

Reviewer call:

- This should be the default high-lane scenario when Q3 is C/D and Q2 includes D.

### 10. Plan Breakdown Crisis

Good for: Lv.5-Lv.9 signal.

Why it works:

- Stress test. It reveals whether the user can handle live facts, uncertainty, communication, and human judgment.

Main risk:

- Too intense for beginners.

Reviewer call:

- Use as a second-round or high-maturity stress case, not default.

### 11. Personal AI Operating System

Good for: Lv.8-Lv.10 signal.

Why it works:

- It directly asks for real history: first run, current run, changes, human boundary, other users.
- This is the only scenario in the bank that can responsibly approach Lv.9-Lv.10.

Main risk:

- It can feel like an audit. Do not use unless the user has already shown evidence.

Reviewer call:

- Keep strict. It should often return "Lv.9 signal, confirmed Lv.8" rather than rushing to Lv.9/Lv.10.

## Strict Findings

### Finding 1: High-level confirmation must remain rare

Lv.8+ should not become easier just because the new bank includes high-level scenarios.

Rule:

- Lv.8 requires repeated use or artifact evidence.
- Lv.9 requires transferable method plus examples.
- Lv.10 requires multi-domain operating system plus other-user evidence.

### Finding 2: Scenario selection must stay invisible

The user should not see "you are routed to system lane". That feels evaluative too early.

Good wording:

```text
我会给你一个更适合你当前使用方式的场景。
```

Bad wording:

```text
你进入 Lv.6-Lv.8 测试区。
```

### Finding 3: Every high-lane answer needs a proof probe

If the user mentions Agent, Skill, MCP, automation, or reusable workflow, ask about 2-3 of:

- tool-use proof
- validation rule
- failure handling
- reuse evidence
- what changed after the first real run

### Finding 4: Work fluency is not AI maturity

For Messy Work Rescue, do not reward:

```text
对齐认知、沉淀方案、闭环推进
```

unless the user says what inputs are processed, what artifact is produced, what is validated, and who decides.

## Recommendation For v0.1.2

Implement in this order:

1. Use `scenario-bank.md` as the canonical scenario source.
2. Make baseline routing explicit in the instructions but invisible to users.
3. Add scenario-specific anchor examples for Home Move, Learning Sprint, Messy Work, Knowledge Product, and Workflow Automation.
4. Extend `sample_run.py` to test:
   - one beginner route,
   - one mid workflow route,
   - one high-baseline weak answer,
   - one real Lv.8 evidence answer.

## Final Call

The scenario bank is now broad enough.

The next risk is not lack of scenarios. The next risk is inconsistent scoring if the model forgets the evidence gates.
