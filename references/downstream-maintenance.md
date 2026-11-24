# Downstream Maintenance

Captain is an independent downstream distribution. Users update from Captain releases; Yao is a fetch-only engineering upstream.

## Remote contract

- `origin`: `caaaptaintop/captain-meta-skill`, Captain's release source.
- `upstream`: `yaojingang/yao-meta-skill`, fetch-only.
- Dao: a pinned mechanism reference; do not merge its unrelated Git history or copy its code without explicit review and attribution.

## Source boundary

Captain retains the Yao Engine source required for creation, evaluation, compilation, packaging, trust, installation, and release checks. Captain owns the public identity, A-F task modes, README, source lock, and downstream policy.

Routine generated outputs are not source and should remain untracked:

- `.previews/`, `dist/`, `reports/`;
- localized or historical Yao homepage copies under `docs/`;
- test scratch directories, caches, local telemetry, and provider raw output.

## Review a Yao update

1. Fetch `upstream` and inspect changes since the Yao pin in `upstream.lock.json`.
2. Create `sync/yao-X.Y.Z` from Captain `main`.
3. Merge or cherry-pick Yao Engine changes while preserving Captain-owned files.
4. Keep generated reports, previews, and duplicated upstream public docs out of the tracked tree.
5. Run focused checks, then `make ci-test`.
6. Update the Yao version and commit pin only after the complete validation passes.
7. Merge through review, bump Captain's own version, and publish a Captain release.

Yao's official self-update channel must not overwrite Captain. Captain users update only from Captain releases.

For a locally customized Captain or any other installed skill, apply the [skill maintenance policy](skill-maintenance-policy.md) before updating. Retain its author base and custom diff; a managed update is not a three-way merge of customized source. Do not discard local adaptations or replace them with release defaults.

Rollback by reverting the integration commit and retaining the previous Captain release.
