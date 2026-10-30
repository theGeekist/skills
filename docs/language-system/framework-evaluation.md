# Framework and tooling evaluation

Reviewed 29 October 2026. This evaluates the supplied research against primary sources and small executable experiments. It recommends a light shared language system, with selected rules and references loaded for the task. It does not establish production runtime support or certify compliance with a standard.

## What to adopt

Use domain discovery to establish meaning, plain-language guidance to explain it, document patterns to organise it, and checks to catch repeatable mistakes. Keep these responsibilities distinct. A spelling dictionary cannot settle a domain disagreement; a readable sentence can still make a false claim.

| Foundation | Decision | Fit and limits |
| --- | --- | --- |
| DDD and bounded contexts | Adopt | Establish meaning within a context and explicit translations across contexts. Retain a project's vocabulary where it expresses the intended meaning. [Source](https://martinfowler.com/bliki/BoundedContext.html). |
| ISO 704:2022 | Reference | Official abstract establishes terminology principles covering concepts, definitions and names. Full normative text was not purchased or assessed. Borrow the concept-first discipline without claiming conformity. [Source](https://www.iso.org/standard/79077.html). |
| ISO 24495-1:2023 | Reference | Supports reader-centred plain-language documents, including technical writing. Assess whether readers can understand and use the material. Full normative text was not acquired. [Source](https://www.iso.org/standard/78907.html). |
| W3C SKOS | Adapt | Stable concept identifiers, preferred/alternative labels, definitions and relationships are useful. A JSON registry can borrow these ideas without claiming to be RDF or SKOS-conformant. Add formal export when needed. [Source](https://www.w3.org/TR/skos-reference/). |
| Diátaxis | Adopt selectively | Use tutorial, how-to, reference and explanation to choose a document's purpose. A short task or conversation need not become four documents. [Source](https://diataxis.fr/start-here/). |
| Good Docs Project | Adopt selected templates | Downloaded concept, how-to and terminology templates offer practical structures. Start from a reader need; remove optional boilerplate. Its terminology template already includes alternatives, rejected terms and sources: this is reusable work, not a gap to invent. [Source](https://gitlab.com/tgdp/templates). |
| MADR | Adopt minimal variant | Record one decision, context, options, outcome and consequences. Preserve the existing project's ADR convention if it already works. Downloaded templates inspected. [Source](https://adr.github.io/madr/). |
| arc42 | Use as a completeness reference | Context, runtime, deployment, quality and glossary views help architecture navigation. Choose relevant views rather than requiring twelve sections for every change. Downloaded template and licence inspected. [Source](https://arc42.org/overview/). |
| Information Mapping | Reference | Its public six information types help select a table, procedure or explanation. The public help page is not a licence to redistribute proprietary training or claim a converted implementation. [Source](https://support.informationmapping.com/hc/en-us/articles/213446789-Present-your-information-in-a-clear-and-consistent-way). |
| DITA | Defer publishing infrastructure | Useful structured-topic and reuse principles; XML infrastructure adds little to this small Markdown collection. The official index lists DITA 2.0 as a draft. [Source](https://dita-lang.org/specifications). |
| ASD-STE100 | Defer adoption | Official site returned HTTP 403 during this evaluation. Issue dates and precise rule counts from the baseline remain unverified here. Do not impose a controlled aerospace dictionary across marketing and conversation. [Candidate source](https://asd-ste100.org/). |

Microsoft's consistent terms and concrete verbs, Google's advice to introduce necessary jargon, and Atlassian's situational UI tone can inform concise local rules. They do not justify combining entire corporate style guides. The Google jargon page explicitly recognises specialist readers and searchable terminology. Atlassian separates public UI/app guidance from its internal marketing guidance. Sources: [Microsoft](https://learn.microsoft.com/en-us/style-guide/word-choice/use-simple-words-concise-sentences), [Google](https://developers.google.com/style/jargon), [Atlassian](https://atlassian.design/foundations/content/voice-tone/).

The GOV.UK source redirected to another redirect page; substantive replacement content was not retrieved. Keep it as a candidate rather than presenting it as evaluated in this pass.

## Accessibility across audiences

A marketing reader should be able to enter a technical document through its purpose, relevant terms and consequences, then follow links into detailed contracts and implementation. An engineer should be able to reach those details directly. Test both routes against the same meaning.

The local acceptance questions should be:

1. Can the reader identify what the page answers and whether it applies to them?
2. Are unfamiliar project terms introduced where needed, with definitions reachable at the point of use?
3. Do headings and links expose the next useful level of detail?
4. Do examples make the behaviour concrete without inventing capabilities?
5. Does a summary preserve material limits and connect to the full evidence?
6. Can a second author follow the same references and produce consistent meaning?

Sentence length is a diagnostic, not a proxy for accessibility. This language work also does not replace rendered-content checks for keyboard access, contrast, semantic headings, alternative text or screen-reader behaviour. The ISO public abstract explicitly distinguishes plain-language guidance from technical digital-accessibility guidance.

## Tools installed and exercised

All experiments were isolated outside the repository under `../evaluation`. No system-wide or user-agent configuration was changed. Versions and checkout commits, raw fixture alerts and the binary hash are in [sources.json](sources.json).

| Tool | Observed version | Executed check | Decision |
| --- | --- | --- | --- |
| Vale | Binary 3.25.1; Python wrapper 3.25.1.0 | Upstream Diataxis suite and custom Google/Diataxis cases | Adopt selected project rules; keep contextual heuristics advisory |
| Agent Skills `skills-ref` | 0.1.0 | Both existing architecture skills validate | Adopt as portable shape validator |
| textlint | 15.8.0, with `no-todo` 2.0.1 | Correctly reports a TODO marker | Defer a second prose engine until a needed rule justifies it |
| CSpell | 10.4.0 | `en-GB` accepts `organisation`/`colour` and catches `qzxfoobar` | Optional spelling complement; build a project dictionary first |

These are smoke tests, not comparative performance or broad accuracy benchmarks. `skills-ref` checks packaging; it cannot show that a skill makes sound architecture decisions. CSpell accepts words without understanding their project meaning.

### Vale package results and false positives

Diataxis v0.1.0's own suite passed **40 rule cases with zero failures**. Four deliberately flawed fixture documents produced 7, 6, 6 and 4 alerts respectively; all four clean fixtures passed. The advertised 20 rules and version are confirmed. [Package](https://github.com/jdkato/diataxis), [explorer](https://vale.sh/explorer/diataxis).

Two additional valid documents exposed limits:

- An explanation contrasted a shared queue with per-project queues and explained their effect on contention. `Explanation.Why` still fired because none of its causal trigger phrases appeared. It checks vocabulary, not explanatory reasoning.
- A field reference with a valid description table triggered `Reference.Examples` solely because it lacked a fenced code block. A code example may improve some references; it is not necessary for every reference.

The Google package produced five alerts on a short agent-status sample: `CLI`, `I`, `will`, generic `Cloud`, and British `colour`. Those policies conflict with this task's audience and register; the `Cloud` suggestion even changed a generic term into a Google product. This is evidence against blanket package adoption, not a defect claim against rules designed for Google's own documentation.

Keep rule names, matched spans, context and the author's disposition visible. Promote an advisory rule to a failing check only after testing representative acceptable and unacceptable examples, including code, quotations and British English. Do not automatically rewrite identifiers or domain terms.

## Agent capabilities: documented versus tested

The [Agent Skills specification](https://agentskills.io/specification) supports `SKILL.md` with required name/description and optional scripts, references and assets. The optional `license` and `metadata` fields already used by this repository are valid. Skills should remain task-specific; their activation is not evidence of an always-on conversation policy.

[Codex AGENTS.md guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md) documents global and project instructions, overrides and a combined size cap. Small persistent rules can point at task-relevant references; installation alone does not prove that a given runtime loaded them.

[Codex hooks documentation](https://learn.chatgpt.com/docs/hooks) confirms `Stop` input fields `last_assistant_message` and `stop_hook_active`. A `decision: "block"` plus `reason` requests continuation; it does not erase an already displayed response. Guard against repeated continuation. Cloud orchestration excludes local command/shell hooks and hooks from local configuration/plugins. Managed remote MCP hooks have separate enterprise conditions. The recorded hook evaluation covers subprocess payload behaviour; it does not establish native host integration.

[Claude Code](https://code.claude.com/docs/en/hooks) documents lifecycle hooks and a Stop protocol. [Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) documents repository-wide, path-specific and agent instructions. These sources establish integration routes; no Claude or Copilot runtime was exercised. CLI, desktop and cloud need separate compatibility evidence. Do not infer support across products from a shared format.

## Corrections and remaining evidence

Preserve the original research as a historical baseline, with these qualifications:

- **DITA 2.0:** the official index calls it a draft; the baseline's unqualified standard wording should be corrected.
- **Diataxis Vale package:** version 0.1.0, 20 rules and 24 September 2026 are confirmed by the official explorer, but tests expose semantic false positives.
- **Hooks:** the Stop mechanism is documented; end-to-end correction and displayed-message behaviour remain untested. Cloud and local support differ materially.
- **October 2026 Google update:** not established by the inspected jargon page, which displays a 2025 date. Do not repeat the particular update claim without its changelog source.
- **ISO/STE adoption:** public abstracts and references are not full-standard audits or redistributed standards. No full-standard conversion or compliance certification was performed.
- **Reader comprehension:** local checks and examples need human review with engineering and non-engineering readers. A passing linter is not evidence that those readers can use the material.

## Reproduction and maintenance

Use the commit hashes in `sources.json` when checking out downloaded references. Python setup used `python3 -m venv ../evaluation/venv`, then `pip install vale==3.25.1.0` and the pinned `agentskills/skills-ref` checkout. The first Vale invocation downloads its binary; the recorded SHA-256 identifies the tested executable. In `evaluation/diataxis-vale`, run `PATH=../venv/bin:$PATH ./test.sh` after resolving the path for the current shell.

The custom Vale cases and results are embedded in the manifest as observed alerts; their complete input text is recorded below for repeatability. Install optional JavaScript candidates with exact versions and a lockfile in an isolated directory; none belongs in the core skill runtime by default.

```markdown
# Run the CLI

I will investigate the Cloud worker and report the result.

The organisation stores colour preferences locally.
```

```markdown
# Per-project queues

A shared queue lets one busy project delay every other project. Per-project queues isolate that contention, giving each project an independent scheduling budget.
```

```markdown
# Build result

The result includes a status and an output path.

| Field | Description |
| --- | --- |
| status | Current build state |
| output | Generated file path |
```

Select `Google` for the status sample, `Explanation` for the queue explanation and `Reference` for the field table. The Diataxis package contains separate styles by document type; the explorer's generic `BasedOnStyles = Diataxis` example is insufficient for those styles as downloaded. Its repository README supplies the working type-specific configuration.

Check licences per downloaded resource. Good Docs templates are MIT-0; MADR offers MIT or CC0-1.0; arc42 template adaptations carry CC BY-SA 4.0 obligations. Vale Google rules are MIT, while the Diataxis rules include a NOTICE acknowledging the framework's separate licence. Keep third-party texts and notices separate from the repository's original MIT guidance. Recheck sources and rule behaviour when versions change.
