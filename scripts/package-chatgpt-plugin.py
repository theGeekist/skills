#!/usr/bin/env python3
"""Build a single-root, skills-only ChatGPT plugin ZIP from Geekist Skills.

GitHub source archives also contain marketplace files and repository tools.
Those archives are not the ChatGPT upload package. Keep one plugin manifest
and all independently loadable skills in the ChatGPT distribution.
"""
import argparse
from pathlib import Path
import json
import sys
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ".codex-plugin/plugin.json"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)


def build_archive(root: Path, output: Path) -> dict:
    root = root.resolve()
    manifest = root / MANIFEST
    skills_root = root / "skills"
    if not manifest.is_file() or not skills_root.is_dir():
        raise ValueError("expected Codex plugin manifest and skills directory")
    definition = json.loads(manifest.read_text(encoding="utf-8"))
    if definition.get("skills") != "./skills/":
        raise ValueError("plugin manifest must point at ./skills/")
    if not definition.get("name") or not definition.get("version"):
        raise ValueError("plugin name and version must be present")

    skills = sorted(skills_root.glob("*/SKILL.md"))
    if not skills:
        raise ValueError("no installable SKILL.md files found")
    files = [manifest]
    for path in sorted(skills_root.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"cannot package symlink: {path}")
        if path.is_file():
            files.append(path)
    if any(path.name == "SKILL.md" and path.parent.parent != skills_root
           for path in files):
        raise ValueError("SKILL.md must be immediately under skills/<name>/")

    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            relative = path.relative_to(root).as_posix()
            info = ZipInfo(relative, date_time=FIXED_TIME)
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=ZIP_DEFLATED,
                             compresslevel=9)

    with ZipFile(output) as archive:
        names = set(archive.namelist())
        expected = {path.relative_to(root).as_posix() for path in files}
        if names != expected or archive.testzip() is not None:
            raise ValueError("archive incomplete or corrupt")
        if sum(name.endswith("/SKILL.md") for name in names) != len(skills):
            raise ValueError("skill count mismatch")
    return {"output": str(output), "plugin": definition["name"],
            "version": definition["version"], "skills": len(skills),
            "files": len(files), "bytes": output.stat().st_size}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(build_archive(ROOT, args.output)))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
