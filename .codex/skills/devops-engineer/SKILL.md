---
name: devops-engineer
description: Use this skill when the repository contains `.agent/agents/devops-engineer.md` and you want Codex to apply that local DevOps persona. It is for deployment, CI/CD, server changes, rollback, production access, and release operations.
---

# DevOps Engineer

## Overview

Use `.agent/agents/devops-engineer.md` as the source of truth for operational work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/devops-engineer.md` exists.
2. Read the file from the top, including frontmatter, risk rules, and deployment process.
3. Load the needed local skills from its `skills:` list: `clean-code`, `deployment-procedures`, `server-management`, `powershell-windows`, `bash-linux`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Treat production and rollback work as high risk; follow the local agent's escalation and verification rules.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- Use broad verification scripts after deployment-related changes, especially `checklist.py` or `verify_all.py` when appropriate.
