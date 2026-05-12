# AI Application Level Rubric

## Scoring Philosophy

Score observed behavior, not self-description. A user can mention advanced tools but still score lower if they cannot explain inputs, steps, validation, handoff, reuse, or human judgment.

Use two labels:

- Signal level: what the answer suggests the user understands.
- Confirmed level: what the answer actually proves.

## Evidence Strength

| Evidence | Meaning | Typical use |
| --- | --- | --- |
| E0 | Pure slogan or tool-name claim | Do not confirm advanced levels |
| E1 | Concrete plan with steps | Can confirm Lv.3-Lv.5, maybe signal Lv.6+ |
| E2 | Real case described or a very concrete implementation plan | Can confirm Lv.6; can confirm weak Lv.7 when inputs, steps, validation, reuse, and failure handling are specific |
| E3 | Checkable artifact exists | Strong confirmation for Lv.7 |
| E4 | Reused and improved at least twice | Needed to confirm Lv.8 |
| E5 | Others can use it or it changes team practice | Needed for Lv.9-Lv.10 confirmation |

## Level Definitions

### Lv.3: Controller

The user can make AI output more useful by adding context, constraints, examples, roles, formats, and follow-up corrections.

Signals:
- Adds background and success criteria.
- Requests structure, tables, or specific tone.
- Knows that vague prompts produce vague answers.

Limits:
- Mostly single-session conversation.
- Weak validation.
- Little workflow reuse.

### Lv.4: Boundary Crosser

The user uses AI to enter unfamiliar domains or do tasks outside their normal skill area.

Signals:
- Uses AI to explore new domains.
- Asks AI to explain unfamiliar options and tradeoffs.
- Can produce a low-risk artifact in an unfamiliar area.

Limits:
- Still relies heavily on AI's generated answer.
- May not build repeatable processes.

### Lv.5: Workflow Builder

The user turns repeated tasks into structured flows.

Signals:
- Asks AI to clarify missing information before output.
- Splits work into stages.
- Uses input checklists, output templates, and review checklists.
- Thinks about repeatable processes.

Limits:
- Workflows may still be manual.
- Tool use and automation are limited.

### Lv.6: Agent User

The user uses AI tools, agents, or external sources for multi-step execution.

Signals:
- Uses Agent, MCP, plugins, file reading, web lookup, scripts, or table workflows.
- Delegates multi-step work to AI.
- Understands that external information needs source checks.

Limits:
- May "let the agent run" without strong validation boundaries.
- May not create reusable skills or systems.

### Lv.7: Skill / System Designer

The user designs reusable AI workflows, skills, templates, or agent procedures.

Signals:
- Talks in inputs, steps, outputs, checks, and reuse.
- Can specify what a skill or workflow should do.
- Can identify external information sources and failure points.
- Produces reusable prompts, checklists, or agent instructions.

Confirmation gate:
- E2 can confirm weak Lv.7 when the answer explains inputs, steps, validation, reuse, and failure handling in enough detail.
- E3 is needed for strong Lv.7 confirmation.
- Without validation or reuse detail, report Lv.7 signal but confirm lower or use a range.

### Lv.8: Creator

The user repeatedly creates usable systems, tools, artifacts, content pipelines, or decision-support systems with AI.

Signals:
- Runs a workflow end to end.
- Produces artifacts others can use.
- Revises the system after failures.
- Reuses the same system across multiple tasks or rounds.

Confirmation gate:
- At least E4 is required to confirm Lv.8.

### Lv.9: Method Owner

The user has a personal AI collaboration method: role design, validation philosophy, decision boundaries, and judgment principles.

Signals:
- Defines what AI should do and what humans must judge.
- Uses opposing roles, critique, verification, and reflection.
- Can explain the method behind the workflow.
- Can transfer the method across domains.

Confirmation gate:
- At least E5 or strong real-case evidence plus method explanation is required.

### Lv.10: One-Person Team

The user has a mature AI operating system that extends their judgment across domains and compresses the work of a small team.

Signals:
- Maintains a personal or team AI system: skills, workflows, knowledge bases, review practices, delivery formats.
- Can produce across research, writing, analysis, building, and coordination.
- Others can rely on or learn from the system.

Confirmation gate:
- Requires E5 and multiple domain examples. Do not confirm from one scenario alone.

## Anti-Inflation Rules

- Tool names alone do not raise the level.
- "I would make a skill" is Lv.7 signal, not Lv.7 confirmation by itself. To confirm weak Lv.7, the user must explain the workflow's inputs, steps, validation rules, reuse shape, and failure handling. A checkable artifact upgrades the evidence to strong Lv.7.
- "I would use Agent/MCP" is Lv.6 signal unless the user specifies sources, validation, and handoff boundaries.
- Lv.8 requires reuse or iteration evidence.
- Lv.9-Lv.10 require method and influence evidence; use range language unless proof is strong.
