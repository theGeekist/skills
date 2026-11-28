#!/usr/bin/env python3
"""Validate installed skills and recognize only recorded upstream notices."""
import argparse
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--validator", default="skills-ref", help="skills-ref executable")
    args = parser.parse_args()
    records = json.loads((ROOT / "standards/upstream-compatibility.json").read_text())
    exceptions = records["validator_notices"]
    observed = set()
    failures = []

    for skill_path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        name = skill_path.parent.name
        result = subprocess.run(
            [args.validator, "validate", str(skill_path.parent)],
            capture_output=True,
            text=True,
            check=False,
        )
        lines = (result.stdout + result.stderr).splitlines()
        messages = [line.strip()[2:] for line in lines if line.strip().startswith("- ")]
        expected = exceptions.get(name)

        if result.returncode == 0:
            print(f"Valid skill: {name}")
            if expected:
                failures.append(f"{name}: recorded validator notice has cleared; update the compatibility record")
            continue

        if expected and messages == expected["messages"]:
            observed.add(name)
            print(f"UPSTREAM COMPATIBILITY NOTICE: {name}")
            print(f"  Consequence: {expected['consequence']}")
            print(f"  Resolution: {expected['resolution']}")
            continue

        failures.append(f"{name}: validator output differs from the recorded result")
        failures.extend(f"  {line}" for line in lines)

    stale = set(exceptions) - observed
    failures.extend(f"{name}: recorded validator notice was not observed" for name in sorted(stale))
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
