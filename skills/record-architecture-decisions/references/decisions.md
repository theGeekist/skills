# Record one consequential decision

Use the repository's existing architecture decision record (ADR) format and status vocabulary. This minimal structure draws on ADR and MADR practice; it is a local writing pattern rather than a mandatory framework sequence.

## Reader route

State the decision and status near the beginning. Explain the problem, important constraints and consequences before optional implementation detail. A reader outside engineering should understand what changes and why. An engineer should find the governing contracts and alternatives directly.

| Part | Question |
| --- | --- |
| Decision and status | What choice was made or is being proposed? |
| Context and drivers | What concrete problem, constraints and priorities shaped it? |
| Options | Which viable alternatives were considered and why? |
| Consequences | What benefits, costs, risks and operating responsibilities follow? |
| Evidence and revisit conditions | What supports the decision, what remains to check, and what observation would change it? |

Preserve the reasoning behind alternatives. Do not invent discarded options or retrofit certainty to make a recorded decision look inevitable. When asked to explain an accepted ADR, explain its actual choice; do not silently reopen it.

## Decisions under uncertainty

Separate design choice, implementation state and validation. A prototype choice can be made with a bounded experiment still pending. Record the expected observation and reconsideration condition. Lack of prior measurement does not automatically reject every candidate; demonstrated incompatibility can rule one out for a stated requirement.

Respect authority recorded by the project or user. State an external publication constraint precisely, while allowing authorised implementation and preparation to continue.

## Keep the choice and its evidence distinct

Invented example: “Per-project queues are proven to scale” overstates a prototype choice when load has not been measured. “Use a per-project queue for the prototype; measure the representative load before setting production limits” keeps the choice while preserving the evidence gap. Record the actual reason for isolation and the agreed reconsideration threshold. Do not invent either to make the decision look complete.

## Maintenance

Link sources and related decisions using meaningful text. Preserve historical records. Supersede or amend according to the repository's convention, documenting the changed reasoning rather than quietly rewriting history.

Use links that work at the intended destination: repository-relative links for a checked-in record, or pinned source URLs where the reader lacks that checkout. Avoid temporary evaluation paths. Explain specialist abbreviations such as FIFO (first in, first out) when they affect the reader's understanding, even in a short record. Honour a requested length by removing optional detail before removing a consequential constraint.

## Sources and local adaptation

[MADR](https://adr.github.io/madr/) supplies the context, options, outcome and consequences pattern; its minimal template was downloaded and inspected. This guide adapts that pattern to the existing project's ADR convention. Evidence/reconsideration guidance and continuation of authorised work are local additions, not a claim that MADR validates the chosen architecture.
