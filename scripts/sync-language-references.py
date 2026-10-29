#!/usr/bin/env python3
"""Reproduce the shared inline baseline and purpose-specific bundled references."""

import argparse
import json
import os
from pathlib import Path
import re
import sys
import tempfile

START = '<!-- shared-baseline:start -->'
END = '<!-- shared-baseline:end -->'


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='report drift without changing files')
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parent.parent
    try:
        standards = root / 'standards'
        profiles = json.loads((standards / 'skill-profiles.json').read_text())
        if profiles.get('version') != 1 or not isinstance(profiles.get('skills'), dict):
            raise ValueError('invalid skill profile version or skills map')
        baseline = (standards / 'baseline.md').read_text().strip()
        if not baseline or START in baseline or END in baseline:
            raise ValueError('baseline must be non-empty prose without generation markers')
        planned = {}
        for skill, profile in profiles['skills'].items():
            if not isinstance(skill, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', skill):
                raise ValueError('invalid skill name')
            refs = profile.get('references') if isinstance(profile, dict) else None
            if not isinstance(refs, list) or len(refs) != len(set(refs)):
                raise ValueError('references must be a list of unique filenames')
            body_path = root / 'skills' / skill / 'SKILL.md'
            body = body_path.read_text()
            if body.count(START) != 1 or body.count(END) != 1 or body.index(START) > body.index(END):
                raise ValueError(f'{skill}: expected one ordered baseline marker pair')
            prefix, rest = body.split(START)
            _, suffix = rest.split(END)
            planned[body_path] = (prefix + START + '\n' + baseline + '\n' + END + suffix).encode()
            for name in refs:
                if not isinstance(name, str) or Path(name).name != name or not name.endswith('.md'):
                    raise ValueError('reference must be a Markdown filename within standards')
                planned[root / 'skills' / skill / 'references' / name] = (standards / name).read_bytes()
        # Validate/read all inputs before any mutation. Hand-authored references are untouched.
        changed = []
        for target, data in planned.items():
            if target.exists() and target.read_bytes() == data:
                continue
            changed.append(str(target.relative_to(root)))
            if args.check:
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = None
            try:
                with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as output:
                    temporary = output.name
                    output.write(data)
                os.chmod(temporary, 0o644)
                os.replace(temporary, target)
            finally:
                if temporary and os.path.exists(temporary):
                    os.unlink(temporary)
        print(json.dumps({'mode': 'check' if args.check else 'sync', 'changed': changed}))
        return 1 if args.check and changed else 0
    except (OSError, ValueError, TypeError, AttributeError) as error:
        print(json.dumps({'error': str(error)}))
        return 2


if __name__ == '__main__':
    sys.exit(main())
