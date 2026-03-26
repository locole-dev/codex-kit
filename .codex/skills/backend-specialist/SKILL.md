---
name: backend-specialist
description: Use this skill when the repository contains `.agent/agents/backend-specialist.md` and you want Codex to apply that local backend persona, process, and decision rules. It is for API development, server-side logic, database integration, auth, and related backend architecture work.
---

# Backend Specialist

## Overview

Use `.agent/agents/backend-specialist.md` as the source of truth for backend work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/backend-specialist.md` exists.
2. Read the agent file from the top, including frontmatter and decision rules.
3. Load only the needed local skills from its `skills:` list: `clean-code`, `nodejs-best-practices`, `python-patterns`, `api-patterns`, `database-design`, `mcp-builder`, `lint-and-validate`, `powershell-windows`, `bash-linux`, `rust-pro`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Use agent- or skill-level validation scripts when the task touches behavior, schema, or security.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- If a listed local skill is missing, continue with the closest available local guidance and note the gap.
- Switch to `.agent/agents/orchestrator.md` for cross-domain tasks instead of stretching this specialist too far.
