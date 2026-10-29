# Use per-project queues for the report-export prototype

**Status: chosen for a reversible prototype.** Production scheduling limits remain undecided.

The shared worker queue lets a large project's report exports delay smaller projects. Per-project queues provide independent scheduling, with additional coordination as the tradeoff. Whether this design meets expected demand still requires measurement.

## Alternatives considered

- **Shared FIFO (first in, first out) queue:** least setup, but contention between projects remains.
- **Per-project queues:** independent scheduling, with additional coordination; chosen for the prototype.
- **Priority queue:** retains one queue, but requires an agreed priority policy.

## Next step and validation

Implement the authorised local prototype and use the local harness to exercise two concurrent projects. Record export latency and whether a large project delays the smaller project's exports. The source notes establish the choice and authorisation; they do not establish implementation or successful validation. Load tests have not run.

Agree a numerical latency budget and run the representative load case before choosing production limits. Use the measured results against that budget as completion evidence. Revisit the prototype decision if the expected workload cannot meet the agreed budget. The missing budget prevents a pass/fail judgement, but does not block the authorised prototype or local tests.

Publication, deployment and external account changes are outside scope.

Supporting context: [queue decision discussion notes](adr-source.md).
