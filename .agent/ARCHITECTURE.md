# Locole Kit Architecture

> Reference map for the Locole `.agent` toolkit.

## Overview

This toolkit is organized around:

- `20` specialist agents under `.agent/agents/`
- `37` reusable skills under `.agent/skills/`
- `11` command-style workflows under `.agent/workflows/`
- `5` root utility scripts under `.agent/scripts/`

Use this file as the high-level map. Open the smallest relevant file after this one instead of loading the whole toolkit into context.

## Directory Layout

```text
.agent/
|-- ARCHITECTURE.md
|-- PROJECT_RULES.md        (generated on demand)
|-- WORKFLOW-AGENT-SKILL-MAP.md
|-- agents/
|-- rules/
|-- scripts/
|-- skills/
|-- workflows/
`-- .shared/
```

## Agents

Open one agent file when the task has a clear domain owner.

| Agent | Focus |
| --- | --- |
| `backend-specialist` | APIs, business logic, integrations |
| `code-archaeologist` | Legacy code, reverse engineering, refactors |
| `database-architect` | Schema design, queries, migrations |
| `debugger` | Root-cause analysis and failure isolation |
| `devops-engineer` | CI/CD, infra, release operations |
| `documentation-writer` | READMEs, docs, changelogs |
| `explorer-agent` | Codebase discovery and repo mapping |
| `frontend-specialist` | Web UI, components, styling |
| `game-developer` | Gameplay systems and engine-specific work |
| `mobile-developer` | Native or cross-platform mobile work |
| `orchestrator` | Multi-domain coordination |
| `penetration-tester` | Offensive security testing |
| `performance-optimizer` | Runtime, bundle, and UX performance |
| `product-manager` | Requirements and acceptance criteria |
| `product-owner` | Scope, backlog, and prioritization |
| `project-planner` | Planning, sequencing, task breakdowns |
| `qa-automation-engineer` | End-to-end automation and QA flows |
| `security-auditor` | Defensive security review and hardening |
| `seo-specialist` | SEO, GEO, discoverability |
| `test-engineer` | Test design, coverage, verification |

## Skills

Skills are reusable knowledge packs. Open `SKILL.md` first, then only the referenced follow-up files you actually need.

### Architecture and planning

`app-builder`, `architecture`, `behavioral-modes`, `brainstorming`, `clean-code`, `intelligent-routing`, `parallel-agents`, `plan-writing`

### Frontend and UX

`frontend-design`, `nextjs-react-expert`, `tailwind-patterns`, `web-design-guidelines`

### Backend and data

`api-patterns`, `database-design`, `mcp-builder`, `nodejs-best-practices`, `python-patterns`, `rust-pro`

### Quality and testing

`code-review-checklist`, `lint-and-validate`, `tdd-workflow`, `testing-patterns`, `webapp-testing`

### Security and operations

`deployment-procedures`, `red-team-tactics`, `server-management`, `vulnerability-scanner`

### Platform-specific

`bash-linux`, `powershell-windows`, `mobile-design`, `game-development`

### Growth and content

`documentation-templates`, `geo-fundamentals`, `i18n-localization`, `performance-profiling`, `seo-fundamentals`

## Workflows

Workflows are command-style procedures for common task shapes.

| Workflow | Use for |
| --- | --- |
| `brainstorm` | Discovery, option exploration, trade-offs |
| `create` | New feature or product creation |
| `debug` | Structured debugging |
| `deploy` | Deployment and rollback flows |
| `enhance` | Improvements to existing functionality |
| `orchestrate` | Multi-agent or multi-specialist coordination |
| `plan` | Plan generation only |
| `preview` | Local preview lifecycle |
| `status` | Project status snapshots |
| `test` | Test generation and execution |
| `ui-ux-pro-max` | Design-system and UI-heavy work |

## Shared Resources

`ui-ux-pro-max` uses the dataset and helper scripts under `.agent/.shared/ui-ux-pro-max/`.

- `data/` contains styles, palettes, typography, product, and stack CSVs.
- `scripts/` contains helpers for search and design-system generation.

Load these only for design-heavy tasks that benefit from the larger dataset.

## Root Scripts

| Script | Purpose |
| --- | --- |
| `.agent/scripts/auto_preview.py` | Start, stop, and inspect a local preview server |
| `.agent/scripts/checklist.py` | Core validation checklist |
| `.agent/scripts/project_rules.py` | Generate or refresh repo-specific coding rules |
| `.agent/scripts/session_manager.py` | Quick project/session summary |
| `.agent/scripts/verify_all.py` | Broader release-style verification |

Many skills also ship focused scripts under `.agent/skills/<skill>/scripts/`.

## Recommended Loading Order

1. Read `.agent/rules/GEMINI.md` for workspace policy.
2. Read `.agent/PROJECT_RULES.md` if it exists and you are about to implement or refactor code.
3. Read one primary file:
   - `.agent/agents/<agent>.md`
   - `.agent/workflows/<workflow>.md`
   - `.agent/skills/<skill>/SKILL.md`
4. Load only the referenced support files you need.
5. Run the narrowest relevant script for verification.

## Notes

- The filename `GEMINI.md` is kept for compatibility with toolchains that expect it.
- The toolkit is designed to be selective. Avoid bulk-loading every file in `.agent`.
- If you need routing help, see `WORKFLOW-AGENT-SKILL-MAP.md`.
