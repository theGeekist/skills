"""Checks for independent skill installation and the optional prose rule."""

import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest
import importlib.util
from collections import Counter
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]


class PackagingTests(unittest.TestCase):
    def test_bundled_references_work_without_repository_siblings(self):
        known = json.loads((ROOT / "standards/upstream-compatibility.json").read_text())
        exceptions = Counter(
            (item["skill"], item["document"], item["target"])
            for item in known["isolated_package_link_exceptions"]
        )
        seen_exceptions = Counter()
        for skill in (ROOT / "skills").iterdir():
            with self.subTest(skill=skill.name), tempfile.TemporaryDirectory() as temporary:
                isolated = Path(temporary) / skill.name
                shutil.copytree(skill, isolated)
                for document in isolated.rglob("*.md"):
                    source = re.sub(r"(?ms)^\x60\x60\x60.*?^\x60\x60\x60\s*", "", document.read_text())
                    targets = re.findall(r"\]\(([^)]+)\)", source)
                    targets.extend(re.findall(r"<(?:img|source)\b[^>]*?\bsrc=\"([^\"]+)\"", source))
                    for target in targets:
                        if re.match(r"[a-z]+:", target) or target.startswith("#"):
                            continue
                        path = (document.parent / target.split("#", 1)[0]).resolve()
                        package_issue = not path.is_relative_to(isolated) or not path.exists()
                        if package_issue:
                            key = (skill.name, document.relative_to(isolated).as_posix(), target)
                            self.assertIn(key, exceptions, f"new isolated-package link issue: {key}")
                            seen_exceptions[key] += 1
        self.assertEqual(seen_exceptions, exceptions, "remove resolved or stale package-link exceptions")

    def test_json_metadata_is_parseable(self):
        for path in [*ROOT.glob(".*-plugin/*.json"), *ROOT.glob(".agents/plugins/*.json")]:
            with self.subTest(path=path):
                self.assertIsInstance(json.loads(path.read_text()), dict)

    def test_chatgpt_plugin_zip_has_one_root_and_every_skill(self):
        module_path = ROOT / "scripts/package-chatgpt-plugin.py"
        spec = importlib.util.spec_from_file_location("package_chatgpt_plugin", module_path)
        package = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(package)
        expected = {
            ".codex-plugin/plugin.json",
            "LICENSE",
            *(p.relative_to(ROOT).as_posix()
              for p in (ROOT / "skills").rglob("*") if p.is_file()),
        }
        skill_names = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
        with tempfile.TemporaryDirectory() as temporary:
            first = Path(temporary) / "first.zip"
            second = Path(temporary) / "second.zip"
            report = package.build_archive(ROOT, first)
            package.build_archive(ROOT, second)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            self.assertEqual(report["skills"], len(skill_names))
            with ZipFile(first) as archive:
                names = set(archive.namelist())
                self.assertEqual(names, expected)
                self.assertIsNone(archive.testzip())
                self.assertEqual(
                    {name.split("/")[1] for name in names if name.endswith("/SKILL.md")},
                    skill_names,
                )
                self.assertFalse(any(name.startswith((".agents/", ".claude-plugin/",
                    "docs/", "tests/", "scripts/")) for name in names))
                self.assertEqual(
                    json.loads(archive.read(".codex-plugin/plugin.json"))["skills"],
                    "./skills/",
                )
                for name in names:
                    self.assertEqual(archive.read(name), (ROOT / name).read_bytes())

    @unittest.skipUnless(os.environ.get("VALE_BINARY"), "set VALE_BINARY to test the optional Vale rule")
    def test_vale_flags_prose_but_preserves_code_and_british_spelling(self):
        with tempfile.TemporaryDirectory() as temporary:
            document = Path(temporary) / "example.md"
            document.write_text("# Example\n\nWe utilise the queue.\n\nThe organisation uses colour.\n\n```text\nutilise\n```\n")
            result = subprocess.run(
                [os.environ["VALE_BINARY"], "--config", str(ROOT / ".vale.ini"),
                 "--output=JSON", str(document)], capture_output=True, text=True, check=False)
            self.assertIn(result.returncode, (0, 1), result.stderr)
            alerts = [alert for group in json.loads(result.stdout).values() for alert in group]
            self.assertEqual([(a["Check"], a["Match"], a["Line"]) for a in alerts],
                             [("Geekist.PlainWords", "utilise", 3)])


if __name__ == "__main__":
    unittest.main()
