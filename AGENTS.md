# Working in this repository

Read CONTRIBUTING.md before changing the skills. Preserve their architecture decisions unless a change explicitly proposes otherwise.

Use the four outcomes in standards/writing.md: consistency, accessibility, readability and repeatability. Make technical material navigable by a reader outside engineering. Keep shared definitions in project references and explain new specialised terms at first use.

Edit standards/writing.md, standards/content-patterns.md and standards/uncertainty.md as the canonical sources. Run `python3 scripts/sync-language-references.py` after changing them, then `python3 scripts/sync-language-references.py --check` before committing.

Apply standards/uncertainty.md to tasks, decisions and handoffs. Record evidence gaps with their next action and completion evidence. Keep implementation progress and validation separate. Missing prior proof alone does not reject an option or halt authorised work; name actual blockers and their affected steps precisely.

Run `python3 -m unittest discover -s tests -v` for validator or adapter changes. Validate changed skills with the Agent Skills reference implementation where available. Test significant instruction changes on realistic tasks; distinguish agent review from human comprehension and runtime tests.

Keep private project evidence and source extracts out of this public repository. Record unavailable checks honestly. Do not install hook configurations or change global agent instructions as a side effect of installing a skill.
