---
name: performance-optimizer
description: Use this skill when the repository contains `.agent/agents/performance-optimizer.md` and you want Codex to apply that local performance persona. It is for profiling, speed improvements, bundle reduction, Core Web Vitals work, and runtime optimization.
---

# Performance Optimizer

## Overview

Use `.agent/agents/performance-optimizer.md` as the source of truth for performance work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/performance-optimizer.md` exists.
2. Read the file from the top, including frontmatter and profiling rules.
3. Load the needed local skills from its `skills:` list: `clean-code`, `performance-profiling`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Measure before and after changes whenever the local agent or skill requests it.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- Pull in broader frontend, backend, or mobile specialists if the performance issue crosses their boundaries.
