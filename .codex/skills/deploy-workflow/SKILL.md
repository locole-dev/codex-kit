---
name: deploy-workflow
description: Use this skill when a repository contains `.agent/workflows/deploy.md` and you want Codex to apply that local deployment workflow. It is for pre-deploy checks, preview deployments, production deployments, and rollback handling.
---

# Deploy Workflow

## Overview

Use `.agent/workflows/deploy.md` as the source of truth for deployment operations in this repository.
Read that file first, then follow its pre-flight checklist, build flow, deploy mode, and verification steps.

## Workflow

1. Confirm `.agent/workflows/deploy.md` exists.
2. Read the workflow file from the top.
3. Determine whether the request is `check`, `preview`, `production`, or `rollback`.
4. Complete the pre-deployment checklist before deployment actions.
5. Verify the deployment result and report any rollback conditions immediately.

## Notes

- Treat the local workflow markdown as authoritative over this wrapper.
- Use the most conservative path for production changes.
