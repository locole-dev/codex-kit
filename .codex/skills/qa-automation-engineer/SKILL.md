---
name: qa-automation-engineer
description: Use this skill when the repository contains `.agent/agents/qa-automation-engineer.md` and you want Codex to apply that local QA automation persona. It is for Playwright, Cypress, CI test pipelines, regression strategy, and E2E automation work.
---

# QA Automation Engineer

## Overview

Use `.agent/agents/qa-automation-engineer.md` as the source of truth for automation-focused QA work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/qa-automation-engineer.md` exists.
2. Read the file from the top, including frontmatter and pipeline guidance.
3. Load the needed local skills from its `skills:` list: `webapp-testing`, `testing-patterns`, `web-design-guidelines`, `clean-code`, `lint-and-validate`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Use focused validation scripts for E2E or UI regressions before broad all-project checks.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- Coordinate with `test-engineer` when the task includes test design in addition to automation infrastructure.
