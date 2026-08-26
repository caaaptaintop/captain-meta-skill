---
name: captain-meta-skill
description: Design, create, evaluate, or safely evolve reusable agent skills from workflows, prompts, SOPs, scripts, or failure evidence. Use for skill architecture, trigger boundaries, minimal packaging, validation, and upstream-aware maintenance. Do not use for one-off prompts, ordinary documentation, summaries, or translation.
metadata:
  author: Captain
---

# Captain Meta Skill

Build the smallest reusable Skill that solves the recurring problem and leaves evidence that it works.

## Route the task

Choose the highest required mode when a request spans several modes:

`F Evolve > E Reflect > D Evaluate > C Generate > B Design > A Root`

- **A Root** — clarify a vague idea into a root problem, success condition, core tension, and smallest next step. Do not write files.
- **B Design** — define positioning, workflow, boundaries, artifacts, and verification. Stop before implementation when design only is requested.
- **C Generate** — create or refactor the explicitly locked target, then verify it and state the rollback boundary.
- **D Evaluate** — declare the evidence level before scoring; static inspection is not runtime proof.
- **E Reflect** — convert failures or feedback into a redacted evidence packet and decide `create`, `merge`, or `discard`.
- **F Evolve** — apply an approved change, keep source and deployment status separate, retest, and roll back failed changes.

Full mode rules: [Captain task modes](references/captain-task-modes.md).

## Working method

1. Confirm the problem repeats and needs a Skill. For a one-off task, solve it directly without creating files.
2. Lock the target directory, package name, intended users, observable success, exclusions, and write boundary.
3. Inspect the nearest existing Skill or reusable asset before creating new structure.
4. Choose the minimum package:
   - always: `SKILL.md`;
   - when the host needs metadata: `agents/interface.yaml`;
   - only when instructions would otherwise bloat the entrypoint: `references/`;
   - only for deterministic reusable logic: `scripts/`;
   - only for repeatable behavioral checks: `evals/` or `tests/`.
5. Keep frontmatter triggers concrete. State what the Skill handles and what it excludes.
6. Validate structure, referenced paths, representative trigger cases, and the requested output contract.
7. Report files changed, evidence level, verification result, remaining risk, and rollback point.

## Evaluation boundary

Use the lowest honest evidence label:

- **E1 Static** — files, links, metadata, and rules inspected.
- **E2 Simulated** — deterministic fixtures or dry runs passed.
- **E3 Runtime** — executed in the intended host with recorded results.
- **E4 Operational** — repeated real use with reviewed outcomes.

Never promote planned checks, generated reports, or missing telemetry into proof.

## Evolution boundary

For failure-led work:

1. Redact sensitive material and preserve the failing input, expected result, actual result, and environment.
2. Find the nearest approved asset.
3. Choose `create`, `merge`, or `discard`; prefer merging into an existing boundary.
4. Apply one attributable change.
5. Retest the failure and the nearest regression case.
6. Record source status and deployment status independently.

Do not create hidden background updaters, raw trajectory stores, a second Skill registry, or an implicit installer.

## Captain maintenance

Captain is an independent distribution. Users update from Captain releases. Maintainers may review and integrate Yao upstream changes, but upstream content is not copied wholesale into each Captain release. See [downstream maintenance](references/downstream-maintenance.md) and [`upstream.lock.json`](upstream.lock.json).
