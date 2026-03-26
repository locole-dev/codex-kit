---
name: status-workflow
description: Use this skill when a repository contains `.agent/workflows/status.md` and you want Codex to apply that local status workflow. It is for project state snapshots, agent status boards, progress summaries, and preview or file statistics reporting.
---

# Status Workflow

## Overview

Use `.agent/workflows/status.md` as the source of truth for project status reporting in this repository.
Read that file first, then follow its structure for project info, active work, file counts, and preview state.

## Workflow

1. Confirm `.agent/workflows/status.md` exists.
2. Read the workflow file from the top.
3. Gather current project info, feature status, and active agent progress.
4. Include preview state and file statistics if the workflow calls for them.
5. Present the status in a concise board-style report.

## Notes

- Treat the local workflow markdown as authoritative over this wrapper.
- Keep status reporting factual and current rather than speculative.
