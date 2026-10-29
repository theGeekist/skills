#!/usr/bin/env python3
"""Validate terminology records and report contextual non-preferred aliases.

This checker does not infer meaning, assess prose quality or approve new concepts.
It uses only the explicit relationships in the supplied registry.
"""

import argparse
import bisect
import json
from pathlib import Path
import re
import sys


class RegistryError(ValueError):
    """A registry or command configuration is invalid."""


def _name(value):
    return value.strip().casefold()


def validate_registry(registry):
    """Return the registry, or raise RegistryError with actionable field paths."""
    errors = []

    def problem(path, message):
        errors.append(f"{path}: {message}")

    def string(value, path):
        if not isinstance(value, str) or not value.strip():
            problem(path, "must be a non-empty string")
            return False
        return True

    def string_list(record, key, path):
        value = record.get(key, [])
        if not isinstance(value, list):
            problem(f"{path}.{key}", "must be an array")
            return []
        return [item for i, item in enumerate(value)
                if string(item, f"{path}.{key}[{i}]")]

    if not isinstance(registry, dict):
        raise RegistryError("registry: must be an object")
    if type(registry.get("version")) is not int or registry["version"] != 1:
        problem("version", "must be the integer 1")

    contexts = registry.get("contexts")
    if not isinstance(contexts, list):
        problem("contexts", "must be an array")
        contexts = []
    context_ids = set()
    for i, context in enumerate(contexts):
        path = f"contexts[{i}]"
        if not isinstance(context, dict):
            problem(path, "must be an object")
            continue
        for key in ("id", "name", "definition"):
            string(context.get(key), f"{path}.{key}")
        context_id = context.get("id")
        if isinstance(context_id, str):
            if context_id in context_ids:
                problem(f"{path}.id", f"duplicate context {context_id!r}")
            context_ids.add(context_id)

    concepts = registry.get("concepts")
    if not isinstance(concepts, list):
        problem("concepts", "must be an array")
        concepts = []
    concept_ids = set()
    names = {}
    references = []
    for i, concept in enumerate(concepts):
        path = f"concepts[{i}]"
        if not isinstance(concept, dict):
            problem(path, "must be an object")
            continue
        for key in ("id", "context", "preferred_term", "definition"):
            string(concept.get(key), f"{path}.{key}")
        concept_id = concept.get("id")
        if isinstance(concept_id, str):
            if concept_id in concept_ids:
                problem(f"{path}.id", f"duplicate concept {concept_id!r}")
            concept_ids.add(concept_id)
        context = concept.get("context")
        if isinstance(context, str) and context not in context_ids:
            problem(f"{path}.context", f"unknown context {context!r}")
        status = concept.get("status")
        if not isinstance(status, str) or status not in ("proposed", "accepted", "deprecated"):
            problem(f"{path}.status", "must be proposed, accepted or deprecated")

        aliases = string_list(concept, "aliases", path)
        relations = string_list(concept, "distinct_from", path)
        for relation in relations:
            references.append((f"{path}.distinct_from", relation, concept_id))
        if "replaced_by" in concept:
            replacement = concept["replaced_by"]
            if string(replacement, f"{path}.replaced_by"):
                references.append((f"{path}.replaced_by", replacement, concept_id))

        labels = concept.get("labels", {})
        if not isinstance(labels, dict):
            problem(f"{path}.labels", "must be an object mapping audiences to labels")
        else:
            for audience, label in labels.items():
                string(audience, f"{path}.labels audience")
                string(label, f"{path}.labels.{audience}")

        sources = concept.get("sources", [])
        if not isinstance(sources, list):
            problem(f"{path}.sources", "must be an array")
        else:
            if status == "accepted" and not sources:
                problem(f"{path}.sources", "accepted concepts require at least one source")
            for j, source in enumerate(sources):
                if not isinstance(source, dict):
                    problem(f"{path}.sources[{j}]", "must be an object")
                    continue
                for key in ("path", "revision"):
                    string(source.get(key), f"{path}.sources[{j}].{key}")

        preferred = concept.get("preferred_term")
        if isinstance(context, str):
            candidates = ([preferred] if isinstance(preferred, str) else []) + aliases
            for term in candidates:
                key = (context, _name(term))
                if key in names:
                    problem(path, f"term {term!r} collides with {names[key]} in context {context!r}")
                else:
                    names[key] = path

    for path, target, owner in references:
        if target not in concept_ids:
            problem(path, f"unknown concept {target!r}")
        elif target == owner:
            problem(path, "a concept cannot refer to itself here")
    if errors:
        raise RegistryError("; ".join(errors))
    return registry


