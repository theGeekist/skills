<!--
Provenance: assistant research supplied by the user in the external-conversation export,
message 3, dated 29 October 2026. The research below is preserved as supplied,
including exported citation, entity, URL and image markup. Those references are
historical identifiers, not verified or reconstructed sources. Source verification,
corrections and adoption decisions belong in separate evaluation records.

Scope: the complete research response from its title through its final assessment.
The earlier explanatory answer and subsequent execution proposal are outside this
research baseline. Transport chunk boundaries are removed; text split across those
boundaries is joined. No absent citation targets have been invented.
-->

# Research: Engineering consistent language across software projects and AI agents

Research reviewed 29 October 2026 · Standards, content design, terminology systems, Codex, Agent Skills and writing-quality tooling

## Executive findings

**The foundations for what you're proposing already exist. The opportunity is to combine them into a coherent, enforceable system that works across both software artefacts and agent conversations.**

The research reveals five important findings.

1\. **Terminology is an established engineering discipline.** ISO standards cover concept modelling, definitions, preferred terms, synonyms and terminology exchange. We needn't invent a method for managing language.

2\. **Information structure is also well established.** Diátaxis, Information Mapping, DITA and architecture decision records provide different ways to structure knowledge for readers and authors.

3\. **Plain language is considerably more rigorous than short sentences.** ISO 24495-1 considers whether readers can find, understand and use the information they need. The GOV.UK and Microsoft guidelines turn much of this into practical editorial rules.

4\. **Agent infrastructure is already capable of supporting much of this.** Codex supports persistent instructions, reusable skills, reference materials, lifecycle hooks and review rules. Vale provides linting for prose, including existing Microsoft, Google and Diátaxis rule packages. citeturn194839search6turn157774search0turn484358search3

5\. **The biggest remaining gap is conversational quality.** Existing tools are strongest at checking completed text. A system that consistently governs what agents *say during work*, which domain concepts they introduce, and how much detail they reveal needs an additional layer of behavioural guidance and validation.

My central recommendation is to treat language as a project-level concern, much like architecture, security or testing. A language system should establish meaning first, support different forms of communication, and evolve with the domain.

There is a strong case for building this. There is a weaker case for building everything from scratch.

---

## 1\. Terminology and domain frameworks

These establish what concepts exist, what they mean and how terminology should be managed.

| Framework | Contribution | Applicability |
|--------|--------|--------|
| **DDD / Ubiquitous Language** | Shared concepts and vocabulary within bounded contexts | Essential |
| **ISO 704:2022** | Rules for concept relationships, terms and definitions | Essential reference |
| **ISO 1087:2019** | Formal vocabulary for terminology engineering | Supporting reference |
| **W3C SKOS** | Machine-readable preferred terms, alternatives and relationships | Useful for complex domains |
| **ISO 30042:2019 / TBX** | Exchange of managed terminology between systems | Optional, especially for larger or multilingual systems |

### DDD and ISO 704 are complementary

You already know DDD's Ubiquitous Language. What ISO 704 adds is a more formal account of terminology itself.

Its concern is the relationship between objects, concepts, definitions and designations—the names or other representations used to refer to concepts. It also provides principles for constructing definitions and forming terms. citeturn194839search0

Consider these apparently interchangeable words in a prospecting system\:

*Lead, prospect, candidate, contact, opportunity.*

They might refer to five different concepts. They might also reflect historical terminology introduced by different developers.

DDD asks us to understand which meanings belong to which bounded contexts. ISO 704 gives us a disciplined method for defining the concepts and their names.

This matters because a glossary compiled from existing code is insufficient. It may simply preserve the ambiguity that the project accumulated.

A proper terminology exercise establishes the meaning before endorsing the name.

### Context boundaries matter more than universal consistency

An important finding from Martin Fowler's treatment of bounded contexts: the same word can legitimately mean different things in different contexts. A DDD model must be internally consistent, but different contexts can maintain different models and explicit translations between them. citeturn484358search6

For example, *opportunity* may mean a potential commercial engagement in a sales context and a statistically promising discovery in a research context.

Forcing both onto one definition could damage the model.

The appropriate invariant is\:

**One coherent meaning per concept within its context, with explicit mappings between contexts.**

That should extend from code and domain events through to documentation and user-facing language.

### W3C SKOS: where terminology becomes structured data

