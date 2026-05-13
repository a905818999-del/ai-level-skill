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
