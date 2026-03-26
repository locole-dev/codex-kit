---
name: preview-workflow
description: Use this skill when a repository contains `.agent/workflows/preview.md` and you want Codex to apply that local preview workflow. It is for preview server start, stop, restart, health checks, and local dev preview management.
---

# Preview Workflow

## Overview

Use `.agent/workflows/preview.md` as the source of truth for preview management in this repository.
Read that file first, then follow its command modes and preview-server handling steps.

## Workflow

1. Confirm `.agent/workflows/preview.md` exists.
2. Read the workflow file from the top.
3. Determine whether the request is status, start, stop, restart, or health check.
4. Use the local preview management script or equivalent command path described by the workflow.
5. Report the preview URL, health, and any port-conflict resolution.

## Notes

- Treat the local workflow markdown as authoritative over this wrapper.
- Favor the repo's local preview mechanism instead of inventing a new one.
