---
name: enhance-workflow
description: Use this skill when a repository contains `.agent/workflows/enhance.md` and you want Codex to apply that local enhancement workflow. It is for iterative feature work, updates to an existing app, and planned modifications to current functionality.
---

# Enhance Workflow

## Overview

Use `.agent/workflows/enhance.md` as the source of truth for iterative product changes in this repository.
Read that file first, then follow its sequence for state discovery, change planning, approval for major edits, implementation, and preview refresh.

## Workflow

1. Confirm `.agent/workflows/enhance.md` exists.
2. Read the workflow file from the top.
3. Inspect the current project state before proposing changes.
4. Identify affected files and dependencies, and present a plan for major edits.
5. Apply changes, test them, and refresh preview if needed.

## Notes

- Treat the local workflow markdown as authoritative over this wrapper.
- Ask for approval on larger or conflicting changes, as the local workflow requires.
