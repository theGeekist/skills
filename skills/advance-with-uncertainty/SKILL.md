---
name: advance-with-uncertainty
description: "Turn evidence gaps and unresolved questions into bounded next actions while preserving honest claims and actual blockers. Use when drafting or reviewing tasks, ADRs, plans, assessments or worker handoffs, especially when labels such as unproven, unqualified or no evidence are being used to reject options or halt authorised implementation."
---

# Advance with uncertainty

Keep authorised work moving while making the limits of current knowledge precise.

<!-- shared-baseline:start -->
Use current project terms and decisions. Explain an unfamiliar term near its first consequential use; distinguish a proposed meaning from an accepted one. Preserve exact identifiers and technical constraints.

Lead with the reader's purpose and main point, then explain the consequences and supporting detail. Make substantial technical material navigable by a reader outside engineering, with descriptive headings and meaningful source links. Match depth to the request; use British English in authored prose.

Keep implementation progress separate from validation. Pair a material evidence gap with a bounded next action and completion evidence. Missing prior proof alone does not reject an option or halt authorised work. Name actual blockers precisely, continue independent authorised work, and preserve existing authorisation.

Check consistency, accessibility, readability and repeatability. Use sources for claims and real events for progress. Preserve uncertainty that affects a decision without inventing certainty or unnecessary approval gates.
<!-- shared-baseline:end -->

Load [the uncertainty conventions](references/uncertainty.md) for a multi-gap assessment, conflicting evidence or a consequential decision. Use [the task and ADR examples](assets/action-records.md) when a concrete structure helps. A short handoff can use the inline baseline and workflow without loading either.

## Identify what the statement establishes

Read the task, decision, current evidence and user intent. Separate implementation state from evidence state. Find the exact claim behind labels such as “unproven”, “unqualified” or “no evidence”. Determine whether the situation is an unrun check, unavailable information, a failed check, a conflicting source or a genuine constraint.

Retain honest negative findings. Scope them to what was examined. Avoid inferring that an option is invalid, a task cannot proceed or a whole project is blocked merely because a particular claim remains untested.

## Decide the next useful action

Connect each material gap to a bounded investigation, implementation, experiment, validation or decision. State the observation, open question, practical implication and completion evidence. Define an observable result rather than the vague instruction “prove it”.

Continue reasonable authorised work where it does not depend on the missing evidence. For a reversible prototype, validation can be part of the task. Compare options using actual constraints and trade-offs; missing prior proof alone is not a reason to discard them.

## Make real blockers specific

Identify the exact action blocked and the missing condition needed to resume it. Preserve permission boundaries, irreversible-action constraints, required inputs and demonstrated failures. Do not invent authority or success to create momentum. Honour explicit instructions to stop.

Continue independent authorised preparation or analysis when possible. Avoid declaring an entire task blocked if only release, deployment or one dependent check is waiting.

Carry forward the authorisation already established in the task. Do not invent another approval gate for routine reversible validation that is within scope; ask only when a genuinely missing decision prevents the named action.

## Write the task, ADR or handoff

Lead with the intended outcome or decision. Record implementation progress and evidence separately. Pair uncertainty with the next action, completion evidence and any actual stop condition.

For a task, specify the expected behaviour and concrete acceptance examples. For an ADR, retain context, viable alternatives, trade-offs and the condition for revisiting the decision. For a worker handoff, make the next executable step and its boundaries explicit.

Use precise source references. If an uncertainty does not affect the reader's decision, keep it in supporting detail rather than making it the document's headline.

Keep the record proportional to the task. A short task or handoff may express the observation, next action and boundary in a few sentences; the reference fields are prompts for reasoning, not mandatory headings to reproduce.

## Review for unintended disqualification

Check whether another worker can identify what they may do now, what they must check and what genuinely requires a decision. Remove unsupported leaps from an evidence label to rejection or a blanket stop. Also check that the rewrite has not implied validation, readiness or permission that does not exist.

Do not ban negative vocabulary or mechanically replace it with positive words. Judge accuracy, usefulness and the action the writing enables. Report unresolved limits alongside the bounded next step.
