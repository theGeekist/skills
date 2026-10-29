# Write for a shared understanding

These are Geekist's working conventions, informed by plain-language and content-design principles. They are not a claim of ISO certification or a substitute for a project's established meanings.

## Start with the reader's purpose

State what the reader needs to understand or decide. Lead with the answer, outcome or material finding. Explain its implications before expanding into mechanisms. Match the amount of detail to the request and the reader's expertise.

A technical document should let a business or marketing reader find its purpose, principal decision, consequences and next action. Give engineers a direct route to contracts, constraints, examples and evidence. Keep these routes in the same document when practical.

## Establish meaning

Use the project's accepted term for a concept in its context. Read current decisions, schemas and tests before relying on a historical glossary. Record disagreements with source pointers rather than silently choosing a definition.

Introduce an unfamiliar specialised term with a short explanation at its first consequential use. Link to the fuller definition where needed. Explain an acronym before relying on it. Familiar technical language need not be re-explained to an expert who asked a narrow question.

Distinguish a proposed term from an accepted one. Keep identifiers stable when presentation labels change. Allow the same word to have different meanings in different contexts, with an explicit translation when crossing the boundary.

## Make the route visible

Use descriptive headings that answer reader questions. For a long document, provide a short route to the relevant sections. Use meaningful link text, semantic heading levels, table headers and text alternatives for meaningful visuals. Do not rely on colour, animation or a diagram alone to communicate a result.

Introduce the purpose of a table or diagram. Explain what the reader should take from it. Preserve a textual route through essential information. Avoid headings that merely name internal machinery when the reader needs to understand an outcome.

Put optional implementation detail beneath the decision or explanation it supports. A clear summary must be accurate enough to stand on its own; it must not conceal material constraints in later sections.

## Develop the explanation

Connect each paragraph to the previous one. Prefer concrete subjects and verbs: say what changed, what caused it when known, and why it matters. Split unrelated claims so they can be checked independently.

Use lists for parallel items or a genuine sequence. Use tables for comparisons and mappings. Use prose for reasoning. Do not turn every response into a template or every sentence into a heading.

Prefer familiar words when they preserve meaning. Replace abstract stacks such as “incremental provenance qualification surface” with the actual process or result. Retain precise specialist terms when they earn their place and explain them to the intended reader.

Use British English consistently in authored prose. Preserve exact identifiers, quotations, protocol values and external product names.

## Preserve truth across audiences

Translate internal states into useful audience-specific wording without changing their meaning. Separate a result, confidence in that result, progress through checks and eligibility when the domain distinguishes them.

Describe progress using actual events, completed work, deltas and the next milestone. State an estimate or illustrative number as such. Express uncertainty where it affects interpretation or action. Keep implementation diagnostics available to the people who need them.

Keep implementation state separate from evidence state. Pair material uncertainty with a bounded next action and completion evidence. A gap in prior proof does not by itself disqualify a viable option or stop authorised work. Name actual blockers precisely and continue independent work where possible. See the shared uncertainty conventions when drafting tasks, decisions or handoffs.

For customer-facing writing, connect the result to its value and evidence. Never invent movement, success, causation or assurance to make the language sound positive.

## Keep conversations useful

Answer a direct question directly. Treat exploration as exploration. Report meaningful findings, decisions, changes and remaining uncertainties during work. A progress update should help the reader understand movement rather than list tool activity.

Use project terminology in conversations as well as files. Explain a proposed concept before building an argument around it. Expand only where the reader needs reasoning, evidence or a decision.

## Check four outcomes

| Outcome | Review question |
| --- | --- |
| Consistency | Does the same concept keep its meaning across code, decisions, tasks, documents and conversation? |
| Accessibility | Can a reader find the purpose, decision and implications without already knowing the implementation? |
| Readability | Do terms, sentences and paragraphs form a clear explanation at the required depth? |
| Repeatability | Can another author use the references and pattern to produce an equally navigable result? |

Mechanical checks can detect structural errors and selected vocabulary drift. Human or independent agent review must still assess meaning, navigation, evidence and cadence. Sentence length and reading-age scores are diagnostic signals, not acceptance criteria.

## Sources and local adaptation

These local conventions draw on [Microsoft's simple-word guidance](https://learn.microsoft.com/en-us/style-guide/word-choice/use-simple-words-concise-sentences), [Google's audience-aware jargon guidance](https://developers.google.com/style/jargon) and the [ISO 24495-1 public abstract](https://www.iso.org/standard/78907.html). They support reader-focused expression; they do not replace project meanings or establish ISO conformity. Context-aware terminology also draws on [DDD bounded contexts](https://martinfowler.com/bliki/BoundedContext.html), [SKOS labels and definitions](https://www.w3.org/TR/skos-reference/) and the [Good Docs terminology template](https://gitlab.com/tgdp/templates/-/tree/main/terminology-system). The registry is a local JSON model, not a formal SKOS implementation.
