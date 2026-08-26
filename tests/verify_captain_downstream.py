#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    lock = json.loads((ROOT / "upstream.lock.json").read_text(encoding="utf-8"))
    cases = json.loads((ROOT / "evals" / "captain_task_modes.json").read_text(encoding="utf-8"))
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

    assert manifest["name"] == "captain-meta-skill"
    assert manifest["version"] == (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    assert lock["yao"]["commit"] == "f5d8f681372edae1915991e2de0c23dc306dd30f"
    assert lock["dao"]["commit"] == "1cae835995c0ff4d9a33a6fec82cca0a54b7cd05"
    assert [case["mode"] for case in cases["cases"]] == ["A", "B", "C", "D", "F"]
    assert "F>E>D>C>B>A" in skill
    maintenance = (ROOT / "references" / "downstream-maintenance.md").read_text(encoding="utf-8")
    assert "must not overwrite Captain" in maintenance
    print("captain downstream checks passed")


if __name__ == "__main__":
    main()
