# Per-project queues for report exports

**Status: chosen for the reversible prototype.** The team will use one queue per project so projects can be scheduled independently. Production scheduling limits remain undecided.

## Context and alternatives

The shared worker queue lets a large project's report exports delay smaller projects. Reducing this contention drives the choice.

- **Shared FIFO (first in, first out):** least setup, but project contention remains.
- **Per-project queues:** independent scheduling, with additional coordination. Chosen for the prototype.
- **Priority queue:** retains one queue, but requires an agreed priority policy.

## Consequences and validation

This adds coordination; its performance under representative load remains unmeasured. The notes record authorisation for the prototype and local tests, but do not establish implementation completion. Load tests have not run.

Next, implement the authorised local prototype. Exercise two concurrent projects in the harness and record whether a smaller project's exports progress while a larger project is busy. Run the representative load case and capture latency measurements before choosing production limits. Agree a numerical latency budget so those measurements can support a pass/fail judgement; no budget has yet been agreed. This does not prevent local implementation or measurement.

Revisit the prototype choice if the expected workload cannot meet that budget. Publication, deployment and external account changes remain outside scope.

Supporting detail: [queue discussion notes](adr-source.md).
