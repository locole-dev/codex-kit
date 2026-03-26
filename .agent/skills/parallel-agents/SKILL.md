---
name: parallel-agents
description: Multi-agent orchestration patterns. Use when multiple independent tasks can run with different domain expertise or when comprehensive analysis requires multiple perspectives.
allowed-tools: Read, Glob, Grep
---

# Parallel Agents

Use this skill when a task benefits from multiple specialist passes or true parallel subagents in a runtime that supports them.

## When To Use It

Good fits:

- cross-domain tasks touching frontend, backend, testing, and security
- comprehensive reviews that need independent perspectives
- work that can be split into non-overlapping subtasks

Do not use it for:

- simple single-file fixes
- tightly coupled work that must stay on one critical path
- situations where the next action depends on one blocking answer

## Coordination Rules

1. Decide the immediate blocking task first.
2. Keep blocking work local when possible.
3. Delegate only bounded side work or genuinely parallel work.
4. Give each delegated task a clear ownership boundary.
5. Pass forward only the context the specialist actually needs.

## Recommended Patterns

### Discovery then specialists

```text
explorer-agent -> domain specialists -> synthesis
```

Use when the codebase is unfamiliar.

### Feature slice split

```text
backend-specialist + frontend-specialist + test-engineer
```

Use when each owns a different file set.

### Security verification lane

```text
implementation specialist + security-auditor + test-engineer
```

Use when auth, secrets, or data boundaries are involved.

## Available Specialists

| Agent | Best for |
| --- | --- |
| `explorer-agent` | Repository discovery |
| `project-planner` | Scoping and sequencing |
| `frontend-specialist` | Web UI |
| `backend-specialist` | APIs and server logic |
| `database-architect` | Schema and queries |
| `mobile-developer` | Mobile implementation |
| `security-auditor` | Defensive review |
| `penetration-tester` | Offensive testing |
| `test-engineer` | Test strategy and gaps |
| `qa-automation-engineer` | E2E automation |
| `performance-optimizer` | Profiling and speed |
| `devops-engineer` | CI/CD and deployment |
| `documentation-writer` | Docs-only requests |
| `seo-specialist` | Discoverability work |
| `debugger` | Root-cause analysis |
| `game-developer` | Game systems |

## Output Expectations

After multiple specialists finish:

1. Merge findings into one coherent report.
2. Resolve or flag conflicts explicitly.
3. Keep recommendations ordered by severity or delivery order.
4. Summarize which validations still need to run.

## Important Reminder

Parallelism is useful only when it reduces waiting. If coordination overhead is larger than the gain, use one specialist and continue directly.
