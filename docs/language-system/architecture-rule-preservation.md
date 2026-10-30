# Preserve architecture meaning while improving language

The backend and frontend playbooks define architecture rules, including defaults, permissions, exceptions and prescribed responses. Editorial changes can improve their organisation and wording while preserving those meanings. Changes to architectural requirements belong in an explicit architecture proposal rather than an unmarked copyedit.

## Compare against the governing source

The original comparison sources are retained in `standards/architecture-rules/` at the pre-language-system revision `fcbd5a9`. The source-integrity test protects those historical inputs; it deliberately permits improvements to active wording.

For each edited section, check:

- the force of the rule: requirement, prohibition, permission or preference;
- its conditions and exceptions;
- dependency direction and ownership;
- thresholds, signals and the response they require;
- whether a summary introduces a requirement absent from the detailed rule.

A passing hash or prose linter cannot establish semantic equivalence. Review the main instructions and their references together, then assess consistency, accessibility, readability and repeatability.

## Recorded review

The [language and meaning review](architecture-language-review.md) records the comparison coverage and checks. It corrected summary drift involving review urgency, locale presentation, shared boundaries and added frontend requirements. The active guidance preserves the original architectural distinctions while using clearer terms and concern-specific navigation.

The [initial architecture split](architecture-refactor.md) separately records the reference organisation and its bounded loading trials.