The entity["other","Simple Knowledge Organization System (SKOS)","W3C standard for knowledge organisation"] is particularly relevant because it already models many of the things a bespoke terminology system would need\:

- Preferred labels (`skos:prefLabel`\)
- Alternative labels (`skos:altLabel`\)
- Definitions (`skos:definition`\)
- Broader, narrower and related concepts
- Contextual notes and mappings between schemes

SKOS is a formal W3C Recommendation rather than an experimental agent convention. citeturn246892search1

I wouldn't immediately introduce RDF or a graph database to support it. A version-controlled YAML or JSON registry could adopt the same concepts and introduce formal SKOS interoperability later.

ISO 30042's TermBase eXchange (TBX) is another established route, especially for translation and interchange between terminology-management systems. It's more relevant when terminology needs to travel between organisations or publishing systems. citeturn484358search0

**Research conclusion\:** A domain glossary should be a structured, context-aware source of truth, rather than a Markdown table of words and definitions.

---

## 2\. Plain language, controlled English and editorial consistency

This is the part of the research most directly concerned with your frustration about dense, inconsistent agent-generated prose.

**urlISO 24495-1:2023 — Plain Languagehttps://www.iso.org/standard/78907.html**

Its four principles are relevance, findability, understandability and usability. This covers document selection, information order and reader comprehension—not just word choice. Particularly valuable as the highest-level quality standard.

---

**urlASD-STE100 — Simplified Technical Englishhttps://asd-ste100.org/**

A controlled writing system with 53 writing rules and a restricted dictionary. Issue 9 was published in January 2025. It permits defined subject-specific terms. Excellent as a model for reducing ambiguity in technical instructions, but too restrictive to adopt wholesale for marketing or ordinary conversations. citeturn248457search8

---

**urlMicrosoft Writing Style Guidehttps://learn.microsoft.com/en-us/style-guide/**

Covers terminology, voice, grammar, technical writing, user interfaces and customer communication. Its core principle is especially useful: when the meaning is the same, use the same word. citeturn246892search3

---

**urlGoogle Developer Documentation Style Guidehttps://developers.google.com/style**

Particularly strong on jargon, technical definitions, abbreviations, procedures, consistent word choices and globally understandable writing. The guide is actively maintained; its October 2026 update addressed subjective language such as *simply*, *quickly* and *properly*\. citeturn314260search1

---

**urlGOV.UK / Home Office Content Patternshttps://design.homeoffice.gov.uk/design-and-content/content/content-patterns**

Takes consistency beyond individual words. It defines reusable content patterns for recurring interactions and messages, including task instructions, forms and alerts. Very relevant to dashboard copy and product interfaces. citeturn248457search4

### The distinction between simplifying words and simplifying thought

A useful insight from these sources is that simpler language does not require reducing technical precision.

Compare\:

Dense agent response

The incremental qualification pipeline has exhibited a positive confidence delta attributable to increased provenance coverage and successful verification of newly ingested signals.

---

Plain English

**Confidence increased by 8 points.**

Three newly collected signals passed verification. Source coverage also improved.

The second version can be more precise because its statements are easier to examine independently. The numerical change is explicit, as are the reasons for it.

But this example also reveals a limitation: a writing linter can flag *attributable*, *exhibited* or excessive sentence length. It cannot independently establish whether the claimed causal relationship is true.

That requires access to the domain model and underlying evidence.

This is where the terminology layer and the writing layer must meet.

---

## 3\. Frameworks for structuring documents and information

The next question is how to turn those rules into consistently useful tasks, ADRs, developer documentation, marketing copy and interface content.

Several established methods address this, with different strengths.

**urlDiátaxishttps://diataxis.fr/**

Distinguishes four kinds of technical documentation: tutorial, how-to, reference and explanation. Each serves a different reader need.

Its greatest advantage is preventing a reference page from turning into a tutorial, or a simple procedure from becoming a lengthy architectural essay. citeturn278327view6

---

**urlInformation Mappinghttps://support.informationmapping.com/hc/en-us/articles/213446789-Present-your-information-in-a-clear-and-consistent-way**

Classifies information into six types: concept, procedure, process, principle, structure and fact. Each has suitable presentation patterns.

More granular than Diátaxis. Especially useful for deciding whether something deserves a paragraph, table, diagram or procedure. citeturn194839search14

---

**urlDITA 2.0https://dita-lang.org/**

An OASIS standard for structured technical content. It has formal topic types such as concept, task and reference, along with reusable and publishable content structures.

