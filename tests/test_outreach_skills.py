"""Guard portability and editorial boundaries of the two outreach skills.

These checks validate instructions and packaging, not native client activation.
"""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class OutreachSkillTests(unittest.TestCase):
    def skill(self, name):
        return (ROOT / "skills" / name / "SKILL.md").read_text()

    def test_independent_skill_packaging(self):
        catalogue = json.loads((ROOT / "standards/skill-catalogue.json").read_text())
        profiles = json.loads((ROOT / "standards/skill-profiles.json").read_text())
        for name, reference in (
            ("research-outreach-opportunities", "outreach-research.md"),
            ("write-outreach", "outreach-writing.md"),
        ):
            with self.subTest(name=name):
                body = self.skill(name)
                self.assertIn(name, catalogue["skills"])
                self.assertEqual(profiles["skills"][name]["references"], [reference])
                self.assertTrue((ROOT / "skills" / name / "references" / reference).is_file())
                self.assertIn("<!-- shared-baseline:start -->", body)
                self.assertIn(f"references/{reference}", body)
                self.assertNotIn("drive.google.com/file/d/", body)
                self.assertNotIn("allow_implicit_invocation: false",
                                 (ROOT / "skills" / name / "agents/openai.yaml").read_text())

    def test_research_uses_crm_for_relationships_not_current_product_truth(self):
        body = self.skill("research-outreach-opportunities")
        self.assertIn("established identities, relationships, correspondence", body)
        self.assertIn("current first-party and relevant independent sources", body)
        self.assertIn("cannot require the investigation to discover a sales opportunity", body)
        self.assertIn("references/hyperbeam-case.md", body)

    def test_writing_learns_only_with_authorised_persistence(self):
        body = self.skill("write-outreach")
        self.assertIn("authorised persistent voice reference", body)
        self.assertIn("original context", body)
        self.assertIn("without silently persisting it", body)
        self.assertIn("cannot require that assessment to produce a message worth sending", body)
        self.assertIn("Do not repeat completed research", body)

    def test_hyperbeam_reference_is_an_investigation_example(self):
        case = (ROOT / "skills/research-outreach-opportunities/references/hyperbeam-case.md").read_text()
        for marker in ("Initial hypothesis:", "Contradictory discovery:",
                       "Further discovery:", "Revised opportunity:"):
            self.assertIn(marker, case)


if __name__ == "__main__":
    unittest.main()
