---
description: Coordinate multiple specialists for complex work that spans more than one domain.
---

# /orchestrate - Multi-Specialist Coordination

$ARGUMENTS

## Goal

Use the `orchestrator` agent to coordinate the right specialists for a complex task.

## Workflow

1. Check whether the task already has a matching plan file.
2. If the task is large and no plan exists, create one with `project-planner` first.
3. Select only the specialists required by the affected domains.
4. Pass shared context forward so later specialists do not repeat discovery.
5. Run the narrowest relevant validation steps before closing the task.

## Typical Specialist Mix

| Task shape | Common specialists |
| --- | --- |
| Web feature | `frontend-specialist`, `backend-specialist`, `test-engineer` |
| Auth or security | `security-auditor`, `backend-specialist`, `test-engineer` |
| Data-heavy change | `database-architect`, `backend-specialist`, `security-auditor` |
| Release readiness | `devops-engineer`, `test-engineer`, `security-auditor` |
| Unknown codebase | `explorer-agent` first, then domain specialists |

## Rules

1. Do not force a fixed number of agents; use the minimum set that covers the task.
2. Do not create a new plan if an existing relevant plan already captures the work.
3. Keep ownership boundaries clear when multiple specialists touch the repo.
4. End with one synthesized report instead of separate unconnected outputs.

## Deliverables

- coordinated specialist work
- one final synthesis
- explicit validation summary
