"""Checks for contextual terminology validation, linting and reference packaging."""

import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_language", ROOT / "scripts/check-language.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


def registry():
    return {
        "version": 1,
        "contexts": [
            {"id": "assessment", "name": "Assessment", "definition": "Assessing evidence."},
            {"id": "delivery", "name": "Delivery", "definition": "Delivering software."},
        ],
        "concepts": [{
            "id": "assessment.confidence",
            "context": "assessment",
            "preferred_term": "Confidence",
            "definition": "Strength of evidence supporting an assessment.",
            "status": "accepted",
            "aliases": ["certainty", "evidence strength"],
            "distinct_from": [],
            "labels": {"dashboard": "Evidence strength"},
            "sources": [{"path": "docs/decisions/scoring.md", "revision": "abc123"}],
        }],
    }


class RegistryTests(unittest.TestCase):
    def test_valid_registry(self):
        value = registry()
        self.assertIs(CHECK.validate_registry(value), value)

    def test_cross_context_homonyms_are_allowed(self):
        value = registry()
        other = copy.deepcopy(value["concepts"][0])
        other.update(id="delivery.confidence", context="delivery")
        value["concepts"].append(other)
        CHECK.validate_registry(value)

    def test_unknown_concept_relation(self):
        value = registry()
        value["concepts"][0]["distinct_from"] = ["assessment.coverage"]
        with self.assertRaisesRegex(CHECK.RegistryError, "unknown concept"):
            CHECK.validate_registry(value)

    def test_duplicate_alias_case_insensitive(self):
        value = registry()
        value["concepts"][0]["aliases"].append("Certainty")
        with self.assertRaisesRegex(CHECK.RegistryError, "collides"):
            CHECK.validate_registry(value)

    def test_alias_collision_with_another_preferred_term(self):
        value = registry()
        other = copy.deepcopy(value["concepts"][0])
        other.update(id="assessment.certainty", preferred_term="Certainty", aliases=[])
        value["concepts"].append(other)
        with self.assertRaisesRegex(CHECK.RegistryError, "collides"):
            CHECK.validate_registry(value)

    def test_duplicate_concept_id(self):
        value = registry()
        value["concepts"].append(copy.deepcopy(value["concepts"][0]))
        with self.assertRaisesRegex(CHECK.RegistryError, "duplicate concept"):
            CHECK.validate_registry(value)

    def test_unknown_context(self):
        value = registry()
        value["concepts"][0]["context"] = "missing"
        with self.assertRaisesRegex(CHECK.RegistryError, "unknown context"):
            CHECK.validate_registry(value)

    def test_accepted_requires_provenance(self):
        value = registry()
        value["concepts"][0]["sources"] = []
        with self.assertRaisesRegex(CHECK.RegistryError, "at least one source"):
            CHECK.validate_registry(value)

    def test_proposed_can_lack_sources(self):
        value = registry()
        value["concepts"][0].update(status="proposed", sources=[])
        CHECK.validate_registry(value)

    def test_deprecated_replacement_must_exist(self):
        value = registry()
        value["concepts"][0].update(status="deprecated", replaced_by="missing")
        with self.assertRaisesRegex(CHECK.RegistryError, "unknown concept"):
            CHECK.validate_registry(value)

    def test_self_relation_rejected(self):
        value = registry()
        value["concepts"][0]["distinct_from"] = ["assessment.confidence"]
        with self.assertRaisesRegex(CHECK.RegistryError, "itself"):
            CHECK.validate_registry(value)

    def test_invalid_types_raise_registry_error(self):
        for malformed in ([], None, {"version": True, "contexts": {}, "concepts": "bad"}):
            with self.subTest(value=malformed), self.assertRaises(CHECK.RegistryError):
                CHECK.validate_registry(malformed)
        fields = {
            "id": [], "context": {}, "preferred_term": 12, "status": [],
            "definition": None, "aliases": {}, "distinct_from": [None],
            "labels": [], "sources": ["bad"], "replaced_by": {},
        }
        for key, malformed in fields.items():
            value = registry()
            value["concepts"][0][key] = malformed
            with self.subTest(field=key), self.assertRaises(CHECK.RegistryError):
                CHECK.validate_registry(value)


