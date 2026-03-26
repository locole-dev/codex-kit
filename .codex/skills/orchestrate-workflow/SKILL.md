---
name: orchestrate-workflow
description: Use this skill when a repository contains `.agent/workflows/orchestrate.md` and you want Codex to apply that local orchestration workflow. It is for complex tasks that need multi-agent planning, coordination, verification, and synthesis.
---

# Orchestrate Workflow

## Overview

Use `.agent/workflows/orchestrate.md` as the source of truth for multi-agent orchestration in this repository.
Read that file first, then follow its required planning phase, approval gate, multi-agent minimum, and verification requirements.

## Workflow

1. Confirm `.agent/workflows/orchestrate.md` exists.
2. Read the workflow file from the top.
3. Respect the minimum-agent and phase rules before delegating work.
4. Complete planning and any required user approval before implementation orchestration.
5. Finish with the required verification scripts and a synthesized orchestration report.

## Notes

- Treat the local workflow markdown as authoritative over this wrapper.
- Do not collapse orchestration into a single-agent delegation if the local workflow forbids it.
