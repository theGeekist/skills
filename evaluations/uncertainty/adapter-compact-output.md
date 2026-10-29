# Evaluate the response-review adapter

Status: Planned; desktop compatibility untested.

Build the authorised reversible prototype on an exploratory branch. No implementation exists. Documentation describes response text and a prior-continuation flag; the desktop event contract remains unverified.

Acceptance: use invented JSON in the local subprocess harness to show correct parsing, one continuation request for a specified terminology mismatch when continuation has not occurred, and no repeated request when it has. Capture inputs, stdout, stderr and exit status against expected results. Report failures explicitly. These checks establish behaviour for supplied payloads only.

Desktop validation is blocked by the absent target client. When available, capture a real event and verify parsing and one-time continuation before claiming desktop compatibility. Publishing, account changes and production rollout remain outside scope.

Next execution step: define the terminology fixture and expected harness outputs, then implement and test the prototype within existing authorisation.
