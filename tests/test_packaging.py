"""Checks for independent skill installation and the optional prose rule."""

import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PackagingTests(unittest.TestCase):
    def test_bundled_references_work_without_repository_siblings(self):
        for skill in (ROOT / "skills").iterdir():
            with self.subTest(skill=skill.name), tempfile.TemporaryDirectory() as temporary:
                isolated = Path(temporary) / skill.name
                shutil.copytree(skill, isolated)
                for document in isolated.rglob("*.md"):
                    for target in re.findall(r"\]\(([^)]+)\)", document.read_text()):
                        if re.match(r"[a-z]+:", target) or target.startswith("#"):
                            continue
                        path = (document.parent / target.split("#", 1)[0]).resolve()
                        self.assertTrue(path.is_relative_to(isolated), target)
                        self.assertTrue(path.exists(), target)

    def test_json_metadata_is_parseable(self):
        for path in [*ROOT.glob(".*-plugin/*.json"), *ROOT.glob(".agents/plugins/*.json")]:
            with self.subTest(path=path):
                self.assertIsInstance(json.loads(path.read_text()), dict)

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
