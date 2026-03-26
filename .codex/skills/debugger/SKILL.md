---
name: debugger
description: Use this skill when the repository contains `.agent/agents/debugger.md` and you want Codex to apply that local debugging persona. It is for bugs, crashes, regressions, root-cause analysis, and failure investigation.
---

# Debugger

## Overview

Use `.agent/agents/debugger.md` as the source of truth for debugging work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/debugger.md` exists.
2. Read the file from the top, including frontmatter and debug process.
3. Load the needed local skills from its `skills:` list: `clean-code`, `systematic-debugging`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Use this specialist to isolate root causes before broad refactors or multi-agent changes.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- Escalate to `orchestrator` when the fix spans multiple systems or needs coordinated execution.
