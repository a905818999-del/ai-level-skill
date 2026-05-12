---
name: ai-level
description: Short trigger for the AI application-level diagnostic. Use when a user says AI-level, wants to test, assess, score, or diagnose someone's AI usage level, or wants a short non-questionnaire AI maturity test with a practical scenario, anti-bluff follow-up, evidence strength, and next-level advice based on Lv.3-Lv.10 AI application maturity.
---

# AI Level

## Overview

Use this skill to run a short but rigorous AI application-level diagnostic. The diagnostic avoids long self-report questionnaires: it uses a few gate questions, one practical scenario, one adaptive anti-bluff follow-up, then returns a level report and next-level advice.

The core ladder is Lv.3-Lv.10:

- Lv.3: can control AI responses with context, constraints, and formats.
- Lv.4: can use AI beyond familiar domains.
- Lv.5: can turn repeated tasks into workflows.
- Lv.6: can use Agent/tooling for multi-step execution.
- Lv.7: can design reusable prompts, skills, agents, or workflows.
- Lv.8: can repeatedly create usable systems or artifacts with AI.
- Lv.9: has a personal AI collaboration method and judgment model.
- Lv.10: operates as a one-person team through a mature AI system.

## Quick Start

When the user wants to run the test, follow this sequence:

1. Show the welcome page from `references/diagnostic-flow.md`.
2. Ask the three baseline gate questions from `references/diagnostic-flow.md`.
3. Ask the practical scenario question from `references/diagnostic-flow.md`.
4. Score the answer using `references/rubric.md` and `references/scoring-guide.md`.
5. If the answer shows Lv.7+ signals, ask one adaptive anchor follow-up before final scoring.
6. Produce the final report using the report template in `references/scoring-guide.md`.

If the user already provided an answer, skip directly to scoring and generate the adaptive anchor follow-up or final report as appropriate.

## Diagnostic Rules

- Do not ask the user to self-select a level.
- Do not reward tool-name dropping unless the answer includes process, validation, and reuse details.
- Separate `signal level` from `confirmed level`.
- Use a range when evidence is mixed, for example `Lv.7-Lv.8, confirmed Lv.7`.
- Treat Lv.8+ as evidence-gated. A single theoretical answer can show Lv.8 signals, but confirmation requires real cases, artifacts, reuse, or method evidence.
- Do not expose internal scoring thoughts before the anchor follow-up. Ask the follow-up directly and naturally.
- Keep wording plain and non-judgmental. Say "evidence is not enough yet", not "you are bluffing".
- Give next-level advice based on the user's actual bottleneck, not generic AI learning tips.

## Reference Files

- `references/diagnostic-flow.md`: user-facing questions, scenario prompt, and anchor follow-up patterns.
- `references/rubric.md`: level definitions, evidence strength, and anti-inflation gates.
- `references/scoring-guide.md`: scoring dimensions, mapping rules, report template, and next-level advice.
- `references/calibration-cases.md`: synthetic colleague cases for tuning and sanity checks.
- `references/trial-protocol.md`: small real-person trial instructions.
- `scripts/sample_run.py`: canned sample run and lightweight regression check for the current flow/report tone.

## Scripts

Run the sample check after changing prompts, scoring language, or report style:

```bash
python scripts/sample_run.py --check
```

The script does not call an LLM. It renders the expected flow for the development sample and checks that key user-facing wording remains present while internal evaluation phrasing stays hidden.

## Output Contract

A final diagnostic report must include:

- Estimated level or range.
- Confirmed level.
- Evidence strength.
- Why this level.
- Why not the next level yet.
- Next-level advice in plain language.
- One short 7-day practice task or next check item.

Keep the report practical. Avoid mystical or status-heavy language.
Use a light social-media style in final reports: concise, punchy, concrete, and easy to share. Do not become clickbait, preachy, or abstract.
