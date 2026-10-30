"""Presentation generation must not change skill authority or activation scope."""
import importlib.util
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location('sync_skill_catalogue', ROOT / 'scripts/sync-skill-catalogue.py')
SYNC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SYNC)


class SkillCatalogueTests(unittest.TestCase):
    def test_generated_pages_and_metadata_have_no_drift(self):
        catalogue = SYNC.load_catalogue(ROOT)
        for path, expected in SYNC.render(ROOT, catalogue).items():
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertEqual(path.read_text(), expected)

    def test_overview_install_release_matches_both_plugin_versions(self):
        catalogue = SYNC.load_catalogue(ROOT)
        for manifest in ('.codex-plugin/plugin.json', '.claude-plugin/plugin.json'):
            version = json.loads((ROOT / manifest).read_text())['version']
            self.assertEqual(catalogue['release'], 'v' + version)

    def test_overview_routes_and_install_target_cover_each_skill(self):
        catalogue = SYNC.load_catalogue(ROOT)
        for name, skill in catalogue['skills'].items():
            with self.subTest(skill=name):
                page = (ROOT / 'docs/skills' / (name + '.md')).read_text()
                self.assertIn(f"/tree/{catalogue['release']} --skill {name}", page)
                self.assertIn(skill['example']['source_facts'], page)
                self.assertIn(skill['example']['before'], page)
                self.assertIn(skill['example']['after'], page)
                self.assertIn('illustrative example', page)
                self.assertIn('ChatGPT plugin registration', page)
                for target in re.findall(r'\]\(([^)]+)\)', page):
                    if re.match(r'[a-z]+:', target):
                        continue
                    path = ROOT / 'docs/skills' / target.split('#', 1)[0]
                    self.assertTrue(path.exists(), target)

    def test_implicit_policy_icons_and_plugin_identity_are_preserved(self):
        catalogue = SYNC.load_catalogue(ROOT)
        planned = SYNC.render(ROOT, catalogue)
        for name in catalogue['skills']:
            metadata = planned[ROOT / 'skills' / name / 'agents/openai.yaml']
            self.assertIn('./assets/geekist-small.svg', metadata)
            self.assertIn('./assets/geekist.svg', metadata)
            if name == 'write-project-content':
                self.assertIn('allow_implicit_invocation: false', metadata)
            else:
                self.assertNotIn('allow_implicit_invocation', metadata)
        for manifest in ('.codex-plugin/plugin.json', '.claude-plugin/plugin.json'):
            before = json.loads((ROOT / manifest).read_text())
            after = json.loads(planned[ROOT / manifest])
            for field in ('name', 'version', 'author', 'license'):
                self.assertEqual(after[field], before[field])
            self.assertEqual(after['name'], 'geekist-architecture-skills')

    def test_marketplace_copy_matches_the_canonical_presentation(self):
        catalogue = SYNC.load_catalogue(ROOT)
        generated = SYNC.render(ROOT, catalogue)
        marketplace = json.loads(generated[ROOT / '.claude-plugin/marketplace.json'])
        self.assertEqual(marketplace['description'], catalogue['plugin']['description'])
        entry = next(p for p in marketplace['plugins'] if p['name'] == 'geekist-architecture-skills')
        self.assertEqual(entry['description'], catalogue['plugin']['description'])
        self.assertEqual(entry['source'], '.')

    def test_changed_activation_intent_requires_review(self):
        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            shutil.copytree(ROOT / 'standards', temporary / 'standards')
            shutil.copytree(ROOT / 'skills', temporary / 'skills')
            path = temporary / 'skills/write-marketing-content/SKILL.md'
            path.write_text(path.read_text().replace('description:', 'description: Changed activation scope. ', 1))
            with self.assertRaisesRegex(ValueError, 'activation description differs'):
                SYNC.load_catalogue(temporary)

    def test_catalogue_rejects_icons_outside_the_independent_skill(self):
        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            shutil.copytree(ROOT / 'standards', temporary / 'standards')
            shutil.copytree(ROOT / 'skills', temporary / 'skills')
            outside = temporary / 'outside.svg'
            outside.write_text('<svg/>')
            path = temporary / 'standards/skill-catalogue.json'
            catalogue = json.loads(path.read_text())
            for target in ('../../outside.svg', str(outside)):
                with self.subTest(target=target):
                    catalogue['skills']['review-project-language']['interface']['icon_small'] = target
                    path.write_text(json.dumps(catalogue))
                    with self.assertRaisesRegex(ValueError, 'must stay inside the skill directory'):
                        SYNC.load_catalogue(temporary)

    def test_source_catalogue_rejects_hidden_policy_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            shutil.copytree(ROOT / 'standards', temporary / 'standards')
            shutil.copytree(ROOT / 'skills', temporary / 'skills')
            path = temporary / 'standards/skill-catalogue.json'
            catalogue = json.loads(path.read_text())
            catalogue['skills']['write-project-content']['allow_implicit_invocation'] = True
            path.write_text(json.dumps(catalogue))
            with self.assertRaisesRegex(ValueError, 'unexpected implicit invocation policy'):
                SYNC.load_catalogue(temporary)


if __name__ == '__main__':
    unittest.main()
