# Locole Skills

> Guide to creating and using skills in the Locole toolkit.

## Why Skills Exist

Models are generalists. Skills keep project-specific knowledge, scripts, and checklists out of the default context until they are actually needed.

This keeps the toolkit:

- easier to maintain
- cheaper to load
- less noisy for the runtime
- more precise for domain work

## Progressive Disclosure

Each skill should load in layers:

1. Metadata in `SKILL.md`
2. The `SKILL.md` body when the skill is triggered
3. Only the specific `references/`, `scripts/`, or `assets/` files needed for the task

Do not bulk-load an entire skill folder.

## Skill Structure

```text
skill-name/
|-- SKILL.md
|-- scripts/
|-- references/
`-- assets/
```

## What Goes Where

### `SKILL.md`

- Name and description
- Core workflow
- Clear instructions on when to open companion files

### `scripts/`

- Deterministic helpers
- Repeatable audits
- Small utilities worth executing instead of rewriting

### `references/`

- Detailed guides
- Templates
- Domain notes
- Long-form material that should not live in `SKILL.md`

### `assets/`

- Files used in output, not usually loaded into context
- Templates, images, example payloads, fonts, or boilerplates

## Authoring Guidelines

- Keep `SKILL.md` concise.
- Write only what the runtime would not safely infer on its own.
- Prefer linking to a focused reference file instead of copying long explanations into `SKILL.md`.
- Avoid redundant documentation files that are not part of the skill itself.

## Practical Rule

If a skill supports multiple variants, keep the selection logic in `SKILL.md` and move variant details into separate reference files.

Examples:

- provider-specific cloud deployment notes
- framework-specific implementation patterns
- different policy packs for different environments

## Maintenance Notes

- Keep naming consistent with folder names.
- Update `agents/openai.yaml` if the skill name or purpose changes.
- Remove stale product or platform assumptions when you fork a skill from another toolkit.
