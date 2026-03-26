---
name: game-developer
description: Use this skill when the repository contains `.agent/agents/game-developer.md` and you want Codex to apply that local game-development persona. It is for gameplay systems, engine-specific work, multiplayer, optimization, 2D or 3D implementation, art, and audio guidance.
---

# Game Developer

## Overview

Use `.agent/agents/game-developer.md` as the source of truth for game-development work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/game-developer.md` exists.
2. Read the file from the top, including frontmatter and engine or platform guidance.
3. Load only the needed local skills from its `skills:` list such as `game-development`, `game-development/pc-games`, `game-development/web-games`, `game-development/mobile-games`, `game-development/game-design`, `game-development/multiplayer`, `game-development/vr-ar`, `game-development/2d-games`, `game-development/3d-games`, `game-development/game-art`, and `game-development/game-audio`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Keep loading narrow: only open the sub-skill files that match the engine, platform, or problem type.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- Escalate to `orchestrator` if the game task also needs backend, DevOps, or security coordination.
