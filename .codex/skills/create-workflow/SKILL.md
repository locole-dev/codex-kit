---
name: create-workflow
description: Use this skill when a repository contains `.agent/workflows/create.md` and you want Codex to apply that local creation workflow. It is for starting new apps, new features, or new product builds with planning, agent coordination, and preview setup.
---

# Create Workflow

## Overview

Use `.agent/workflows/create.md` as the source of truth for creation flows in this repository.
Read that file first, then follow its sequence from request analysis to planning, build coordination, and preview.

## Workflow

1. Confirm `.agent/workflows/create.md` exists.
2. Read the workflow file from the top.
3. Clarify missing product details before building.
4. Route planning through `project-planner`, then hand off implementation through the local builder and specialist agents.
5. Finish by starting or updating preview if the workflow calls for it.

## Notes

- Treat the local workflow markdown as authoritative over this wrapper.
- Use this workflow for new build requests; use `enhance-workflow` for iterative changes to an existing app.
