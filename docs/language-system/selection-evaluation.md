# Purpose-specific selection and selective loading

The expanded collection gives agents recognisable entry points for marketing,
technical documentation, implementation tasks, decisions, interface copy and
language review. In three catalogue-only trials, each responder selected the
expected primary skill for all twelve ordinary requests, including one request
requiring no skill. Natural authoring trials also selected relevant instructions
without the prompt naming a skill. These results support the purpose-specific split;
they do not certify automatic activation in every client.

## What was tested

The [method](../../evaluations/skill-selection/method.md) separates package
structure, catalogue selection, resource loading and native runtime activation.
The first three were exercised locally. See [portability](portability.md) for
client-specific evidence.

Two fresh-context responders received only names, descriptions and twelve
ordinary requests. Expected choices were retained separately and scored after
the outputs. The requests cover marketing, marketing from a technical source,
technical guidance, tasks, ADRs, interface states, terminology, cross-artefact
review, uncertainty, backend/frontend architecture and arithmetic.

A later reviewer refinement sharpened the task description's boundary with
ADRs. One more fresh responder used that final catalogue. Results were **12/12,
12/12 and 12/12**, with no ordinary request selecting the explicit-only
compatibility chooser. These are repeated observations on twelve authored cases,
not thirty-six distinct tasks or a measured native activation rate. The final
catalogue's names and descriptions comprise approximately 440 words; that
persistent discovery cost should be considered alongside smaller skill cores.

The [catalogue inputs, exact prompts, raw outputs and scoring](../../evaluations/skill-selection/)
are preserved. The [snapshot manifest](../../evaluations/skill-selection/snapshot-manifest.json)
identifies working-tree skill files by SHA-256 rather than attributing their
contents to the base Git revision. Initial header setup was corrected before any
behaviour responder began.

## Authoring and observed loading

Marketing and ADR responders received an isolated catalogue and invented source
facts. They chose their own relevant skill instructions, wrote the artefact and
performed no publication or implementation. Linux file-access monitoring
recorded which files were accessed. It does not prove that every byte entered
model context, and it cannot identify a native skill loader.

Initial loading was selective: the marketing responder accessed its skill core
and marketing reference, totalling 724 words; the ADR responder accessed its core,
decision reference and uncertainty reference, totalling 1,392 words. No other
skill body was accessed in those initial runs. Word totals measure files, not
model tokens.

The initial marketing email was accurate but included a list of unpromised
absent features. The initial ADR retained the decision and next authorised action
but was 224 words against a 220-word request, left FIFO unexplained and linked to
notes that would not travel with publication. Its exact bytes are retained as a
[plain-text record](../../evaluations/skill-selection/adr-output.txt) so the
historical local-only link is not presented as a working published route.

References were refined to keep material caveats without an absent-feature
inventory, explain necessary acronyms, honour the requested length and use a
source route that works at the intended destination. Fresh revisions preserve
these improvements. The revised ADR prompt also identifies notes that travel
with the output; both guidance and prompt changed, so this is not an isolated
causal comparison.

Two revised monitoring logs contain an early bulk-access batch from setup.
Those raw logs remain available, but no retrospectively chosen cutoff is used
to attribute their reads. Two final fresh runs use the stable copies, monitors
started separately from setup and a recorded pre-dispatch marker. The final
assessment records accesses relative to that marker, preserving any setup events
separately.

| Final ordinary request | Observed skill files | Words in accessed skill files | Output words |
| --- | --- | ---: | ---: |
| Marketing email | Marketing core + marketing reference | 772 | 111 / 130 |
| Decision record | ADR core + decision and uncertainty references | 1,454 | 218 / 220 |

Both final runs have no recorded setup accesses before the pre-dispatch marker.
The final marketing email keeps the material trial security caveat and a useful
trial action without listing absent team features. The final ADR explains FIFO,
links to the notes beside the delivered record and continues authorised prototype
work while preserving the open measurement and production-limit decisions.

The intermediate revised ADR read `advance-with-uncertainty` as a companion,
including its identical uncertainty reference. That was relevant but duplicated
context. The final ADR run used its own optional uncertainty reference without
loading a second skill. Preserve this observed variation: purpose-specific skills
reduce unnecessary loading opportunities, but do not impose a constant context
cost across agents or runs. The [loading assessment](../../evaluations/skill-selection/loading-assessment.json)
records initial, setup-contaminated and clean final observations separately.


## Structural checks and native-client scope

Seven deterministic checks cover the declared collection, one canonical inline
baseline per skill, direct bundled references, specialist reference separation,
explicit-only Codex chooser metadata, ordinary request fixtures and standalone
frontmatter fences. They pass. These checks establish packaging and shared-source
consistency; they cannot decide whether prose is useful.

Native runtime activation is outside these catalogue and staged-authoring results. The evidence establishes agent selection from supplied metadata and resource access in the recorded cases. It does not establish human-reader comprehension or universal cross-agent support.
