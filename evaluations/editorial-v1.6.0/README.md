# Bounded editorial task trials

Two fresh-context workers used isolated copies of the changed skills and only the supplied invented case files. They were asked to complete ordinary writing/review work. The author assessed their outputs against the supplied facts; this was not a native client activation test, a human comprehension study or a competitor benchmark.

## Replay the setup

Copy `review-project-language` from the v1.6.0 collection into the `review/` case directory and `write-marketing-content` into `marketing/`. The staged Markdown hashes are in `instruction-hashes.json`. The skill directory is deliberately not duplicated in this evaluation record. Its links in the raw outputs refer to that replay layout.

Review prompt:

> Use the review-project-language skill in this directory to review task.md, interface.md and marketing.md against source.md. Apply the corrections. Give a compact revision record showing consequential edits and their reasons. Save corrected files separately with '-revised' suffix and response.md containing findings/revision record. Do not read outside this directory. Do not send or publish anything.

Marketing prompt:

> Use the write-marketing-content skill in this directory and source.md to write a short launch paragraph for independent consultants, plus a clear call to action. Use a warm, lightly witty voice. Keep any supporting claim notes outside the finished customer copy. Save response.md. Do not read outside this directory or publish anything.

The executed prompts also specified their absolute isolated working directories. The prompts above preserve the task wording without requiring that original workspace path.

## Observed outputs

The [review response](review/response.md) distinguishes document-check approval from purchase confirmation, removes public-profile promises and preserves the authorised local prototype. It records the untried mail-provider check without inventing validation or permission to send external invitations. Its compact table exposes original wording, corrections, reasons and source constraints. No implementation tests were run by that worker.

The [marketing response](marketing/response.md) retains laptop operation, workspace-owner access and selected-note Markdown export, with a light stylistic aside. It avoids invented time-saving, reliability and public-signup claims and keeps supporting claim notes separate. It includes absent collaboration/cloud features as suitability constraints; that is an editorial choice, not a requirement to enumerate absent features in every campaign.

These cases show the requested behaviour on the supplied examples. They do not establish universal reliability, originality relative to all writing skills, measurable SEO benefit or superiority to competitors.
