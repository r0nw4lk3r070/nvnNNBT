# Business Toolkit — Volledige Inventaris & Index

_Gegenereerd: 2026-04-21_

---

## 1. Workspace Structuur

```
workspaces/business-toolkit/
├── config.json                          # Agent config (model, provider, apiBase)
├── SOUL.md                              # Persoonlijkheid, harde regels, phased execution
├── AGENTS.md                            # Agent-instructies (rol, tools, restricties)
├── TOOLS.md                             # Tool-gebruik notities
├── HEARTBEAT.md                         # Periodieke taken (leeg)
├── USER.md                              # Gebruikersprofiel
├── README.md                            # Korte beschrijving
├── output/
│   └── market-research-consumer-ai-inference-belgium.md   # Voorbeeld output
├── skills/
│   ├── market-research/SKILL.md
│   ├── deep-research/SKILL.md
│   ├── content-engine/SKILL.md
│   ├── brand-voice/SKILL.md
│   ├── investor-materials/SKILL.md
│   ├── investor-outreach/SKILL.md
│   ├── seo/SKILL.md
│   ├── security-review/SKILL.md
│   └── continuous-learning/SKILL.md
├── memory/
│   ├── MEMORY.md                        # Langdurige context (leeg, template)
│   └── HISTORY.md                       # Geschiedenis (1 entry: initialisatie)
├── cron/
│   └── jobs.json                        # Geplande taken (leeg)
└── workspace/                           # Geneste workspace kopie (identieke structuur)
    ├── config.json
    ├── SOUL.md
    ├── AGENTS.md
    ├── TOOLS.md
    ├── HEARTBEAT.md
    ├── USER.md
    ├── memory/MEMORY.md
    └── cron/jobs.json
```

---

## 2. Skills — Detail Index

### 2.1 market-research
| Veld | Waarde |
|---|---|
| **Doel** | Marktanalyse, concurrentieonderzoek, TAM/SAM/SOM |
| **Fasen** | 1. Scope → 2. Verzamelen → 3. Analyseren → 4. Rapporteren |
| **Output** | Markdown rapport met executive summary, data-tabellen, bronvermelding |
| **Dependencies** | web_search, web_fetch, read_file, write_file |
| **Voorbeeld output** | `output/market-research-consumer-ai-inference-belgium.md` |
| **Status** | ✅ Werkend, maar bekend probleem: "0 terug" bij rapport schrijven (context overflow). Fix in SOUL.md, wacht op test |

### 2.2 deep-research
| Veld | Waarde |
|---|---|
| **Doel** | Diepgaand multi-bron onderzoek over elk topic |
| **Fasen** | 1. Vraag definiëren → 2. Bronnen zoeken → 3. Diep lezen → 4. Synthetiseren → 5. Rapport |
| **Output** | Geciteerd onderzoeksdossier met claims + bronnen |
| **Dependencies** | web_search, web_fetch |
| **Status** | ✅ Werkend |

### 2.3 content-engine
| Veld | Waarde |
|---|---|
| **Doel** | Platform-native content maken (X, LinkedIn, nieuwsbrief, video) |
| **Principe** | Bron-eerst, anti-slop. Geen generieke AI-taal |
| **Fasen** | 1. Bron analyseren → 2. Platform selecteren → 3. Draft → 4. Herschrijven → 5. Review |
| **Output** | Platform-specifieke content in markdown |
| **Status** | ✅ Werkend |

### 2.4 brand-voice
| Veld | Waarde |
|---|---|
| **Doel** | Voice-profiel opbouwen uit echt bronmateriaal |
| **Fasen** | 1. Bronnen verzamelen → 2. Patronen extraheren → 3. Voice-kaart → 4. Validatie → 5. Opslaan |
| **Output** | Herbruikbaar voice-profiel (opgeslagen in workspace) |
| **Status** | ✅ Werkend |

### 2.5 investor-materials
| Veld | Waarde |
|---|---|
| **Doel** | Pitch decks, one-pagers, memo's, financiële modellen, accelerator-applicaties |
| **Fasen** | 1. Context verzamelen → 2. Structuur → 3. Draft → 4. Iteratie → 5. Final |
| **Output** | Investor-ready documenten in markdown |
| **Status** | ✅ Werkend |

