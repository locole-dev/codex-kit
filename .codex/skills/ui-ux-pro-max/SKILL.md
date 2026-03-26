---
name: ui-ux-pro-max
description: Use this skill when a repository contains the Locole `ui-ux-pro-max` workflow and shared design dataset under `.agent/workflows/ui-ux-pro-max.md` and `.agent/.shared/ui-ux-pro-max/`. It covers design-system generation, style and palette lookup, typography guidance, stack-specific UI direction, and implementation support for web or mobile design tasks.
---

# UI UX Pro Max

## Overview

Use the local workflow file `.agent/workflows/ui-ux-pro-max.md` together with the shared datasets and scripts in `.agent/.shared/ui-ux-pro-max/`.
Start with the workflow file, then load only the exact script or CSV sources needed for the current design problem.

## Workflow

1. Read `.agent/workflows/ui-ux-pro-max.md` first.
2. Extract product type, style keywords, industry, and stack from the request.
3. Default to `html-tailwind` if the user does not name a stack.
4. Start with the design-system command before narrower lookups.
5. Add focused searches only if the design-system result still leaves gaps.

## Key Commands

```bash
python .agent/.shared/ui-ux-pro-max/scripts/search.py "<query>" --design-system -p "Project Name"
python .agent/.shared/ui-ux-pro-max/scripts/search.py "<query>" --design-system --persist -p "Project Name"
python .agent/.shared/ui-ux-pro-max/scripts/search.py "<query>" --domain <domain>
python .agent/.shared/ui-ux-pro-max/scripts/search.py "<query>" --stack <stack>
```

## Available Domains

`product`, `style`, `typography`, `color`, `landing`, `chart`, `ux`, `react`, `web`, `prompt`

## Available Stacks

`html-tailwind`, `react`, `nextjs`, `vue`, `svelte`, `swiftui`, `react-native`, `flutter`, `shadcn`, `jetpack-compose`

## Notes

- Treat `.agent/workflows/ui-ux-pro-max.md` as the canonical procedure.
- Use `.agent/.shared/ui-ux-pro-max/scripts/search.py` instead of recreating the recommendation logic manually.
- Load CSV files under `.agent/.shared/ui-ux-pro-max/data/` only when you need deeper evidence or alternatives.
- Follow the pre-delivery checklist embedded in the local workflow before shipping UI changes.
