# Downstream Maintenance

Captain is an independent distribution. Users update from Captain releases; Yao is a fetch-only source for maintainer review.

## Remote contract

- `origin`: `caaaptaintop/captain-meta-skill`, Captain's release source.
- `upstream`: `yaojingang/yao-meta-skill`, fetch-only.
- Dao: a pinned mechanism reference; do not merge its unrelated Git history.

## Review an upstream Yao update

1. Fetch `upstream` and inspect changes since `upstream.lock.json`.
2. Create `sync/yao-X.Y.Z` from Captain `main`.
3. Select only changes that improve Captain's current contract. Do not restore the full Yao working tree by default.
4. Resolve Captain-owned files intentionally and run `make test`.
5. Update the Yao version and commit pin only after validation passes.
6. Merge through review, bump Captain's own version, and publish a Captain release.

Prefer cherry-picking or manually integrating a focused upstream change. Use a full upstream merge only when Captain deliberately adopts the corresponding subsystem. Published history must not be rewritten.

Rollback by reverting the integration commit and retaining the previous Captain release.
