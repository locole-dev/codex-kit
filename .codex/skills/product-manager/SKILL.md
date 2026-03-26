---
name: product-manager
description: Use this skill when the repository contains `.agent/agents/product-manager.md` and you want Codex to apply that local product-management persona. It is for feature definition, acceptance criteria, requirements clarification, and product-spec work.
---

# Product Manager

## Overview

Use `.agent/agents/product-manager.md` as the source of truth for product-definition work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/product-manager.md` exists.
2. Read the file from the top, including frontmatter and discovery guidance.
3. Load the needed local skills from its `skills:` list: `plan-writing`, `brainstorming`, `clean-code`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Use this specialist to clarify scope before implementation begins.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- Hand off to implementation agents after the requirements are concrete enough.