Worth understanding for its modelling principles. Its XML authoring and publishing infrastructure would probably be unnecessary for a typical Git-based project. citeturn248457search6turn210336search5

---

**urlThe Good Docs Projecthttps://www.thegooddocsproject.dev/template**

Provides actual, reusable templates for concepts, how-to guides, references, tutorials, README files and other software documentation.

This is one of the most immediately reusable resources for building documentation skills without inventing every template. citeturn210336search7

There is also urlISO/IEC/IEEE 26514:2022https://www.iso.org/standard/77451.html, which specifically governs the design and development of information for software users. It covers establishing user information needs, selecting presentation methods and maintaining documentation throughout the software lifecycle. citeturn968581search4

### How the frameworks fit your artefacts

| Artefact | Most useful foundation | Suggested information order |
|--------|--------|--------|
| Engineering tasks | Information Mapping + plain language | Outcome → Context → Expected behaviour → Acceptance criteria |
| ADRs | Nygard / MADR | Decision → Context → Alternatives → Consequences |
| Architecture documents | arc42 + Information Mapping | Purpose → Boundaries → Design → Trade-offs |
| API references | Diátaxis / DITA | Purpose → Contract → Behaviour → Examples |
| Developer guides | Diátaxis + Google style | Goal → Requirements → Procedure → Verification |
| Marketing content | Content design + voice and tone | Customer need → Value → Evidence → Action |
| Dashboards | UX content patterns | Result → Change → Explanation → Next action |
| Agent conversations | Plain language + project vocabulary | Answer → Supporting reasoning → Implication, as needed |

These are proposed defaults, rather than formally prescribed sequences from the standards.

ADRs are a good example. The established Nygard format already has a disciplined structure, while MADR extends it with options, decision drivers and supporting material. There is little reason for an agent to invent a new decision-document format. citeturn246892search0turn246892search15

For dashboards and marketing, I'd add urlAtlassian's voice and tone principleshttps://atlassian.design/foundations/content/voice-tone/\. They distinguish informing, encouraging, motivating and celebrating according to the user's situation.

That matters when a product displays movement towards an outcome. A message about a successful verification step should sound different from a message explaining a genuine error. citeturn314260search7

### A particular concern: narrative cadence

None of these frameworks completely standardises sentence rhythm, progression of ideas or the amount of explanation appropriate to a conversation.

They supply principles and patterns, but cadence still needs editorial judgement.

I would define cadence through examples of **good responses for specific situations**, rather than impose one universal response template.

A two-line answer to a direct technical question should remain two lines. An architecture investigation deserves explanation, diagrams and trade-offs. A status update should communicate movement. A decision document should preserve enough reasoning for future maintainers.

The shared invariant is clarity. The amount and sequence of detail should follow the reader's task.

This is where agents need richer guidance than simply “be concise”.

---

## 4\. What already exists for Codex and other agents?

This is the most promising part of the research because there is considerably more infrastructure available than there was a year ago.

### Agent Skills is now a portable specification

The official urlAgent Skills specificationhttps://agentskills.io/specification defines a standard `SKILL.md` format, with supporting instructions, scripts, reference files and assets.

Codex supports the format, as do other compatible agent systems. The specification uses progressive disclosure: agents first discover a skill through its metadata, then load detailed instructions and references when needed. citeturn278327view0turn194839search6

This maps closely to the workflow you're describing.

A documentation skill could reference an approved terminology registry, the relevant document framework, a template, positive examples and a validation script.

However, a fundamental distinction needs to be preserved\:

**Skills are suitable for specific tasks. Persistent instructions are better for rules that must apply to every conversation.**

A documentation skill might activate when Codex writes an ADR. It might never activate while Codex discusses the architecture with you.

That distinction is critical.

### Codex's existing enforcement layers

| Mechanism | What it can do for language | Limitation |
|--------|--------|--------|
| Global `AGENTS.md` | Establish conversational tone, terminology behaviour and verbosity preferences across repositories | Instruction-following, rather than deterministic enforcement |
| Repository `AGENTS.md` | Identify domain references, preferred terms and project-specific rules | Can become bloated if filled with entire glossaries |
| Agent Skills | Package document-writing and domain workflows, with examples and validators | Implicit activation is task-dependent |
| Lifecycle hooks | Load context, inspect changes, validate agent responses and request corrections | Support varies by runtime and hook |
| Custom review rules | Make terminology and content-quality issues part of Codex review | Most useful during reviews rather than general conversation |
| Evaluation suites | Test whether the agent consistently follows writing and terminology requirements | Require representative tests and scoring criteria |

