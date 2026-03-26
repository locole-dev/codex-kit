# @locole/locole-skills

Bootstrap the Locole `.agent` toolkit and shared `.codex/skills` into any repository so your whole team can use the same Cursor/Codex workflow from source control.

Instead of installing personal skills separately on every machine, this package copies a team-owned toolkit directly into the project.

## Why this exists

- Keep AI workflows versioned with the codebase
- Share the same agents, workflows, and skills across the team
- Avoid duplicated per-machine setup in `~/.codex/skills`
- Generate project-specific coding rules inside each repo
- Make onboarding new repositories fast and repeatable

## What gets installed

Running `locole-skills init` copies:

- `.agent/`
  - specialist agents
  - reusable skills
  - command-style workflows
  - helper scripts
  - optional generated `PROJECT_RULES.md`
- `.codex/skills/`
  - Codex skill wrappers
  - `locole-kit`
  - workflow and agent wrappers for the toolkit

## Install

Global install:

```bash
npm install -g @locole/locole-skills
```

Install inside a project:

```bash
npm install -D @locole/locole-skills
npx locole-skills init
```

Requirements:

- Node.js `>=18`

## Quick start

From the root of the target repository:

```bash
locole-skills init
```

If `.agent` or `.codex/skills` already exists and you want to replace them:

```bash
locole-skills init --force
```

After that, commit `.agent` and `.codex` so the repository becomes the source of truth for your team.

## First-time repo onboarding

Once the toolkit is installed, use this command in chat:

```text
Use $locole-kit and sync the project rule for this repository.
```

That flow will:

1. Run `python .agent/scripts/project_rules.py sync .`
2. Generate or refresh `.agent/PROJECT_RULES.md`
3. Detect the repo stack, layout, and common commands
4. Produce repo-specific working rules for future implementation tasks
5. Preserve anything you add manually under `## Manual Overrides`

When the repository changes later, run the same command again to update the generated rules.

## How it works

The package is designed around two layers:

### 1. Project-local toolkit

The `.agent` directory contains the working model:

- `agents/` for specialist personas
- `skills/` for domain knowledge and scripts
- `workflows/` for common task flows
- `scripts/` for automation such as validation and project rule generation

### 2. Codex wrappers

The `.codex/skills` directory exposes the toolkit to Codex as discoverable skills, including `locole-kit` as the main entrypoint.

## CLI reference

```text
locole-skills init [--force]
locole-skills --help
locole-skills --version
```

## Included scripts

The root toolkit currently includes helper scripts such as:

- `project_rules.py` to generate repo-specific coding rules
- `checklist.py` for core validation
- `verify_all.py` for broader release-style verification
- `session_manager.py` for repo/session summaries
- `auto_preview.py` for local preview lifecycle tasks

## Verification commands

Run these from the target repository root after `locole-skills init`:

```bash
python .agent/scripts/checklist.py .
python .agent/scripts/verify_all.py .
python .agent/scripts/verify_all.py . --url http://localhost:3000
```

Use `--url` only when you want web checks such as Lighthouse or Playwright.

## Development

Useful local checks while maintaining this package:

```bash
node bin/locole-skills.js --help
node bin/locole-skills.js --version
npm pack --dry-run
```

## Publish

This package ships the following paths via `package.json`:

- `bin/`
- `.agent/`
- `.codex/skills/`
- `LICENSE`

Publish steps:

```bash
npm login
npm publish --access public
```

## Notes

- If Cursor/Codex does not refresh skills after a pull, restart the app.
- If a personal copy still exists in `~/.codex/skills`, you may see duplicate names. Prefer a single source to avoid confusion.
- `GEMINI.md` is kept as a compatibility filename, but it acts as a general workspace policy file for the toolkit.

## License

[MIT](./LICENSE)
