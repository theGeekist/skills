---
name: write-project-content
description: "Write, rewrite and organise general project writing: research notes, investigation findings, reports, meeting summaries, progress updates, explanations and other substantive prose. Use when the user asks for a written deliverable without a more specific Geekist writing skill. Not for ordinary discussion or automatically invoking every specialist."
---

# Write general project content

Use this skill for substantive writing without a more specific home: reports, investigations, research notes, findings, summaries, project updates and explanations. This is an authoring and editing skill, not a mandatory document template or prerequisite for specialists.

<!-- shared-baseline:start -->
Use current project terms and decisions. Explain an unfamiliar term near its first consequential use; distinguish a proposed meaning from an accepted one. Preserve exact identifiers and technical constraints.

Lead with the reader's purpose and main point, then explain the consequences and supporting detail. Make substantial technical material navigable by a reader outside engineering, with descriptive headings and meaningful source links. Match depth to the request; use British English in authored prose.

Keep implementation progress separate from validation. Pair a material evidence gap with a bounded next action and completion evidence. Missing prior proof alone does not reject an option or halt authorised work. Name actual blockers precisely, continue independent authorised work, and preserve existing authorisation.

Check consistency, accessibility, readability and repeatability. Use sources for claims and real events for progress. Preserve uncertainty that affects a decision without inventing certainty or unnecessary approval gates.
<!-- shared-baseline:end -->

## Write or revise general work

Identify the reader, main point and whether the user wants a draft, rewrite or synthesis. Preserve the author's voice, accepted terminology, source authority and material conditions. Organise observations, conclusions and possible actions in the way the reader needs; don't invent results or impose universal report headings.

For revisions, retain precise facts while improving flow and clarity. For investigation notes and reports, preserve useful findings and unresolved questions without turning the result into a list of disclaimers. Use prose for reasoning and headings, lists, links or tables only where they make the writing easier to read.

A chat draft, Markdown file, Google Doc or other destination follows the user's requested format and existing conventions. This skill does not imply that a file must be created or grant filesystem access.

## Use specialists when they fit better

| Requested work | Preferred skill |
| --- | --- |
| Implementation ticket, acceptance criteria or worker handoff | `write-implementation-tasks` |
| Architecture decision record or explanation of an ADR | `record-architecture-decisions` |
| Tutorial, how-to, technical reference or architecture explanation | `write-technical-documentation` |
| Campaign, product announcement, positioning or landing-page copy | `write-marketing-content` |
| Labels, dashboard states, progress messages, errors or notifications | `write-interface-content` |
| Existing text needing terminology, readability or navigation review | `review-project-language` |
| Discovering or reconciling project meanings | `establish-project-language` |
| Evidence language causing unsupported rejection or stopped work | `advance-with-uncertainty` |

For reports, meeting notes, project summaries and other general writing without a tighter match, use this skill directly. If a specialist clearly matches, select it instead: it need not load this general writer first. For mixed deliverables, choose only the relevant guidance.

If a specialist isn't installed, preserve the shared baseline and the existing format; complete the task without claiming the missing skill was loaded. Normal conversation, factual Q&A and exploratory discussion do not automatically imply a written artefact. Consult source contracts when claims depend on them, without loading architecture guidance just because a subject is technical.

## Sources and adaptation

This general writing entry point also supports explicit workflow choice. See [its rationale and Agent Skills packaging source](references/routing.md). It does not introduce another writing framework or require every specialist to load together.
