# Maintain meaning and guidance through change

## Start with the right evidence

For a new project, begin with scenarios, actors, outcomes and candidate concepts. For an existing project, inspect current instructions, decisions, contracts, schemas, tests and product language. Record source paths and revisions. Discovering a name establishes evidence of use; it does not resolve a conflicting meaning.

## Lifecycle and completion criteria

| Part | Stages | Ready for use when | Revisit when |
| --- | --- | --- | --- |
| Terminology | Discover → compare → propose → adopt → use → revise or retire | Definitions are distinct, contexts clear, sources recorded and acceptance explicit | Meaning, contract, schema or audience interpretation changes |
| Shared reference | Research → verify → evaluate → adapt → validate → maintain | Provenance, permissions and limitations are recorded; guidance works on examples | Source changes, repeated confusion or conflicting rules appear |
| Skill | Need → implement → validate format → forward-test → release → revise | Trigger fits the task, references load independently and behaviour survives representative cases | Missed activation, scope creep, failed examples or stale references |
| Persistent instruction | Identify repeated need → write small rule → test → adopt | Rule applies throughout the intended scope without loading a full handbook | It conflicts with local instructions or adds irrelevant context |
| Hook or client adapter | Verify host capability → implement → subprocess-test → host-test → opt in | Exact event semantics and local runtime behaviour are demonstrated | Client version or execution mode changes |
| Artefact | Reader and purpose → source meaning → choose structure → draft → review → publish → maintain | Readers find purpose, main point, consequences and detail; claims match sources | Behaviour, decision, audience need or linked source changes |
| Conversation | Read context → answer or investigate → explain meaningful findings → review | Depth fits the exchange and terminology remains consistent | New concepts, changed decisions, compaction or reader correction |

## Change responsibilities

The contributor proposes a change with sources and affected uses. The normal repository reviewer or authorised user resolves a consequential domain change. The document author checks navigation and evidence. The adapter maintainer verifies runtime support. These are roles in the existing workflow rather than new mandatory job titles.

Adopt a routine wording improvement through the normal change. Use a decision record for changed meaning, authority or compatibility. Retain stable IDs when labels change. Mark obsolete concepts deprecated and record a replacement where one exists.

## Apply a change consistently

Search affected code contracts, tasks, decisions, documentation, interfaces and agent instructions. Identify which uses share the context before replacing words. Preserve machine identifiers and historical quotations unless the actual change includes them.

Update the canonical reference first, regenerate bundled copies and run drift checks. Test representative examples before widening adoption. Keep runtime-specific code in adapters; never copy a new domain definition into each agent's instruction file.

## Measure repeatability

Record the prompt, source revision, skill revision, output and evaluation. Repeat with fresh context against the same sources. Check retained facts and navigable structure; identical prose is unnecessary. Separate mechanical results, qualitative agent assessment and human reading evidence.

Promote a check to a blocking gate only after testing meaningful positive and negative cases. Preserve a clear exception path for domain-specific language. Review false positives and regressions with actual examples.

## Keep uncertainty actionable

Evidence state and implementation state evolve separately. Use [the uncertainty conventions](../../standards/uncertainty.md) when an unresolved claim affects a task, decision or handoff. Record the next bounded action and completion evidence. A concrete blocker should identify the dependent step and resume condition; independent authorised work can continue.
