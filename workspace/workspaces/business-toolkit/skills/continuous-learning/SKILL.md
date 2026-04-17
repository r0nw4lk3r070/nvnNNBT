# Continuous Learning

Instinct-based learning system that observes sessions, creates atomic instincts with confidence scoring, and evolves them into reusable skills and patterns.

## Tools

- `read_file` — read existing instinct files, observations, and skill definitions
- `write_file` — create and save instinct files, evolved skills
- `edit_file` — update instincts, adjust confidence scores
- `exec` — run project detection, list files, manage instinct directories

## When to Activate

- Reviewing patterns from a completed session or task
- Extracting reusable behaviors from user corrections and preferences
- Tuning confidence thresholds for learned behaviors
- Reviewing, exporting, or importing instinct libraries
- Evolving instincts into full skills or workflows
- Managing project-scoped vs global instincts
- Promoting instincts from project to global scope

## The Instinct Model

An instinct is a small learned behavior:

```yaml
---
id: prefer-functional-style
trigger: "when writing new functions"
confidence: 0.7
domain: "code-style"
source: "session-observation"
scope: project
project_id: "a1b2c3d4e5f6"
project_name: "my-react-app"
---

# Prefer Functional Style

## Action
Use functional patterns over classes when appropriate.

## Evidence
- Observed 5 instances of functional pattern preference
- User corrected class-based approach to functional on 2025-01-15
```

**Properties:**
- **Atomic** — one trigger, one action
- **Confidence-weighted** — 0.3 = tentative, 0.9 = near certain
- **Domain-tagged** — code-style, testing, git, debugging, workflow, etc.
- **Evidence-backed** — tracks what observations created it
- **Scope-aware** — `project` (default) or `global`

## How It Works

```
Session Activity (in a project directory)
      |
      | Agent observes prompts, tool calls, outcomes
      | + detects project context (git remote / repo path)
      v
+---------------------------------------------+
|  projects/<project-hash>/observations.jsonl  |
|   (prompts, tool calls, outcomes, project)  |
+---------------------------------------------+
      |
      | Pattern detection (manual or triggered)
      v
+---------------------------------------------+
|          PATTERN DETECTION                   |
|   * User corrections -> instinct             |
|   * Error resolutions -> instinct            |
|   * Repeated workflows -> instinct           |
|   * Scope decision: project or global?       |
+---------------------------------------------+
      |
      | Creates/updates
      v
+---------------------------------------------+
|  projects/<project-hash>/instincts/personal/ |
|   * prefer-functional.yaml (0.7) [project]  |
|   * use-react-hooks.yaml (0.9) [project]    |
+---------------------------------------------+
|  instincts/personal/  (GLOBAL)               |
|   * always-validate-input.yaml (0.85) [global]|
|   * grep-before-edit.yaml (0.6) [global]     |
+---------------------------------------------+
      |
      | Evolution
      v
+---------------------------------------------+
|  projects/<hash>/evolved/ (project-scoped)  |
|  evolved/ (global)                           |
|   * commands/new-feature.md                  |
|   * skills/testing-workflow.md               |
|   * agents/refactor-specialist.md            |
+---------------------------------------------+
```

## Project Detection

The system detects the current project automatically:

1. **Git remote URL** — hashed to create a portable project ID (same repo on different machines gets the same ID)
2. **Git repo root path** — fallback using local path (machine-specific)
3. **Global fallback** — if no project is detected, instincts go to global scope

Each project gets a 12-character hash ID (e.g., `a1b2c3d4e5f6`). A registry file maps IDs to human-readable names.

Use `exec` to detect project context:
```bash
git remote get-url origin 2>/dev/null || echo "no-remote"
git rev-parse --show-toplevel 2>/dev/null || echo "no-repo"
```

## Creating Instincts

When you observe a pattern worth remembering, create an instinct:

1. **Identify the pattern** — user correction, repeated workflow, error resolution
2. **Write the instinct YAML** — trigger, action, confidence, domain, scope
3. **Save to the right scope** — project instinct in `projects/<hash>/instincts/`, global in `instincts/personal/`
4. **Set initial confidence** — start at 0.3 for new patterns, higher for explicit corrections

