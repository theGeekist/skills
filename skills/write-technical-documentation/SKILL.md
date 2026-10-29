---
name: write-technical-documentation
description: "Write technical documentation: tutorials, how-to guides, API or configuration references, architecture explanations and developer guides. Use for learning, task completion, contract lookup or conceptual understanding, including technical documents that business readers must navigate. Use the ADR skill for decision records."
---

# Write technical documentation

Choose the structure that serves the reader's purpose while preserving the exact project behaviour.

<!-- shared-baseline:start -->
Use current project terms and decisions. Explain an unfamiliar term near its first consequential use; distinguish a proposed meaning from an accepted one. Preserve exact identifiers and technical constraints.

Lead with the reader's purpose and main point, then explain the consequences and supporting detail. Make substantial technical material navigable by a reader outside engineering, with descriptive headings and meaningful source links. Match depth to the request; use British English in authored prose.

Keep implementation progress separate from validation. Pair a material evidence gap with a bounded next action and completion evidence. Missing prior proof alone does not reject an option or halt authorised work. Name actual blockers precisely, continue independent authorised work, and preserve existing authorisation.

Check consistency, accessibility, readability and repeatability. Use sources for claims and real events for progress. Preserve uncertainty that affects a decision without inventing certainty or unnecessary approval gates.
<!-- shared-baseline:end -->

## Match the form to the reader

Determine whether the reader needs to learn by doing, complete a task, look up an exact contract or understand why the system works this way. Read the current documentation authority and relevant source revision. Use linked sections or pages when distinct purposes need different detail; do not create four documents automatically.

For substantial material, make purpose, main behaviour or decision and consequences easy to find. Explain required specialist terms near first use and provide meaningful links to contracts, examples and decisions. Preserve identifiers, units, defaults and failure behaviour in technical detail.

## Choose the useful detail

Load [documentation patterns](references/technical-documentation.md) when choosing or restructuring a document, writing a procedure/reference or checking mixed-audience navigation. For a narrow factual correction, inspect only the affected contract and existing form. Load [uncertainty guidance](references/uncertainty.md) if an evidence gap changes implementation or validation work.

Check examples and procedures where available and authorised. Separate inspected behaviour from executed checks and planned verification. Deliver the requested documentation and material limitations, without appending an editorial checklist to the document.

## Sources and adaptation

Diátaxis, Good Docs and the arc42 architecture-documentation template inform reader-purpose selection, procedures and architecture navigation. See [the sources and how they are adapted](references/technical-documentation.md#sources-and-local-adaptation); no complete framework template is mandatory.
