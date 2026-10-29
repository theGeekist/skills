# Recommendation

Keep the existing teams of responsibilities side by side, and move the instructions that coordinate them into one clear place. Checkout should not become the owner of everything in commerce, and Editor should not become the owner of Assets merely because it uses them.

For a marketing colleague: Inventory answers stock questions and manages reservations; Checkout validates orders; Payments handles payment rules. One shared workflow should tell those teams when to act. Both the website server and background worker can then follow the same instructions, reducing the chance that an order behaves differently depending on how it arrives. In the web app, the page should coordinate choosing an asset and saving a document. A shared button should display and accept clicks, while the feature owns what saving means. These targeted changes make behavior easier to find and change without a disruptive folder reshuffle.

The main distinction is **using a public service versus directing a multi-step process**. A narrow public query or picker dependency is reasonable. Sequencing reservation and payment, or picking and saving, belongs at the composition boundary. Folder names alone do not establish that boundary.

## Backend boundaries

- Keep `libs/commerce/checkout` and `libs/commerce/inventory` as peers. Preserve the existing commerce grouping. Confirm Payments' actual location and ownership before choosing its import path; none was supplied.
- Retain Checkout's narrow call to Inventory's public stock-eligibility query when it is simply an input to Checkout validation. Do not ban every sibling import. If that call grows into coordination, move that coordination out.
- Extract the reservation/payment sequence currently inside Checkout and copied by `packages/http-server` and `packages/worker` into one shared application/use-case/workflow surface following existing conventions. Both runtimes call it. If no such surface exists, introduce the smallest shared workflow library under an established root; its exact name is a repository decision, not a reason to rename all projects.
- Keep inventory eligibility/reservation rules in Inventory and payment capture rules in Payments. The shared workflow owns sequence and cross-step failure handling, including retry, idempotency and compensation decisions where required. It must not become a container for all commerce rules.
- Keep runtime request/message mapping, startup, dependency composition and configuration in the two runtime entrypoints. Keep `libs/platform/storage` as approved agnostic infrastructure if inspection confirms it contains no commerce rules.
- Give capabilities small public commands, queries, boundary data types and optional events. Keep persistence models, internal helpers and volatile implementation types private. A workflow is business-specific application code, not a generic storage utility.

## Frontend boundaries

- Keep `modules/editor` and `modules/assets` as peers. Their existing names express the required boundaries; no conversion to `features/` is necessary.
- Editor may use the Assets public picker as a narrow UI dependency. Move the sequence “pick asset, then save document” into the relevant existing `pages` composition surface. Assets still owns picking behavior; Editor owns document state and save rules. Pass results and events explicitly through their public interfaces.
- Remove save/retry workflow ownership from `shared/ui/SaveButton`. Put document-saving behavior and its retry rules inside Editor; let the page sequence feature actions. The shared button may accept a callback and pending/error presentation data and hold local interaction state. If it is inherently document-specific, make that wrapper Editor-local instead.
- Keep components, hooks, API mapping and state local to their owning feature by default. Do not globalize everything. Promote only a stable, agnostic abstraction demonstrated in two or more features, with repeated-edit friction and a clear correctness/consistency benefit. Global state must likewise be demonstrably cross-feature.
- Prepare for native through stable feature interfaces and reusable feature behavior. Add platform variants only when needed; different web/native page or screen composition is acceptable. A future native client alone does not justify a global hook layer or a shared page abstraction now. A thin cross-platform composition helper can be considered if actual shared sequencing later warrants it.
- Keep Editor and Assets copy with those features, and truly generic component copy with its component. Compose locale and configuration in the app shell and use locale-aware formatting even with one English locale. Backend machine codes stay language-neutral; delivery owns localized presentation while capabilities own meaning.

## What can proceed and what needs checking

Proceed with a targeted plan to consolidate the duplicated backend workflow, relocate frontend sequencing and SaveButton's feature logic, preserve peer boundaries and current roots, and introduce mechanical import checks. Migrate affected code when touched. Do not couple this work to a wholesale `apps/` plus `packages/` migration or blanket sibling-import ban.

Before implementation, inspect repository instructions, workspace metadata, framework conventions, public entrypoints and the actual dependency graph. Check whether the apparent peers are independently owned, where an existing orchestration surface lives, whether duplicate workflows have diverged, and whether storage is genuinely agnostic. Verify the picker call's actual scope. Check payment/reservation ordering, partial failures, cancellation, compensation and retry contracts with the owning capabilities. The supplied facts do not settle these policies or prove any deep import currently exists.

## Verification and completion

Add ecosystem-appropriate lint/build/architecture checks for public-surface imports and forbidden cross-boundary deep imports, with approved infrastructure dependencies. Path aliases alone are not enforcement. Cover alternate import paths so relative imports cannot bypass the policy. Allow the deliberate narrow public dependencies above; prevent runtime or shared UI code from reaching private state and models. Introduce checks for touched boundaries first and inventory existing violations so migration remains reviewable.

Run public-contract and capability tests plus workflow integration tests proving both runtimes invoke the same orchestration. Exercise reservation rejection, payment failure after reservation, duplicate delivery and retries according to the agreed contracts; verify any required compensation. On the frontend, test pick/cancel/save, save failure/retry, state ownership and the button callback/presentation contract. Run applicable type, lint, build and UI checks. Review the resulting dependency graph and confirm pages/workflows remain thin and shared UI contains no document workflow rules.

No source was inspected or changed and no tests were run: this is a recommendation based only on the invented facts. There is no supplied size evidence requiring additional splits.

These decisions follow the backend and frontend [placement/contracts](../../skills/backend-slice-architecture/references/placement-and-contracts.md) ([frontend](../../skills/frontend-slice-architecture/references/placement-and-contracts.md)), [workspace/migration](../../skills/backend-slice-architecture/references/workspace-and-migration.md) ([frontend](../../skills/frontend-slice-architecture/references/workspace-and-migration.md)), and [review rules](../../skills/backend-slice-architecture/references/review.md) ([frontend](../../skills/frontend-slice-architecture/references/review.md)). Repository paths above are supplied facts, not inspected code links.