### Instinct Creation Steps

1. Observe a pattern in the current session
2. Determine scope: is this project-specific or universally applicable?
3. Write the instinct file with YAML frontmatter and markdown body
4. Save it using `write_file` to the appropriate directory
5. Log the instinct creation in `memory/HISTORY.md`

## Confidence Scoring

Confidence evolves over time:

| Score | Meaning | Behavior |
|-------|---------|----------|
| 0.3 | Tentative | Suggested but not enforced |
| 0.5 | Moderate | Applied when relevant |
| 0.7 | Strong | Auto-approved for application |
| 0.9 | Near-certain | Core behavior |

**Confidence increases** when:
- Pattern is repeatedly observed
- User doesn't correct the suggested behavior
- Similar instincts from other sources agree

**Confidence decreases** when:
- User explicitly corrects the behavior
- Pattern isn't observed for extended periods
- Contradicting evidence appears

## Instinct Evolution

Related instincts can be clustered and evolved into full skills:

1. **Review instincts** — find related instincts in the same domain
2. **Cluster** — group instincts that share triggers or themes
3. **Synthesize** — combine into a coherent skill SKILL.md
4. **Save** — write the evolved skill to the `evolved/` directory
5. **Update** — mark source instincts as evolved, increase their confidence

## Scope Decision Guide

| Pattern Type | Scope | Examples |
|-------------|-------|---------|
| Language/framework conventions | **project** | "Use React hooks", "Follow Django REST patterns" |
| File structure preferences | **project** | "Tests in `tests/`", "Components in src/components/" |
| Code style | **project** | "Use functional style", "Prefer dataclasses" |
| Error handling strategies | **project** | "Use Result type for errors" |
| Security practices | **global** | "Validate user input", "Sanitize SQL" |
| General best practices | **global** | "Write tests first", "Always handle errors" |
| Tool workflow preferences | **global** | "Read before Edit", "Search before Write" |
| Git practices | **global** | "Conventional commits", "Small focused commits" |

## Instinct Promotion (Project → Global)

When the same instinct appears in multiple projects with high confidence, it's a candidate for promotion to global scope.

**Auto-promotion criteria:**
- Same instinct ID in 2+ projects
- Average confidence >= 0.8

**How to promote:**

1. Identify instincts that appear across multiple projects
2. Verify they meet confidence thresholds
3. Copy the instinct to `instincts/personal/` (global)
4. Update the scope from `project` to `global`
5. Log the promotion in `memory/HISTORY.md`

## File Structure

```
<workspace>/
+-- identity.json              # Your profile, technical level
+-- projects.json              # Registry: project hash -> name/path/remote
+-- observations.jsonl         # Global observations (fallback)
+-- instincts/
|   +-- personal/              # Global auto-learned instincts
|   +-- inherited/             # Global imported instincts
+-- evolved/
|   +-- skills/                # Global generated skills
|   +-- commands/              # Global generated commands
+-- projects/
    +-- a1b2c3d4e5f6/          # Project hash (from git remote URL)
    |   +-- project.json       # Per-project metadata
    |   +-- observations.jsonl
    |   +-- instincts/
    |   |   +-- personal/      # Project-specific auto-learned
    |   |   +-- inherited/     # Project-specific imported
    |   +-- evolved/
    |       +-- skills/
    |       +-- commands/
    +-- f6e5d4c3b2a1/          # Another project
        +-- ...
```

## Privacy

- Observations stay **local** on the machine
- Project-scoped instincts are isolated per project
- Only **instincts** (patterns) can be exported — not raw observations
- No actual code or conversation content is shared
- You control what gets exported and promoted

## Quality Gate

Before creating or evolving an instinct:
- the pattern is genuinely repeatable, not a one-off
- the trigger is specific enough to be useful
- the action is actionable, not vague
- confidence is set appropriately (0.3 for new, higher for confirmed patterns)
- scope is correct (project vs global)