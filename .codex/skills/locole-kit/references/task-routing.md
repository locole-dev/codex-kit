# Task Routing

Use this table to decide which `.agent` files to open first.

| Request type | Open first | Then open |
| --- | --- | --- |
| Need a broad map of the toolkit | `.agent/ARCHITECTURE.md` | Relevant agent, workflow, or skill files |
| Need to follow workspace rules | `.agent/rules/GEMINI.md` | Matching agent or workflow |
| Need to bootstrap or refresh repo-specific coding rules | `.agent/scripts/project_rules.py` | `.agent/PROJECT_RULES.md`, then the relevant agent/workflow |
| Multi-domain implementation | `.agent/agents/orchestrator.md` | Required specialist agents, then relevant skills |
| Planning or scoping | `.agent/agents/project-planner.md` | `.agent/workflows/plan.md`, planning skills |
| Codebase discovery | `.agent/agents/explorer-agent.md` | `ARCHITECTURE.md` if needed |
| Frontend or UI work | `.agent/agents/frontend-specialist.md` | `frontend-design`, `tailwind-patterns`, or `ui-ux-pro-max` resources |
| Backend or API work | `.agent/agents/backend-specialist.md` | `api-patterns`, `nodejs-best-practices`, `database-design` |
| Database design | `.agent/agents/database-architect.md` | `database-design` |
| Mobile work | `.agent/agents/mobile-developer.md` | `mobile-design` |
| Debugging | `.agent/agents/debugger.md` | `.agent/workflows/debug.md`, `systematic-debugging` |
| Security review | `.agent/agents/security-auditor.md` | `vulnerability-scanner`, `red-team-tactics` |
| Testing or QA | `.agent/agents/test-engineer.md` | `testing-patterns`, `webapp-testing`, `tdd-workflow` |
| Deployment | `.agent/agents/devops-engineer.md` | `.agent/workflows/deploy.md`, `deployment-procedures` |
| Product discovery | `.agent/agents/product-manager.md` or `.agent/agents/product-owner.md` | `brainstorming`, `plan-writing` |
| Run final checks | `.agent/rules/GEMINI.md` | `.agent/scripts/checklist.py` or `.agent/scripts/verify_all.py` |
| MCP setup | `.agent/mcp_config.json` | Relevant environment files |

## Selective loading rules

1. Read one primary entry file first.
2. If it references a skill, open that skill's `SKILL.md` before any companion docs.
3. Load only the specific follow-up files needed for the request.
4. Prefer focused skill scripts over broad all-project scripts when the task is narrow.
