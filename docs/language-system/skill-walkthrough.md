# A walkthrough of the eleven skills

Use a skill for the work in front of you: establishing a meaning, recording a decision, explaining a system or writing a product message. The collection shares a language baseline, while each skill has its own purpose and sources. You can use one skill without running an eleven-step process.

This guide connects each skill to its inspiration and a concrete request. For the underlying research, follow the [original research](research-baseline.md), [framework evaluation](framework-evaluation.md) and [source manifest](sources.json). The [evidence map](../../standards/framework-evidence.md) distinguishes reviewed guidance, downloaded templates, local decisions and sources that were considered but deferred.

## Find the work you need

| Your immediate question | Start with |
| --- | --- |
| What does this project mean by this term? | [Establish project language](#establish-project-language) |
| What can we do while a claim remains untested? | [Advance with uncertainty](#advance-with-uncertainty) |
| What should the next worker implement? | [Write implementation tasks](#write-implementation-tasks) |
| Why did we choose this approach? | [Record architecture decisions](#record-architecture-decisions) |
| How should we explain or document it? | [Write technical documentation](#write-technical-documentation) |
| How do we explain its value to customers? | [Write marketing content](#write-marketing-content) |
| What should the product say at this moment? | [Write interface content](#write-interface-content) |
| Where has our language become inconsistent or difficult? | [Review project language](#review-project-language) |
| Where should backend behaviour and coordination belong? | [Backend slice architecture](#backend-slice-architecture) |
| Where should interface behaviour and page composition belong? | [Frontend slice architecture](#frontend-slice-architecture) |
| Which writing workflow fits this request? | [Choose a project-writing workflow](#choose-a-project-writing-workflow) |

## Establish project language

[`establish-project-language`](../../skills/establish-project-language/SKILL.md) discovers meanings from the actual project before choosing names. Domain-driven design's [bounded contexts](https://martinfowler.com/bliki/BoundedContext.html) inform meaning within an area of work. [SKOS](https://www.w3.org/TR/skos-reference/) informs distinctions between concepts and their labels; [Good Docs terminology guidance](https://gitlab.com/tgdp/templates/-/tree/main/terminology-system) informs maintainable records. The repository's JSON registry is a local adaptation, rather than a formal SKOS implementation.

**Example request:** “Code says reservation, the help page says booking, and support uses registration. Find out whether they mean the same thing.”

The useful result is a small account of the concepts, contexts, aliases and source evidence. Unresolved meanings stay visible as proposals. Finding a term in code establishes its use, rather than automatically establishing its acceptance. Follow [the bundled writing and source guidance](../../skills/establish-project-language/references/writing.md).

## Advance with uncertainty

[`advance-with-uncertainty`](../../skills/advance-with-uncertainty/SKILL.md) implements [@pipewrk](https://github.com/pipewrk)'s requirement that honest evidence language should enable the next useful action. It is a local workflow, rather than an imported uncertainty framework.

**Example request:** “The ticket says mobile compatibility is unproven. Rewrite it so a worker knows what to build and check.”

The result separates implementation state from evidence state: build the authorised part, run a bounded compatibility check and record its observation before claiming compatibility. A demonstrated failure or missing permission still constrains its dependent action. The skill preserves those boundaries while avoiding a blanket stop. Read [the conventions and their origin](../../skills/advance-with-uncertainty/references/uncertainty.md).

## Write implementation tasks

[`write-implementation-tasks`](../../skills/write-implementation-tasks/SKILL.md) turns an intended outcome into work another person or agent can execute. Its task pattern is a local synthesis. [Good Docs how-to guidance](https://gitlab.com/tgdp/templates/-/tree/main/how-to) informs attention to goals and successful completion; it does not supply a compulsory ticket process.

**Example request:** “Write a task to let a customer cancel a booking, using our current cancellation policy.”

The result identifies the observable behaviour, relevant existing contract, acceptance examples and validation. It names any genuinely blocked step and what would let it resume. A worker should find the next executable action without reconstructing a chat history. The [task pattern](../../skills/write-implementation-tasks/references/tasks.md) explains the structure and its sources.

## Record architecture decisions

[`record-architecture-decisions`](../../skills/record-architecture-decisions/SKILL.md) records a consequential choice and its reasons. [MADR](https://adr.github.io/madr/) informs context, viable options, outcome and consequences. The skill keeps the project's existing decision format; evidence and reconsideration guidance are local additions.

**Example request:** “Record why we chose one cancellation workflow for the website and the background worker.”

The resulting architecture decision record, or ADR, distinguishes the choice from its implementation and validation. Readers can find what changes, why, which constraints mattered and what would warrant reconsideration. The author should preserve actual alternatives rather than inventing a debate to fill a template. See [decision-record patterns and sources](../../skills/record-architecture-decisions/references/decisions.md).

## Write technical documentation

[`write-technical-documentation`](../../skills/write-technical-documentation/SKILL.md) starts with the reader's purpose. [Diátaxis](https://diataxis.fr/start-here/) distinguishes learning, completing a task, looking up a contract and understanding a concept. Selected [Good Docs templates](https://gitlab.com/tgdp/templates) inform usable procedures and explanations. [arc42](https://arc42.org/overview/) supplies architecture views to consider when they answer the reader's question.

**Example request:** “Explain cancellation to product and support teams, and link the exact developer contract.”

The result leads with behaviour and consequences, explains necessary terms and gives engineers a direct route to technical detail. A separate customer how-to may be useful; creating four Diátaxis documents or twelve arc42 sections is not automatic. See [documentation patterns](../../skills/write-technical-documentation/references/technical-documentation.md).

## Write marketing content

[`write-marketing-content`](../../skills/write-marketing-content/SKILL.md) connects an audience's situation to supported product value. Audience, value and claim patterns are local guidance. [Microsoft's plain-word guidance](https://learn.microsoft.com/en-us/style-guide/word-choice/use-simple-words-concise-sentences) and [Google's jargon guidance](https://developers.google.com/style/jargon) inform expression; neither validates a product promise or establishes conversion effectiveness.

**Example request:** “Announce self-service cancellation to workshop organisers using the capabilities in this release.”

The result explains the supported benefit in language those organisers can use. Available behaviour, planned work and illustrative claims remain distinct. A stronger claim that needs evidence gets a specific follow-up note, separate from the finished copy. The [marketing guidance](../../skills/write-marketing-content/references/marketing.md) records those distinctions and sources.

## Write interface content

[`write-interface-content`](../../skills/write-interface-content/SKILL.md) writes for the user's actual situation and available actions. [Atlassian's voice and tone guidance](https://atlassian.design/foundations/content/voice-tone/) informs that situational approach. The requirements to distinguish state, confidence and progress, and to report progress from actual events, are local rules.

**Example request:** “Write the cancellation confirmation, pending message and recoverable error for these implemented states.”

The result maps copy to the supplied states and actions. Essential conditions remain visible in text. A missing state is raised as a proposal rather than quietly described as implemented behaviour. The [interface patterns](../../skills/write-interface-content/references/interface-content.md) cover recovery, metrics and accessibility.

## Review project language

[`review-project-language`](../../skills/review-project-language/SKILL.md) checks existing material across its reader journey. Microsoft and Google writing guidance inform expression; the ISO plain-language public abstract informed the research. Consistency, accessibility, readability and repeatability are [@pipewrk](https://github.com/pipewrk)'s four priorities, rather than a quoted ISO checklist or certification.

**Example request:** “Review the booking task, ADR, help page and confirmation screen for changed meanings and difficult navigation.”

The result identifies material findings with their location, effect and smallest useful correction. Different wording can preserve the same meaning. Matching wording can still conceal a contradiction. The [review criteria](../../skills/review-project-language/references/review.md) separate meaning and reader navigation from selected linter findings.

## Backend slice architecture

[`backend-slice-architecture`](../../skills/backend-slice-architecture/SKILL.md) applies [@pipewrk](https://github.com/pipewrk)'s original backend rules when that model is chosen or requested for review. The rules govern owned capabilities, public interfaces, coordination and earned sharing. External writing guides improve how the rules are explained; they do not authorise architectural changes.

**Example request:** “Review where booking cancellation and refund coordination belong under our backend rules.”

The result should identify the affected boundary and relevant rule, using the actual repository's conventions and contracts. It should preserve conditions and exceptions, including the distinction between a narrow public dependency and workflow coordination. Read [placement rules and their origin](../../skills/backend-slice-architecture/references/placement-and-contracts.md). A general research reference to domain-driven design does not convert this playbook into a strict DDD architecture.

## Frontend slice architecture

[`frontend-slice-architecture`](../../skills/frontend-slice-architecture/SKILL.md) applies [@pipewrk](https://github.com/pipewrk)'s original frontend rules. Features own their behaviour; scenes compose pages and screens; sharing is earned through repetition. Microsoft and Google writing principles inform explanation, while the architectural authority stays with the original rules.

**Example request:** “Review the cancellation feature and its web and mobile scenes without changing our framework.”

The result explains ownership, public interfaces and composition through the repository's existing platform conventions. It preserves the rules' exceptions and package-safe boundaries, using the public interfaces and dependency boundaries defined by the playbook. Follow [placement rules and sources](../../skills/frontend-slice-architecture/references/placement-and-contracts.md); platform detail is loaded when relevant.

## Choose a project-writing workflow

[`write-project-content`](../../skills/write-project-content/SKILL.md) remains an explicit compatibility entry point. Its routing table and context-budget decision are local choices. [Agent Skills](https://agentskills.io/specification) informs the portable format and selective resource loading, rather than prescribing this collection's routing table.

**Example request:** “Use write-project-content to choose the right workflow for explaining this decision to customers.”

The result selects the relevant specialist or bounded combination. Ordinary marketing or documentation requests can go directly to their purpose-specific skills. The router is optional, and its metadata does not establish identical automatic activation in every client. See [routing sources](../../skills/write-project-content/references/routing.md).

## Follow one change through the collection

Consider an **invented workshop-booking service** adding self-service cancellation. This is an illustration of possible work, rather than an implemented repository feature or an executed test.

| Work in this example | Useful skill | What to carry forward |
| --- | --- | --- |
| Reconcile reservation, booking and registration | Establish project language | Accepted meanings, remaining proposals and source contracts |
| Check cancellation/refund ownership if boundary design is in scope | Backend and frontend architecture | Existing rules, platform boundaries and explicit composition |
| Prepare the next worker's cancellation task | Write implementation tasks | Observable behaviour and current cancellation policy |
| Record a consequential shared-workflow choice | Record architecture decisions | Actual options, consequences and reconsideration conditions |
| Explain the change to support and developers | Write technical documentation | Behaviour first, linked contracts and task-specific detail |
| Announce supported value to organisers | Write marketing content | Available capabilities and substantiated claims |
| Write confirmation, pending and recovery states | Write interface content | Implemented state transitions and available actions |
| Compare the resulting material | Review project language | Consistent meaning and a clear route for each reader |

If a compatibility check remains unrun, **advance-with-uncertainty** helps express its next action and the claim that depends on it. Independent authorised work can continue. If the writer explicitly needs help choosing a workflow, the compatibility router can select one.

The stable element is project meaning: the same cancellation condition must survive its translation from technical contract to task, help page, announcement and screen. The amount of detail and wording should change with the reader's purpose. The [maintenance lifecycles](lifecycles.md) explain when to revisit these artefacts as behaviour, sources or audience needs change.
