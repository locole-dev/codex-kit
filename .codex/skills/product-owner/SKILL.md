---
name: product-owner
description: Use this skill when the repository contains `.agent/agents/product-owner.md` and you want Codex to apply that local product-owner persona. It is for roadmap, backlog, MVP, prioritization, and stakeholder-driven scoping work.
---

# Product Owner

## Overview

Use `.agent/agents/product-owner.md` as the source of truth for prioritization and scope work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/product-owner.md` exists.
2. Read the file from the top, including frontmatter and prioritization guidance.
3. Load the needed local skills from its `skills:` list: `plan-writing`, `brainstorming`, `clean-code`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Use this specialist to turn broad goals into a sequenced backlog or MVP cut.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- Hand off to product-manager or project-planner if the work shifts from prioritization into formal specification or execution planning.
