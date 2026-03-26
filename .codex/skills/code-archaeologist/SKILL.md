---
name: code-archaeologist
description: Use this skill when the repository contains `.agent/agents/code-archaeologist.md` and you want Codex to apply that local legacy-code and reverse-engineering persona. It is for refactoring plans, reading messy systems, explaining undocumented code, and modernization guidance.
---

# Code Archaeologist

## Overview

Use `.agent/agents/code-archaeologist.md` as the source of truth for legacy-code analysis in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/code-archaeologist.md` exists.
2. Read the file from the top, including frontmatter and refactoring rules.
3. Load the needed local skills from its `skills:` list: `clean-code`, `refactoring-patterns`, `code-review-checklist`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Use this specialist for discovery and modernization; switch to `orchestrator` if implementation spans multiple domains.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- If `refactoring-patterns` is absent locally, fall back to the remaining local guidance and state that the dependency is missing.
