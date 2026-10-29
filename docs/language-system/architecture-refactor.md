# Architecture skill context split

The backend and frontend skills now keep the decision rules in a short core and load detailed material according to the concern being decided. Each skill remains independently installable: every linked reference lives inside its skill directory. Existing architecture boundaries and metadata names are retained.

## Context cost

Counts use whitespace-separated words including frontmatter. The final backend core is 907 words and the frontend core is 979 words, including the same 144-word generated baseline. These counts are an authoring checkpoint, not token measurements.

| Skill | Original main file | Final core with shared baseline | Detailed references |
| --- | ---: | ---: | ---: |
| Backend architecture | 2,411 | 907 | 1,684 |
| Frontend architecture | 2,198 | 979 | 1,494 |

A narrow task loads the core plus its relevant reference or section, rather than every example and checklist. A complete architecture review explicitly reads all three references. Its total context is slightly larger than the old monolith because the decision core repeats essential rules; this change reduces initial and task-selective loading, not every possible request. Byte/word counts do not establish a host token count or actual loading behaviour.

## Preserved section mapping

The following 24 detailed sections were copied verbatim into local references. Core rules summarise their invariant boundaries, while the routing table requires the detailed reference before deciding or changing the relevant concern.

### backend-slice-architecture

| Original section | New reference |
| --- | --- |
| File naming and nesting | [`placement-and-contracts.md`](../../skills/backend-slice-architecture/references/placement-and-contracts.md) |
| Key concepts | [`placement-and-contracts.md`](../../skills/backend-slice-architecture/references/placement-and-contracts.md) |
| Rules for decisions | [`placement-and-contracts.md`](../../skills/backend-slice-architecture/references/placement-and-contracts.md) |
| Delivery channels | [`placement-and-contracts.md`](../../skills/backend-slice-architecture/references/placement-and-contracts.md) |
| Internationalisation and configuration | [`placement-and-contracts.md`](../../skills/backend-slice-architecture/references/placement-and-contracts.md) |
| Capability public surface contract | [`placement-and-contracts.md`](../../skills/backend-slice-architecture/references/placement-and-contracts.md) |
| Workspace mapping | [`workspace-and-migration.md`](../../skills/backend-slice-architecture/references/workspace-and-migration.md) |
| Illustrative folder shapes | [`workspace-and-migration.md`](../../skills/backend-slice-architecture/references/workspace-and-migration.md) |
| Evolution model | [`workspace-and-migration.md`](../../skills/backend-slice-architecture/references/workspace-and-migration.md) |
| Amber / red flags | [`review.md`](../../skills/backend-slice-architecture/references/review.md) |
| Sizing rules | [`review.md`](../../skills/backend-slice-architecture/references/review.md) |
| Review/refactor checklist | [`review.md`](../../skills/backend-slice-architecture/references/review.md) |

### frontend-slice-architecture

| Original section | New reference |
| --- | --- |
| File naming and nesting | [`placement-and-contracts.md`](../../skills/frontend-slice-architecture/references/placement-and-contracts.md) |
| Folder guidance | [`placement-and-contracts.md`](../../skills/frontend-slice-architecture/references/placement-and-contracts.md) |
| Public import guidance | [`placement-and-contracts.md`](../../skills/frontend-slice-architecture/references/placement-and-contracts.md) |
| Rules for decisions | [`placement-and-contracts.md`](../../skills/frontend-slice-architecture/references/placement-and-contracts.md) |
| State guidance | [`placement-and-contracts.md`](../../skills/frontend-slice-architecture/references/placement-and-contracts.md) |
| Multi-platform rule (web/native) | [`placement-and-contracts.md`](../../skills/frontend-slice-architecture/references/placement-and-contracts.md) |
| Internationalisation and configuration | [`placement-and-contracts.md`](../../skills/frontend-slice-architecture/references/placement-and-contracts.md) |
| Feature public surface contract | [`placement-and-contracts.md`](../../skills/frontend-slice-architecture/references/placement-and-contracts.md) |
| Existing monorepo adaptation | [`workspace-and-migration.md`](../../skills/frontend-slice-architecture/references/workspace-and-migration.md) |
| Illustrative folder shape for a larger feature | [`workspace-and-migration.md`](../../skills/frontend-slice-architecture/references/workspace-and-migration.md) |
| Amber / red flags | [`review.md`](../../skills/frontend-slice-architecture/references/review.md) |
| Review/refactor checklist | [`review.md`](../../skills/frontend-slice-architecture/references/review.md) |

The old purpose, authority/adaptation, conceptual introduction, ownership and strong defaults remain in the decision core in condensed form. The old navigation list is replaced by concern-specific loading routes. Communication expectations are supplied by the generated shared baseline and a short recommendation prompt. Exact metadata names, activation descriptions, licence and author metadata are unchanged.

## Checks and forward test

Both skills pass the Agent Skills reference validator. Local reference targets resolve, and a section-content comparison confirms all 24 moved sections remain verbatim. The packaging suite checks that a copied skill can resolve its references without repository siblings.

An independent worker applied both provisional refactored skills to an invented backend/frontend scenario; its prompt, output, read record and assessment are retained under [`evaluations/architecture-split`](../../evaluations/architecture-split/). The broad provisional review retained boundary rules and read all relevant references. A second final-core request read only the backend core and workspace reference, returning the correct brief answer. The tasks use explicit skill paths to test behaviour and reference loading after selection. They do not test natural host activation, another vendor runtime or human marketing comprehension. See the assessment for the first trial's baseline/hash limitations.
