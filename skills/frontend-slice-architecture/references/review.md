# Review signals and checklist

Read these original rules before deciding or changing this concern.

## Amber / red flags

Amber (watch):

* a simple UI change touches multiple features,
* scenes start accumulating business rules,
* duplicate hooks appearing across features,
* imports begin reaching into feature internals,
* onboarding feedback says “hard to find where behaviour lives”.

Red (act now):

* deep imports across features become normal,
* a scene becomes a “god file” (route + rules + state + UI),
* shared components start carrying feature workflow logic,
* global hooks become a dumping ground,
* features exceed size thresholds and become mini-monoliths.

Standard responses:

* duplication -> promote once abstraction is obvious,
* oversized feature -> split into sibling features,
* oversized scene -> push rules/state back into features; keep scene thin,
* deep imports -> enforce public surfaces and refactor immediately.

## Review/refactor checklist

1. Start every new behaviour in a feature.
2. Verify each feature exports a clear `index.*` public API.
3. Remove deep imports and replace with public-surface imports.
4. Keep route/page composition in scenes only; keep scenes thin.
5. Promote shared hooks/components only when repetition is painful.
6. Split oversized features/scenes before they become team bottlenecks.
7. Keep shared components free of feature workflow rules.
8. Preserve package-readiness: stable imports, clean boundaries.
