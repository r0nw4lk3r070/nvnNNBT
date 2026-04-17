# MKT Tools

## Core Tools
- **web_fetch** — Fetch and analyze web pages for marketing audits, competitor analysis, SEO checks
- **exec** — Run Python scripts, shell commands, file operations
- **read_file** — Read source files, templates, previous audit results
- **write_file** — Write reports, proposals, email sequences, calendar files

## Scripts (workspace/scripts/)
| Script | Purpose | Usage |
|--------|---------|-------|
| `analyze_page.py` | Extract SEO elements, content structure, CTAs, tracking, schema from a URL | `python workspace/scripts/analyze_page.py <url>` |
| `competitor_scanner.py` | Scan competitor websites for positioning, pricing, trust signals | `python workspace/scripts/competitor_scanner.py <url1> [url2] ...` |
| `social_calendar.py` | Generate 30-day social media content calendar JSON | `python workspace/scripts/social_calendar.py <topic> [platforms] [days]` |
| `generate_pdf_report.py` | Generate professional PDF marketing report from JSON data | `python workspace/scripts/generate_pdf_report.py <data.json> <output.pdf>` |

## Templates (workspace/templates/)
| Template | Purpose |
|----------|---------|
| `email-welcome.md` | 5-email welcome sequence framework |
| `email-nurture.md` | 6-email lead nurture sequence framework |
| `email-launch.md` | 8-email product launch sequence framework |
| `proposal-template.md` | Client marketing proposal structure |
| `content-calendar.md` | 30-day content calendar grid |
| `launch-checklist.md` | 8-week product launch checklist |

## Dependencies
- `reportlab>=4.0` — Required for PDF report generation (`pip install reportlab`)
- All other scripts use Python stdlib only (no external dependencies)

## Workflow
1. Use `web_fetch` to retrieve target pages
2. Use `exec` to run analysis scripts for automated data collection
3. Combine script output with expert manual analysis
4. Use `write_file` to generate client-ready deliverables
5. For PDF reports: assemble JSON data → run `generate_pdf_report.py`