---
name: record-architecture-decisions
description: "Write, explain or update architecture decision records (ADRs), including context, viable options, decision drivers, consequences, status and reconsideration conditions. Use when the requested artefact is a decision record; use architecture skills for designing boundaries and technical documentation for general explanations."
---

# Record architecture decisions

Record one consequential choice so future readers can understand its reasons and effects.

<!-- shared-baseline:start -->
Use current project terms and decisions. Explain an unfamiliar term near its first consequential use; distinguish a proposed meaning from an accepted one. Preserve exact identifiers and technical constraints.

Lead with the reader's purpose and main point, then explain the consequences and supporting detail. Make substantial technical material navigable by a reader outside engineering, with descriptive headings and meaningful source links. Match depth to the request; use British English in authored prose.

Keep implementation progress separate from validation. Pair a material evidence gap with a bounded next action and completion evidence. Missing prior proof alone does not reject an option or halt authorised work. Name actual blockers precisely, continue independent authorised work, and preserve existing authorisation.

Check consistency, accessibility, readability and repeatability. Use sources for claims and real events for progress. Preserve uncertainty that affects a decision without inventing certainty or unnecessary approval gates.
<!-- shared-baseline:end -->

## Establish the decision and its authority

Read the repository's decision convention, related decisions and the actual source material. Establish whether the task proposes a choice, records one already made, explains an accepted decision or supersedes a previous record. Preserve the existing status vocabulary and decision authority.

Lead with the decision and its status. Explain the problem and drivers, viable alternatives and practical consequences. Retain the constraints that change the choice. Link the exact technical contracts rather than making a business reader begin with signatures or type lists.

## Choose the useful detail

Load [decision-record patterns](references/decisions.md) when creating or revising a full architecture decision record (ADR), comparing options or handling supersession. Load [uncertainty guidance](references/uncertainty.md) only when incomplete evidence, a failed experiment or an actual blocker affects the decision. A short explanation of a settled choice need not load the full pattern.

Distinguish the decision from its implementation and validation. Record a bounded experiment and reconsideration condition where appropriate. Deliver the requested record; do not reopen accepted choices or fabricate alternatives to fill a template.

## Edit before delivery

Compare the draft with its sources for added claims, omitted conditions and changed authority or status. Then remove repeated staging and explain the reader's situation instead of narrating internal fields or the writing process. Prefer concrete subjects and verbs; retain precise terms and deliberate voice. Recheck facts after cutting or restructuring. Deliver finished prose, with material source questions kept separately when needed.

## Sources and adaptation

The decision-record pattern draws on Markdown Architectural Decision Records (MADR) while preserving the project's own convention. See [MADR and the local additions](references/decisions.md#sources-and-local-adaptation).
