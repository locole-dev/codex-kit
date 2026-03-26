---
name: documentation-writer
description: Use this skill when the repository contains `.agent/agents/documentation-writer.md` and you want Codex to apply that local documentation persona. It is for explicit requests to write README files, API docs, changelogs, and similar documentation artifacts.
---

# Documentation Writer

## Overview

Use `.agent/agents/documentation-writer.md` as the source of truth for documentation work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/documentation-writer.md` exists.
2. Read the file from the top, including frontmatter and scope limits.
3. Load the needed local skills from its `skills:` list: `clean-code`, `documentation-templates`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Use this skill only for explicit documentation requests unless the local agent says otherwise.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- Keep this skill narrow; do not auto-route ordinary coding tasks here.
