---
name: test-workflow
description: Use this skill when a repository contains `.agent/workflows/test.md` and you want Codex to apply that local testing workflow. It is for generating tests, running test suites, coverage checks, and test-targeted verification.
---

# Test Workflow

## Overview

Use `.agent/workflows/test.md` as the source of truth for test generation and execution in this repository.
Read that file first, then follow its distinction between generating tests, running suites, and reporting coverage.

## Workflow

1. Confirm `.agent/workflows/test.md` exists.
2. Read the workflow file from the top.
3. Determine whether the request is to run all tests, generate tests for a target, run watch mode, or show coverage.
4. Follow the local project's testing patterns and framework conventions.
5. Report the test plan, generated files, or execution results in the format the workflow expects.

## Notes

- Treat the local workflow markdown as authoritative over this wrapper.
- Prefer the project's existing test stack and patterns over generic defaults.
