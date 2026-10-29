# What llm-core supplies and who runs the work

`@geekist/llm-core` supplies portable contracts for AI applications, controls around consequential actions, and evidence of what happened. A host application chooses a runtime integration, which executes the work. Adopting the kernel therefore requires explicit integration and infrastructure choices; it does not supply a default agent loop or workflow executor.

Here, **kernel** means the common contract, control and evidence layer. **Conformance** means checking that an implementation follows those contracts. These responsibilities let applications share precise rules while choosing their execution integration.

The [package overview](https://github.com/theGeekist/llm-core/blob/4f9e37ac92bcd055a836806ea463510ed32a8bcc/packages/llm-core/README.md) describes a version 2 candidate requiring Node.js 22 or newer and says it is not yet published to npm. This account concerns that source revision, rather than independently checked registry availability. The accompanying [proposed terminology registry](llm-core-terminology.json) records source-derived meanings; its formulations have not been adopted by the source project.

## How portability preserves a clear boundary

A **portable contract** describes data that can cross implementations without carrying a live framework object or credential. Constrained TypeScript under `src/contracts` is the authoring authority; generated JSON Schema Draft 7 describes the exchanged data in a language-neutral format. Hand-editing a generated schema does not change the authoritative contract.

A **schema reference** (`SchemaRef`) combines an absolute identifier, semantic version and digest—a fingerprint of the exact published schema bytes. An **evidence reference** (`EvidenceRef`) identifies evidence and its content integrity through a storage-neutral resource reference. It contains no physical storage location and does not grant permission to disclose the content. The host still supplies authorised storage and retrieval. Namespaced JSON extensions preserve provider-specific data without making native runtime objects portable.

For the decision and exact fields, read [ADR-003: schema authority, identity and native extensions](https://github.com/theGeekist/llm-core/blob/4f9e37ac92bcd055a836806ea463510ed32a8bcc/packages/llm-core/docs/final-architecture/decisions/ADR-003-schema-identity.md), then the [schema contracts](https://github.com/theGeekist/llm-core/blob/4f9e37ac92bcd055a836806ea463510ed32a8bcc/packages/llm-core/src/contracts/schema.ts) and [schema-reference tests](https://github.com/theGeekist/llm-core/blob/4f9e37ac92bcd055a836806ea463510ed32a8bcc/packages/llm-core/tests/contracts/schema.test.ts).

## How an action earns permission to execute

Three concerns remain separate:

| Concern | Meaning and consequence |
| --- | --- |
| Effect class | Read-only, reversible, external-write, destructive or privileged. Reversible actions still require the controls for non-read-only effects. |
| Policy decision | A versioned rule returns allow, deny or require-approval. Requiring approval leaves a prerequisite outstanding. |
| Approval | An authenticated actor decides on the exact identified action within a valid time window. A changed action, mismatched identity or expired window invalidates approval. |

Policy and approval bind to an **action digest**, rather than the wording on an approval card. It covers normalised execution arguments, tool identity and version, input schema and other execution-affecting details. The digest uses HMAC-SHA-256: a hash-based message authentication code calculated with a secret key, scoped to the tenant or security domain. The key protects the binding of potentially sensitive inputs; it does not encrypt them. A display may redact arguments, while execution must remain bound to the authorised action.

Non-read-only effects require an **idempotency key**, identifying an operation across repeat requests, and a durable receipt journal with recorded control prerequisites before invocation. The host supplies policy, authentication, digest and journal **ports**: interfaces through which the kernel requests those implementations. These controls do not imply that every action always requires human approval.

Continue to [ADR-005: tool control and events](https://github.com/theGeekist/llm-core/blob/4f9e37ac92bcd055a836806ea463510ed32a8bcc/packages/llm-core/docs/final-architecture/decisions/ADR-005-tool-control-events.md), the [policy implementation](https://github.com/theGeekist/llm-core/blob/4f9e37ac92bcd055a836806ea463510ed32a8bcc/packages/llm-core/src/features/control/policy.ts) and [approval verification](https://github.com/theGeekist/llm-core/blob/4f9e37ac92bcd055a836806ea463510ed32a8bcc/packages/llm-core/src/features/control/approval.ts). The [policy tests](https://github.com/theGeekist/llm-core/blob/4f9e37ac92bcd055a836806ea463510ed32a8bcc/packages/llm-core/tests/control/policy.test.ts) and [approval tests](https://github.com/theGeekist/llm-core/blob/4f9e37ac92bcd055a836806ea463510ed32a8bcc/packages/llm-core/tests/control/approval.test.ts) cover approval-required status, changed action digests, identity mismatches and expired approval windows.

## How the system records an uncertain outcome

A **tool execution receipt** records lifecycle progress. Its **effect disposition** separately records what is known about the external change. For example, an exception after `started` can leave the lifecycle `indeterminate` and disposition `unknown`; it does not establish that nothing happened. Cancellation after start remains a request until a known outcome is acknowledged.

The **receipt journal** is the authoritative durable record. It records reservations atomically—as one indivisible operation—along with transition history, revisions and temporary fenced ownership. **Fenced ownership** gives one temporary execution owner a journal-issued token; earlier tokens are invalid, so an outdated owner cannot record transitions as the current owner. An event sink receives redacted facts for observation and cannot replace that journal.

An idempotency reservation uses the complete current combination of security domain, optional tenant, tool ID, tool version and idempotency key. Repeating that combination with a different action digest conflicts.

**Receipt reconciliation** asks an integration to establish the external outcome from attributable evidence. It avoids blindly re-running a started or ambiguous action. If the result remains unresolved, the receipt retains that uncertainty and can require further reconciliation. This helps operators recover without accidentally duplicating an external write.

The [receipt contracts](https://github.com/theGeekist/llm-core/blob/4f9e37ac92bcd055a836806ea463510ed32a8bcc/packages/llm-core/src/features/evidence/receipt.ts) define lifecycle, disposition, ownership and reconciliation. The first [receipt-reconciliation test](https://github.com/theGeekist/llm-core/blob/4f9e37ac92bcd055a836806ea463510ed32a8bcc/packages/llm-core/tests/application/tool-execution/receipt-reconciliation.test.ts) recovers a stale indeterminate receipt from external evidence while keeping execution count at one. These tests were inspected as source; they were not executed for this language pilot.

## What this means for adoption

Describe llm-core as the portable contract, conformance, authority and evidence layer. Describe a runtime as supported only when the evidence qualifies that exact integration. [ADR-016: integration-owned execution](https://github.com/theGeekist/llm-core/blob/4f9e37ac92bcd055a836806ea463510ed32a8bcc/packages/llm-core/docs/final-architecture/decisions/ADR-016-integration-owned-execution.md) keeps the local runner as private conformance evidence and gives execution to host-selected integrations. Importing or compiling a specification does not authorise execution.

One source discrepancy remains: ADR-005's reservation-uniqueness summary omits `securityDomain`, which the current `ToolReceiptReservationKey` and equality check include. This explanation follows the complete source contract and makes the difference visible; it does not amend the project's decision.

This pilot is an evaluation-coordinator revision of an agent-authored explanation. It addresses the reader's terminology and navigation findings. The revised version has not received a new blind-reader or human comprehension test; earlier outcomes remain recorded in the [project evaluation](../../../docs/language-system/project-evaluation.md).
