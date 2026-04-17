# Skill: Legislation Analysis

Break down EU legal texts into structured, actionable analysis — obligations, timelines, role mappings, and compliance implications.

## When to use

- User asks "what does X require?" or "what are my obligations under Y?"
- User wants a regulation broken down into practical requirements
- User asks to compare obligations across multiple regulations
- User needs a compliance timeline or deadline overview

## Approach

1. **Scope the question** — Determine which articles, annexes, or provisions are relevant to the user's role (provider, deployer, importer, manufacturer, etc.).
2. **Map obligations** — For each relevant provision, extract: who must do what, by when, with what evidence, and what the penalties are for non-compliance.
3. **Build a timeline** — List key dates: entry into force, application dates, transitional periods, transposition deadlines (for directives).
4. **Cross-reference** — Note interactions with other regulations (e.g. AI Act Art. 6 risk classification interacts with product safety legislation).
5. **Present** — Structured output: scope → obligations by role → timeline → interactions → open questions. Use tables for clarity.

## Notes

- Always distinguish between mandatory obligations ("shall"), conditional obligations ("where applicable"), and guidance ("may", "should").
- Note which provisions are subject to implementing/delegated acts still to be adopted — these may change the practical requirements.
- For compliance timelines: flag both the legal deadline and the practical reality (e.g. harmonised standards not yet available).
- Save significant analyses to `workspace/library/` for future reference.
- When comparing regulations, use a matrix format: obligation | Regulation A | Regulation B | Overlap?