# Decisions

## 2026-04-18 — Strict Phased Execution als harde regel
**Context**: Agents (vooral business-toolkit) crashen met "0 terug" bij complexe taken. Ze proberen alles in één turn te doen, context raakt vol, model geeft niets terug.
**Besluit**: Strict Phased Execution toevoegen als hard rule in SOUL.md van elke workspace. Agent moet per fase stoppen, opslaan, en rapporteren.
**Alternatieven**: Kleinere chunks schrijven (binnen één turn) — lost het niet op want context blijft vol.

## 2026-04-18 — Docs bestandssysteem voor ART
**Context**: MEMORY.md raakt snel vol als alle content daar wordt opgeslagen.
**Besluit**: /workspace/docs/ als archief. MEMORY.md wordt de index (korte notities + verwijzingen). Content leeft in docs/todos.md, docs/issues.md, docs/decisions.md, docs/projects/.
**Alternatieven**: Alles in MEMORY.md — schaalt niet.