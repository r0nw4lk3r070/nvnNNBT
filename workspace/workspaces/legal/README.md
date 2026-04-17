# LEGAL — AI Legal Assistant

AI-powered contract review and legal document generation for the nanobot platform.

## Quick Facts

| Field | Value |
|-------|-------|
| **Agent Name** | LEGAL |
| **Folder** | BMTNOSl |
| **Focus** | Contract review, risk analysis, compliance auditing, legal document generation |
| **Skills** | 13 |
| **Agents** | 5 (parallel analysis) |
| **Scripts** | 1 (PDF report generation) |
| **Templates** | 1 (contract review template) |

## Skills

### Contract Analysis
| Skill | Description |
|-------|-------------|
| `legal-review` | **Flagship** — Full contract review with 5 parallel agents. Contract Safety Score, clause-by-clause analysis, prioritized recommendations. |
| `legal-risks` | Deep risk analysis with severity scoring for every clause. Financial exposure estimates. |
| `legal-compare` | Side-by-side comparison of two contract versions. Flags dangerous changes. |
| `legal-plain` | Translates every clause from legalese into plain English. |
| `legal-negotiate` | Generates specific counter-proposals with replacement language for every unfavorable clause. |
| `legal-missing` | Finds protections that SHOULD be in the contract but aren't. |

### Document Generation
| Skill | Description |
|-------|-------------|
| `legal-nda` | Generates custom NDAs — mutual, one-way, employee, vendor. |
| `legal-terms` | Generates terms of service based on what the website actually does. GDPR/CCPA compliant. |
| `legal-privacy` | Generates a privacy policy by scanning what data the site collects. |
| `legal-agreement` | Generates business agreements — freelancer contracts, partnerships, SOWs, MSAs, and more. |
| `legal-freelancer` | Specialized review from the freelancer's perspective. Flags common contractor traps. |

### Compliance & Reporting
| Skill | Description |
|-------|-------------|
| `legal-compliance` | Compliance gap analysis — GDPR, CCPA, ADA, PCI-DSS, CAN-SPAM, SOC 2. |
| `legal-report-pdf` | Professional PDF report with score gauges, risk charts, and prioritized actions. |

## The Flagship: Full Contract Review

The most powerful skill. Run it on any contract and get:

1. **Contract Safety Score** (0-100) with letter grade
2. **Risk Dashboard** — high/medium/low risk clause counts
3. **Clause-by-Clause Analysis** — every clause scored, explained in plain English, with specific fix recommendations
4. **Missing Protections** — what should be there but isn't
5. **Obligations Timeline** — every deadline and consequence mapped
6. **Compliance Flags** — regulatory issues flagged
7. **Negotiation Priorities** — ranked list of what to change first
8. **Next Steps** — actionable checklist

### How It Works

5 AI agents launch in parallel:

| Agent | Role | Weight |
|-------|------|--------|
| Clause Analyst | Identifies and categorizes every clause | 20% |
| Risk Assessor | Scores each clause for risk | 25% |
| Compliance Checker | Flags regulatory issues | 20% |
| Terms Mapper | Maps obligations, deadlines, and triggers | 15% |
| Recommendations Engine | Generates specific fixes | 20% |

Results are aggregated into a unified report with a single Contract Safety Score.

## Use Cases

### For Freelancers & Agencies
- Review client contracts before signing
- Generate NDAs for new client engagements
- Create statements of work with proper protections
- Offer contract review as a paid service (€500-€1,500 per review)

### For Small Businesses
- Review vendor and supplier contracts
- Generate privacy policies and terms of service
- Run compliance audits on your website
- Understand what you're actually agreeing to

### For AI Automation Agencies
- Add contract review to your service offering
- Generate professional PDF reports for clients
- Offer monthly legal document management retainers
- Pair with the EUAI agent for deep EU regulatory compliance

## Billing Guidelines

| Service | Price Range |
|---------|-------------|
| Basic contract review | €500 - €1,500 |
| Compliance audit (single site) | €750 - €2,000 |
| NDA / Terms / Privacy generation | €300 - €800 |
| Freelancer contract review | €400 - €1,000 |
| Full review + PDF report + negotiation strategy | €1,500 - €3,000 |

## Project Structure

```
BMTNOSl/
├── SOUL.md                    # Agent identity, personality, voice
├── AGENTS.md                  # Instructions, responsibilities, workflow
├── USER.md                    # Client profile
├── TOOLS.md                   # Tool usage patterns
├── HEARTBEAT.md               # Periodic tasks (disabled)
├── README.md                  # This file
├── cron/
│   └── jobs.json              # Cron definitions
├── memory/
│   ├── MEMORY.md              # Persistent context
│   └── HISTORY.md             # Interaction log
├── sessions/                  # Session storage
├── skills/
│   ├── legal-review/SKILL.md
│   ├── legal-risks/SKILL.md
│   ├── legal-compare/SKILL.md
│   ├── legal-plain/SKILL.md
│   ├── legal-negotiate/SKILL.md
│   ├── legal-missing/SKILL.md
│   ├── legal-nda/SKILL.md
│   ├── legal-terms/SKILL.md
│   ├── legal-privacy/SKILL.md
│   ├── legal-agreement/SKILL.md
│   ├── legal-freelancer/SKILL.md
│   ├── legal-compliance/SKILL.md
│   └── legal-report-pdf/SKILL.md
├── agents/
│   ├── legal-clauses.md
│   ├── legal-risks.md
│   ├── legal-compliance.md
│   ├── legal-terms.md
│   └── legal-recommendations.md
└── workspace/                 # Runtime mirror
    ├── SOUL.md, AGENTS.md, USER.md, TOOLS.md, HEARTBEAT.md
    ├── cron/, memory/, sessions/
    ├── skills/                 # Mirror of all skills
    ├── agents/                 # Mirror of all agents
    ├── scripts/
    │   └── generate_legal_pdf.py
    └── templates/
        └── contract-review-template.md
```

## Requirements

- **nanobot-ai** (Python framework)
- **Python 3.8+** (for PDF generation)
- **reportlab** — `pip install reportlab` (for PDF generation only)

## Disclaimer

This tool is for informational and educational purposes only. It does **not** provide legal advice and should **not** be used as a substitute for consultation with a licensed attorney. Always have a qualified lawyer review any contract before signing.