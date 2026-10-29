"""Architecture edits must preserve the user-owned rules and exceptions."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parent.parent

class ArchitectureRulePreservation(unittest.TestCase):
    def test_every_original_section_is_retained_verbatim(self):
        for name in ('backend-slice-architecture', 'frontend-slice-architecture'):
            with self.subTest(skill=name):
                original = (ROOT / 'standards' / 'architecture-rules' / (name + '.md')).read_text()
                folder = ROOT / 'skills' / name
                documents = [(folder / 'SKILL.md').read_text()] + [p.read_text() for p in (folder / 'references').glob('*.md')]
                for section in re.split(r'(?=^## )', original, flags=re.M)[1:]:
                    self.assertTrue(any(section.strip() in doc for doc in documents), section.splitlines()[0])

if __name__ == '__main__':
    unittest.main()
