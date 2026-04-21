Arena — 🔄 Partially done

UI section exists: team list, spawn test/prod, stop, promote to production, delegation log panel
Backend: Arena is built on top of the Teams spawn with mode: test — no separate arena.py router needed, and it's not needed per the Phase 3 spec
Missing pieces:
Delegation trace — the log panel shows entries from knowledge/shared.db's log table, but members aren't actually writing to it yet (agents would need a tool that POSTs to that table)
Session replay — not built (rerun a previous session's plan)
Member model override — temporarily swap one member's model without respawning
Phase 3 pipeline/cron mode — ❌ Not built

The spec describes a cron-driven mode where the manager polls knowledge/queue on a schedule — not yet implemented

----


the daily stack:
GitHub Pages is the easiest way to host your static sites for free.