Official Codex guidance explicitly recommends using a global `AGENTS.md` for personal communication preferences and repository files for project-specific conventions. citeturn157774search1

That provides a natural foundation for your requirement that Codex conversations themselves follow the language system.

### The especially interesting discovery: Codex `Stop` hooks

Current Codex documentation describes a `Stop` hook that receives the latest assistant message through `last_assistant_message`\.

The hook can inspect that text and request another continuation with a reason if it finds a problem. It also receives `stop_hook_active`, allowing the implementation to guard against repeated continuation loops. citeturn309782view1

This suggests a practical conversational review mechanism.

**Codex produces a response**

**`Stop` hook examines the response**

Terms · Jargon · Clarity · Relevance · Excessive detail

**Pass**

Allow turn to finish

**Needs revision**

Request a corrective continuation

There is an important qualification: a continuation is not necessarily a clean replacement of already displayed streaming content. We would need to test the user experience in your particular Codex interface. This is a promising correction mechanism, not a guarantee that users never see the original response.

Other useful hook points include `SessionStart`, `UserPromptSubmit` and the compaction lifecycle, where project terminology context could be reintroduced or refreshed. citeturn157774search0

The official documentation also distinguishes local hooks from cloud-orchestrated Work, where support is more limited. An implementation would need to be tested against the actual execution mode.

### Cross-agent portability

This architecture needn't be tied permanently to Codex.

GitHub Copilot supports repository-wide and path-specific instructions. Claude Code supports persistent instructions, skills and lifecycle hooks. Both have mechanisms for applying project-specific guidance to agent work. citeturn462696search0turn462696search8

The best portable assets would therefore be the terminology registry, writing rules, examples and standard Agent Skills.

Agent-specific instruction files and hooks could act as thin adapters.

I wouldn't attempt to maintain independent language policies for every agent.

---

## 5\. Existing tools worth adopting or enhancing

The research identified several concrete tools rather than merely frameworks.

image_group{"query":["Vale prose linter official logo vale-cli"],"aspect_ratio":"1:1","layout":"carousel","num_per_query":1}

**urlVale — prose linterhttps://vale.sh/**

Strongest immediate candidate

A configurable, markup-aware linter for written material. Supports terminology substitutions, style rules and existing style-guide packages. Suitable for local development, CI and editor integration. citeturn266660search1

---

**urltextlinthttps://textlint.org/**

A JavaScript-based natural-language linter with pluggable rules, including terminology checks and automatic fixes.

A credible alternative if we want deeper integration with Bun/TypeScript, or custom rules over Markdown syntax trees. citeturn319728view4

---

**urlCSpellhttps://cspell.org/**

Project dictionaries, spelling checks and developer-friendly integration. It explicitly supports agent workflows and the addition of legitimate project vocabulary. Useful for catching accidental terminology mutations and misspellings. citeturn266660search2turn266660search11

---

**urlVale Package Explorerhttps://vale.sh/explorer**

Offers ready-made Google and Microsoft writing rules, plus packages addressing jargon, general prose quality and AI-writing patterns.

These are reusable starting points, with individual rules to review rather than blindly enabling everything. citeturn484358search3

### A particularly relevant existing package

There is now a urlDiátaxis package for Valehttps://vale.sh/explorer/diataxis\.

Released on 24 September 2026, its initial version provides 20 rules that test whether documentation follows its intended form.

For example, reference pages should describe behaviour rather than drift into instructions. How-to guides should focus on achieving goals. Tutorials should teach through a sequence of activities.

The package is very new—version 0.1.0 when checked—so I would treat it as experimental and test for false positives before making it a mandatory CI check. citeturn484358search1

This is useful evidence that the idea of **linting information structure, not just grammar**, is already taking shape.

### Vale versus textlint

I'd begin with Vale.

Its existing editorial packages and independent CLI make it particularly attractive across mixed technology stacks. It can enforce conventions regardless of whether a document was produced by Codex, a developer or a marketing writer.

textlint becomes more interesting when we want custom language analysis inside a TypeScript-based toolchain, particularly for rules that inspect Markdown structure or need bespoke logic.

