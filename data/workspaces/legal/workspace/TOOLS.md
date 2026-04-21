# Tool Usage Notes

Tool signatures are provided automatically via function calling.
This file documents non-obvious constraints and LEGAL-specific patterns.

## File tools

- `edit_file` / `write_file` — create or update files in the workspace
- `read_file` — read contracts, templates, and reference files in the workspace

## exec — Safety Limits

- Commands have a configurable timeout (default 60s)
- Dangerous commands are blocked (rm -rf, format, dd, shutdown, etc.)
- Output is truncated at 10,000 characters
- Use for: running PDF generation scripts, compliance checks

## web — Search

Use web search for:
- Looking up current regulations (GDPR, EU AI Act, CCPA)
- Checking legal precedents or recent case law
- Verifying compliance requirements by jurisdiction

## Memory tools

- `memory/MEMORY.md` — persistent facts: client preferences, recurring risk patterns, jurisdiction notes
- `memory/HISTORY.md` — review log

Load MEMORY.md at conversation start. Write to it when something is worth keeping.

## LEGAL workflow

1. Receive contract/document — read it fully with `read_file`
2. Identify contract type and jurisdiction
3. Run analysis: clause-by-clause review, risk scoring, compliance check
4. Generate Contract Safety Score (0-100)
5. Produce recommendations with specific replacement language
6. If requested, generate PDF report via `exec` running `workspace/scripts/generate_legal_pdf.py`

## Skills

Skills are in `skills/` — each skill is a folder with a `SKILL.md`.
Load a skill's SKILL.md when the task matches its domain.

## Agents

5 parallel analysis agents in `agents/`:
- `legal-clauses.md` — Clause Analyst (weight: 20%)
- `legal-risks.md` — Risk Assessor (weight: 25%)
- `legal-compliance.md` — Compliance Checker (weight: 20%)
- `legal-terms.md` — Terms Mapper (weight: 15%)
- `legal-recommendations.md` — Recommendations Engine (weight: 20%)