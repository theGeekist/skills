# Validation results and next checks

The initial evaluation below is retained as a checkpoint. The later all-eleven language/source review, current checks and preserved-meaning audit are in [architecture language review](architecture-language-review.md), with source lineage in [the framework map](../../standards/framework-evidence.md).

Reviewed 29 October 2026. The collection now has eleven portable skill packages: focused writing/review entry points, terminology discovery, actionable uncertainty, two smaller architecture cores and an explicit compatibility chooser. Shared references, lifecycles and the optional local Codex adapter are implemented. The next adoption checks concern real-reader comprehension and client-specific loading.

## Executed checks

| Check | Observed result | What it establishes |
| --- | --- | --- |
| Python suite with optional Vale integration enabled | 57 tests pass | Registry errors, contextual aliases, code exclusions, baseline/reference drift, isolated skill references, frontmatter fences and bounded Stop behaviour |
| Agent Skills reference validator | All eleven skills validate | Portable skill shape and frontmatter, paired with explicit fence checks |
| Baseline and bundled-reference comparison | No drift | Each skill embeds the canonical 144-word baseline and its declared reference copies |
| Selected Vale rules | No findings in skills, standards and selected system docs | These texts meet the small advisory word rule; semantic clarity needs separate assessment |
| Architecture forward test | Ownership, public dependencies and explicit coordination retained in a synthetic case | Wording changes preserve the tested architectural distinctions |
| Project discovery and writing | Initial failures captured; corrected fresh runs find hidden sources and produce valid registries | The revised instructions address two observed workflow defects |
| Blind navigation reader | Finds purpose, decision and consequences; identifies terms and links to improve | Preliminary agent evidence for reader navigation, with concrete editorial follow-up |
| Ordinary-request catalogue selection | Three runs of twelve cases select the expected purposes | Agent discrimination of catalogue descriptions, including marketing, mixed requests and no-skill cases; not native client activation |
| Observed staged authoring reads | Marketing and ADR runs read only their selected skill and relevant references | Selective resource access, measured as files/words rather than model prompt tokens |
| Google skill-reach offline checks | Strict lint and overlap exit successfully on all eleven skills | No lint warnings/errors; informational overlaps are retained for task testing, without a native activation claim |

The core suite runs without Vale; its optional integration case is then explicitly skipped. CI runs the dependency-free suite, baseline/reference and registry checks, and the portable validator from a pinned Agent Skills commit. Local optional-tool results are not represented as a completed remote CI run.

## Learning from independent runs

Initial domain discovery produced a status outside the registry's three lifecycle values. Initial writing runs missed terminology in a hidden planning directory. Both original outputs were preserved. Instructions now enumerate allowed statuses and require discovery of declared authority paths, including hidden paths. Fresh-context retests exercise those corrections.

The independent reader could recover the main decisions, while identifying jargon and source-navigation gaps. The pilot artefacts are revised to explain necessary terms near first use and provide clickable source routes. These edits are author revisions; they are not relabelled as a fresh human-comprehension pass.

Repeat runs retained important facts but varied in how much domain language they explained. The next evaluation should repeat the same authoring task with a reader-navigation check, retaining output and source revisions. Compare consistent meaning and route quality rather than identical wording.

See [project evaluation](project-evaluation.md) for coverage and limitations, and [architecture cases](../../evaluations/architecture/) for the synthetic boundary test. Detailed private source evidence is retained outside this public repository.

The purpose-sized follow-up adds [selection and observed file reads](selection-evaluation.md), [architecture split trials](architecture-refactor.md), [context costs](skill-design.md) and [portable tooling/host evidence](portability.md). These report setup corrections and first-output editorial findings alongside the successful selection cases.

## Honest uncertainty and continued implementation

The standalone skill has dedicated task/ADR cases in [uncertainty evaluation](uncertainty-evaluation.md). It distinguishes an open evidence question from a real blocker, preserves implementation progress and requires a bounded next action. The cases also check that optimism does not invent permission or successful validation.

## What can proceed now

Review and use the portable skills and shared references on bounded project work. Run the supplied checks when updating terminology or guidance. Use the documented registry format and preserve each project's current authority.

For a selected local client, test one instruction-loading case and one Stop correction case using the version and mode recorded in the result. The optional adapter already has subprocess coverage; host compatibility can be recorded after this observation. No client configuration was installed automatically.

Ask an engineering reader and a marketing reader to locate the pilot's purpose, decision, consequences and technical contract. Record their answers and navigation difficulties without coaching, then revise the artefact. This supplies direct comprehension evidence alongside the existing agent tests.

## Scope of the evidence

No source repository implementation was changed, no deployment or release was performed, and project runtime suites were not run for a documentation-only source inspection. Not every prepared lifecycle/dashboard case was exercised. The public and private evaluations record the executed cases separately.

There is no before/after control study or universal readability claim. The change provides a working implementation and concrete regression cases. Additional runtime and human-reader checks have named next actions in the [recommendation pipeline](recommendations.json).
