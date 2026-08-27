#!/usr/bin/env python3
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
EXPECTED_MODES = ["A", "B", "C", "D", "E", "F"]
FORBIDDEN_TRACKED_ROOTS = {".previews", "docs", "reports"}
REQUIRED_DIRS = {
    "scripts",
    "tests",
    "references",
    "evals",
    "skill-ir",
    "schemas",
    "security",
    "templates",
}
CORE_SCRIPTS = [
    "init_skill.py",
    "validate_skill.py",
    "yao.py",
    "trigger_eval.py",
    "run_output_eval.py",
    "compile_skill.py",
    "cross_packager.py",
    "verify_package.py",
    "simulate_install.py",
    "trust_check.py",
    "registry_audit.py",
    "upgrade_check.py",
    "render_review_studio.py",
]
CORE_QUALITY_TESTS = [
    "verify_compile_skill.py",
    "verify_output_eval_lab.py",
    "verify_package_verification.py",
    "verify_install_simulation.py",
    "verify_trust_check.py",
]
EXPECTED_COMMITS = {
    "yao": "f5d8f681372edae1915991e2de0c23dc306dd30f",
    "dao": "1cae835995c0ff4d9a33a6fec82cca0a54b7cd05",
}
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(\s*(?:<([^>]+)>|([^\s)]+))")


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "--"], cwd=ROOT, check=True, capture_output=True, text=True
    )
    return [line for line in result.stdout.splitlines() if line]


def markdown_files() -> list[Path]:
    excluded = {".git", ".yao", "dist"}
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if path.is_file() and not excluded.intersection(path.relative_to(ROOT).parts)
    )


def verify_markdown_links(paths: list[Path]) -> int:
    checked = 0
    for source in paths:
        for match in MARKDOWN_LINK.finditer(source.read_text(encoding="utf-8")):
            target = (match.group(1) or match.group(2)).strip()
            parsed = urlsplit(target)
            if not parsed.path or parsed.scheme or parsed.netloc:
                continue
            candidate = (source.parent / unquote(parsed.path)).resolve()
            assert candidate.exists(), (
                f"broken markdown link: {source.relative_to(ROOT)} -> {target}"
            )
            checked += 1
    return checked


def main() -> None:
    manifest = json.loads(read("manifest.json"))
    lock = json.loads(read("upstream.lock.json"))
    cases = json.loads(read("evals/captain_task_modes.json"))
    skill = read("SKILL.md")
    readme = read("README.md")
    files = tracked_files()
    version = read("VERSION").strip()

    assert manifest["name"] == "captain-meta-skill"
    assert manifest["version"] == version == lock["version"]
    assert all(lock[name]["commit"] == commit for name, commit in EXPECTED_COMMITS.items())
    assert [case["mode"] for case in cases["cases"]] == EXPECTED_MODES
    assert all(f"**{mode} " in skill for mode in EXPECTED_MODES)
    root_case = cases["cases"][0]["must"]
    assert all(
        field in root_case
        for field in (
            "surface request",
            "root problem",
            "first principle",
            "success condition",
            "core tension",
            "constraints and assumptions",
            "smallest next step",
        )
    )
    assert "single implementation and verification source" in skill
    assert "No background agent mutates files" in skill
    assert "## 一句话定位" in readme and "## One-line Positioning" in readme
    assert "yaojingang/yao-meta-skill" in readme
    assert "gnipbao/dao-skill" in readme
    assert "must not overwrite Captain" in read("references/downstream-maintenance.md")

    missing_dirs = sorted(path for path in REQUIRED_DIRS if not (ROOT / path).is_dir())
    assert not missing_dirs, f"missing required directories: {', '.join(missing_dirs)}"
    missing_scripts = sorted(
        path for path in CORE_SCRIPTS if not (ROOT / "scripts" / path).is_file()
    )
    assert not missing_scripts, f"missing core scripts: {', '.join(missing_scripts)}"
    missing_tests = sorted(
        path for path in CORE_QUALITY_TESTS if not (ROOT / "tests" / path).is_file()
    )
    assert not missing_tests, f"missing core quality tests: {', '.join(missing_tests)}"

    forbidden = sorted(
        path for path in files if path.split("/", 1)[0] in FORBIDDEN_TRACKED_ROOTS
    )
    assert not forbidden, f"forbidden tracked paths: {', '.join(forbidden)}"
    local_links = verify_markdown_links(markdown_files())
    print(
        "Captain capability restoration summary: "
        f"version={version}; modes={'/'.join(EXPECTED_MODES)}; "
        f"directories={len(REQUIRED_DIRS)}; core_scripts={len(CORE_SCRIPTS)}; "
        f"quality_tests={len(CORE_QUALITY_TESTS)}; markdown_local_links={local_links}; "
        "forbidden_tracked=0"
    )


if __name__ == "__main__":
    main()
