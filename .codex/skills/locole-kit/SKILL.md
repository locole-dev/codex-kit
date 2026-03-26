---
name: locole-kit
description: Use this skill when working in a repository that contains the Locole `.agent` toolkit and Codex needs to follow its local operating model. It covers routing a request to the right `.agent/agents/*.md`, `.agent/skills/*`, `.agent/workflows/*.md`, workspace rules in `.agent/rules/GEMINI.md`, architecture discovery in `.agent/ARCHITECTURE.md`, validation scripts in `.agent/scripts/`, and MCP hints in `.agent/mcp_config.json`.
---

# Locole Kit

## Overview

Use the local `.agent` directory as the source of truth for project-specific agent behavior, workflow commands, and reusable skills.
Read selectively: load the smallest number of files needed to satisfy the request.

## Quick Start

1. Confirm that `.agent/` exists in the workspace root.
2. For first-time onboarding or whenever the stack changes, run `python .agent/scripts/project_rules.py sync .` and then read `.agent/PROJECT_RULES.md`.
3. Read `.agent/rules/GEMINI.md` before code, design, orchestration, or validation work. Treat it as the highest-priority workspace policy and compatibility entrypoint.
4. Read `.agent/ARCHITECTURE.md` when you need a global map of agents, skills, workflows, and validation scripts.
5. Route the request to the smallest relevant subset of `.agent` files using [references/task-routing.md](references/task-routing.md).
6. If a `.agent/skills/<name>/SKILL.md` file is needed, read that index first and then open only the referenced support files that match the task.
7. If the user asks for checks, audits, or final verification, choose the narrowest matching script first; use `.agent/scripts/checklist.py` or `.agent/scripts/verify_all.py` for broad project validation.

## Onboarding Command

Use this exact command in chat when entering a repo for the first time or when you want to refresh the repo-specific rules:

`Use $locole-kit and sync the project rule for this repository.`

When triggered, you should:

1. Run `python .agent/scripts/project_rules.py sync .`
2. Read `.agent/PROJECT_RULES.md`
3. Summarize the key generated rules back to the user
4. Follow those rules for later implementation work in the repository

## Routing Rules

### Agent routing

- For implementation tasks, read the matching file in `.agent/agents/`.
- If the task spans multiple domains, start with `.agent/agents/orchestrator.md`.
- If the request is vague and needs decomposition, prefer `.agent/agents/project-planner.md` or `.agent/agents/explorer-agent.md`.

### Workflow routing

- For slash-command style requests such as planning, debugging, deploying, testing, brainstorming, or orchestration, read the matching file in `.agent/workflows/`.
- Follow the workflow literally when it includes gating steps, required artifacts, or approval checkpoints.

### Skill routing

- For domain guidance, read `.agent/skills/<skill>/SKILL.md` first.
- If that `SKILL.md` acts as an index, load only the specific companion files it points to.
- Treat `.agent/.shared/ui-ux-pro-max/` as a large optional resource set. Read or execute only the exact files needed for UI/design tasks.

## File Loading Order

Use this order unless the task clearly requires a smaller subset:

1. `.agent/rules/GEMINI.md`
2. `.agent/PROJECT_RULES.md` if it exists and the task involves implementation or refactoring
3. One of:
   - `.agent/agents/<agent>.md`
   - `.agent/workflows/<workflow>.md`
   - `.agent/skills/<skill>/SKILL.md`
4. Only the referenced support files for that path
5. `.agent/ARCHITECTURE.md` if you still need broader context

## Validation

- Use `.agent/scripts/project_rules.py sync .` to bootstrap or refresh project-specific coding rules.
- Use `.agent/scripts/checklist.py` for general development-time checks.
- Use `.agent/scripts/verify_all.py` for broader release-style verification.
- Prefer skill-local scripts under `.agent/skills/<skill>/scripts/` when the request is narrow, such as accessibility, SEO, schema, or security scans.
- Report which scripts ran and summarize failures by severity.

## MCP And Environment Notes

- Read `.agent/mcp_config.json` only when the task involves MCP setup or server registration.
- Treat entries in that file as examples until verified against the current environment.

## References

- Use [references/content-map.md](references/content-map.md) for a compact map of `.agent`.
- Use [references/task-routing.md](references/task-routing.md) to decide which files to open first for common request types.
- Avoid bulk-loading every agent, workflow, or skill file unless the user explicitly asks for a full audit of `.agent`.
