# Purpose-sized skills with a shared baseline

## Decision

Give each authoring purpose a direct entry point. Keep a short, canonical baseline inline in every independently installable skill, and load supporting detail only when the task needs it. Retain `write-project-content` as an explicit compatibility chooser rather than an authoring prerequisite.

A marketing agent can select `write-marketing-content` from a customer-copy request. An ADR author can select `record-architecture-decisions` without loading the architecture playbooks; actual boundary design still belongs to those playbooks. The [skill table](../../README.md#choose-a-language-skill) maps the complete collection.

## Why this split

The previous broad writer covered tasks, decisions, developer documentation, marketing, interfaces and reviews. Its main file was small, but its scope competed with specialist purposes and it directed authors to broad shared material. The architecture playbooks loaded their full examples, mappings and checklists on every activation.

The revised collection has eleven skills: two architecture playbooks, terminology discovery, actionable uncertainty, six writing/review specialists and one compatibility chooser. The common baseline is 144 words. The six specialist bodies are roughly 316–345 words including that baseline, excluding discovery metadata.

The authored baseline is `standards/baseline.md`. The synchroniser embeds the same text in each skill and copies the references declared in `standards/skill-profiles.json`. Independent installation therefore preserves meaning without sibling dependencies. Authors should change the canonical file and regenerate, not edit generated copies separately.

## Context costs

The full catalogue's descriptions grow from 192 to 433 whitespace-separated words. More precise entry points have an upfront discovery cost. Hosts may shorten descriptions, so each begins with the concrete purpose. These counts are not model-token measurements.

Active context is more selective. The six writing specialists carry one relevant pattern reference, with uncertainty detail available only where appropriate. A straightforward change can use the inline baseline and actual project sources. The full reference set is available without being mandatory on every invocation.

Architecture core files fall from 2,411 to 907 words for backend and 2,198 to 979 for frontend, including their metadata. Details remain local and rules are loaded before the relevant decision. A complete review can read slightly more total material than before; the gain is smaller initial context and less unrelated detail for a narrow task. See [the mapping and observed trial](architecture-refactor.md).

Exact word counts are recorded in [context-budget.json](context-budget.json). Observed staged-file accesses are recorded in [selection evaluation](selection-evaluation.md). A file-access event establishes that bytes were read; it does not establish exact prompt tokens or internal reasoning.

## Selection and portability

Keep four questions separate:

1. Does each package conform to the portable format and resolve its own references?
2. Can an agent distinguish purposes using the catalogue metadata and an ordinary request?
3. Which bodies and references does it read when doing the work?
4. Does a specific native client discover, select and load the installed package correctly?

The first three can be exercised here. The last requires the actual client and execution mode. The [portability report](portability.md) records primary sources, tool versions, offline checks and host limits. No universal activation claim follows from a shared file format.

Codex's optional metadata disables implicit use of the compatibility router. That policy is not a portable universal switch. Its description also makes the explicit-only role clear, and other hosts need their own discovery checks. Persistent conversational guidance remains separate from task-specific skill activation.
