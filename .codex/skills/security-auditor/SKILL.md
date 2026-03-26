---
name: security-auditor
description: Use this skill when the repository contains `.agent/agents/security-auditor.md` and you want Codex to apply that local defensive-security persona. It is for vulnerability review, OWASP-style checks, zero-trust thinking, auth hardening, and supply-chain or application security work.
---

# Security Auditor

## Overview

Use `.agent/agents/security-auditor.md` as the source of truth for defensive-security work in this repository.
Read that file first, then load only the relevant local skills it references.

## Workflow

1. Confirm `.agent/agents/security-auditor.md` exists.
2. Read the file from the top, including frontmatter and security review rules.
3. Load the needed local skills from its `skills:` list: `clean-code`, `vulnerability-scanner`, `red-team-tactics`, `api-patterns`.
4. Apply workspace-wide rules from `.agent/rules/GEMINI.md` if present.
5. Prefer the narrowest matching security or validation script before broad all-project checks.

## Notes

- Treat the local agent markdown as authoritative over this wrapper.
- Hand off to `penetration-tester` only when the task truly needs offensive testing rather than defensive review.
