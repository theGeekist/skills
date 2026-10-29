"""Verify the shared core and independently loadable specialist references.

These structural checks do not claim to test native client skill activation.
"""

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
START = "<!-- shared-baseline:start -->"
END = "<!-- shared-baseline:end -->"


class SkillLoadingTests(unittest.TestCase):
    def profiles(self):
        return json.loads((ROOT / "standards/skill-profiles.json").read_text())["skills"]

    def test_installed_skills_are_declared_in_loading_profiles(self):
        installed = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
        self.assertEqual(set(self.profiles()), installed)

    def test_frontmatter_fences_are_standalone_lines(self):
        for name in self.profiles():
            with self.subTest(skill=name):
                lines = (ROOT / "skills" / name / "SKILL.md").read_text().splitlines()
                self.assertEqual(lines[0], "---")
                closing = lines[1:].index("---") + 1
                self.assertGreater(closing, 2)
                self.assertTrue(any(line.startswith("name:") for line in lines[1:closing]))
                self.assertTrue(any(line.startswith("description:") for line in lines[1:closing]))
                self.assertFalse(any(line.endswith("---") and line != "---"
                                     for line in lines[1:closing]))

    def test_one_canonical_baseline_is_inline_in_every_skill(self):
        expected = (ROOT / "standards/baseline.md").read_text().strip()
        for name in self.profiles():
            with self.subTest(skill=name):
                text = (ROOT / "skills" / name / "SKILL.md").read_text()
                self.assertEqual(text.count(START), 1)
                self.assertEqual(text.count(END), 1)
                actual = text.split(START, 1)[1].split(END, 1)[0].strip()
                self.assertEqual(actual, expected)

    def test_declared_reference_is_local_direct_and_matches_its_source(self):
        for name, profile in self.profiles().items():
            body = (ROOT / "skills" / name / "SKILL.md").read_text()
            for reference in profile["references"]:
                with self.subTest(skill=name, reference=reference):
                    self.assertIn(f"references/{reference}", body)
                    copied = ROOT / "skills" / name / "references" / reference
                    canonical = ROOT / "standards" / reference
                    self.assertEqual(copied.read_bytes(), canonical.read_bytes())

    def test_each_skill_exposes_a_local_source_route(self):
        # Attribution must survive an independent install; this does not prove
        # semantic equivalence or that an external source endorses a local rule.
        for name in self.profiles():
            with self.subTest(skill=name):
                folder = ROOT / "skills" / name
                body = (folder / "SKILL.md").read_text()
                source_section = re.search(r"(?ms)^## Sources[^\n]*\n(.*?)(?=^## |\Z)", body)
                self.assertIsNotNone(source_section, name)
                targets = re.findall(r"\]\((references/[^)]+)\)", source_section.group(1))
                self.assertTrue(targets, name)
                for target in targets:
                    path, _, anchor = target.partition("#")
                    reference = folder / path
                    self.assertTrue(reference.is_file(), target)
                    text = reference.read_text()
                    if anchor:
                        headings = re.findall(r"(?m)^#+ (.+)$", text)
                        slugs = {re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-") for h in headings}
                        self.assertIn(anchor, slugs)
                    self.assertRegex(text, r"\]\(https://")

    def test_specialists_bundle_their_own_artefact_guidance(self):
        expected = {
            "write-implementation-tasks": "tasks.md",
            "record-architecture-decisions": "decisions.md",
            "write-technical-documentation": "technical-documentation.md",
            "write-marketing-content": "marketing.md",
            "write-interface-content": "interface-content.md",
            "review-project-language": "review.md",
        }
        all_specialist_references = set(expected.values())
        profiles = self.profiles()
        for name, reference in expected.items():
            with self.subTest(skill=name):
                self.assertEqual(set(profiles[name]["references"]) & all_specialist_references,
                                 {reference})
                skill = ROOT / "skills" / name
                bundled = {path.name for path in (skill / "references").glob("*.md")}
                self.assertEqual(bundled & all_specialist_references, {reference})

    def test_compatibility_router_is_explicit_only_in_codex_metadata(self):
        metadata = (ROOT / "skills/write-project-content/agents/openai.yaml").read_text()
        self.assertRegex(metadata, r"(?m)^policy:\s*$")
        self.assertRegex(metadata, r"(?m)^\s+allow_implicit_invocation:\s*false\s*$")
        description = (ROOT / "skills/write-project-content/SKILL.md").read_text().split("---", 2)[1]
        self.assertRegex(description.lower(), r"explicit")

    def test_catalogue_cases_include_positive_mixed_and_no_skill_requests(self):
        cases = json.loads((ROOT / "evaluations/skill-selection/cases.json").read_text())["cases"]
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        self.assertTrue(any(not case["primary"] for case in cases))
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertTrue(case["prompt"].strip())
                # Ordinary requests must not tell responders which skill to choose.
                for name in self.profiles():
                    self.assertNotIn(name, case["prompt"])
                self.assertFalse(set(case["primary"]) & set(case["reject"]))


if __name__ == "__main__":
    unittest.main()
