---
name: establish-project-language
description: "Discover, reconcile and maintain project concepts and terminology from code, schemas, tests, decisions and existing content. Use when starting a project, onboarding to an existing domain, resolving competing meanings, proposing new terms, or establishing shared language across agents and artefacts."
---

# Establish project language

Create a small, traceable account of what the project means. Start with the repository's current sources and decisions. Preserve useful established terms and make competing meanings visible.

<!-- shared-baseline:start -->
Use current project terms and decisions. Explain an unfamiliar term near its first consequential use; distinguish a proposed meaning from an accepted one. Preserve exact identifiers and technical constraints.

Lead with the reader's purpose and main point, then explain the consequences and supporting detail. Make substantial technical material navigable by a reader outside engineering, with descriptive headings and meaningful source links. Match depth to the request; use British English in authored prose.

Keep implementation progress separate from validation. Pair a material evidence gap with a bounded next action and completion evidence. Missing prior proof alone does not reject an option or halt authorised work. Name actual blockers precisely, continue independent authorised work, and preserve existing authorisation.

Check consistency, accessibility, readability and repeatability. Use sources for claims and real events for progress. Preserve uncertainty that affects a decision without inventing certainty or unnecessary approval gates.
<!-- shared-baseline:end -->

Load [extended writing guidance](references/writing.md) only when drafting a substantial mixed-audience domain explanation or reviewing its navigation; a small terminology correction can use the inline baseline.

## Discover the concepts

Read repository instructions, current decisions, public contracts, schemas, representative tests and audience-facing content. Include declared planning and authority directories even when their names begin with a dot. Use the tracked-file inventory or an explicit hidden-file search; an ordinary glob may miss the project's terminology. Identify the contexts in which the terms are used. A context is the area of work within which a definition holds; one word may legitimately mean something different elsewhere.

For a new project, use concrete scenarios and acceptance examples to develop candidate meanings. For an existing project, compare actual behaviour with documentation rather than treating either as automatically correct. Record the source revision and path for each consequential finding.

## Resolve meaning before naming

Describe each concept in plain English before selecting its preferred term. Distinguish aliases for the same concept from genuinely different concepts. Record contradictions with examples and propose the smallest clarification. Mark unresolved proposals explicitly.

Use [the registry example](assets/terminology.example.json) as a starting shape. Record stable concept IDs, context, preferred term, definition, status, aliases, relationships and sources. Use only `proposed`, `accepted` or `deprecated` for status. An observed meaning with source evidence can remain `proposed` until the project's adoption criteria are met; record observations in the definition and sources rather than inventing lifecycle values. Use audience labels to change presentation without redefining the concept. Retain deprecated IDs and their replacement where applicable.

Do not infer acceptance from discovering a name in code. Follow the repository's normal decision process; use the user's explicit decision where available. Avoid creating a terminology approval ceremony for routine wording.

## Explain the domain

Lead with what the system does and why its principal distinctions matter. Introduce technical terms near their first use. Provide a route from purpose and consequences to definitions, relationships and source evidence so a reader outside engineering can navigate the document.

Keep the registry small enough to maintain. Add a concept when ambiguity, a boundary or repeated use justifies it. Avoid cataloguing ordinary English or every local variable.

## Validate and maintain

Where the repository provides a checker, validate IDs, context membership, collisions and relationships. Review definitions and audience labels against current behaviour independently; a valid JSON file does not establish semantic correctness.

Revisit affected terms when a decision, schema, contract or product meaning changes. Identify the tasks, documentation, interfaces and agent instructions that use them. Retire old terms with a migration note rather than silently changing the meaning of an existing ID.

Finish with accepted findings, remaining proposals and source pointers. Report what was actually inspected and checked.

When a meaning remains unresolved and affects the next action, load [the uncertainty conventions](references/uncertainty.md) to record the next investigation or decision. A proposed term or incomplete glossary does not automatically block independent authorised implementation.

## Sources and adaptation

Context-aware terminology draws on domain-driven design (DDD), the Simple Knowledge Organization System (SKOS) for labels and definitions, and the Good Docs terminology guidance. See [sources and local registry adaptations](references/writing.md#sources-and-local-adaptation). These inform meaning and naming; they do not impose a DDD architecture.
