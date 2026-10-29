#!/usr/bin/env python3
"""Copy canonical writing references into independently installable skills."""

import argparse
import json
import os
from pathlib import Path
import sys
import tempfile


SKILL_REFERENCES = {
    "establish-project-language": ("writing.md", "content-patterns.md", "uncertainty.md"),
    "write-project-content": ("writing.md", "content-patterns.md", "uncertainty.md"),
    "advance-with-uncertainty": ("writing.md", "uncertainty.md"),
}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report drift without changing files")
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parent.parent
    pairs = [(root / "standards" / name,
              root / "skills" / skill / "references" / name)
             for skill, names in SKILL_REFERENCES.items() for name in names]
    try:
        # Read all sources before writing so a missing source cannot cause a partial sync.
        sources = {source: source.read_bytes() for source, _ in pairs}
        changed = []
        for source, target in pairs:
            data = sources[source]
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
        print(json.dumps({"mode": "check" if args.check else "sync", "changed": changed}))
        return 1 if args.check and changed else 0
    except OSError as error:
        print(json.dumps({"error": str(error)}))
        return 2


if __name__ == "__main__":
    sys.exit(main())
