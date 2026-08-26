#!/usr/bin/env python3
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
EXPECTED_MODES = ["A", "B", "C", "D", "E", "F"]
FORBIDDEN_DIRS = {
    ".previews",
    "assets",
    "docs",
    "evidence",
    "examples",
    "failures",
    "registry",
    "reports",
    "runtime",
    "schemas",
    "scripts",
    "security",
    "skill-ir",
    "skill_atlas",
    "templates",
}


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, check=True, capture_output=True, text=True
    )
    return [line for line in result.stdout.splitlines() if line]


def verify_markdown_links(paths: list[str]) -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\((?!https?://|#)([^)]+)\)")
    for relative in paths:
        source = ROOT / relative
        for target in link_pattern.findall(source.read_text(encoding="utf-8")):
            clean = target.split("#", 1)[0]
            if clean:
                assert (source.parent / clean).resolve().exists(), f"broken link: {relative} -> {target}"


def main() -> None:
    manifest = json.loads(read("manifest.json"))
    lock = json.loads(read("upstream.lock.json"))
    cases = json.loads(read("evals/captain_task_modes.json"))
    skill = read("SKILL.md")
    readme = read("README.md")
    files = tracked_files()

    assert manifest["name"] == "captain-meta-skill"
    assert manifest["version"] == read("VERSION").strip() == lock["version"]
    assert skill.startswith("---\nname: captain-meta-skill\ndescription:")
    assert "Do not use for one-off prompts" in skill
    assert lock["yao"]["commit"] == "f5d8f681372edae1915991e2de0c23dc306dd30f"
    assert lock["dao"]["commit"] == "1cae835995c0ff4d9a33a6fec82cca0a54b7cd05"
    assert [case["mode"] for case in cases["cases"]] == EXPECTED_MODES
    assert all(f"**{mode} " in skill for mode in EXPECTED_MODES)
    assert "## 中文" in readme and "## English" in readme
    assert "yaojingang/yao-meta-skill" in readme and "gnipbao/dao-skill" in readme
    assert "Captain Meta Skill contributors" in read("LICENSE")
    assert not FORBIDDEN_DIRS.intersection(path.split("/", 1)[0] for path in files)
    assert len(files) <= 20, f"package grew beyond the minimal boundary: {len(files)} files"
    verify_markdown_links(["README.md", "SKILL.md", "THIRD_PARTY_NOTICES.md"])
    print(f"captain checks passed: {len(files)} tracked files")


if __name__ == "__main__":
    main()
