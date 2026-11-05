# Compare writing skills

Choose a writing skill by the work it needs to do. A focused copyeditor may be enough for one draft; a project with shared terminology, decisions and product copy also needs a way to preserve meaning across those artefacts.

This comparison covers the instruction and package revisions linked below. It compares their scope and organisation, rather than claiming a winner from unrun writing or reader tests.

## Choose by purpose

| Skill | Main use | Organisation and trade-off |
| --- | --- | --- |
| [Humanizer](https://github.com/blader/humanizer) | Edit structure, rhythm, inflated language, factual changes and voice mismatches | A detailed single-file guide with paired examples and contextual exceptions |
| [Plain Writing](https://github.com/docwriter-org/plain-writing-skill) | Explain mechanisms and context in a consistent, literal register | An inline ruleset whose deliberate style restrictions may not suit every author |
| [Writing Clearly and Concisely](https://github.com/obra/the-elements-of-style) | Copyedit sentences and paragraphs using Strunk's 1918 text | A small entry point that directs the reader to a substantial complete reference |
| [Plain Language Editor](https://github.com/marketingskills/plain-language-editor) | Find a document's main point, clarify relationships and audit claims | An editorial sequence with an attributed pattern catalogue and optional surface checks |
| [Geekist Skills](../../README.md) | Preserve project meaning and evidence constraints across tasks, decisions, documentation, marketing and interfaces | Eleven focused entry points with a shared baseline and concern-specific references |

These scopes overlap. Humanizer and Plain Language Editor both address structure and factual integrity; neither is adequately described as a banned-word list. A broader project workflow does not by itself produce better prose.

## Important version differences

### Humanizer

The reviewed [v3.1.0 instructions](https://github.com/blader/humanizer/blob/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0/SKILL.md) group 26 patterns into six sections. They check unsupported additions and omitted claims, preserve technical material and use supplied samples to guide voice. Intentional stylistic choices are treated differently from repeated defects.

Its [README](https://github.com/blader/humanizer/blob/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0/README.md) demonstrates editing results and links to a community model-judge experiment. That experiment predates this version and is not a comparison with Geekist or a human-comprehension study.

### Plain Writing and the revision-view fork

The reviewed [canonical instructions](https://github.com/docwriter-org/plain-writing-skill/blob/f0d3630983ac7a82aa580f1c1509d72df739ee12/skills/plain-writing/SKILL.md) contain 25 rules and a `deslopify` command. They favour literal explanations and restrict devices such as analogies and catchy labels. This is a particular writing register, not a universal requirement for understandable prose.

The [Hamel fork](https://github.com/hamelsmu/plain-writing-skill/blob/295afb568bccbd816912816312ef89a195f1752f/SKILL.md) retains an HTML revision view showing original, revised and difference views with edit explanations. The inspected canonical revision does not contain that template or workflow. Pin the repository and revision when comparing them.

The canonical [evaluation method](https://github.com/docwriter-org/plain-writing-skill/blob/f0d3630983ac7a82aa580f1c1509d72df739ee12/evals/README.md) reports rule-adherence results using model-generated writing and model judging. Those results do not establish reader comprehension or cross-skill superiority.

### Strunk-based variants

The reviewed [Obra skill](https://github.com/obra/the-elements-of-style/blob/05fc4f0d2b97b7c042dd9949ad658568e4a1324e/skills/writing-clearly-and-concisely/SKILL.md) summarises 18 rules and includes the complete 1918 reference. Its positive-form advice permits legitimate denial and antithesis; it is not a blanket ban on negative statements or uncertainty.

The [Softaworks variant](https://github.com/softaworks/agent-toolkit/blob/3027f20f3181758385a1bb8c022d4041dfb4de84/skills/writing-clearly-and-concisely/SKILL.md) splits the reference by concern and adds AI-writing guidance. The different loading policy matters even though the packages share source material.

### Plain Language Editor

The reviewed [instructions](https://github.com/marketingskills/plain-language-editor/blob/df7b314509eb47a722aa620f11784fab76a595e6/SKILL.md) combine document-level editing, factual checks, voice preservation and a generated pattern reference. They also prescribe aggressive shortening and particular sentence and punctuation rules. Check those preferences against the intended author and artefact.

## What we learnt and incorporated

Existing agent writing skills approach the problem from several directions. Humanizer examines wording that can obscure the author's intention and checks whether a revision changes its claims. Plain-writing approaches make explanations easier to follow, while document-first editing gives greater attention to structure.

Some implementations also make revisions easier to inspect by explaining which changes matter. These practices were relevant to Geekist because improving a document requires understanding the information it carries and the audience it serves.

| Practice | Inspiration | Geekist implementation |
| --- | --- | --- |
| Check revisions against their sources for additions, omissions and changed meaning | Humanizer | [Review workflow](../../skills/review-project-language/SKILL.md#check-the-finished-revision) and final passes in five drafting skills |
| Improve document structure before sentence-level editing | Plain Language Editor; Plain Writing | [Review reference](../../standards/review.md#edit-structure-then-expression) |
| Explain actual behaviour through concrete language | Plain Writing; Plain Language Editor | Final editing passes in [task writing](../../skills/write-implementation-tasks/SKILL.md#edit-before-delivery), [decision records](../../skills/record-architecture-decisions/SKILL.md#edit-before-delivery) and [technical documentation](../../skills/write-technical-documentation/SKILL.md#edit-before-delivery), with corresponding checks in [marketing](../../skills/write-marketing-content/SKILL.md#edit-before-delivery) and [interface content](../../skills/write-interface-content/SKILL.md#edit-before-delivery) |
| Preserve deliberate voice and necessary terminology | Humanizer; Plain Language Editor | [Shared writing conventions](../../standards/writing.md#edit-without-flattening-the-writers-voice) and the review workflow |
| Explain consequential revisions and identify retained constraints | Hamel's Plain Writing variant | [Optional revision record](../../standards/review.md#make-consequential-edits-inspectable) |
| Use examples with contextual exceptions | Humanizer; Plain Language Editor | [Eight locally authored editorial patterns](../../standards/editorial-patterns.md) |
| Keep skill entry points focused | Strunk-based variants; Agent Skills guidance | Purpose-specific instructions with [bundled references](../../standards/skill-profiles.json) |
| Demonstrate the practical outcome before introducing implementation details | Competitor README and package organisation | [Eleven skill overviews](../skills/index.md) with source facts and before-and-after examples |
| Keep public descriptions consistent | Competitor package organisation | [Presentation catalogue](../../standards/skill-catalogue.json) with generated overviews and client metadata |

The examples and editorial patterns were written for Geekist. We adapted the underlying practices without copying upstream templates or pattern datasets. The [adoption guide](competitive-adoption.md) explains how these checks work together, and the [implementation map](implementation-status.json) identifies their source routes.

## Where our approach differs

Projects introduce complications when several documents depend upon the same underlying information. An architecture decision may establish a constraint that needs to remain visible in a developer guide. Marketing can describe the resulting feature in different language, provided that its explanation continues to respect what the product does.

Geekist therefore treats accepted project terminology as a reference for subsequent writing. Source authority matters because a claim in one document may depend upon a qualification established elsewhere. Editorial judgement remains important: a technical reference needs precision, while promotional material benefits from an engaging voice. Applying an identical style to both would make the collection easier to describe but less useful in practice.

Evidence gaps require similar care. A pending capacity test may limit performance claims without preventing an authorised implementation from proceeding. The uncertainty workflow helps authors describe that distinction, so an ordinary measurement does not acquire the authority of a constitutional crisis.

## Context and validation

At the inspected revisions, the main instruction files contain 5,219 whitespace-separated words for Humanizer, 2,319 for canonical Plain Writing, 325 for Obra and 4,384 for Plain Language Editor. Obra's complete reference adds 12,154 words; Plain Language Editor's pattern reference adds 3,949. These are file measurements, not model tokens or observed runtime context.

Geekist's current package measurements are maintained in [context-budget.json](context-budget.json). Core size alone is not a quality measure: a short entry point may require a large reference, and a complete review may legitimately need several concerns.

Upstream scripts were not executed during this source comparison. Geekist's executed checks and task trials are recorded in [validation results](validation-results.md). Native activation, human comprehension, comparative prose quality and search performance are distinct measurements.

## Discovery and search

Clear names, examples, installation commands and source links help readers understand a package. Skill descriptions help agents choose a purpose. Neither mechanism establishes search rankings or native activation by itself.

These writing tools are not complete SEO workflows. Search intent, indexing, page metadata, structured data and traffic measurement require their own work. See [discovery and installation](discoverability.md) and [Google Search Central's guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide).
