# Validation results

The collection is checked at several levels: generated sources, package structure, terminology, representative writing behaviour and client integration. Results at one level do not substitute for another.

## Published checkpoints

| Check | Recorded result | Scope |
| --- | --- | --- |
| v1.6.0 Python suite with optional Vale enabled | 66 tests pass | Registry validation, source/reference drift, catalogue generation, standalone packages and bounded adapter behaviour |
| Portable Agent Skills validator | All eleven packages valid | Frontmatter and package shape |
| Shared baseline and bundled references | No drift | Canonical baseline and declared local copies |
| Presentation catalogue | No drift | Generated overview pages, prompts and plugin presentation |
| Configured Vale rules | No findings in the checked skills and presentation pages | Selected advisory wording patterns |
| Ordinary-request catalogue selection | Three runs select the expected purposes for all twelve cases | Supplied metadata catalogue; not native activation |
| Observed authoring reads | Marketing and ADR trials access relevant cores and references | Staged file access, measured as files and words |
| Offline skill-reach checks | Strict lint and overlap complete successfully | Lexical selection signals, not a native loader |
| Bounded editorial tasks | Cross-artefact corrections and source-grounded marketing retain the supplied constraints | Two isolated task cases |

The checkpoint numbers describe the recorded revision. Current test output may contain additional cases. The optional Vale integration test is explicitly skipped when its executable is not configured.

## Behaviour and source evidence

The [editorial trials](../../evaluations/editorial-v1.6.0/README.md) retain invented source facts, prompts, outputs and instruction hashes. The review case distinguishes document-check approval from purchase confirmation, removes unsupported public-profile claims and preserves authorised local work. The marketing case avoids inventing performance results or a public sign-up route.

The [project evaluation](project-evaluation.md) records terminology discovery and cross-audience explanations against public source contracts. Its initial failures led to concrete changes: inspect hidden authority paths, use declared registry statuses and provide meaningful links into exact contracts. The [uncertainty cases](uncertainty-evaluation.md) exercise evidence gaps, continuation and genuine action boundaries.

The [architecture review](architecture-language-review.md) checks retained rule meaning. The [selection evaluation](selection-evaluation.md) and [portability report](portability.md) retain separate results for description choice, resource access and native integration.

## Current-source checkpoint: 30 October 2026

The current source passes 75 tests with optional Vale enabled. The added cases cover editorial-pattern schema, attribution, reference generation and standalone packaging. The patterns support contextual judgement; generation checks do not decide whether a claim is true.

## Reproduce repository checks

```sh
python3 scripts/sync-editorial-patterns.py --check
python3 scripts/sync-skill-catalogue.py --check
python3 scripts/sync-language-references.py --check
python3 scripts/check-language.py registry standards/terminology.json
python3 -m unittest discover -s tests -v
```

For portable-format and optional-tool setup, follow [integration](integration.md). Check source revisions and hashes when replaying a case; the repository commit alone does not identify an uncommitted instruction snapshot.

## Interpretation

These records demonstrate the checked structure and behaviour on the published cases. They do not establish universal readability, human comprehension, native activation across clients, comparative prose superiority or search-ranking gains. Those are different measurements. The [competitive comparison](competing-writing-skills.md) describes the alternatives and their inspected instructions without presenting structural checks as a quality ranking.
