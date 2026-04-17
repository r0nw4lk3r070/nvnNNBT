# Tool Usage Notes

## File tools — workspace only

All file reads and writes are scoped to `E:\Art\skill-sets\geo-seo`.
- `edit_file` / `write_file` — create or update files inside workspace
- `read_file` — read any file inside workspace
- Never attempt paths outside workspace

## exec — Shell commands

Shell exec is enabled. Use to run Python scripts in `workspace/scripts/`.
- Working directory: `E:\Art\skill-sets\geo-seo`
- Primary use: running audit scripts, PDF generation, page fetching
- Do NOT run destructive commands without explicit confirmation

## web_fetch — Page fetching

- Use to fetch target URLs for audit analysis
- Use to check robots.txt, llms.txt, sitemap.xml
- Use to verify brand presence on platforms (YouTube, Reddit, LinkedIn)
- 30-second timeout per fetch
- Always check robots.txt before crawling internal links
- Rate limit: 1 second between requests

## web_search — Brand & competitor research

- Use to search for brand mentions across platforms
- Use to find competitor GEO strategies
- Use to verify Wikipedia/Wikidata entity presence
- Use to research platform-specific ranking factors

## Python scripts

Scripts in `workspace/scripts/`:
- `fetch_page.py` — fetch and parse web pages (modes: page, robots, llms, sitemap, blocks, full)
- `citability_scorer.py` — score content blocks for AI citation readiness
- `brand_scanner.py` — scan brand mentions across platforms
- `llmstxt_generator.py` — validate and generate llms.txt files
- `generate_pdf_report.py` — professional PDF report generation (reportlab)

### Usage
```bash
python workspace/scripts/fetch_page.py <url> [page|robots|llms|sitemap|blocks|full]
python workspace/scripts/citability_scorer.py <url>
python workspace/scripts/brand_scanner.py <brand_name> [domain]
python workspace/scripts/llmstxt_generator.py <url> [validate|generate]
python workspace/scripts/generate_pdf_report.py <json_data_file> [output.pdf]
```

### Dependencies
- `requests`, `beautifulsoup4`, `lxml` — page fetching and parsing
- `reportlab` — PDF generation
- Install: `pip install -r workspace/scripts/requirements.txt`

## JSON-LD Schema templates

Templates in `workspace/schema/`:
- `organization.json` — Organization schema with sameAs
- `local-business.json` — LocalBusiness schema
- `article-author.json` — Article + Person schema (E-E-A-T)
- `software-saas.json` — SoftwareApplication schema
- `product-ecommerce.json` — Product schema with offers
- `website-searchaction.json` — WebSite + SearchAction schema

Use these as starting points for schema generation commands.

## Output locations

| Type | Path |
|------|------|
| Audit reports (MD) | `workspace/reports/` |
| Audit reports (PDF) | `workspace/reports/` |
| Generated files | `workspace/generated/` |
| Prospect data | `workspace/prospects/prospects.json` |
| Proposals | `workspace/prospects/proposals/` |
| Monthly deltas | `workspace/prospects/reports/` |

## Memory

- `memory/MEMORY.md` — audit history, prospect data, key findings
- `memory/HISTORY.md` — chronological log of audits and decisions