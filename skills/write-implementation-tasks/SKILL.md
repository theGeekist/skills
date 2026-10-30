---
name: write-implementation-tasks
description: "Write implementation tasks and worker handoffs. Use for engineering tickets, implementation plans and acceptance criteria that need an observable outcome, concrete behaviour, validation and actionable dependencies. Use the ADR skill when the requested artefact is a decision record; use architecture skills for designing boundaries."
---

# Write implementation tasks

Turn the requested outcome into a task another worker can execute without reconstructing the conversation.

<!-- shared-baseline:start -->
Use current project terms and decisions. Explain an unfamiliar term near its first consequential use; distinguish a proposed meaning from an accepted one. Preserve exact identifiers and technical constraints.

Lead with the reader's purpose and main point, then explain the consequences and supporting detail. Make substantial technical material navigable by a reader outside engineering, with descriptive headings and meaningful source links. Match depth to the request; use British English in authored prose.

Keep implementation progress separate from validation. Pair a material evidence gap with a bounded next action and completion evidence. Missing prior proof alone does not reject an option or halt authorised work. Name actual blockers precisely, continue independent authorised work, and preserve existing authorisation.

Check consistency, accessibility, readability and repeatability. Use sources for claims and real events for progress. Preserve uncertainty that affects a decision without inventing certainty or unnecessary approval gates.
<!-- shared-baseline:end -->

## Establish the outcome and constraints

Read the project's task conventions and the current contracts relevant to the change. Identify the outcome, existing behaviour, constraints and concrete acceptance examples. Use the project's lifecycle states rather than inventing a new status vocabulary.

State what can proceed, how success and failure will be observed, and what evidence to capture. Separate implementation progress from validation; an unrun check can be part of the authorised task. Name a blocker only for the step that genuinely depends on it.

## Choose the useful detail

Load [task and handoff patterns](references/tasks.md) when choosing acceptance detail, splitting work or preparing a worker handoff. Load [uncertainty guidance](references/uncertainty.md) only when an evidence gap or failed check materially affects the next action. Do not load both by default for a straightforward ticket.

Use the existing architecture and task authority. Preserve technical choices already made; propose implementation detail only when needed. Deliver the requested task with source links and a concrete next step, without adding a universal process checklist.

## Edit before delivery

Compare the draft with its sources for added claims, omitted conditions and changed authority or status. Then remove repeated staging and explain the reader's situation instead of narrating internal fields or the writing process. Prefer concrete subjects and verbs; retain precise terms and deliberate voice. Recheck facts after cutting or restructuring. Deliver finished prose, with material source questions kept separately when needed.

## Sources and adaptation

The task pattern is a local synthesis, informed by the Good Docs goal-oriented how-to guidance. See [the source and limits of that adaptation](references/tasks.md#sources-and-local-adaptation).
