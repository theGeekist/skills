# Preserve architecture meaning while improving language

The backend and frontend rules are authoritative. Apply the shared language baseline, clearer explanations and purpose-sized organisation while preserving every rule, exception and intended meaning. Architectural changes require explicit user approval; editorial improvements within that constraint are authorised.

## What the reviews found

The first audit against the pre-language-system source at `fcbd5a9` found conflicting summaries: backend red/action signals had been softened, locale proximity had become ownership, shared boundaries had been narrowed, and frontend summaries added independent testability and an approval qualifier. Detailed references largely retained the original rules, but that did not make conflicting summaries acceptable.

A subsequent exact-wording restoration overcorrected. Verbatim retention protects text, whereas the requested outcome is accessible language with preserved architecture meaning. The revised skills therefore keep the shared baseline, concise decision guidance, first-use explanations and concern-specific references. Rules retain their original force, conditions and exceptions.

## How to check future edits

Use `standards/architecture-rules/` as the original comparison sources. The source-integrity test protects these historical inputs; it deliberately permits changes to active wording. A passing hash or linter cannot prove semantic equivalence.

Review each original section against the active core and relevant reference. Check prohibitions, permissions, defaults, exceptions, thresholds, dependency direction and prescribed responses. Inspect the core separately for new requirements or conflicting summaries. Then apply the four language outcomes: consistency, accessibility, readability and repeatability. Keep automated findings and independent judgement distinct.

See [the language and meaning review](architecture-language-review.md) for the executed checks and findings for this revision. Existing [architecture split trials](architecture-refactor.md) remain historical evidence rather than results for this revision.
