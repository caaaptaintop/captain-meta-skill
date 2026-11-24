#!/usr/bin/env python3
"""Exercise real file boundaries and the public Yao maintenance-check entry."""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from skill_maintenance import check_maintenance
from cross_packager import make_zip


class MaintenanceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.before = self.base / "before"
        self.before.mkdir()
        (self.before / "SKILL.md").write_text("---\nname: demo-skill\ndescription: Demo.\n---\nDemo\n")
        self.after = self.base / "after"
        shutil.copytree(self.before, self.after)

    def check(self, kind, allow=(), **kwargs):
        return check_maintenance(self.before, self.after, kind, list(allow), **kwargs)

    def local(self):
        (self.after / "local-data").mkdir()
        (self.after / "local-data/ADAPTATION.md").write_text("Config location only.\n")

    def test_read_only_does_not_create_local_data(self):
        self.assertTrue(self.check("local")["ok"])
        self.assertFalse((self.after / "local-data").exists())

    def test_first_local_config_requires_note(self):
        self.local()
        (self.after / "local-data/config.json").write_text('{"path":"example"}')
        allow = ["local-data/ADAPTATION.md", "local-data/config.json"]
        self.assertTrue(self.check("local", allow)["ok"])
        (self.after / "local-data/ADAPTATION.md").unlink()
        self.assertFalse(self.check("local", allow)["ok"])

    def test_local_source_edit_is_rejected_even_if_allowlisted(self):
        self.local()
        (self.after / "SKILL.md").write_text("Unexpected source customization")
        self.assertFalse(self.check("local", ["SKILL.md", "local-data/ADAPTATION.md"])["ok"])

    def test_custom_source_requires_provenance_and_exact_boundary(self):
        (self.after / "SKILL.md").write_text("Authorized feature")
        self.assertFalse(self.check("custom", ["SKILL.md"])["ok"])
        provenance = dict(source_ref="https://example.org/author.git", base_revision="known-base")
        self.assertTrue(self.check("custom", ["SKILL.md"], **provenance)["ok"])
        (self.after / "unrelated.txt").write_text("Extra write")
        self.assertFalse(self.check("custom", ["SKILL.md"], **provenance)["ok"])

    def test_update_preserves_private_data_and_adapters(self):
        for dirname in ("local-data", "adapters"):
            (self.before / dirname).mkdir()
            (self.before / dirname / "keep.txt").write_text("private-sentinel-not-in-report")
            shutil.copytree(self.before / dirname, self.after / dirname)
        (self.after / "SKILL.md").write_text("New author version")
        provenance = dict(source_ref="https://example.org/author.git", base_revision="known-base")
        self.assertTrue(self.check("update", ["SKILL.md"], **provenance)["ok"])
        for dirname in ("local-data", "adapters"):
            path = self.after / dirname / "keep.txt"
            path.write_text("Accidental overwrite")
            report = self.check("update", ["SKILL.md", f"{dirname}/keep.txt"], **provenance)
            self.assertFalse(report["ok"])
            self.assertNotIn("private-sentinel-not-in-report", json.dumps(report))
            path.write_text("private-sentinel-not-in-report")

    def test_modes_and_link_targets_are_compared_without_following(self):
        (self.after / "SKILL.md").chmod(0o755)
        self.assertFalse(self.check("local")["ok"])
        (self.after / "SKILL.md").chmod((self.before / "SKILL.md").stat().st_mode & 0o7777)
        external = self.base / "external"
        external.mkdir()
        (external / "must-not-read").write_text("private sentinel")
        (self.before / "link").symlink_to(external)
        (self.after / "link").symlink_to(external)
        self.assertTrue(self.check("local")["ok"])
        with self.assertRaises(ValueError):
            self.check("local", ["link/must-not-read"])
        (self.after / "link").unlink()
        (self.after / "link").symlink_to(self.base / "missing")
        self.assertFalse(self.check("local")["ok"])

    def test_unsafe_allowlist_and_nested_copies_are_rejected(self):
        for path in ("../outside", "/outside", ".", "scripts/*", "local-data/../SKILL.md", ".git/config"):
            with self.assertRaises(ValueError):
                self.check("local", [path])
        with self.assertRaises(ValueError):
            check_maintenance(self.before, self.before, "local", [])
        nested = self.after / "nested"
        nested.mkdir()
        with self.assertRaises(ValueError):
            check_maintenance(self.after, nested, "local", [])

    def test_public_cli_reports_failure_and_refuses_source_report_write(self):
        cmd = [sys.executable, str(ROOT / "scripts/yao.py"), "maintenance-check",
               str(self.after), "--before", str(self.before), "--kind", "local"]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertTrue(json.loads(proc.stdout)["ok"])
        original = (self.after / "SKILL.md").read_bytes()
        proc = subprocess.run([*cmd, "--output-json", str(self.after / "SKILL.md")], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 2, proc.stderr)
        self.assertEqual((self.after / "SKILL.md").read_bytes(), original)
        (self.after / "SKILL.md").write_text("Unrelated change")
        proc = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(proc.returncode, 2, proc.stderr)

    def test_private_data_excluded_from_real_archive_with_and_without_git(self):
        self.local()
        sentinel = self.after / "local-data/private.txt"
        sentinel.write_text("private-sentinel-must-not-ship")
        output = self.base / "package"
        output.mkdir()
        for git_backed in (False, True):
            if git_backed:
                subprocess.run(["git", "init", "--quiet"], cwd=self.after, check=True)
                # Even an accidentally tracked private file must not ship.
                subprocess.run(["git", "add", "."], cwd=self.after, check=True)
            archive_path = make_zip(self.after, output, "demo-skill")
            with zipfile.ZipFile(archive_path) as archive:
                self.assertIn("demo-skill/SKILL.md", archive.namelist())
                self.assertFalse(any("local-data" in Path(name).parts for name in archive.namelist()))
                self.assertFalse(any(b"private-sentinel-must-not-ship" in archive.read(name) for name in archive.namelist()))


if __name__ == "__main__":
    unittest.main()
