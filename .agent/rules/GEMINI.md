---
trigger: always_on
---

# Workspace Rules (GEMINI Compatibility)

> This file keeps the conventional `GEMINI.md` name for compatibility. In the Locole toolkit it is the top-level workspace policy file, not a vendor-specific runtime contract.

## Core Policy

1. Start with the smallest relevant context.
2. Read selectively before acting.
3. Prefer the narrowest agent, workflow, or skill that can solve the task.
4. Preserve existing project patterns unless the user explicitly asks for a redesign.
5. Validate the changed surface area before you finish.

## Loading Order

Use this order unless the task clearly needs less:

1. `.agent/rules/GEMINI.md`
2. `.agent/PROJECT_RULES.md` if it exists and the task involves implementation, refactoring, or tests
3. One primary file from:
   - `.agent/agents/`
   - `.agent/workflows/`
   - `.agent/skills/<name>/SKILL.md`
4. Only the follow-up files referenced by that primary file
5. `.agent/ARCHITECTURE.md` if you still need broader context

## Routing Rules

### When to open an agent

- Open an agent file for implementation, review, or domain-specific problem solving.
- Use `orchestrator` when the request clearly spans multiple domains.
- Use `project-planner` when the user wants planning, sequencing, or a written plan instead of code.
- Use `explorer-agent` when you first need to map an unfamiliar codebase.

### When to open a workflow

- Open a workflow for command-style tasks such as planning, debugging, deployment, testing, preview, or orchestration.
- Follow workflow gating rules when the workflow includes mandatory checkpoints.

### When to open a skill

- Open `SKILL.md` first.
- If `SKILL.md` acts as an index, only load the referenced support files needed for the active task.
- Prefer skill-local scripts over broad all-project scripts when the task is narrow.

## Planning vs. Implementation

- If the user asks for planning only, produce a plan and do not write code.
- If the task is implementation work and the path is reasonably clear, proceed directly instead of forcing a planning ceremony.
- Reuse an existing plan file when one already covers the task. Do not create duplicates without a reason.

## Communication Rules

- Reply in the user's language when practical.
- Keep code, identifiers, and code comments in English unless the codebase already uses another convention.
- Ask clarifying questions only when a wrong assumption would materially change the result.

## Change Rules

- Make the smallest coherent change that solves the request.
- Keep related files in sync when a change affects public APIs, schemas, plans, or docs.
- Avoid large speculative rewrites unless the user explicitly asks for them.

## Validation Rules

- Run the narrowest relevant validation first.
- If the user asks to bootstrap or refresh repo-specific coding rules, run `python .agent/scripts/project_rules.py sync .` and then read `.agent/PROJECT_RULES.md`.
- Use `.agent/scripts/checklist.py` for broad development-time checks.
- Use `.agent/scripts/verify_all.py` for broader release-style checks.
- Report which checks ran, what failed, and any important gaps when you could not run a check.

## Environment and MCP

- Read `.agent/mcp_config.json` only for MCP setup or troubleshooting.
- Treat that file as an example configuration, not a guarantee about the current machine.

## Quick Reference

- Architecture map: `.agent/ARCHITECTURE.md`
- Workflow and routing map: `.agent/WORKFLOW-AGENT-SKILL-MAP.md`
- Root validation scripts: `.agent/scripts/`
- Shared UI dataset: `.agent/.shared/ui-ux-pro-max/`
