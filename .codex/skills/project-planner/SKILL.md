---
name: project-planner
description: Use this skill when the repository contains `.agent/agents/project-planner.md` and you want Codex to apply that local planning persona. It is for new projects, major feature planning, task breakdowns, file-structure planning, and dependency sequencing.
---

# Project Planner

## Overview

Use `.agent/agents/project-planner.md` as the source of truth for planning work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/project-planner.md` exists.
2. Read the file from the top, including frontmatter, planning phases, and output expectations.
3. Load the needed local skills from its `skills:` list: `clean-code`, `app-builder`, `plan-writing`, `brainstorming`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. If a matching planning workflow exists under `.agent/workflows/`, read that too before drafting the plan.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- Hand off to `orchestrator` when the plan is ready for coordinated implementation.
