---
name: plan-workflow
description: Use this skill when a repository contains `.agent/workflows/plan.md` and you want Codex to apply that local planning workflow. It is for plan-file generation, task breakdown, dynamic plan naming, and planning-only mode without code changes.
---

# Plan Workflow

## Overview

Use `.agent/workflows/plan.md` as the source of truth for planning mode in this repository.
Read that file first, then follow its no-code rule, Socratic gate, dynamic file naming, and planning deliverable requirements.

## Workflow

1. Confirm `.agent/workflows/plan.md` exists.
2. Read the workflow file from the top.
3. Stay in planning-only mode and avoid code changes.
4. Route the work through the local `project-planner` guidance.
5. Create and report the exact `docs/PLAN-{slug}.md` file specified by the workflow.

## Notes

- Treat the local workflow markdown as authoritative over this wrapper.
- Use this when the deliverable is a plan, not an implementation.
