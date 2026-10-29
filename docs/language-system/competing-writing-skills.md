# Competing writing skills: prose, organisation and discoverability

Reviewed 29 October 2026. Source review supporting the Geekist Skills collection.

## Findings that affect our direction

We should have compared existing writing skills during the original research. That work concentrated on underlying frameworks, prose tooling and the structure of our own collection. The missing competitive review left us without a fair basis for deciding which editorial practices to reuse, complement or build ourselves.

The alternatives have substantial value. Humanizer provides specific editing patterns and factual-preservation checks. Plain Writing imposes a consistent explanatory register. Writing Clearly and Concisely packages a recognised copyediting source. A fourth relevant candidate, Plain Language Editor, combines document structure, claims review and an inspectable pattern catalogue.

Geekist's strongest distinct scope is maintaining project meanings across tasks, decisions, technical documentation, marketing and interfaces, while keeping evidence gaps actionable. That scope does not establish better prose. Several competing skills have more concrete editorial examples and clearer front-door positioning.

On discoverability, competitors offer useful mechanisms we can adopt. We have verified a stale GitHub description and narrow topics on our own repository. We have not established superior search rankings, traffic or conversion for any competitor.

## Scope and method

Three independent workers inspected the named alternatives, including their complete skill instructions, source material, package trees, READMEs, metadata and available evaluation descriptions. The parent reviewed Geekist, primary sources, search results and Plain Language Editor. Revisions are pinned below. Upstream scripts were read where relevant; none were executed and no competing skill was installed into the account.

This is a source and packaging comparison. It contains measured file sizes and observed public discovery mechanisms, plus explicitly identified recommendations. We did not run a controlled rewrite experiment, native client activation trial, human comprehension study or SEO traffic analysis. Word counts use whitespace splitting and include frontmatter unless labelled otherwise. They are not token counts or a guarantee of actual host loading.

## Which alternative helps with which problem?

| Skill | Useful when | Main trade-off |
| --- | --- | --- |
| Humanizer, blader | A draft has repetitive staging, inflated claims, awkward rhythm, formatting residue or a voice mismatch | Detailed single-file editor; its full instruction file loads together |
| Plain Writing, canonical docwriter-org | Explanations assume project context or need a consistent, literal prose register | Strong register preferences can conflict with essays, humour and marketing |
| Writing Clearly and Concisely, obra | You want a general sentence and paragraph copyeditor grounded in Strunk | Tiny entry point directs the agent to a large complete reference |
| Plain Language Editor, marketingskills | A draft lacks a main point, hides facts behind jargon or makes inconsistent claims | Substantial editorial process and stylistic prescriptions; full audit adds a pattern reference |
| Geekist collection | Meaning and evidence must remain consistent across several kinds of project work | More entry points and project conventions to discover; editorial examples remain less developed |

These scopes overlap. Humanizer and Plain Language Editor both address structure and facts, so presenting either as a vocabulary filter would understate its instructions.

## 1. Humanizer: a substantive editorial alternative

Reviewed **v3.1.0**, commit `0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0`.

The skill groups 26 editing patterns into six sections. It distinguishes stronger problems from weaker signals, checks factual additions and omissions, protects technical material and allows deliberate stylistic choices. Supplied writing samples guide voice. It does not grant permission to invent anecdotes or details.

Its strongest lessons are concrete before/after examples, explicit exceptions and a README that demonstrates the result immediately. One root `SKILL.md` makes inspection and installation straightforward. `AGENTS.md` and a package validator check agreement between versions, descriptions, counts and documentation.

A large single core is the context trade-off. Some formatting preferences still need reconciliation with an author's intended register. These are compatibility considerations, not observed failures in our tests.

The README cites a community model-judge preference experiment. That experiment predates v3.1.0, used judges from one model family and completed only part of its planned trials. It supplies limited upstream evidence rather than a human-reader result or a comparison against Geekist.

