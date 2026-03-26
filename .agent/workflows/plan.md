---
description: Create a project plan using the project-planner agent. Planning only; no code writing.
---

# /plan - Planning Mode

$ARGUMENTS

## Goal

Create or update a task-specific plan file in the project root. Do not write implementation code in this workflow.

## Rules

1. Use `project-planner`.
2. Ask only the clarifying questions needed to remove real ambiguity.
3. Reuse an existing matching plan file if one already exists.
4. Name the plan file from the task slug, not a fixed `PLAN.md`.
5. Report the exact file path that was created or updated.

## Output Convention

- File name: `./{task-slug}.md`
- Content should include:
  - goal
  - assumptions
  - scope
  - task breakdown
  - dependencies
  - validation strategy

## Example Names

| Request | Plan file |
| --- | --- |
| `/plan e-commerce site with cart` | `./ecommerce-cart.md` |
| `/plan add dark mode feature` | `./dark-mode.md` |
| `/plan refactor auth system` | `./auth-refactor.md` |

## After Planning

Report:

```text
[OK] Plan ready: ./{task-slug}.md
```
