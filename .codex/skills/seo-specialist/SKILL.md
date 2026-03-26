---
name: seo-specialist
description: Use this skill when the repository contains `.agent/agents/seo-specialist.md` and you want Codex to apply that local SEO and GEO persona. It is for search visibility, content optimization, AI citation strategy, Core Web Vitals, and E-E-A-T improvements.
---

# SEO Specialist

## Overview

Use `.agent/agents/seo-specialist.md` as the source of truth for SEO and GEO work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/seo-specialist.md` exists.
2. Read the file from the top, including frontmatter and search-visibility guidance.
3. Load the needed local skills from its `skills:` list: `clean-code`, `seo-fundamentals`, `geo-fundamentals`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Use targeted SEO or performance checks after changes affecting pages, content, or metadata.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- Pull in frontend or performance specialists when the SEO issue depends on implementation details outside content strategy.
