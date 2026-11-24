# Captain Task Modes

Task mode describes what the user needs now. Maturity tier describes how much engineering and governance the resulting Skill needs. Determine both independently.

## Modes

- `A Root`: turn a fuzzy idea into a surface request, provisional root problem, first principle, success condition, core tension, material constraints and assumptions, and one smallest next step. Do not write files unless asked.
- `B Design`: define positioning, workflow, boundaries, artifacts, and verification. Stop before implementation when the user asks for design only.
- `C Generate`: create or refactor the explicitly locked target, verify it, and report the rollback boundary.
- `D Evaluate`: use the Yao evidence, trust, and quality gates; state the evidence level and evaluation boundary before scoring. Static review and dry runs are E1 evidence, never runtime proof.
- `E Reflect`: build the normalized evidence packet used by the Yao adaptation workflow, identify the nearest existing asset, and recommend `create`, `merge`, or `discard`; do not mutate files.
- `F Evolve`: the active agent applies only an explicitly authorized change to the locked target through the Yao engine, keeps deployment status separate from source status, retests, and rolls back on failed verification. No background agent mutates files.

For compound requests choose the highest required mode: `F > E > D > C > B > A`. A higher mode may include lower-mode work. A lower mode's no-write boundary applies during that analysis substage; once the user has authorized C/F implementation, use that stage's locked target and write boundaries. User requests for design-only, review-only, or no modifications remain binding until explicitly changed. Evidence standards remain in force throughout.

## Single-Engine Rule

Dao-inspired modes classify the task and add root-diagnosis and nearest-asset decisions. They do not create a separate evaluator, adaptation engine, scoring system, or installer. Captain defines the shared task and evidence contracts; Yao remains the only execution and verification engine.

## Root Diagnosis

Before structure, record:

- the surface request;
- the real recurring problem;
- the first principle that must remain true;
- the observable success condition;
- the core tension or tradeoff;
- environmental constraints, available assets, and affected people;
- assumptions that would materially change the design.
- one smallest useful next step.

Ask only about unresolved assumptions that change the result.

## Evolution Decision

Before C/F writes, follow [skill maintenance policy](skill-maintenance-policy.md). Local configuration is created on demand and kept outside reusable source; authorized functional customization may change source with provenance and a reproducible diff; upstream updates preserve local data and merge customizations before replacement. Existing task authorization is not a reason to request it again. Each skill's adaptation note records concrete local facts only.

Use this sequence:

1. Build a redacted evidence packet.
2. Search the nearest approved local asset before creating anything.
3. Decide `create`, `merge`, or `discard` and state why.
4. Keep source, installed package, generated child Skill, and runtime state in separate locations.
5. Record source status and deployment status independently.
6. Retest the failing case and the nearest regression case.
7. Roll back failed verified changes.

Do not add a hidden background evolution engine, raw trajectory store, second registry, or implicit installer. Add machinery only when a current Captain requirement and a runnable check justify it.
