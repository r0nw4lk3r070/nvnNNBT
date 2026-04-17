# Market Research

Produce research that supports decisions, not research theater. Uses a phased approach to prevent context overflow.

## Tools

- `web_search` — find market data, competitor info, industry reports
- `web_fetch` — read full content from research sources
- `read_file` — read existing research and source-of-truth documents
- `write_file` — save intermediate notes and final reports
- `edit_file` — update research notes with new findings

## When to Activate

- researching a market, category, company, investor, or technology trend
- building TAM/SAM/SOM estimates
- comparing competitors or adjacent products
- preparing investor dossiers before outreach
- pressure-testing a thesis before building, funding, or entering a market

## Research Standards

1. Every important claim needs a source.
2. Prefer recent data and call out stale data.
3. Include contrarian evidence and downside cases.
4. Translate findings into a decision, not just a summary.
5. Separate fact, inference, and recommendation clearly.

## Phased Workflow

Market research is split into phases. **Save intermediate results after each phase** to keep context available for the next phase. Never try to do all research and all writing in one go.

### Phase 1: Data Collection

1. Define the research scope and sub-questions
2. For each sub-question, run 2-3 `web_search` queries
3. Collect: market sizing data, competitor info, financials, trends, regulatory context
4. Deep-read 3-5 key sources with `web_fetch` if needed

**Save after collection**: Write a research notes file with all key data points, numbers, and source URLs. Use `write_file` to save to `workspace/research-notes-<topic>.md`.

### Phase 2: Analysis & Sizing

1. Read the research notes from Phase 1 with `read_file`
2. Build TAM/SAM/SOM estimates with explicit assumptions
3. Map competitive landscape with positioning gaps
4. Identify risks, contrarian evidence, and downside cases
5. Update the research notes file with analysis results using `edit_file`

**Save after analysis**: The notes file should now contain all data AND analysis — ready for report writing.

### Phase 3: Write Report

1. Read the research notes file with `read_file` (your only input)
2. Write the full market research report using `write_file`
3. Save to `workspace/reports/<topic-slug>.md`
4. Run the quality gate

**Deliver:** Post executive summary + recommendation in chat, save full report to file.

## Common Research Modes

### Investor / Fund Diligence
Collect:
- fund size, stage, and typical check size
- relevant portfolio companies
- public thesis and recent activity
- reasons the fund is or is not a fit
- any obvious red flags or mismatches

### Competitive Analysis
Collect:
- product reality, not marketing copy
- funding and investor history if public
- traction metrics if public
- distribution and pricing clues
- strengths, weaknesses, and positioning gaps

### Market Sizing
Use:
- top-down estimates from reports or public datasets
- bottom-up sanity checks from realistic customer acquisition assumptions
- explicit assumptions for every leap in logic

### Technology / Vendor Research
Collect:
- how it works
- trade-offs and adoption signals
- integration complexity
- lock-in, security, compliance, and operational risk

## Output Format

Default structure:
1. executive summary
2. key findings
3. implications
4. risks and caveats
5. recommendation
6. sources

## Quality Gate

Before delivering:
- all numbers are sourced or labeled as estimates
- old data is flagged
- the recommendation follows from the evidence
- risks and counterarguments are included
- the output makes a decision easier

## Anti-Patterns

- **Doing everything in one pass**: Search results fill context → no room to write. Always save notes between phases.
- **Re-reading all search results**: After saving notes, only re-read the notes file, not the raw search output.
- **Too many search queries**: 6-10 well-targeted searches beat 20+ scatter-shot ones. Each search adds to context.
- **Skipping the save step**: If you don't save notes after Phase 1, the data is lost when context fills up.