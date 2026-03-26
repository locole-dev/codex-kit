# Workflow Agent Skill Map

This document explains how the Locole toolkit layers `workflow`, `agent`, and `skill`.

## Mental Model

- `workflow`: the procedure for a task shape
- `agent`: the primary specialist or persona that executes the work
- `skill`: the focused knowledge, scripts, or references the agent loads on demand

Typical flow:

```text
workflow -> agent -> skill -> referenced files/scripts
```

Workspace-wide policy still comes from [rules/GEMINI.md](./rules/GEMINI.md).

## Routing Types

### Hard-routed workflow

The workflow strongly implies one main agent or one exact procedure.

### Soft-routed workflow

The workflow defines the frame, while the concrete agent depends on the current task.

## Workflow Map

| Workflow | Routing style | Typical agent or skill path |
| --- | --- | --- |
| `brainstorm` | Soft-routed | `project-planner`, `product-manager`, `product-owner`, `brainstorming` |
| `create` | Hard-routed | `project-planner` -> implementation specialists |
| `debug` | Soft-routed | `debugger`, sometimes `explorer-agent` or `test-engineer` |
| `deploy` | Soft-routed | `devops-engineer`, `deployment-procedures`, `server-management` |
| `enhance` | Soft-routed | Relevant specialist based on the affected layer |
| `orchestrate` | Hard-routed | `orchestrator` plus the required specialists |
| `plan` | Hard-routed | `project-planner` |
| `preview` | Soft-routed | Preview scripts, sometimes `devops-engineer` |
| `status` | Soft-routed | `explorer-agent`, `project-planner`, or the active specialist |
| `test` | Soft-routed | `test-engineer`, `qa-automation-engineer`, testing skills |
| `ui-ux-pro-max` | Hard-routed | UI workflow file plus shared design dataset and scripts |

## What Each Layer Owns

### Workflow

- Defines sequencing
- Defines checkpoints
- Defines output expectations

### Agent

- Owns the main reasoning style for the domain
- Decides how to apply the domain rules
- Loads the skills declared in its frontmatter

### Skill

- Provides reusable knowledge
- Points to scripts, references, and templates
- Should be loaded selectively, not wholesale

## Practical Examples

### Example: frontend feature

1. Open `workflows/enhance.md` if the request is framed as an improvement.
2. Route to `agents/frontend-specialist.md`.
3. Load only the needed skills such as `frontend-design`, `tailwind-patterns`, or `lint-and-validate`.

### Example: planning-only request

1. Open `workflows/plan.md`.
2. Use `agents/project-planner.md`.
3. Load planning skills like `plan-writing`, `brainstorming`, or `architecture` only as needed.

### Example: multi-domain implementation

1. Open `workflows/orchestrate.md`.
2. Use `agents/orchestrator.md`.
3. Pull in only the specialists needed for the affected domains.

## Good Defaults

- Start with one primary file.
- Prefer one agent over many when the task is clearly single-domain.
- Escalate to orchestration only when the task genuinely crosses boundaries.
- Reuse existing plan files instead of creating parallel planning tracks.

## Reminder

`workflow` does not replace `agent`, and `agent` does not replace `skill`.

They are separate layers:

- workflow = how the task should flow
- agent = who leads the task
- skill = what specialized knowledge gets loaded
