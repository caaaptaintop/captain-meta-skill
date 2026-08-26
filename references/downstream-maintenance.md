# Downstream Maintenance

Captain is an independently released downstream distribution. The official Yao repository is a read-only upstream, not Captain's user update channel.

## Remote Contract

- `origin`: the independent `captain-meta-skill` repository.
- `upstream`: `https://github.com/yaojingang/yao-meta-skill.git`, fetch-only.
- Dao is a pinned mechanism source recorded in `upstream.lock.json`; do not merge its unrelated Git history.

## Maintainer Update

1. Fetch `upstream` and create `sync/yao-X.Y.Z` from Captain `main`.
2. Merge `upstream/main` without rewriting published history.
3. Resolve only conflicts in the small Captain overlay.
4. Run the frozen Captain scenarios plus Yao CI, package verification, install simulation, and upgrade checks.
5. Update `upstream.lock.json` only after the merged commit passes.
6. Merge through review and publish a new Captain version.

Captain users update only from Captain releases. Yao's managed `self-update` supports official Yao installations and must not overwrite Captain.

Rollback means reverting the upstream merge or Captain patch commit and retaining the previous Captain release.
