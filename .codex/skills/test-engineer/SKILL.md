---
name: test-engineer
description: Use this skill when the repository contains `.agent/agents/test-engineer.md` and you want Codex to apply that local testing persona. It is for test design, TDD, coverage improvement, debugging test failures, and verification strategy.
---

# Test Engineer

## Overview

Use `.agent/agents/test-engineer.md` as the source of truth for testing work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/test-engineer.md` exists.
2. Read the file from the top, including frontmatter and testing rules.
3. Load the needed local skills from its `skills:` list: `clean-code`, `testing-patterns`, `tdd-workflow`, `webapp-testing`, `code-review-checklist`, `lint-and-validate`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Prefer the narrowest relevant test or validation script for the code path you changed.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- Coordinate with `qa-automation-engineer` when the task is primarily about automation infrastructure or CI rather than test design.
