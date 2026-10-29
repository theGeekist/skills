---
name: write-project-content
description: "Compatibility router for explicit requests to use write-project-content or to choose a project-writing workflow. Keep ordinary task, ADR, technical-documentation, marketing, interface-copy and language-review requests with their purpose-specific skills; this router is not their default prerequisite."
---

# Choose a project-writing workflow

Retain this entry point for existing callers. When invoked explicitly, select the workflow that matches the requested artefact; avoid loading an umbrella plus every specialist.

<!-- shared-baseline:start -->
Use current project terms and decisions. Explain an unfamiliar term near its first consequential use; distinguish a proposed meaning from an accepted one. Preserve exact identifiers and technical constraints.

Lead with the reader's purpose and main point, then explain the consequences and supporting detail. Make substantial technical material navigable by a reader outside engineering, with descriptive headings and meaningful source links. Match depth to the request; use British English in authored prose.

Keep implementation progress separate from validation. Pair a material evidence gap with a bounded next action and completion evidence. Missing prior proof alone does not reject an option or halt authorised work. Name actual blockers precisely, continue independent authorised work, and preserve existing authorisation.

Check consistency, accessibility, readability and repeatability. Use sources for claims and real events for progress. Preserve uncertainty that affects a decision without inventing certainty or unnecessary approval gates.
<!-- shared-baseline:end -->

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

Use an available specialist directly. For mixed requests, use only the workflows needed for distinct deliverables and keep their domain meanings aligned. If a named specialist is not installed, preserve this baseline and the existing project format, state the limited fallback and complete the bounded writing task without inventing dependency availability.

Do not require a marketing author to load an architecture skill merely because the subject is technical. Read source contracts when needed to support a claim. A normal conversation uses persistent guidance rather than activating this router for every response.
