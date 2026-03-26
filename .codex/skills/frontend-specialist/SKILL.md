---
name: frontend-specialist
description: Use this skill when the repository contains `.agent/agents/frontend-specialist.md` and you want Codex to apply that local frontend persona. It is for UI components, styling, responsive design, state management, and frontend architecture work.
---

# Frontend Specialist

## Overview

Use `.agent/agents/frontend-specialist.md` as the source of truth for frontend work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/frontend-specialist.md` exists.
2. Read the file from the top, including frontmatter, design rules, and anti-patterns.
3. Load only the needed local skills from its `skills:` list: `clean-code`, `nextjs-react-expert`, `web-design-guidelines`, `tailwind-patterns`, `frontend-design`, `lint-and-validate`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Use any matching local workflow, especially `ui-ux-pro-max`, when the task is design-heavy.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- Respect any local design bans or mandatory review loops defined in the agent file.
