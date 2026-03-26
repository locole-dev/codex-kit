---
name: brainstorm-workflow
description: Use this skill when a repository contains `.agent/workflows/brainstorm.md` and you want Codex to apply that local brainstorming workflow. It is for structured option exploration, comparing approaches, and recommending a direction before implementation.
---

# Brainstorm Workflow

## Overview

Use `.agent/workflows/brainstorm.md` as the source of truth for structured idea exploration in this repository.
Read that file first, then follow its option-generation and comparison format.

## Workflow

1. Confirm `.agent/workflows/brainstorm.md` exists.
2. Read the workflow file from the top.
3. Clarify the problem, user, and constraints before proposing solutions.
4. Produce at least three distinct options with pros, cons, and effort levels.
5. End with a recommendation and the tradeoff logic behind it.

## Notes

- Treat the local workflow markdown as authoritative over this wrapper.
- Keep the output exploratory; do not jump into implementation unless the user explicitly switches modes.