Sources: [pinned skill](https://github.com/blader/humanizer/blob/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0/SKILL.md), [README](https://github.com/blader/humanizer/blob/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0/README.md), [package instructions](https://github.com/blader/humanizer/blob/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0/AGENTS.md), [community experiment](https://github.com/blader/humanizer/issues/229). Repository licence: MIT.

## 2. Plain Writing: distinguish the canonical skill from the fork

Canonical **docwriter-org/plain-writing-skill**, commit `f0d3630983ac7a82aa580f1c1509d72df739ee12`. The older Shreyashankar repository URL redirects here.

The canonical skill has 25 rules with examples. It explains mechanisms, supplies missing context, maintains terminology and provides a `deslopify` command. It also deliberately prefers literal, unmemorable prose and prohibits analogies, dashes, catchy labels and demonstratives. Those are a particular register, with useful applications to technical explanations; they would constrain parts of Geekist's creative voice.

An important source discrepancy: the canonical repository's About text mentions a revision view, but the inspected current skill and tree contain no revision template or workflow. The **Hamel fork**, commit `295afb568bccbd816912816312ef89a195f1752f`, actually retains an HTML revision view with original, revised and difference tabs and edit explanations. We should learn from that inspectability without attributing it to the wrong version.

The canonical evaluation reports 65 versus 2 wins across 67 tasks. Both writer and judge use the same model, and judging rewards the skill's own rules. Raw outputs are excluded from the repository. This is upstream rule-adherence evidence; we did not reproduce it.

Sources: [canonical skill](https://github.com/docwriter-org/plain-writing-skill/blob/f0d3630983ac7a82aa580f1c1509d72df739ee12/skills/plain-writing/SKILL.md), [canonical README](https://github.com/docwriter-org/plain-writing-skill/blob/f0d3630983ac7a82aa580f1c1509d72df739ee12/README.md), [evaluation method](https://github.com/docwriter-org/plain-writing-skill/blob/f0d3630983ac7a82aa580f1c1509d72df739ee12/evals/README.md), [Hamel fork skill](https://github.com/hamelsmu/plain-writing-skill/blob/295afb568bccbd816912816312ef89a195f1752f/SKILL.md), [revision template](https://github.com/hamelsmu/plain-writing-skill/blob/295afb568bccbd816912816312ef89a195f1752f/assets/revision_template.html). Canonical licence: MIT. The inspected fork tree has no licence file; preserve that distinction when considering reuse.

## 3. Writing Clearly and Concisely: source-led copyediting

Original **obra/the-elements-of-style**, commit `05fc4f0d2b97b7c042dd9949ad658568e4a1324e`.

The skill packages William Strunk Jr.'s 1918 text, summarises 18 rules and covers human-facing prose broadly. The complete reference addresses grammar, composition and usage. Its positive-form guidance permits legitimate denial and antithesis; it should not be described as banning negative statements or uncertainty.

The core directs a full-reference read, with a delegated copyedit option when context is tight. Delegation relocates the reference cost rather than removing it. Its packaging also has a useful maintenance approach: one configuration drives multiple client manifests and installation pages, with no unconditional session-start injection. Those files do not prove every client works.

The **Softaworks variant** is materially different. At `3027f20f3181758385a1bb8c022d4041dfb4de84`, it splits Strunk guidance into sections and adds an AI-writing reference. This improves selective loading opportunities, but optional references can still be large. Shared Strunk material does not by itself prove a historical fork relationship.

Sources: [original skill](https://github.com/obra/the-elements-of-style/blob/05fc4f0d2b97b7c042dd9949ad658568e4a1324e/skills/writing-clearly-and-concisely/SKILL.md), [complete reference](https://github.com/obra/the-elements-of-style/blob/05fc4f0d2b97b7c042dd9949ad658568e4a1324e/skills/writing-clearly-and-concisely/elements-of-style.md), [README and source attribution](https://github.com/obra/the-elements-of-style/blob/05fc4f0d2b97b7c042dd9949ad658568e4a1324e/README.md), [Softaworks variant](https://github.com/softaworks/agent-toolkit/blob/3027f20f3181758385a1bb8c022d4041dfb4de84/skills/writing-clearly-and-concisely/SKILL.md). Obra declares Public Domain and attributes the 1918 source; the inspected Softaworks root declares MIT.

## 4. Additional candidate: Plain Language Editor

Reviewed **marketingskills/plain-language-editor**, commit `df7b314509eb47a722aa620f11784fab76a595e6`.

This is particularly relevant to our accessibility goals. Its seven main moves cover the document's main point, unnecessary commentary, sentence relationships, jargon, parsing, factual claims and contradictions. It also addresses copy that mechanically exposes database or API structure. It protects voice and supports findings without rewriting.

Its organisation offers a concrete lesson: a structured, attributed 120-pattern catalogue generates a readable reference, with stable identifiers, optional conservative Node checks and documented regression tests. We inspected the instructions and README; we did not execute those checks. A complete second editorial pass requires the reference.

Potential friction includes aggressive default shortening, sentence-length prescriptions and an absolute dash rule. Its own description of Humanizer as surface-only understates the current Humanizer's scope. We should compare instructions directly rather than repeat competitors' positioning claims.

Sources: [pinned skill](https://github.com/marketingskills/plain-language-editor/blob/df7b314509eb47a722aa620f11784fab76a595e6/SKILL.md), [README and package layout](https://github.com/marketingskills/plain-language-editor/blob/df7b314509eb47a722aa620f11784fab76a595e6/README.md), [pattern reference](https://github.com/marketingskills/plain-language-editor/blob/df7b314509eb47a722aa620f11784fab76a595e6/references/ai-slop-patterns.md). Repository licence: MIT; its README identifies upstream pattern/voice provenance and notices.

## Structure and context: what we can measure

| Package | Main skill words | Additional material and loading policy |
| --- | ---: | --- |
| Humanizer | 5,219 | Entire editorial product is in the core; no selectively loaded guidance references |
| Plain Writing, canonical | 2,319 | Rules inline; evaluation material is separate |
| Plain Writing, Hamel fork | 1,440 | Revision template adds 587 words if read |
| Writing Clearly and Concisely, obra | 325 | Complete reference: 12,154 words; core directs reading it |
| Plain Language Editor | 4,384 | Pattern reference: 3,949 words, required for a full second audit pass |
| Geekist six writing/review specialists | 395–434 each | Local purpose references; uncertainty detail selected where relevant |
| Geekist architecture skills | 1,033 backend / 992 frontend | Three concern-specific references per skill; full review reads all three |

Geekist also has discovery, uncertainty and explicit routing skills at 756, 782 and 453 words respectively. The eleven descriptions share discovery context, and every core repeats the 144-word baseline. A smaller selected core does not establish a smaller complete task or better results. Obra's small entry point also demonstrates why core size alone is misleading.

Useful organisation to borrow: visible edits from the Hamel fork; specific paired examples and exceptions from Humanizer; section-level source loading from the Softaworks variant; one metadata source from Obra; structured patterns and generated references from Plain Language Editor. Adapt selectively, preserve attribution and validate against our requirements.

## SEO and discoverability: three separate questions

### Can an agent choose the right skill?

Purpose-specific names and descriptions help make the intended task explicit. Humanizer describes editing; Plain Writing and Obra target prose broadly. Geekist distinguishes tasks, decisions, documentation, marketing and interfaces. That precision can reduce overlap, while its catalogue requires more choices.

This is a source-based assessment of selection cues. We did not run a comparative native selector test. Adding every popular keyword to every description would obscure purpose. Keep stable identifiers and test representative requests before changing activation scope.

### Can a person find and understand the package?

Competitors frequently make a single promise, show a before/after result and supply a short install/use example near the top. Obra's generated client pages and Humanizer's consistent metadata are concrete discoverability mechanisms. Registry pages exist for the named skills, including variants under older owners; a listing can point to a different revision than expected.

Our verified GitHub repository metadata still says **“Portable backend and frontend architecture skills from Geekist”**. Its homepage is unset. Its topics are `agent-skills`, `architecture`, `backend`, `claude-code`, `codex` and `frontend`. The expanded README covers writing, but these external discovery surfaces still describe the earlier two-skill collection. The stable plugin identifier also remains `geekist-architecture-skills`; compatibility is a reason to retain the identifier while improving displayed copy.

Search retrieved a SkillsCat snapshot showing our two architecture skills. That observation does not establish that the nine newer skills are absent from every index. A direct skills.sh lookup failed through the retrieval tool, so its current Geekist coverage remains unresolved. We should check the actual listings and refresh supported submissions rather than label the collection undiscoverable.

Sources: [live repository metadata endpoint](https://api.github.com/repos/theGeekist/skills), [current repository](https://github.com/theGeekist/skills), [observed SkillsCat profile](https://skills.cat/u/theGeekist), [Humanizer listing](https://www.skills.sh/blader/humanizer/humanizer), [canonical Plain Writing listing](https://www.skills.sh/docwriter-org/plain-writing-skill/plain-writing), [Obra listing](https://www.skills.sh/obra/the-elements-of-style/writing-clearly-and-concisely).

The separate humanizerskill.com site states that it is unofficial and unaffiliated. Its install, example and FAQ pages illustrate useful reader routes, but we should not attribute that site or its SEO strategy to Humanizer's maintainer.

### Do these skills make the resulting content rank better?

The reviewed writing skills focus on prose. They do not supply a complete search-intent, keyword-research, technical-indexing, structured-data, internal-linking or performance-measurement workflow. Clearer explanations can support useful content; neither a writing skill nor a directory listing establishes higher rankings.

Google recommends content users can understand, descriptive presentation and discoverable links, while explicitly avoiding ranking guarantees. Assess SEO improvements through actual indexing, impressions, queries, visits and useful outcomes over time. Source: [Google Search Central's SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide).

## Recommended next changes

| Priority | Change | Reason and observable completion |
| --- | --- | --- |
| First | Update GitHub About, homepage and topics | Describe the actual collection; verify visible metadata against all eleven skills |
| First | Lead with the writing problem and one before/after example | Let readers recognise the benefit before the research catalogue |
| First | Give every skill a directly linkable human overview | Purpose, example request, output, sources and exact installation command in one route |
| First | Publish a fair alternatives section | State when each comparator helps and pin the versions discussed |
| Next | Add optional annotated revision output | Make consequential edits and retained conditions inspectable without requiring a large HTML artefact for every task |
| Next | Add concrete editorial examples and exception cases | Improve usefulness beyond broad principles while protecting author voice and architecture meaning |
| Next | Generate repeated metadata and add drift checks | Keep manifests, human descriptions and installation pages aligned; test client support separately |
| Next | Check directory coverage and the Geekist content route | Verify listings, create useful linked pages, and measure discovery rather than promise SEO gains |

This comparison records the source-review checkpoint. Subsequent adopted improvements and remaining discovery work are recorded in [design and differences](design-and-differences.md) and [discoverability](discoverability.md). The comparison itself did not execute upstream scripts or measure SEO traffic.

## Evaluation before claiming better prose

Use six shared cases: a jargon-heavy explanation; conflicting project terminology; an implementation task with pending evidence; an ADR with an unresolved measurement; marketing with a bounded product claim; and an expressive Geekist passage.

Compare the same model without a skill, each relevant competitor and the appropriate Geekist specialist. Preserve the prompt, source facts, model settings and loaded-file record. Judge factual retention, original conditions, reader navigation, voice and usefulness, rather than rewarding one skill's punctuation rules. Have engineering and marketing readers locate the purpose, consequence and detailed contract. Native trigger selection needs a separate ordinary-request trial.

The article can acknowledge that clear writing, editorial examples and existing skills supplied substantial foundations. Geekist's contribution can then be assessed on its actual implementation: shared project meanings, purpose-specific workflows, traceable sources and continued action under uncertainty.
