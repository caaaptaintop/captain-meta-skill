# Captain Meta Skill — Repository Instructions

## Scope

This repository is the independent source of `captain-meta-skill`. Keep the current tree focused on Captain; upstream Yao history remains available through Git and the fetch-only `upstream` remote.

## Editing rules

- Prefer deletion and reuse over new framework code.
- Keep `SKILL.md` concise; add a reference only when the entrypoint would become hard to scan.
- Do not restore inherited Yao reports, previews, CLIs, schemas, registries, or generated evidence unless a Captain requirement and a runnable check justify them.
- Keep Yao and Dao source pins and license attribution intact.
- Do not rewrite published Git history or push to `upstream`.

## Verification

Run:

```bash
make test
```

The check must remain standard-library only and verify identity, source pins, links, task-mode coverage, and the intentionally small package boundary.
