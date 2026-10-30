# Choose a structure for the reader's task

Use these patterns as starting points. Preserve the project's existing format where it serves the same purpose. Omit irrelevant sections; add detail that changes understanding or a decision.

| Content | Reader's question | Suggested route |
| --- | --- | --- |
| Task | What should change, and how will we know? | Outcome → context → expected behaviour → acceptance examples → verification |
| Decision record | What did we decide, and why? | Status and decision → context and drivers → considered options → consequences → evidence |
| Architecture explanation | What is this for, and how does it work? | Purpose and effect → system boundary → principal decisions → mechanism → trade-offs → technical references |
| Tutorial | Help me learn this by doing it | Learning outcome → prerequisites → supported sequence → observed result |
| How-to guide | Help me complete this task | Goal → requirements → actions → verification → recovery where relevant |
| Reference | What is the exact contract? | Scope → names and definitions → inputs/outputs → behaviour and constraints → examples |
| Explanation | Help me understand why | Question → concept and context → relationships → reasoning and trade-offs → further detail |
| Marketing | Why should this matter to me? | Reader's need → value → credible evidence → next action |
| Dashboard | Where are we, and what is changing? | Result → movement → supporting evidence → next milestone or action |
| Conversation | What do I need from this exchange? | Answer or finding → supporting reasoning → implication, as needed |

The four documentation purposes above draw on Diátaxis. The decision pattern draws on ADR practice. These routes combine those ideas with Geekist's editorial conventions; they are not quotations or mandatory framework sequences.

For tasks and decisions, record open evidence questions alongside the next action, expected observation and any specific blocker. Keep implementation status separate from validation status. An untested proposal can justify a bounded prototype; it is not automatically a rejected option. Use `advance-with-uncertainty` when evidence language is causing work to halt or options to be discarded without a concrete constraint.

## Provide an entry point to technical material

For a substantial technical document, make the following easy to find:

1. **Purpose:** the problem and who is affected.
2. **Main point:** the decision, behaviour or finding.
3. **Consequences:** what changes for readers, users or maintainers, including material constraints.
4. **Terms:** short explanations near first use and links to accepted definitions.
5. **Detail:** contracts, mechanisms, examples and evidence under descriptive headings.

For example, a business reader of an authentication decision should be able to find who can gain access and who decides. An engineer should be able to continue to the permission checks, failure behaviour and protocol contracts. Both routes must describe the same authority model.

## Example: a technical decision with two routes

**Decision:** The application checks project membership before allowing a project operation.

**Why it matters:** Signing in establishes identity. Membership determines which project the person may work on. A connected identity service can supply information, while the application retains the project-access decision.

**Implementation:** Name the actual membership query, operation boundary and failure response here, using current source references. Include the case where identity is valid but membership is absent.

This example is invented. It illustrates information order rather than prescribing a particular project's authority model.

## Example: progress without changing the meaning

**Twelve of fifteen checks complete.** Three checks finished in the latest run. The remaining checks cover source availability.

If the domain also supplies a confidence score, show it separately and explain its calculation. Completed checks alone do not justify a confidence percentage.

The numbers are illustrative. Use real run events for a live interface.

## Review a completed artefact

Ask one reader familiar with the implementation and one reader outside that specialism to find the main point, explain its consequence and locate the relevant detail. Record where either reader needed to guess. Use an independent agent as a preliminary review when useful, and label it as agent review rather than human comprehension evidence.

Use a fresh request with the same references to check repeatability. Compare retained facts, terminology and navigation rather than identical wording.
