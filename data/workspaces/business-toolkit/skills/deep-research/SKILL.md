# Deep Research

Produce thorough, cited research reports from multiple web sources. Uses a phased approach to prevent context overflow.

## Tools

- `web_search` — search the web for sources, reports, and data
- `web_fetch` — read full content from key source URLs
- `read_file` — read existing context and prior research
- `write_file` — save intermediate notes and final reports
- `edit_file` — update research notes with new findings

## When to Activate

- User asks to research any topic in depth
- Competitive analysis, technology evaluation, or market sizing
- Due diligence on companies, investors, or technologies
- Any question requiring synthesis from multiple sources
- User says "research", "deep dive", "investigate", or "what's the current state of"

## Phased Workflow

Research is split into phases. **Save intermediate results after each phase** to keep context available for the next phase. Never try to do all research and all writing in one go.

### Phase 1: Plan & Search

1. Ask 1-2 quick clarifying questions if needed, or proceed with defaults
2. Break the topic into 3-5 research sub-questions
3. For each sub-question, run 2-3 `web_search` queries with different keyword variations
4. Aim for 15-30 unique sources total
5. Prioritize: academic, official, reputable news > blogs > forums

**Save after search**: Write a research notes file with all key data points, numbers, and source URLs found. Use `write_file` to save to `workspace/research-notes-<topic>.md`.

### Phase 2: Deep-Read Key Sources

1. Read the research notes from Phase 1 with `read_file`
2. Identify the 3-5 most promising URLs from the notes
3. Fetch full content using `web_fetch` for each
4. Extract key findings, data points, and quotes
5. Update the research notes file with deep-read findings using `edit_file`

**Save after deep-read**: Update the research notes file. It should now contain all data needed to write the report, so the original search results can be dropped from context.

### Phase 3: Write Report

1. Read the research notes file with `read_file` (this is your only input — no need to keep raw search results in context)
2. Synthesize findings into the report structure below
3. Write the full report using `write_file` to `workspace/reports/<topic-slug>.md`
4. Run the quality gate

**Deliver:**
- **Short topics**: Post the full report in chat
- **Long reports**: Post the executive summary + key takeaways in chat, save full report to file

## Report Structure

```markdown
# [Topic]: Research Report
*Generated: [date] | Sources: [N] | Confidence: [High/Medium/Low]*

## Executive Summary
[3-5 sentence overview of key findings]

## 1. [First Major Theme]
[Findings with inline citations]
- Key point ([Source Name](url))
- Supporting data ([Source Name](url))

## 2. [Second Major Theme]
...

## 3. [Third Major Theme]
...

## Key Takeaways
- [Actionable insight 1]
- [Actionable insight 2]
- [Actionable insight 3]

## Sources
1. [Title](url) — [one-line summary]
2. ...

## Methodology
Searched [N] queries across web and news. Analyzed [M] sources.
Sub-questions investigated: [list]
```

## Quality Rules

1. **Every claim needs a source.** No unsourced assertions.
2. **Cross-reference.** If only one source says it, flag it as unverified.
3. **Recency matters.** Prefer sources from the last 12 months.
4. **Acknowledge gaps.** If you couldn't find good info on a sub-question, say so.
5. **No hallucination.** If you don't know, say "insufficient data found."
6. **Separate fact from inference.** Label estimates, projections, and opinions clearly.

## Anti-Patterns

- **Doing everything in one pass**: Search results fill context → no room to write. Always save notes between phases.
- **Re-reading all search results**: After saving notes, only re-read the notes file, not the raw search output.
- **Too many web_fetch calls**: 3-5 deep reads is enough. More fills context without proportional value.