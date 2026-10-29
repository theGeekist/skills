# Actionable uncertainty in tasks and decisions

These invented examples illustrate reasoning and structure. They are not evidence about a real adapter, release or project.

## Task

**Outcome:** Exercise the adapter in one local client session.

**Current position:** Payload tests pass. Local client behaviour has not been observed.

**Next action:** Build the authorised local prototype, capture the client's event payload and run one correction case. Keep the registration reversible.

**Completion evidence:** Record the client version, event and observed continuation count. A clean case finishes; an alias case requests one correction; the correction turn finishes.

**Boundary:** Claim local client compatibility only after that observation. Continue the prototype and test preparation now.

## Decision record

**Decision:** Use the proposed parser for the bounded prototype.

**Context:** Existing examples show the required input shape. Malformed-input behaviour is still to be tested.

**Alternatives:** Compare extending the current parser with adopting the candidate. Record the actual maintenance and integration costs.

**Consequences:** Keep malformed-input tests in the implementation task. Revisit the decision if the parser cannot return the required structured error without losing input position.

An untested error path creates validation work. It does not, by itself, establish that the candidate is unsuitable.

## Handoff with a genuine blocker

**Prepared:** The release artefact and local verification record.

**Blocked action:** Publishing, pending the required maintainer approval.

**Continue now:** Finish the authorised release notes and reproducibility checks.

**Resume condition:** Approval recorded for the prepared release. Keep external publication separate from local preparation.
