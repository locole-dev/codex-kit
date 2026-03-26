---
name: orchestrator
description: Use this skill when the repository contains `.agent/agents/orchestrator.md` and you want Codex to apply that local multi-agent coordination persona. It is for complex work that spans multiple domains and benefits from planning, decomposition, sequencing, and coordinated specialist execution.
---

# Orchestrator

## Overview

Use `.agent/agents/orchestrator.md` as the source of truth for cross-domain work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/orchestrator.md` exists.
2. Read the file from the top, including frontmatter, coordination rules, and sequencing requirements.
3. Load the needed local skills from its `skills:` list: `clean-code`, `parallel-agents`, `behavioral-modes`, `plan-writing`, `brainstorming`, `architecture`, `lint-and-validate`, `powershell-windows`, `bash-linux`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. If a matching workflow exists under `.agent/workflows/`, read that too before implementation.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- Respect any minimum-agent, approval, or verification gates defined by the local orchestration workflow.