class LintTests(unittest.TestCase):
    def test_contextual_alias_warning(self):
        findings = CHECK.lint_text("We use certainty.\nConfidence is separate.", registry(), "assessment")
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["line"], 1)
        self.assertEqual(findings[0]["preferred"], "Confidence")
        self.assertEqual(findings[0]["rule"], "nonpreferred-alias")
        self.assertEqual(findings[0]["severity"], "warning")

    def test_other_context_is_not_linted(self):
        self.assertEqual(CHECK.lint_text("certainty", registry(), "delivery"), [])

    def test_word_boundaries(self):
        self.assertEqual(CHECK.lint_text("uncertainty", registry(), "assessment"), [])

    def test_preferred_term_is_clean(self):
        self.assertEqual(CHECK.lint_text("Confidence", registry(), "assessment"), [])

    def test_audience_mapping_and_label_protection(self):
        findings = CHECK.lint_text("Evidence strength: certainty", registry(), "assessment", "dashboard")
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["preferred"], "Evidence strength")
        self.assertEqual(findings[0]["term"], "certainty")

    def test_label_outside_its_audience_remains_an_alias(self):
        findings = CHECK.lint_text("Evidence strength", registry(), "assessment")
        self.assertEqual(findings[0]["preferred"], "Confidence")

    def test_unknown_audience_falls_back_to_preferred_term(self):
        findings = CHECK.lint_text("certainty", registry(), "assessment", "report")
        self.assertEqual(findings[0]["preferred"], "Confidence")

    def test_code_fences_inline_code_urls_and_relative_links_ignored(self):
        text = """# Confidence
```text
certainty
```
~~~
certainty
~~~
`certainty` and ``code with ` certainty``.
https://example.com/certainty [reference](certainty.md)
    certainty
certainty
"""
        findings = CHECK.lint_text(text, registry(), "assessment")
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["line"], 11)

    def test_unclosed_fence_is_code_to_end(self):
        self.assertEqual(CHECK.lint_text("```\ncertainty", registry(), "assessment"), [])

    def test_fence_only_closes_on_matching_marker(self):
        text = "```\n~~~\ncertainty\n```\ncertainty"
        findings = CHECK.lint_text(text, registry(), "assessment")
        self.assertEqual([item["line"] for item in findings], [5])

    def test_proposed_terms_do_not_establish_lint_policy(self):
        value = registry()
        value["concepts"][0]["status"] = "proposed"
        self.assertEqual(CHECK.lint_text("certainty", value, "assessment"), [])

    def test_invalid_context_is_configuration_error(self):
        with self.assertRaisesRegex(CHECK.RegistryError, "unknown context"):
            CHECK.lint_text("certainty", registry(), "missing")


class CommandTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.path = self.root / "terms.json"
        self.path.write_text(json.dumps(registry()), encoding="utf-8")

    def tearDown(self):
        self.temporary.cleanup()

    def run_checker(self, *args):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/check-language.py"), *args],
                                capture_output=True, text=True)
        self.assertNotIn("Traceback", result.stderr)
        return result, json.loads(result.stdout)

    def test_clean_registry_exit_zero(self):
        result, output = self.run_checker("registry", str(self.path))
        self.assertEqual(result.returncode, 0)
        self.assertTrue(output["valid"])

    def test_findings_exit_one(self):
        text = self.root / "draft.md"
        text.write_text("certainty", encoding="utf-8")
        result, output = self.run_checker("lint", "--registry", str(self.path), "--context", "assessment", str(text))
        self.assertEqual(result.returncode, 1)
        self.assertEqual(len(output["findings"]), 1)

    def test_malformed_json_exit_two(self):
        self.path.write_text("{broken", encoding="utf-8")
        result, output = self.run_checker("registry", str(self.path))
        self.assertEqual(result.returncode, 2)
        self.assertFalse(output["valid"])

    def test_missing_file_exit_two(self):
        result, output = self.run_checker("registry", str(self.root / "missing.json"))
        self.assertEqual(result.returncode, 2)
        self.assertIn("error", output)

    def test_invalid_json_types_exit_two(self):
        self.path.write_text(json.dumps({"version": [], "contexts": [12], "concepts": [None]}), encoding="utf-8")
        result, output = self.run_checker("registry", str(self.path))
        self.assertEqual(result.returncode, 2)
        self.assertIn("must be", output["error"])

    def test_reference_sync_detects_drift_and_reproduces_sources(self):
        (self.root / "scripts").mkdir()
        script = self.root / "scripts/sync-language-references.py"
        shutil.copyfile(ROOT / "scripts/sync-language-references.py", script)
        (self.root / "standards").mkdir()
        for name in ("writing.md", "content-patterns.md", "uncertainty.md"):
            (self.root / "standards" / name).write_text(f"# {name}\nCanonical content.\n", encoding="utf-8")
        def sync(*args):
            return subprocess.run([sys.executable, str(script), *args], capture_output=True, text=True)
        result = sync("--check")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(len(json.loads(result.stdout)["changed"]), 8)
        self.assertFalse((self.root / "skills").exists())
        self.assertEqual(sync().returncode, 0)
        self.assertEqual(sync("--check").returncode, 0)
        for skill in ("establish-project-language", "write-project-content"):
            for name in ("writing.md", "content-patterns.md"):
                self.assertEqual((self.root / "standards" / name).read_bytes(),
                                 (self.root / "skills" / skill / "references" / name).read_bytes())
        (self.root / "skills/write-project-content/references/writing.md").write_text("drift", encoding="utf-8")
        self.assertEqual(sync("--check").returncode, 1)


if __name__ == "__main__":
    unittest.main()
