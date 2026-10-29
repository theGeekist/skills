# Implementation tasks and handoffs

Use the project's task format and lifecycle states. Keep domain terms tied to current decisions, contracts and examples. A task should tell its next worker what outcome to produce and how to recognise it.

## Choose the useful detail

| Part | Record |
| --- | --- |
| Outcome | Observable change and who benefits |
| Context | Existing behaviour, source links and constraints that affect the change |
| Behaviour | Concrete success, rejection and boundary cases |
| Acceptance | Observable results, including meaningful failure cases |
| Validation | Available check or experiment; distinguish planned from executed |
| Dependencies | Named blocked step and resume condition, with independent work that can continue |

Omit fields that add no useful information. Keep the task at the smallest coherent outcome; split independent outcomes when that improves ownership or verification. Avoid prescribing a folder structure or implementation sequence unless the local architecture or fragility warrants it.

## Preserve action through uncertainty

An unrun compatibility check can belong in the task. Record what it must establish, how to run it and which later claim depends on it. A demonstrated incompatibility needs a bounded fix or reconsideration. Missing external authority constrains that action, not unrelated preparation.

Prefer “Build the authorised adapter and check one local client event before claiming desktop compatibility” to a blanket conclusion that the untested adapter is unsuitable. Keep any actual permission boundary intact.

## Acceptance examples

For a membership check, state what a member may do, what a non-member observes and where the authoritative membership decision is made. Authentication alone must not silently become project access. Use the actual project's contract rather than importing this invented example as its design.

For a handoff, include current state, the next executable step, where evidence lives and the exact condition that would require a decision. Do not make another worker reconstruct the task from an activity log.

## Preserve the condition in the task

Invented source contract: workspace members may export the last 30 days as CSV. “Add report exports” hides the membership, period and format conditions. A useful task names the permitted action and includes acceptance checks for a member request and a request outside the permitted membership, period or format. Link the actual contract; this example does not establish access rules for another project.

An open performance measurement can become a validation step. It should not silently remove an authorised implementation outcome or be rewritten as a successful measurement.

## Sources and local adaptation

This task and handoff pattern is a local synthesis. The downloaded [Good Docs how-to guidance](https://gitlab.com/tgdp/templates/-/tree/main/how-to) informs goal and completion-oriented structure, but it is not a ticket template or a mandated delivery process. Observable acceptance, precise blockers and continued authorised work are local requirements.
