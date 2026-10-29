# ADR: Prepare the model-specific prompt package for release review

Status: Proposed

## Decision

Prepare a release candidate locally, validate the available fixtures, package it and draft release notes. A release candidate is a package prepared for review; it is not a published or model-validated release. Prepare model evaluation instructions so the missing evaluation can run when credentials are available.

Do not publish to the public catalogue. External publication is outside the user's authorisation and the catalogue cannot undo an initial publication. Local preparation can continue without either publication permission or model credentials.

## Context and current evidence

The complete scenario is recorded in [the supplied ADR](publishing-adr.md).

The prompt package has been written. Unit fixtures pass through a local parser. This supports the narrow claim that those fixtures pass that parser; it does not establish the package's behaviour on the named model. No evaluation has run against that model, and this environment has no model credential. The absence of that evaluation is an evidence gap, not a demonstrated failure or a basis for declaring the package unsafe.

No deployed package currently exists. A local packaging command is available, but the scenario does not report a completed release candidate or packaging result. The user has authorised local release preparation, fixture validation, packaging and release-note drafting. They have not authorised external publication under the organisation's name.

## Alternatives and trade-offs

| Option | Assessment |
| --- | --- |
| Prepare a local release candidate and evaluation instructions | Chosen. Produces a reviewable package within the authorised scope and makes the remaining evidence gap explicit. Requires later model evaluation before claiming model behaviour has been validated. |
| Defer all work until credentials are available | Leaves useful authorised preparation undone. Credentials are needed to run the model evaluation, not to prepare the package and its evaluation instructions. |
| Abandon the package now | Not supported by an unrun evaluation. Reconsider if subsequent checks demonstrate failures that cannot reasonably be corrected or the user withdraws the work. |
| Publish now and evaluate afterwards | Not permitted. Publication lacks user authorisation and an initial publication cannot be undone. Gathering evidence later does not resolve that boundary. |

## Remaining questions and completion evidence

| Observation or gap | Practical implication | Bounded next action and completion evidence |
| --- | --- | --- |
| Existing fixtures pass the local parser; the release candidate has not been reported as packaged | Local test results must be associated with the candidate under review | Run the available local parser tests, record their command and results, then run the packaging command. Record its outcome and the resulting artefact's identity and contents. If a check fails, retain the failure and investigate its effect before claiming that check passed. |
| Named-model behaviour has not been evaluated | Model-specific effectiveness and readiness remain unestablished | Prepare instructions identifying the candidate, named model, evaluation cases, expected behaviours, acceptance criteria and result-recording method. Record criteria requiring a later decision instead of inventing them. When credentials are available, run the evaluation and retain actual outputs and a pass/fail assessment against the recorded criteria. Preparing instructions alone does not validate model behaviour. |
| Release notes have not been reported as drafted | Reviewers need an accurate account of scope and limits | Draft notes identifying what the package contains, the local checks actually completed, and the unrun model evaluation. Completion evidence is a reviewable draft with no unsupported model-validation or publication claims. |

## Actual blockers and resume conditions

Running the named-model evaluation is blocked by the missing credential. It can resume when an appropriate credential is available in an authorised evaluation environment; preparing its instructions can proceed now.

Public catalogue publication is blocked by missing explicit user authorisation. It must remain stopped unless the user authorises that external action for the concrete candidate, with the irreversible initial publication understood. Model evaluation results do not themselves grant publication permission. This ADR does not establish publication readiness or assume later approval.

## Consequences and reconsideration

The team can produce a locally checked, packaged candidate and reviewable release notes without pretending the model evaluation has passed. Local parser success and packaging success remain distinct from model behaviour and public release status.

Revisit the candidate if local checks or later model evaluation reveal material failures: record the observed behaviour and decide whether to correct the package, narrow its claims or discontinue it based on that evidence. Revisit publication only when the candidate, evaluation evidence or explicit unresolved limits, and the user's publication decision are available.

## Recommended next execution step

In a subsequent authorised execution task, run the available local parser tests and record the command and outcome for the candidate. If they pass, run the packaging command and capture its result and artefact identity; then draft release notes and the model evaluation instructions with the limits above. If a check fails, report the concrete failure and investigate it while continuing independent documentation preparation where useful.

The review package is complete when it contains the identified artefact, local validation and packaging results, draft release notes, and reproducible model evaluation instructions with unresolved criteria clearly marked. Stop before any external publication. Do not claim named-model validation without a completed evaluation.

This document proposes the revision and next task only. No parser tests, packaging, model evaluation or external actions were performed for this revision.