### 2.6 investor-outreach
| Veld | Waarde |
|---|---|
| **Doel** | Cold emails, warm intros, follow-ups naar investeerders |
| **Principe** | Altijd gepersonaliseerd, nooit generiek. Geen spam. |
| **Fasen** | 1. Doelgroep → 2. Research per target → 3. Persoonlijke hook → 4. Draft → 5. Review |
| **Output** | Gepersonaliseerde outreach-berichten |
| **Status** | ✅ Werkend |

### 2.7 seo
| Veld | Waarde |
|---|---|
| **Doel** | Technische SEO-audits, on-page optimalisatie, structured data, keyword mapping |
| **Fasen** | 1. Crawl → 2. Technische audit → 3. Content audit → 4. Structured data → 5. Rapport |
| **Output** | SEO-audit rapport met actiepunten |
| **Status** | ✅ Werkend |

### 2.8 security-review
| Veld | Waarde |
|---|---|
| **Doel** | Code security checklists, input validatie, auth, CSRF, rate limiting, pre-deploy audits |
| **Fasen** | 1. Scope → 2. Checklist → 3. Scan → 4. Rapport → 5. Aanbevelingen |
| **Output** | Security-audit rapport met severity-scores |
| **Status** | ✅ Werkend |

### 2.9 continuous-learning
| Veld | Waarde |
|---|---|
| **Doel** | Instinct-systeem: patronen observeren, opslaan met confidence-scores, evolueren naar herbruikbare skills |
| **Fasen** | 1. Observeren → 2. Patroon herkennen → 3. Instinct opslaan → 4. Valideren → 5. Evolueren |
| **Output** | Instincts opgeslagen in memory (confidence-based) |
| **Status** | ✅ Werkend |

---

## 3. Config & Runtime

| Veld | Waarde |
|---|---|
| **Model** | qwen3:32b |
| **Provider** | ollama |
| **apiBase** | http://host.docker.internal:11434/v1 |
| **Heartbeat** | Elke 30 min, geen actieve taken |
| **Cron jobs** | Geen |
| **Memory** | Leeg (template-only) |

---

## 4. Bekende Problemen

| Probleem | Status |
|---|---|
| "0 terug" bij rapport schrijven (context overflow) | Fix in SOUL.md (strict phased execution), wacht op test |
| Geneste `workspace/` directory (dupliceert root) | Cosmetisch, geen functioneel probleem |

---

## 5. Gebruiksmogelijkheden — Wat we ermee kunnen

### Direct inzetbaar (via ART, zonder spawnen)
- Skill-instructies lezen en toepassen in dit gesprek
- Market research, deep research, content, SEO-audits uitvoeren met web_search + web_fetch

### Als aparte agent (via spawn)
- Zelfstandige business-toolkit agent die periodiek taken uitvoert
- Heartbeat-gedreven: marktdiensten monitoren, content produceren op schema
- Eigen memory, eigen cron jobs

### Koppeling met andere workspaces
- **editorial** → content-engine + brand-voice voor The Daily Stack
- **browser-harness** → SEO-audits op live sites, security-reviews op web-apps
- **Elke workspace** → deep-research voor onderwerpsverkenning

---

## 6. Bestanden per Categorie

### Identity files
- `config.json` — Agent configuratie
- `SOUL.md` — Persoonlijkheid, regels, phased execution protocol
- `AGENTS.md` — Rolbeschrijving, tool-instructies, restricties
- `TOOLS.md` — Tool-gebruik notities
- `HEARTBEAT.md` — Periodieke taken (leeg)
- `USER.md` — Gebruikersprofiel

### Skills
- `skills/market-research/SKILL.md`
- `skills/deep-research/SKILL.md`
- `skills/content-engine/SKILL.md`
- `skills/brand-voice/SKILL.md`
- `skills/investor-materials/SKILL.md`
- `skills/investor-outreach/SKILL.md`
- `skills/seo/SKILL.md`
- `skills/security-review/SKILL.md`
- `skills/continuous-learning/SKILL.md`

### Output
- `output/market-research-consumer-ai-inference-belgium.md`

### Memory & Scheduling
- `memory/MEMORY.md` — Leeg (template)
- `memory/HISTORY.md` — 1 entry (initialisatie)
- `cron/jobs.json` — Leeg

### Dupliceerde workspace
- `workspace/` — Volledige kopie van identity files (vermoedelijk artefact van initialisatie)