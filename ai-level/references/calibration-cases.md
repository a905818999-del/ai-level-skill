# Calibration Cases

Use these cases to sanity-check scoring. They are not user-facing.

## Case 1: Format Improver

Answer: "I would ask AI to make a 5-day itinerary, not too tiring, with a table and budget."

Expected: Lv.3. The user adds constraints and format, but no decomposition or validation.

## Case 2: Context Adder

Answer: "I would tell AI the travelers' ages, budget, city, interests, and ask it to give three options with pros and cons."

Expected: Lv.4-Lv.5. Good context and comparison, weak validation/reuse.

## Case 3: Workflow Splitter

Answer: "I would first ask AI to list missing information, then compare destinations, then build itinerary, budget, and risk plan. I would verify key transport and opening hours myself."

Expected: Lv.5. Strong workflow, basic verification.

## Case 4: Tool User

Answer: "I would use AI with travel sites, maps, weather, and train information, then ask it to generate a schedule and budget."

Expected: Lv.6 signal, confirmed Lv.5-Lv.6 depending on validation detail.

## Case 5: Agent Runner

Answer: "I would give the task to an agent, let it search routes, hotels, weather, reviews, and make an HTML page."

Expected: Lv.6 signal. If no validation or input design, do not confirm Lv.7.

## Case 6: Skill Designer

Answer: "I would make a reusable travel-planning skill with inputs, source checks, itinerary rules, budget rules, risk alternatives, and HTML output."

Expected: Lv.7 signal. Confirm weak Lv.7 if the anchor follow-up provides concrete inputs, steps, validation, reuse shape, and failure handling. Treat artifact evidence as strong Lv.7.

## Case 7: Reuser

Answer: "I have a travel-planning template I used twice. It collects constraints, compares routes, checks sources, outputs a share page, and I revised it after a bad hotel recommendation."

Expected: Lv.8 if details are credible. Evidence should be E4.

## Case 8: Method Owner

Answer: "For family decisions, I use AI as researcher, critic, and coordinator. I define what counts as success first, then use AI to expand options, attack assumptions, and prepare a decision page. I keep final tradeoff decisions human."

Expected: Lv.8-Lv.9 signal. Confirm Lv.9 only with real examples and transferable method evidence.

## Case 9: One-Person System

Answer: "I maintain a personal skill library for travel, purchasing, learning plans, and business research. Other colleagues use parts of it. Each flow has inputs, source rules, output templates, and review rules."

Expected: Lv.9-Lv.10 signal. Confirmation requires examples across domains and evidence others can use it.

## Case 10: Tool-Orchestrating Planner

Answer: "I would use workbuddy or openclaw, call 12306, Xiaohongshu, browser-use, and travel skills to collect enough food, transport, hotel, and activity information. I would discuss with the agent to find a plan that satisfies older adults, children, and my own interests. During the process I would ask for multiple options, give feedback, iterate, generate an HTML page for companions, and maybe turn the flow into a reusable skill."

Expected: Lv.7-Lv.8 signal, confirmed Lv.7 after anchor if the user can explain missing inputs, source freshness, tool-call verification, hallucination checks, and reuse. The follow-up must not repeat "which tools or inputs" if the answer already named them. Ask only about missing decision standards, tool-use proof, and structured feedback rules.

## Case 11: Beginner Routed Correctly

Baseline: "1A 2A 3A"

Scenario: First Real Ask.

Answer: "I would ask AI to help me write it. If it is bad, I might ask again."

Expected: Lv.1 signal, confirmed Lv.1. Do not give a heavy workflow scenario. Do not mention Agent or Skill in the advice.

## Case 12: Low Baseline, Strong Practical Structure

Baseline: "1B 2C 3A"

Scenario: Expensive Family Purchase.

Answer: "I do not use AI very often, but I would first tell it budget, must-have requirements, who will use the product, and what I am worried about. Then I would ask it to make a comparison table, explain unfamiliar terms, list risks, and tell me which facts I should check myself before buying."

Expected: Lv.4-Lv.5 signal, confirmed Lv.4 or weak Lv.5. Baseline is modest but the practical answer deserves upgrade.

## Case 13: High Baseline, Weak Practical Answer

Baseline: "1D 2D 3D"

Scenario: Personal Workflow Automation.

Answer: "I would let an Agent search everything, summarize it, and output a result. If it is not good, I will ask it to improve. Later I can make it a Skill."

Expected: Lv.6-Lv.7 signal, confirmed Lv.6. Tool and Skill names are not enough. Anchor should ask about input schema, validation rules, tool-use proof, and what changes after repeated runs.

## Case 14: Real Lv.7 System Designer

Scenario: Knowledge Product Launch.

Answer: "I would define the audience and output first, collect all notes and links into a source folder, ask AI to cluster the material, produce an outline, generate a draft, run an anti-slop review, then export a share page. I would keep a checklist for inputs, review rules, and final publish checks so next time I can reuse the flow."

Expected: Lv.7 signal, confirmed weak Lv.7 if the user can explain review rules and failure handling. Evidence E2 unless a real artifact exists.

## Case 15: Lv.8 Claim Without Reuse Evidence

Scenario: Personal Workflow Automation.

Answer: "I would design a complete system with inputs, checks, agents, outputs, and HTML reports."

Expected: Lv.7-Lv.8 signal, confirmed Lv.7 max. No real run, reuse, artifact, or iteration evidence.

## Case 16: Real Lv.8 Evidence

Scenario: Personal Workflow Automation.

Answer: "I have run this weekly digest flow four times. The first version only summarized links. After two bad items slipped in, I added source timestamp, confidence, why-this-matters, and reject-reason fields. Now another colleague can fill the source folder and run the same template."

Expected: Lv.8, confirmed Lv.8 if details are credible. Evidence E4, possibly E5 if colleague use is real and repeatable.

## Case 17: Lv.9 Signal, Needs Cross-Domain Proof

Scenario: Personal AI Operating System.

Answer: "My method is that AI expands options, finds evidence, writes drafts, and plays critic. I decide goals, tradeoffs, and final calls. I use this for travel, purchases, study plans, and project reviews."

Expected: Lv.9 signal. Confirm Lv.8-Lv.9 only if the user gives concrete examples across domains and explains human/AI boundaries. Do not confirm Lv.9 from method language alone.

## Case 18: Lv.10 Claim, Evidence Gate Required

Scenario: Personal AI Operating System.

Answer: "I maintain a skill library, source rules, review checklists, examples, and onboarding notes. I use it across research, writing, analysis, planning, and delivery. Two teammates can use parts of it without me."

Expected: Lv.10 signal. Confirm Lv.10 only with strong E5 evidence: multiple domains, real artifacts, other-user adoption, and sustained practice. Otherwise confirm Lv.9 or Lv.8-Lv.9.

## Case 19: Messy Work Fluent Bluff

Scenario: Messy Work Rescue.

Answer: "I would let AI align stakeholders, clarify priorities, form consensus, and close the loop."

Expected: Lv.4-Lv.5 signal, confirmed Lv.4. Fluent workplace language is not evidence. Missing concrete inputs, artifact shape, validation, and decision boundaries.

## Case 20: Crisis Replanning With Human Boundary

Scenario: Plan Breakdown Crisis.

Answer: "I would first ask AI to list what facts changed and which ones must be live-checked. Then I would generate 2-3 fallback plans, mark the risk of each, and write a short message for affected people. AI can propose options, but I decide whether the risk is acceptable and what to tell people."

Expected: Lv.6-Lv.7 signal. Confirm Lv.6 if no reuse; confirm Lv.7 if the user describes a reusable replanning protocol.
