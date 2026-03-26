---
name: debug-workflow
description: Use this skill when a repository contains `.agent/workflows/debug.md` and you want Codex to apply that local debugging workflow. It is for systematic investigation of bugs, errors, regressions, and unexpected behavior.
---

# Debug Workflow

## Overview

Use `.agent/workflows/debug.md` as the source of truth for systematic debugging in this repository.
Read that file first, then follow its information gathering, hypothesis testing, root-cause, and fix structure.

## Workflow

1. Confirm `.agent/workflows/debug.md` exists.
2. Read the workflow file from the top.
3. Gather the symptom, error, reproduction steps, and recent changes.
4. Form and test hypotheses in order of likelihood.
5. Explain the root cause, apply the fix, and include prevention steps.

## Notes

- Treat the local workflow markdown as authoritative over this wrapper.
- Prefer evidence-driven investigation over guessing.
