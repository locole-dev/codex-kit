---
name: explorer-agent
description: Use this skill when the repository contains `.agent/agents/explorer-agent.md` and you want Codex to apply that local discovery persona. It is for codebase audits, architecture mapping, repo exploration, and investigative analysis before planning or implementation.
---

# Explorer Agent

## Overview

Use `.agent/agents/explorer-agent.md` as the source of truth for discovery work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/explorer-agent.md` exists.
2. Read the file from the top, including frontmatter and investigation workflow.
3. Load the needed local skills from its `skills:` list: `clean-code`, `architecture`, `plan-writing`, `brainstorming`, `systematic-debugging`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Use this specialist to gather context before handing off to another implementation-oriented agent.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- Pair this skill with `project-planner` or `orchestrator` when discovery needs to turn into execution.