def load_registry(path):
    """Read and validate a UTF-8 JSON registry. Raise RegistryError on failure."""
    try:
        registry = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise RegistryError(f"{path}: {error}") from error
    return validate_registry(registry)


def _masked_text(text):
    """Mask code and URLs while preserving offsets and line numbers."""
    def mask(value):
        return re.sub(r"[^\n]", " ", value)

    lines = text.splitlines(keepends=True)
    fence = None
    for i, line in enumerate(lines):
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\r\n"))
        if fence:
            lines[i] = mask(line)
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
        elif match and (match[1][0] != "`" or "`" not in match[2]):
            fence = match[1]
            lines[i] = mask(line)
        elif line.startswith("    ") or line.startswith("\t"):
            lines[i] = mask(line)
    result = "".join(lines)
    # Match same-length backtick delimiters; unmatched delimiters remain prose.
    result = re.sub(r"(?<!`)(`+)(?!`)([\s\S]*?)(?<!`)\1(?!`)",
                    lambda match: mask(match[0]), result)
    result = re.sub(r"(?:https?://|www\.)[^\s<>]+", lambda match: mask(match[0]), result)
    # Markdown destinations (including relative paths) are machine references.
    result = re.sub(r"\]\([^\n)]*\)", lambda match: "]" + mask(match[0][1:]), result)
    return result


def _term_pattern(term):
    return re.compile(r"(?<!\w)" + re.escape(term) + r"(?!\w)", re.IGNORECASE)


def lint_text(text, registry, context, audience=None):
    """Return alias warnings for one explicit context and optional audience.

    Preferred names and the selected audience's labels are protected. Proposed
    concepts do not establish an approved replacement and are therefore skipped.
    Findings identify lexical matches only; a person must assess applicability.
    """
    validate_registry(registry)
    if not isinstance(context, str) or context not in {item["id"] for item in registry["contexts"]}:
        raise RegistryError(f"unknown context {context!r}")
    if audience is not None and (not isinstance(audience, str) or not audience.strip()):
        raise RegistryError("audience must be a non-empty string")
    masked = _masked_text(text)
    concepts = [item for item in registry["concepts"] if item["context"] == context]
    protected = []
    for concept in concepts:
        if concept["status"] == "proposed":
            continue
        terms = [concept["preferred_term"]]
        if audience and audience in concept.get("labels", {}):
            terms.append(concept["labels"][audience])
        for term in terms:
            protected.extend((match.start(), match.end()) for match in _term_pattern(term).finditer(masked))
    line_starts = [0] + [match.end() for match in re.finditer("\n", text)]
    findings = []
    for concept in concepts:
        if concept["status"] == "proposed":
            continue
        preferred = concept.get("labels", {}).get(audience, concept["preferred_term"])
        for alias in concept.get("aliases", []):
            for match in _term_pattern(alias).finditer(masked):
                if any(start <= match.start() and match.end() <= end for start, end in protected):
                    continue
                findings.append({
                    "line": bisect.bisect_right(line_starts, match.start()),
                    "term": text[match.start():match.end()],
                    "preferred": preferred,
                    "rule": "nonpreferred-alias",
                    "severity": "warning",
                    "concept": concept["id"],
                    "context": context,
                })
    return sorted(findings, key=lambda finding: (finding["line"], finding["term"], finding["concept"]))


def main(argv=None):
    class Parser(argparse.ArgumentParser):
        def error(self, message):
            raise RegistryError(message)

    parser = Parser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    registry_command = commands.add_parser("registry", help="validate a JSON registry")
    registry_command.add_argument("path")
    lint = commands.add_parser("lint", help="report contextual non-preferred aliases")
    lint.add_argument("--registry", required=True)
    lint.add_argument("--context", required=True)
    lint.add_argument("--audience")
    lint.add_argument("file")
    try:
        args = parser.parse_args(argv)
        registry = load_registry(args.path if args.command == "registry" else args.registry)
        findings = []
        if args.command == "lint":
            text = Path(args.file).read_text(encoding="utf-8")
            findings = lint_text(text, registry, args.context, args.audience)
        print(json.dumps({"valid": True, "findings": findings}, ensure_ascii=False))
        return 1 if findings else 0
    except (RegistryError, OSError, UnicodeError) as error:
        print(json.dumps({"valid": False, "findings": [], "error": str(error)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    sys.exit(main())
