"""Keep the original architecture sources stable for semantic review.

This protects the comparison sources, not the wording of the active skills.
Automated checks cannot establish semantic equivalence; see the review record.
"""
from pathlib import Path
import hashlib
import unittest

ROOT = Path(__file__).resolve().parent.parent
SOURCES = {'backend': '888057be6739d2fd05255208f9a1cd5cfe28cd43e0a8f7e6b2833ccd6cca26bc', 'frontend': 'c56ac1ef54d83aeafa6786f482c06082892e0f0674efa1087a2963735c419f0e'}

class ArchitectureSourceIntegrity(unittest.TestCase):
    def test_original_comparison_sources_are_unchanged(self):
        for name, digest in SOURCES.items():
            with self.subTest(skill=name):
                source = ROOT / 'standards' / 'architecture-rules' / (name + '-slice-architecture.md')
                self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), digest)

if __name__ == '__main__':
    unittest.main()
