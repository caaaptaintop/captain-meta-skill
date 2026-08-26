---
name: captain-meta-skill
description: Create, improve, or evaluate an existing skill from workflows, prompts, SOPs, scripts. Use for migration/release/package, routing, evals/tests, install/trust checks, 优化已有 skill, 补 trigger 评测. Exclude summary/translation/docs, brainstorming, one-off prompts, copy-only edits, outline-only requests.
metadata:
  author: Captain
---

# Captain Meta Skill

## Router Rules

- Route by frontmatter `description` using the lightest mode.
- Keep `SKILL.md` lean: guidance in `references/`, logic in `scripts/`, evidence in `reports/`.

## Modes

- `Scaffold`: exploratory; `Production`: team; `Library`: shared; `Governed`: release-critical.
- Rules: [Method](references/skill-engineering-method.md), [Modes](references/operating-modes.md), [Boundaries](references/resource-boundaries.md).

## Task Modes

- Task modes: `A Root`, `B Design`, `C Generate`, `D Evaluate`, `E Reflect`, `F Evolve`; priority `F>E>D>C>B>A`; separate from maturity. [Rules](references/captain-task-modes.md).

## Compact Workflow

1. Require a reusable output contract; skip one-offs.
2. Lock problem, success, tension, modes, target path, and identity before writes.
3. Scan `3-5` references and assets; test `description`.
4. Evolution: `evidence -> nearest asset -> create/merge/discard -> deployment -> retest/rollback`.

Playbooks: [Target Safety](references/target-safety.md), [Intent](references/intent-dialogue.md), [Skill IR](references/skill-ir-method.md), [Output Eval](references/output-eval-method.md), [Review Studio](references/review-studio-method.md).

## Skill OS 2.0 Gates

For production/library/governed releases, run Skill IR, compiler, trigger/output eval, Atlas, conformance, trust, package/install, upgrade, drift, waiver, Review Studio.

## Governed Package Boundary

Governed/file-backed packages: label `input_files` a `file-backed fixture`; include `owner`, `review cadence`, `output contract`, `rollback boundary`; require `trust report` and `reports/output_quality_scorecard.md`; mark unavailable telemetry/approvals/metrics/benchmarks as `missing evidence`; never fabricate evidence.

Preserve labels literally when they apply: `file-backed fixture`, `input_files`, `output contract`, `rollback boundary`, `trust report`, `reports/output_quality_scorecard.md`, `missing evidence`.

## First-Turn Style

- Infer non-core gaps; ask one core-fork question per round, max two, then use recorded preferred inference.
- In Chinese, sound soft and companion-like; use [Intent Dialogue](references/intent-dialogue.md).

## Output Contract

Builds: `SKILL.md`, aligned interface, justified assets, boundary/gate summary. Audits: findings + fixes; edit only when asked. No-skill: no files.

## Reference Map

Primary: [Method](references/skill-engineering-method.md), [Artifact Design](references/artifact-design-doctrine.md), [Systems](references/systems-thinking-doctrine.md), [Governance](references/governance.md), [SkillOps](references/skillops-decision-policy.md).

Downstream: [Maintenance](references/downstream-maintenance.md).
