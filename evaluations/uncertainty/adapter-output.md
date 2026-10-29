# Proposed revision: Evaluate the response-review adapter

Build a reversible local prototype and use the available subprocess harness to check its response-review behaviour. Record desktop compatibility as an open question until it can be observed in the target client.

**Status:** Ready for authorised local prototyping; implementation and tests have not started.

## Context and current evidence

The current implementation does not exist. The supplied task reports documentation describing an event with the latest response text and an indication of whether continuation has already been requested. That description supports designing a prototype; it does not establish the actual event shape or behaviour in the target desktop client.

The local subprocess harness can send invented event JSON to a script and inspect its standard output, standard error and exit status. No target desktop client is installed in this environment. No local or desktop test results have been supplied, and there is no demonstrated runtime failure that disqualifies the adapter.

The user has authorised a reversible prototype on an exploratory branch and local tests. Publishing, account-setting changes and production rollout remain outside this task.

## Expected behaviour and local acceptance examples

Use the documented payload and response contract when preparing fixtures. Record the exact fields and output format used so the local results can be reproduced. Do not present invented JSON as a captured desktop event.

Before testing terminology correction, record an agreed mismatch and its preferred wording. The following examples specify the required behaviour without inventing a project terminology rule:

- A valid event containing the latest response text and the continuation indicator is parsed correctly; the test confirms the values used by the adapter.
- A response containing the agreed terminology mismatch, with continuation not already requested, produces one continuation request according to the documented output contract. The request identifies the correction needed.
- A response containing the same mismatch, with continuation already requested, produces no further continuation request.
- A response using the agreed preferred wording produces no continuation request.

Capture the fixture, expected result, actual standard output, standard error and exit status for each case. A failing case is a finding to diagnose and fix or to use in a specific design decision; it is not a basis for claiming local acceptance.

## What completion establishes

Complete the local prototype milestone when the implementation exists, the cases above pass in the subprocess harness, and the evidence record states the tested contract and its limits.

Passing these checks would establish the script's behaviour for the supplied synthetic inputs in the local subprocess environment. It would not establish that the desktop client emits those inputs, invokes the script, accepts its output or performs a continuation. Desktop compatibility and end-to-end continuation behaviour remain unverified.

## Remaining uncertainty and exact blockers

Desktop validation is blocked by the absence of the target client. That blocks a desktop compatibility claim, not local implementation or harness tests. When a target client is available and a client experiment is separately authorised, record its version, capture a real event and verify a clean response, a mismatch requiring one continuation, and a subsequent event that produces no repeated continuation. Compare the observed event and output handling with the prototype contract before claiming compatibility.

An agreed terminology pair is required for the terminology acceptance case. If it is not yet specified, continue preparing the parser and harness cases while obtaining that input; do not silently treat an illustrative pair as an accepted project rule.

Publishing, account-setting changes and production rollout must not be performed under the existing authorisation. A passing local check does not expand that authorisation.

# Recommended next execution step

In a subsequent implementation task, begin the authorised exploratory-branch prototype by translating the documented event and output contract into explicitly synthetic harness fixtures, recording the agreed terminology pair, and implementing the smallest script needed to exercise the acceptance cases. Run the cases and report the actual results with the limited claim they support. Keep desktop validation as a separate pending step; do not wait for desktop evidence before doing the independent local work.

This revision and recommendation are analysis only. No implementation, tests, client interaction or external actions were performed for this review.
