# Record uncertainty so work can advance

Honest evidence and useful progress belong together. Describe what is known, what is missing and what the gap means for the next decision. Treat uncertainty as something to investigate and reduce.

## Separate the states

Implementation state describes whether work is planned, implemented, checked or deployed. Evidence state describes which claims have been examined, using which sources or tests. A working implementation may lack host-level validation. A well-supported design may still need implementation. Record both accurately.

“Unproven”, “unqualified” and “no evidence” can be honest within a defined scope. On their own, they are poor task conclusions. They do not establish that a design is invalid, a task is unauthorised or useful work is impossible. Equally, an optimistic label does not establish that something works.

## Turn a gap into a next step

For each consequential gap, record:

| Item | What the reader needs |
| --- | --- |
| Observation | What was inspected or tested, with its source and scope |
| Open question | The precise claim that remains to be established |
| Implication | Which decision, implementation step or release depends on it |
| Next action | A bounded investigation, implementation, experiment or validation that reduces the gap |
| Completion evidence | The observable result that would answer the question |
| Blocker, if any | The specific missing input, authority or constraint that prevents a named action |

Use the smallest useful next action. Continue independent authorised work while a dependent action is blocked. In a task, make the expected behaviour and completion evidence explicit. In an ADR, explain how the uncertainty affects options and what would trigger reconsideration. In a handoff, name the next executable step so another worker can continue.

## Distinguish missing evidence from contrary evidence

An unrun test is an open question. A failing test is evidence about an observed behaviour under stated conditions. Neither justifies a broader claim without reasoning. Record a failure and decide whether to fix, narrow the scope, investigate or reject the option based on its actual impact.

Where a reversible experiment is authorised, a lack of prior proof can justify the experiment. An option does not become unsuitable merely because it still needs testing. Compare viable options using constraints, costs and evidence rather than requiring every proposal to arrive pre-validated.

## Preserve real boundaries

Missing permission for an irreversible external action can block that action. A required input, incompatible contract, demonstrated safety constraint or explicit failed acceptance condition can also block a named step. State exactly which step and why. Do not invent permission, readiness or success to keep progress moving.

Proceed with authorised preparation, local implementation or analysis that does not depend on the missing condition. Identify the decision or evidence needed to resume the dependent step. Honour explicit user instructions to stop.

Carry forward existing authorisation. Do not add a new permission gate for routine reversible validation already within scope. Keep uncertainty records proportional: a few sentences can be enough to establish the observation, next action and boundary.

## Examples

**Adapter task:** “The adapter passes local payload tests. Its behaviour in the desktop client remains to be checked. Build the authorised local prototype, capture one real client event, and verify that the correction runs once. Desktop compatibility can be claimed after that check.”

**Decision record:** “Choose a per-project queue for the prototype. It isolates scheduling in the current design; throughput under expected load still needs measurement. Run the representative load case before selecting production limits. Revisit the queue design if it exceeds the agreed latency budget.”

**External action:** “The release package is prepared and local checks pass. Publishing requires the missing maintainer approval. Continue the authorised release notes and reproducibility checks; publish once approval is recorded.”

These examples are invented. They retain uncertainty and define movement without declaring an untested result successful.

## Improve the sentence without changing the evidence

Invented task conclusion: “No evidence of desktop compatibility. Disqualify the adapter.” If no desktop trial has run, write “Desktop behaviour remains unchecked. Capture one client event and compare it with the local payload tests before claiming compatibility.” Keep any observed failing behaviour in the record and link its actual scope.

A concise negative statement can be accurate and useful. “The client rejected this payload” should remain a failure when observed; explain the bounded fix or reconsideration rather than replacing it with optimistic wording.

## Review for implementation impact

Ask whether another worker can identify what to do next, what they may proceed with, what evidence to collect and what genuinely blocks a dependent action. Check that an evidence label has not silently become a rejection, a blanket stop or an invented success claim.

Avoid global bans on negative words or automatic positive substitutions. The quality criterion is accurate reasoning that supports the next useful action.

## Sources and local adaptation

This is a local workflow rule developed from Jason's explicit requirement: honest evidence language must support bounded next actions rather than silently disqualify authorised work. It is not attributed to an external uncertainty framework. [MADR](https://adr.github.io/madr/) provides a related decision-record structure; it does not prescribe this continuation rule or establish that an untested option works.