There is no immediate need for both engines. CSpell complements either, because spelling and terminology governance solve different problems.

The hardest checks—whether a new concept is genuinely justified, whether a claim is supported, or whether an explanation flows naturally—still call for contextual evaluation rather than simple lexical rules.

---

## 6\. A project architecture that brings this together

Based on the research, I would organise this around a **project language contract**\: a version-controlled set of definitions, writing conventions and tests that agents and humans share.

The contract would have three distinct responsibilities.

**Meaning\:** which concepts exist, where they belong, how they relate and what terminology is approved.

**Expression\:** how those concepts are communicated to different audiences, with appropriate voice, cadence and presentation.

**Enforcement\:** how changes to text, documents and agent behaviour are checked against the contract.

The project repository could look something like this\:

```text
AGENTS.md
language/
  domains/
    prospecting.yaml
    evaluation.yaml
  terms/
    concepts.yaml
    public-labels.yaml
  editorial/
    plain-language.md
    voice-and-tone.md
    conversation.md
  patterns/
    tasks.md
    decisions.md
    dashboards.md
    marketing.md
  examples/
    good-responses.md
    good-documentation.md
.agents/skills/
  domain-discovery/SKILL.md
  write-documentation/SKILL.md
  review-language/SKILL.md
.vale.ini
docs/
  decisions/
  guides/
  reference/
```

This is an illustrative structure, not a recommendation to create every file immediately.

The significant design decision is that **the language reference exists independently of the skills that consume it**\.

That avoids a common failure mode where one skill defines a concept differently from another.

### What should a domain term actually contain?

Consider a hypothetical opportunity-assessment system.

```yaml
id: evaluation.confidence
context: evaluation

preferred_term: Confidence

definition: >
  A measure of the strength of evidence
  supporting an opportunity assessment.

distinct_from:
  - evaluation.coverage
  - evaluation.eligibility

labels:
  dashboard: Confidence
  report: Opportunity confidence

related_decision: docs/decisions/0007-scoring.md
```

Even this relatively small record contributes something valuable.

It establishes that *confidence*, *coverage* and *eligibility* are different concepts.

A dashboard may show a confidence score, a separate coverage measure and a separate eligibility state. A marketing writer may explain their relationship in plain English. An ADR may define how confidence is calculated.

All three can use the same conceptual foundation without duplicating definitions or inventing incompatible meanings.

I'd also keep concept identifiers stable when public wording changes. A new customer-facing label needn't require renaming every internal type, database column or event.

### Establishing terminology in new and existing projects

For a new project, I would begin with a working domain map and a small set of candidate definitions. DDD exploration, event discussions, example scenarios and acceptance criteria provide the material.

For an existing project, the process is different. The agent should inspect established code, schemas, events, tests, documentation and user-facing content to discover the language already in use.

It should then identify competing meanings, historical aliases and undefined concepts.

Importantly, discovering a term isn't equivalent to approving it.

An agent should be able to propose a concept or naming change, explain where it came from, and connect it to the appropriate bounded context. The project's terminology owner—or a suitable review process—decides whether to adopt it.

That keeps language evolving without allowing every agent session to invent its own vocabulary.

---

## 7\. Making Codex conversations follow the same rules

I would give the conversational experience equal importance to generated files.

In fact, this is where I suspect much of the everyday improvement would be felt.

### Persistent conversational behaviour

A global Codex instruction could establish an everyday writing baseline along these lines\:

Illustrative conversational policy

Respond in clear British English, appropriate to the reader's expertise. Lead with the answer or material finding. Develop the explanation in a natural sequence.

Use established project terms consistently. Define unfamiliar domain terms when introducing them. Distinguish proposed terminology from accepted terminology.

Prefer concrete statements and examples over abstract descriptions. Preserve technical precision, meaningful caveats and evidence.

Match the length and structure of the response to the question. Treat progress updates as communication about meaningful changes rather than detailed activity logs.

The policy is intentionally short.

In September 2026, OpenAI published guidance warning that excessive skill descriptions and long `AGENTS.md` files can reduce agent effectiveness. The recommendation is to keep persistent instructions focused and load reference materials when relevant. citeturn968581search0

That supports a layered approach rather than one enormous prompt containing every conceivable rule.

### Conversational quality needs testing

The response should be evaluated on several independent dimensions, rather than one subjective readability score.

