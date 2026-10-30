# Design requirements

The collection supports consistent project meaning and readable material across engineering and business audiences. The same concept, permission or constraint should remain recognisable as it moves from code and decisions into tasks, documentation, marketing and interfaces.

## Four outcomes

| Outcome | Requirement |
| --- | --- |
| Consistency | Shared concepts retain their accepted meanings across artefacts and audiences |
| Accessibility | Readers can find purpose, decisions, consequences, definitions and detailed sources |
| Readability | Terms, sentences and paragraphs explain the subject at the required depth |
| Repeatability | Another author can follow the references and preserve meaning and navigation |

Technical precision remains necessary. A marketing reader should be able to navigate a technical document without implementing its contracts; an engineer should be able to reach those contracts directly.

## Evidence and implementation

Evidence state and implementation state are separate. Labels such as “unproven”, “unqualified” and “no evidence” can be accurate without rejecting an option or halting independent authorised work. A material gap needs a bounded next action and completion evidence.

The [uncertainty skill](../../skills/advance-with-uncertainty/SKILL.md) implements this requirement. It also preserves genuine failed requirements, authority boundaries and dependent stop conditions. A blanket ban on negative vocabulary would defeat that purpose.

## Focused entry points

Each of the eleven skills has a concrete purpose. Task, ADR, technical-documentation, marketing, interface and review requests can select their specialist directly. The compatibility router remains optional and explicit.

Every independently installed skill carries the same canonical baseline and its own required references. Supporting material is loaded by concern rather than by a compulsory full-research read. Architecture playbooks preserve their governing rules and exceptions while using the same reader-focused communication baseline.

## Inspectable sources and checks

The repository links the [original research](research-baseline.md), [verified sources](sources.json), [framework adaptations](../../standards/framework-evidence.md), [competing skills](competing-writing-skills.md) and [recorded evaluations](validation-results.md). Source inspection, executed checks, qualitative agent assessment and human comprehension are distinct forms of evidence.

Optional validators and adapters remain separate from the portable Markdown instructions. Installing a skill must not silently install hooks or replace global conversation instructions. Client-specific activation and loading semantics are documented separately from the shared format.
