---
name: write-project-content
description: Write or review tasks, decision records, architecture explanations, developer documentation, product content and conversation examples using established project meaning and clear reader navigation. Use when drafting or revising these artefacts for consistency, accessibility, readability and repeatability across technical and business audiences.
---

# Write project content

Help the reader find the main point, understand its implications and continue to the detail they need. Preserve technical precision and established project meanings.

Read [writing conventions](references/writing.md). Select a structure from [content patterns](references/content-patterns.md); use [the drafting prompts](assets/drafting-prompts.md) when a starting outline helps.

## Establish the task

Identify the reader, their purpose and the requested artefact. Infer these from available context before asking a question. Read repository instructions, current terminology and the source material needed to support the claims. Include declared authority or planning paths that begin with a dot; inspect tracked or hidden files rather than relying on ordinary globs. Identify the authoritative decision when sources disagree; explain unresolved disagreement rather than silently inventing a resolution.

Use accepted terms consistently within their context. Mark proposed concepts explicitly. Introduce unfamiliar terms near first use. Preserve exact code identifiers, protocol names and quotations.

## Draft a navigable explanation

Lead with purpose and the main finding or decision. Explain consequences before optional mechanisms. Use descriptive headings and meaningful links for longer material. Give an engineer a direct route to contracts, constraints and evidence, while allowing a marketing reader to understand what the document is for and what its main decision changes.

Choose the documentation purpose: learning by doing, completing a task, looking up a contract, or understanding a concept. Avoid mixing them without a clear reason and route.

For customer-facing content, connect outcomes to value and supporting evidence. Keep results, confidence, coverage and progress separate wherever the domain distinguishes them. Derive movement from real events; label examples and estimates clearly.

For conversation examples, match the depth to the exchange. A direct question may need one sentence. An investigation may need evidence and trade-offs. Report meaningful changes during work.

## Review the result

Check meaning against source material before editing for style. Verify that a reader can find the purpose, main point, consequences and technical detail. Check first-use explanations, heading hierarchy, link text and text alternatives for essential visuals.

Use configured vocabulary and prose checks where available. Treat their findings as specific signals. Review accuracy, coherence, evidence and reader navigation independently.

For consequential documents, ask an independent reader or agent to locate and explain the main decision using only the artefact and its linked references. Test a second request against the same material to assess repeatability. Record whether this was human review, agent review or a deterministic check.

Deliver the requested artefact with material limitations or unresolved decisions. Avoid appending an editorial checklist to ordinary user-facing copy.

For tasks, ADRs and handoffs with evidence gaps, apply [the uncertainty conventions](references/uncertainty.md) or use `advance-with-uncertainty`. Distinguish implementation progress from validation. Pair a consequential gap with the next action and a specific blocker only where it prevents a named step.
