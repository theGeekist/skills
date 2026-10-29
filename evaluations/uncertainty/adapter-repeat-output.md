# Proposed revision: Evaluate the response-review adapter

**Status:** Ready for an authorised local prototype; desktop compatibility remains untested.

## Intended outcome

Build a reversible local response-review adapter on an exploratory branch and evaluate its parsing and continuation behaviour with the available subprocess harness. Record precisely what those checks establish and what still requires a real desktop client.

## Current implementation and evidence

The adapter has not been implemented. Documentation describes an event containing the latest response text and an indication of whether continuation has already been requested. That documented contract has not been tested in the target desktop client. The supplied scenario reports no failed desktop test or demonstrated incompatibility.

The local subprocess harness can send invented event JSON to a script and inspect standard output, standard error and exit status. This supports checks of the script against the chosen fixtures and documented contract. It cannot establish that the desktop client emits those events, invokes the script or honours its continuation response.

## Scope and boundaries

The user has authorised a reversible prototype on an exploratory branch and local tests. Publishing, changing account settings and production rollout are outside this task. Do not perform those actions to obtain evidence.

There is no installed target desktop client in this environment. Actual desktop execution is therefore unavailable here; it is not a prerequisite for local implementation or subprocess testing. Desktop compatibility must remain an open claim until a separate, appropriately authorised client check is possible.

## Work to perform

1. Translate the documented event and response contract into local fixtures. Record the documentation source and exact field names and output format when available; the supplied scenario does not provide those details. Mark any assumed contract details explicitly.
2. Define a terminology fixture with one explicit mismatch and its expected correction. Use an already agreed pair if available; otherwise label the pair illustrative and leave agreement as an open input to the final mismatch acceptance check. Parsing and continuation-guard preparation can proceed independently.
3. Implement the local adapter and run the subprocess harness for a clean response, the terminology mismatch and an event reporting that continuation has already occurred.
4. Record each fixture, expected result, actual output, standard error and exit status. Investigate or fix failures against the fixture contract before reporting the corresponding local criterion as passed.
5. Record desktop validation as pending and describe a future check without attempting installation, account changes or any other external action under this task.

## Acceptance criteria

- **Parsing:** Given a valid fixture representing the documented event, the adapter reads both the response text and the continuation indicator correctly. Preserve the input and observed result as evidence; do not present an assumed schema as an observed client payload.
- **Clean response:** Given text without the selected mismatch and an indicator that continuation has not occurred, the adapter requests no continuation.
- **Terminology mismatch:** Given the agreed mismatch and an indicator that continuation has not occurred, the adapter emits one continuation request containing the expected terminology correction, in the documented response format. Record the exact agreed pair and request. An illustrative pair alone does not establish agreement.
- **Continuation guard:** Given the mismatch with an indicator that continuation has already occurred, the adapter emits no further continuation request. The harness checks both indicator states so that suppression is distinguishable from an adapter that never requests continuation.
- **Evidence limits:** The report distinguishes implementation completed, local cases passed or failed, contract assumptions and desktop behaviour untested. Local subprocess results establish behaviour for the supplied inputs in this environment; they do not establish desktop integration or production readiness.

## Pending desktop check

The open question is whether the target desktop client supplies the documented event, invokes the adapter and honours its continuation response without repeating the correction. A later authorised check needs access to that client and a permitted reversible integration method. Completion evidence would include the client version, a captured event, the adapter response and observed continuation counts for a clean case, a mismatch case and the subsequent continuation event. Do not claim client compatibility before obtaining that evidence.

# Recommended next execution step

Begin the authorised local prototype by documenting the event/response fixture contract and preparing the three subprocess cases, then implement and run the adapter on the exploratory branch. Keep unknown schema details and terminology agreement explicit rather than inventing them. If an indispensable contract detail is unavailable, identify the exact affected assertion and missing input while continuing independent fixture and guard preparation.

Do not wait for desktop evidence to start this reversible local work. The missing client blocks actual desktop validation and a desktop-compatibility claim, while publishing, account changes and production rollout remain outside the authorisation. This recommendation describes future execution only; no implementation or external action has been performed for this revision.
