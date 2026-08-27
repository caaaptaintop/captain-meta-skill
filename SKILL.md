---
name: captain-meta-skill
description: Create, evaluate, migrate, package, release, or safely evolve reusable agent skills from workflows, prompts, SOPs, scripts, or failure evidence. Use to improve an existing skill, add trigger evals/tests, run CLI-assisted generation, Skill IR, trust checks, install simulation, and release gates. Exclude one-off prompts, ordinary documentation, summaries, translation, and copy-only edits.
metadata:
  author: Captain
---

# Captain Meta Skill

Build the smallest reusable Skill for a recurring problem and prove it with proportionate gates. Captain routes; Yao executes and verifies; Dao contributes mechanisms only.

## Router Rules

`F Evolve > E Reflect > D Evaluate > C Generate > B Design > A Root`

- **A Root** — return request, root problem, first principle, success, tension, constraints/assumptions, and smallest next step; do not write.
- **B Design** — define positioning, workflow, boundaries, artifacts, and verification; do not implement.
- **C Generate** — change only the locked target, verify, and report rollback.
- **D Evaluate** — use Yao evidence, trust, and quality gates; E1 is not runtime proof.
- **E Reflect** — build a redacted evidence packet, find the nearest asset, choose `create`, `merge`, or `discard`; do not write.
- **F Evolve** — the authorized active agent changes the locked target through Yao, retests, records deployment separately, and rolls back failures. No background agent mutates files.

Full contracts: [Captain task modes](references/captain-task-modes.md).

## Modes

Choose task and rigor independently: `Scaffold`, `Production`, `Library`, or `Governed`. Dao routing adds no second evaluator, scorer, installer, or engine; Yao remains the single implementation and verification source. See [modes](references/operating-modes.md) and [gates](references/gate-selection.md).

## Compact Workflow

1. Require repeated use; lock identity, target, output contract, exclusions, maturity, writes, and rollback.
2. Inspect the nearest asset; ask only when a missing answer changes the contract.
3. Build the minimum package and validate structure, routing, resources, and governance.
4. For Production+, run Skill IR, compilation, trigger/output eval, trust, conformance, package verification, and install simulation.
5. Publish only when authorized; label evidence honestly and record deployment separately.

## Output Contract

Use `scripts/yao.py` with an explicit target; `--self` is only for Captain. Return changed files, gates, evidence level (`E1` static, `E2` simulated, `E3` runtime, `E4` operational), result, risk, and rollback. Never inflate evidence or commit generated/private output.

## Reference map

[Task modes](references/captain-task-modes.md) · [method](references/skill-engineering-method.md) · [evaluation](references/eval-playbook.md) · [packaging](references/packaging-contracts.md) · [trust](references/trust-security-method.md) · [maintenance](references/downstream-maintenance.md) · [`upstream.lock.json`](upstream.lock.json)
