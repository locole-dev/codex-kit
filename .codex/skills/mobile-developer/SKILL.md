---
name: mobile-developer
description: Use this skill when the repository contains `.agent/agents/mobile-developer.md` and you want Codex to apply that local mobile-development persona. It is for React Native, Flutter, iOS, Android, Expo, and mobile UX implementation work.
---

# Mobile Developer

## Overview

Use `.agent/agents/mobile-developer.md` as the source of truth for mobile work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/mobile-developer.md` exists.
2. Read the file from the top, including frontmatter and platform-specific guidance.
3. Load the needed local skills from its `skills:` list: `clean-code`, `mobile-design`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Keep the solution aligned with the specific platform or framework named by the user.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- Use the mobile specialist instead of the frontend specialist for native or hybrid mobile tasks.