| Dimension | What we would measure |
|--------|--------|
| Terminology | Consistent use of approved concepts within the relevant context |
| New concepts | Whether unfamiliar project terms are explained or explicitly proposed |
| Clarity | Directness, unnecessary abstraction and ambiguous references |
| Density | Amount of information relative to the user's request |
| Cadence | Whether ideas follow a coherent and appropriate sequence |
| Evidence | Whether factual claims have suitable support |
| Continuity | Whether the response preserves established decisions and vocabulary |
| Usefulness | Whether the reader can understand or act on the result |

Some of these can be checked deterministically.

Others require examples and human-judged or model-graded evaluations.

OpenAI has published a specific methodology for urltesting Agent Skills with evaluationshttps://developers.openai.com/blog/eval-skills\. It uses a test prompt, captured run, artefacts and a set of checks to compare successive versions.

That is a credible way to evaluate changes rather than assuming a revised prompt will always produce better writing. citeturn462696search2

For example, a test might ask Codex to explain a domain model, create an ADR and write a customer dashboard description using the same underlying data. We can assess whether each output preserves the same definitions while adopting its appropriate tone and information structure.

### Why automatic readability scores are insufficient

I would be cautious about making sentence length, word count or reading-age scores hard requirements.

An architecture document may need a specialised technical term. A short sentence may still be vague. A longer explanation may genuinely be necessary to establish why a decision was made.

Likewise, banning a word such as *unqualified* everywhere would be a poor design choice if it is a precise internal status.

The stronger rule is contextual: an internal status should be translated into a useful explanation when presented to a customer.

The aim is to simplify the reading experience while preserving the underlying meaning.

---

## 8\. What should be adopted, enhanced or built?

Here is my assessment after reviewing the current ecosystem.

| Capability | Assessment | Direction |
|--------|--------|--------|
| Domain definitions and context mapping | Established methods available | Adopt DDD + ISO terminology principles |
| Machine-readable terminology | Mature standards available | Start with a small registry; borrow from SKOS |
| Plain-language guidance | Mature standards available | Adopt ISO 24495-1 principles |
| Technical documentation structures | Well established | Adopt Diátaxis and existing templates |
| ADR conventions | Mature | Adopt Nygard / MADR |
| Editorial linting | Strong existing tooling | Adopt Vale |
| Project-specific term checking | Partially addressed | Extend Vale or textlint |
| Agent skill packaging | Portable standard exists | Adopt Agent Skills |
| Codex conversation conventions | Supported through instructions | Configure globally and by repository |
| Live agent-response validation | Hooks enable useful checks | Experiment and validate |
| Domain-aware semantic review | Existing components, no complete solution identified | Build a focused evaluation layer |
| End-to-end consistency across all artefacts | No comprehensive turnkey solution identified | Integrate existing components |

The last two rows are where custom engineering is most defensible.

A custom system could use the same concept registry to inform agent prompts, generate linter rules, suggest terminology corrections, select document templates and evaluate final outputs.

That would be a meaningful extension of existing frameworks rather than a reinvention of them.

## 9\. Where I would begin

I wouldn't start by producing a full suite of skills.

First, I would take one existing project and establish its real terminology and bounded contexts. This will expose ambiguities that a theoretical style guide cannot anticipate.

Next, I would establish a concise conversational policy and one documentation skill backed by existing templates and Vale. Both would draw from the same language reference.

Then I would test the system against actual Codex conversations and artefacts that have previously required corrections: excessively dense explanations, invented terms, inconsistent names, unclear decisions and poorly structured documents.

That gives us measurable before-and-after results.

Only then would I expand into dedicated skills for ADRs, tasks, marketing and dashboards.

The distinction I would retain throughout is that language governance should improve comprehension without turning writing into a rigid approval exercise. Domain discovery remains exploratory. Established terminology provides continuity. Agent communication remains natural.

## My assessment

There is a credible foundation here for a reusable, agent-compatible language system.

**The mature components are terminology engineering, structured documentation and prose linting. The emerging capability is enforcing those standards inside autonomous agent workflows and conversations.**

That is the interesting engineering problem.

The strongest starting combination I found is **DDD + ISO 704 + ISO 24495-1 + Diátaxis + Vale + Agent Skills**, with Codex's global instructions and hooks extending the approach into conversations.

I'd treat that as the research baseline, then develop and evaluate the smallest useful implementation before deciding whether it warrants becoming a standalone framework, shared skill package or open-source tool.
