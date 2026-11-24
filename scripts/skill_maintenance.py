"""Read-only file-boundary verification for Yao skill maintenance."""

import argparse
import json
import os
import stat
from pathlib import Path, PurePosixPath

from adaptation_patch_safety import sha256_file


SCRIPT_INTERFACE = "internal-module"
SCRIPT_INTERFACE_REASON = "Imported by yao.py for maintenance-check; compares an explicit backup with the locked target."
IGNORED_DIRS = {".git", "__pycache__"}
PROTECTED_ROOTS = {"local-data", "adapters"}


def allowed_path(value: str) -> str:
    path = PurePosixPath(value)
    if (not value or value != str(path) or path.is_absolute()
            or ".." in path.parts or path == PurePosixPath(".")
            or set(path.parts) & IGNORED_DIRS or "\\" in value
            or any(c in value for c in "*?[]")):
        raise ValueError(f"Expected an exact relative file path: {value}")
    return value


def file_tree(root: Path) -> dict[str, dict]:
    """Hash files without following symlinked directories or files."""
    nodes = {}
    for parent, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in IGNORED_DIRS)
        for path in [Path(parent), *(Path(parent) / n for n in sorted(files)),
                     *(Path(parent) / n for n in dirs if (Path(parent) / n).is_symlink())]:
            rel = path.relative_to(root).as_posix()
            info = path.lstat()
            node = {"mode": stat.S_IMODE(info.st_mode)}
            if stat.S_ISLNK(info.st_mode):
                node.update(kind="link", target=os.readlink(path))
            elif stat.S_ISREG(info.st_mode):
                node.update(kind="file", sha256=sha256_file(path))
            elif stat.S_ISDIR(info.st_mode):
                node.update(kind="dir")
            else:
                raise ValueError(f"Unsupported special file in explicit tree: {rel}")
            nodes[rel] = node
    return nodes


def check_maintenance(before: Path, after: Path, kind: str, allow: list[str],
                      source_ref: str = "", base_revision: str = "") -> dict:
    if not before.is_dir() or not after.is_dir() or before.resolve() == after.resolve():
        raise ValueError("Provide distinct existing before-copy and target directories.")
    if before.resolve() in after.resolve().parents or after.resolve() in before.resolve().parents:
        raise ValueError("The before-copy and target must not contain each other.")
    allowed = {allowed_path(p) for p in allow}
    for rel in allowed:
        for root in (before, after):
            for parent in PurePosixPath(rel).parents:
                if parent != PurePosixPath(".") and (root / str(parent)).is_symlink():
                    raise ValueError(f"Allowed path traverses a symlink: {rel}")
    old, new = file_tree(before), file_tree(after)
    changed = sorted(p for p in old.keys() | new.keys() if old.get(p) != new.get(p))
    failures = []
    if kind != "local" and (not source_ref.strip() or not base_revision.strip()):
        failures.append("custom/update requires a truthful source_ref and base_revision (or an explicitly unknown base plus snapshot).")
    for rel in changed:
        node = old.get(rel) or new.get(rel)
        structural_parent = (node["kind"] == "dir" and (rel not in old or rel not in new)
                             and any(PurePosixPath(rel) in PurePosixPath(a).parents for a in allowed))
        if rel not in allowed and not structural_parent:
            failures.append(f"Change outside the exact allowlist: {rel}")
        parts = PurePosixPath(rel).parts
        first = parts[0] if parts else "."
        if kind == "local" and first != "local-data":
            failures.append(f"Local configuration changed source: {rel}")
        if kind == "update" and first in PROTECTED_ROOTS:
            failures.append(f"Upstream update changed protected content: {rel}")
    if kind == "local" and changed:
        adaptation = after / "local-data" / "ADAPTATION.md"
        if not adaptation.is_file() or not adaptation.resolve().is_relative_to(after.resolve()):
            failures.append("Local configuration changes require an in-target local-data/ADAPTATION.md.")
    return {
        "ok": not failures, "change_kind": kind, "changed_files": changed,
        "source_ref": source_ref, "base_revision": base_revision,
        "failures": failures,
        "scope": "File hashes, types, POSIX modes and link targets only; no external-link data, ACL, xattr, authorization or business validation.",
        "filesystem_interception": False, "creates_local_data": False,
    }


def command_maintenance_check(args: argparse.Namespace) -> int:
    try:
        report = check_maintenance(Path(args.before).expanduser().resolve(),
                                   Path(args.skill_dir).resolve(), args.kind, args.allow,
                                   args.source_ref, args.base_revision)
    except (OSError, ValueError) as exc:
        report = {"ok": False, "failures": [str(exc)]}
    if args.output_json:
        output = Path(args.output_json)
        # Evidence belongs outside both compared trees and must never replace a source file.
        roots = (Path(args.before).expanduser().resolve(), Path(args.skill_dir).resolve())
        if output.resolve() in roots or any(r in output.resolve().parents for r in roots):
            report = {"ok": False, "failures": ["Write check evidence outside both compared trees."]}
        else:
            try:
                output.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
                with output.open("x", encoding="utf-8") as handle:
                    json.dump(report, handle, ensure_ascii=False, indent=2)
                    handle.write("\n")
                output.chmod(0o600)
            except OSError as exc:
                report = {"ok": False, "failures": [f"Cannot create new evidence file: {exc}"]}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 2
