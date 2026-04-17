# MKT — AI Marketing Suite

## Quick Start

1. Load this skill-set in the Lab
2. Run a marketing audit: provide a URL and request an audit
3. Generate reports, proposals, email sequences, social calendars, ad campaigns, and more

## Skills (14)

| Skill | Command | Output |
|-------|---------|--------|
| market-audit | `audit` | MARKETING-AUDIT.md — Full audit with 5 parallel agents |
| market-copy | `copy` | COPY-SUGGESTIONS.md — Copy analysis & rewrites |
| market-emails | `emails` | EMAIL-SEQUENCES.md — Email sequence generation |
| market-social | `social` | SOCIAL-CALENDAR.md — 30-day social calendar |
| market-ads | `ads` | AD-CAMPAIGNS.md — Multi-platform ad campaigns |
| market-funnel | `funnel` | FUNNEL-ANALYSIS.md — Conversion funnel analysis |
| market-competitors | `competitors` | COMPETITOR-REPORT.md — Competitive intelligence |
| market-landing | `landing` | LANDING-CRO.md — Landing page CRO analysis |
| market-launch | `launch` | LAUNCH-PLAYBOOK.md — Product launch playbook |
| market-proposal | `proposal` | CLIENT-PROPOSAL.md — Client proposal generator |
| market-report | `report` | MARKETING-REPORT.md — Full marketing report |
| market-report-pdf | `report-pdf` | MARKETING-REPORT.pdf — PDF report with charts |
| market-seo | `seo` | SEO-AUDIT.md — SEO content audit |
| market-brand | `brand` | BRAND-VOICE.md — Brand voice analysis |

## Parallel Agents (5)

| Agent | Focus | Scores |
|-------|-------|--------|
| market-content | Content quality, messaging, copy | Content & Messaging (0-100) |
| market-conversion | CRO, funnels, landing pages | Conversion Optimization (0-100) |
| market-competitive | Competitive positioning | Competitive Positioning (0-100) |
| market-technical | Technical SEO, site architecture | SEO & Discoverability (0-100) |
| market-strategy | Strategy, pricing, growth | Brand & Trust (0-100), Growth & Strategy (0-100) |

## Scripts (4)

| Script | Purpose |
|--------|---------|
| `workspace/scripts/analyze_page.py` | Extract SEO elements, content, CTAs, tracking, schema |
| `workspace/scripts/competitor_scanner.py` | Scan competitor websites for positioning, pricing, trust |
| `workspace/scripts/social_calendar.py` | Generate 30-day social calendar JSON |
| `workspace/scripts/generate_pdf_report.py` | Generate PDF marketing report with charts |

## Templates (6)

| Template | Purpose |
|----------|---------|
| `workspace/templates/email-welcome.md` | 5-email welcome sequence |
| `workspace/templates/email-nurture.md` | 6-email lead nurture sequence |
| `workspace/templates/email-launch.md` | 8-email product launch sequence |
| `workspace/templates/proposal-template.md` | Client marketing proposal |
| `workspace/templates/content-calendar.md` | 30-day content calendar grid |
| `workspace/templates/launch-checklist.md` | 8-week launch checklist |

## Scoring Methodology

**Marketing Score 0-100** — weighted composite:

| Category | Weight | What It Measures |
|----------|--------|-----------------|
| Content & Messaging | 25% | Copy quality, value props, clarity, persuasion |
| Conversion Optimization | 20% | CTAs, forms, friction, social proof, urgency |
| SEO & Discoverability | 20% | On-page SEO, technical SEO, content structure |
| Competitive Positioning | 15% | Differentiation, market awareness, alternatives |
| Brand & Trust | 10% | Brand consistency, trust signals, social proof |
| Growth & Strategy | 10% | Pricing, referral, retention, expansion |

## Dependencies

- `reportlab>=4.0` — Required for PDF report generation (`pip install reportlab`)
- All other scripts use Python stdlib only

## Billing Context

- Marketing audit: €1,000-3,000 per audit
- Full marketing strategy: €3,000-10,000/month retainer
- PDF deliverables are primary sales collateral for client onboarding