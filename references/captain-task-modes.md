# Captain Task Modes

Task mode describes what the user needs now. Maturity tier describes how much engineering and governance the resulting Skill needs. Determine both independently.

## Modes

- `A Root`: turn a fuzzy idea into a provisional root problem, success condition, core tension, and one smallest next step. Do not write files unless asked.
- `B Design`: define positioning, workflow, boundaries, artifacts, and verification. Stop before implementation when the user asks for design only.
- `C Generate`: create or refactor the explicitly locked target, verify it, and report the rollback boundary.
- `D Evaluate`: state the evidence level and evaluation boundary before scoring. Static review and dry runs are E1 evidence, never runtime proof.
- `E Reflect`: build an evidence packet from failures or feedback, identify the nearest existing asset, and recommend `create`, `merge`, or `discard`.
- `F Evolve`: apply only an approved change, keep deployment status separate from source status, retest, and roll back on failed verification.

For compound requests choose the highest required mode: `F > E > D > C > B > A`. A higher mode may include lower-mode work, but it must preserve every lower mode's write and evidence boundary.

## Root Diagnosis

Before structure, record:

- the real recurring problem;
- the observable success condition;
- the core tension or tradeoff;
- environmental constraints, available assets, and affected people;
- assumptions that would materially change the design.

Ask only about unresolved assumptions that change the result.

## Evolution Decision

Use this sequence:

1. Build a redacted evidence packet.
2. Search the nearest approved local asset before creating anything.
3. Decide `create`, `merge`, or `discard` and state why.
4. Keep source, installed package, generated child Skill, and runtime state in separate locations.
5. Record source status and deployment status independently.
6. Retest the failing case and the nearest regression case.
7. Roll back failed verified changes.

Do not add a hidden background evolution engine, raw trajectory store, second registry, or implicit installer. Add machinery only when a current Captain requirement and a runnable check justify it.
