---
name: penetration-tester
description: Use this skill when the repository contains `.agent/agents/penetration-tester.md` and you want Codex to apply that local offensive-security persona. It is for attack simulation, exploit analysis, adversarial testing, and finding exploitable weaknesses.
---

# Penetration Tester

## Overview

Use `.agent/agents/penetration-tester.md` as the source of truth for offensive-security work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/penetration-tester.md` exists.
2. Read the file from the top, including frontmatter and attack-simulation rules.
3. Load the needed local skills from its `skills:` list: `clean-code`, `vulnerability-scanner`, `red-team-tactics`, `api-patterns`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Keep the work scoped to authorized testing inside the current repository and environment.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- If the local workflow indicates defensive review or approval requirements, obey them before running risky checks.
