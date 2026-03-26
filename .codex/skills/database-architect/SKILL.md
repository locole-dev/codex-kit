---
name: database-architect
description: Use this skill when the repository contains `.agent/agents/database-architect.md` and you want Codex to apply that local database persona. It is for schema design, migrations, indexing, query tuning, and data-modeling work.
---

# Database Architect

## Overview

Use `.agent/agents/database-architect.md` as the source of truth for database work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/database-architect.md` exists.
2. Read the file from the top, including frontmatter and schema rules.
3. Load the needed local skills from its `skills:` list: `clean-code`, `database-design`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Use related validation scripts after schema or migration changes.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- For cross-cutting API, security, or orchestration work, switch to the matching local agent instead of overloading this one.
