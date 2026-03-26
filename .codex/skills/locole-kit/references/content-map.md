# `.agent` Content Map

Use this file as a compact directory guide before opening larger `.agent` files.

## Top level

| Path | Purpose | Open when |
| --- | --- | --- |
| `.agent/ARCHITECTURE.md` | High-level map of agents, skills, workflows, and scripts | You need global orientation |
| `.agent/PROJECT_RULES.md` | Generated project-specific coding rules | Before implementation or refactoring, if it exists |
| `.agent/rules/GEMINI.md` | Workspace operating rules and routing policy | Before code, design, or orchestration |
| `.agent/mcp_config.json` | Example MCP server configuration | MCP setup or troubleshooting |

## Agents

Open one file from `.agent/agents/` when the request has a clear domain owner.

Common entries:

| Agent file | Primary use |
| --- | --- |
| `orchestrator.md` | Cross-domain work and multi-agent coordination |
| `project-planner.md` | Planning, breakdowns, scope discovery |
| `frontend-specialist.md` | Web UI and frontend implementation |
| `backend-specialist.md` | API and server-side work |
| `database-architect.md` | Schema and data modeling |
| `debugger.md` | Root-cause analysis |
| `devops-engineer.md` | Deployment and CI/CD |
| `test-engineer.md` | Test strategy and coverage |
| `security-auditor.md` | Security review and hardening |
| `mobile-developer.md` | Mobile product and app tasks |

## Workflows

Files under `.agent/workflows/` are command-style procedures:

| Workflow file | Use for |
| --- | --- |
| `brainstorm.md` | Discovery and ideation |
| `create.md` | New feature or product creation |
| `debug.md` | Structured debugging |
| `deploy.md` | Deployment flow |
| `enhance.md` | Improving existing functionality |
| `orchestrate.md` | Multi-agent execution |
| `plan.md` | Planning and task breakdown |
| `preview.md` | Preview and review flow |
| `status.md` | Project status checks |
| `test.md` | Test execution flow |
| `ui-ux-pro-max.md` | Rich UI/design process |

## Skills

Files under `.agent/skills/` are reusable domain packs. Open `SKILL.md` first.

Representative skill groups:

| Group | Examples |
| --- | --- |
| Architecture and planning | `architecture`, `app-builder`, `brainstorming`, `plan-writing` |
| Frontend and UI | `frontend-design`, `tailwind-patterns`, `web-design-guidelines`, `nextjs-react-expert` |
| Backend and data | `api-patterns`, `database-design`, `nodejs-best-practices`, `python-patterns` |
| Quality and testing | `testing-patterns`, `webapp-testing`, `tdd-workflow`, `lint-and-validate` |
| Security and ops | `vulnerability-scanner`, `red-team-tactics`, `deployment-procedures`, `server-management` |
| Mobile and game | `mobile-design`, `game-development` |

## Shared design dataset

| Path | Notes |
| --- | --- |
| `.agent/.shared/ui-ux-pro-max/data/` | CSV datasets for design styles, colors, typography, icons, stacks, and UX guidance |
| `.agent/.shared/ui-ux-pro-max/scripts/` | Helpers for design system generation and search |

Load these only for design-heavy tasks that explicitly benefit from the larger dataset.

## Validation scripts

| Path | Scope |
| --- | --- |
| `.agent/scripts/project_rules.py` | Bootstrap or refresh repo-specific coding rules |
| `.agent/scripts/checklist.py` | Core validation suite |
| `.agent/scripts/verify_all.py` | Broader end-to-end verification |

Many skills also expose focused scripts under `.agent/skills/<skill>/scripts/`.
