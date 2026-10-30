"""Validate inspectable examples and reproducible editorial-reference generation.

These checks establish schema and packaging properties, not semantic truth or
AI authorship. Source-based editorial judgement remains necessary.
"""
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
SPEC = importlib.util.spec_from_file_location('sync_editorial_patterns', ROOT / 'scripts/sync-editorial-patterns.py')
SYNC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SYNC)


class EditorialPatternTests(unittest.TestCase):
    def source(self):
        return json.loads((ROOT / 'standards/editorial-patterns.json').read_text())

    def test_generated_reference_matches_its_validated_source(self):
        source = SYNC.validate(self.source())
        self.assertEqual((ROOT / 'standards/editorial-patterns.md').read_text(), SYNC.render(source))
        for pattern in source['patterns']:
            with self.subTest(pattern=pattern['id']):
                self.assertIn(f'<a id="{pattern["id"].lower()}"></a>', SYNC.render(source))
                for field in ('source_facts', 'before', 'after', 'exception'):
                    self.assertIn(pattern[field], SYNC.render(source))

    def test_duplicate_identifiers_are_rejected(self):
        source = self.source()
        source['patterns'].append(copy.deepcopy(source['patterns'][0]))
        with self.assertRaisesRegex(ValueError, 'duplicate pattern identifier'):
            SYNC.validate(source)

    def test_each_example_requires_source_facts_and_a_contextual_exception(self):
        for field in ('source_facts', 'exception'):
            with self.subTest(field=field):
                source = self.source()
                del source['patterns'][0][field]
                with self.assertRaisesRegex(ValueError, field):
                    SYNC.validate(source)

    def test_unattributed_and_unknown_sources_are_rejected(self):
        for value in ([], ['not-a-source'], ['local', 'local']):
            with self.subTest(value=value):
                source = self.source()
                source['patterns'][0]['sources'] = value
                with self.assertRaisesRegex(ValueError, 'sources'):
                    SYNC.validate(source)

    def test_source_links_and_priority_values_are_constrained(self):
        source = self.source()
        source['sources']['local']['url'] = 'file:///private/source'
        with self.assertRaisesRegex(ValueError, 'HTTPS'):
            SYNC.validate(source)
        source = self.source()
        source['patterns'][0]['severity'] = 'AI-written'
        with self.assertRaisesRegex(ValueError, 'severity'):
            SYNC.validate(source)

    def test_examples_must_show_a_revision(self):
        source = self.source()
        source['patterns'][0]['after'] = source['patterns'][0]['before']
        with self.assertRaisesRegex(ValueError, 'must show a revision'):
            SYNC.validate(source)

    def test_check_mode_detects_drift_without_overwriting_it(self):
        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            (temporary / 'scripts').mkdir()
            (temporary / 'standards').mkdir()
            script = temporary / 'scripts/sync-editorial-patterns.py'
            shutil.copyfile(ROOT / 'scripts/sync-editorial-patterns.py', script)
            shutil.copyfile(ROOT / 'standards/editorial-patterns.json', temporary / 'standards/editorial-patterns.json')
            target = temporary / 'standards/editorial-patterns.md'
            target.write_text('stale reference\n')
            result = subprocess.run([sys.executable, str(script), '--check'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertEqual(target.read_text(), 'stale reference\n')
            regenerated = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
            self.assertEqual(regenerated.returncode, 0, regenerated.stderr)
            checked = subprocess.run([sys.executable, str(script), '--check'], capture_output=True, text=True)
            self.assertEqual(checked.returncode, 0, checked.stderr)

    def test_invalid_source_does_not_replace_the_reference(self):
        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            (temporary / 'scripts').mkdir()
            (temporary / 'standards').mkdir()
            script = temporary / 'scripts/sync-editorial-patterns.py'
            shutil.copyfile(ROOT / 'scripts/sync-editorial-patterns.py', script)
            source = self.source()
            source['patterns'][1]['id'] = source['patterns'][0]['id']
            (temporary / 'standards/editorial-patterns.json').write_text(json.dumps(source))
            target = temporary / 'standards/editorial-patterns.md'
            target.write_text('previous reference\n')
            result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2, result.stderr)
            self.assertEqual(target.read_text(), 'previous reference\n')


if __name__ == '__main__':
    unittest.main()
