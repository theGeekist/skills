# Changelog and provenance

## v2.4.0 (current)

**Trigger:** the pattern taxonomy's attribution ran through `blader/humanizer` throughout the README and this file, its 33-pattern list, its version number, its category names, even though humanizer's own README states plainly that it's "Based on Wikipedia's 'Signs of AI writing' guide, maintained by WikiProject AI Cleanup." Citing the secondary repackaging as the reference point rather than the primary source it draws from was imprecise sourcing, the same category of issue (though lower stakes) as the fabricated-citation correction in v2.0.0. Requested fix: cite Wikipedia directly, verified against the live page rather than assumed from memory, and keep `blader/humanizer` to a Credits-only mention.

**What was verified before changing anything:** fetched `en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing` directly and confirmed its section structure (Content; Language and Grammar; Style; Communication Intended for the User; Markup; Citations; several smaller sections) and its own stated evidence base ("observations, not rules," drawn from real examples across Wikipedia articles, drafts, and comments, maintained by WikiProject AI Cleanup). Also fetched `en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup` to confirm what "participant" actually means there (self-adding to a public list via a Wikipedia account), specifically to avoid writing an unverifiable affiliation claim into this project's own README, the same discipline Section 4 asks of every draft this skill produces.

**What changed:**

- `references/plain-style-diagnostics.md`'s intro now cites the Wikipedia guide directly as the primary source for Clusters A through C's empirical grounding, separate from Orwell's essay (still the primary source for the four-fault section).
- New README "References" section: the Wikipedia guide as primary source, WikiProject AI Cleanup as its maintaining organization, both linked. No claim of project participation or affiliation, only citation, matching how humanizer's own README credits the same two sources.
- README's "Coverage" section rebuilt from the guide's own Content, Language and Grammar, Style, and Communication sections rather than humanizer's numbered list, with the guide's Wikipedia-specific markup and citation items (broken wikitext, invalid DOIs, `utm_source` parameters, and similar) explicitly named and excluded as out of Bespoke's scope, not silently dropped.
- `blader/humanizer` now appears only in Credits, reframed as the tool early development was benchmarked against, itself downstream of the same Wikipedia guide, rather than as the ongoing comparison point.

**What this doesn't do:** no pattern coverage changed. Every mapping in the rebuilt table points to the same `plain-style-diagnostics.md` and `typographic-markers.md` locations the old humanizer-keyed table pointed to; only the left-hand column's source and the surrounding framing changed. Historical changelog entries below that describe benchmarking against humanizer are left as written, they're an accurate record of what happened at each point in this project's history, not a claim about where the project's sourcing stands today.

## v2.3.0

**Trigger:** the intake asked for a voice sample when none existed, but never posed the own-style-or-default choice explicitly, and had no enforced minimum on what counted as "a sample." In practice this let a few adjectives ("direct, a little dry") stand in for a real fingerprint, exactly the weak signal Section 1 already argued against in its own closing line. Requested fix: an explicit choice, own style or default, and a hard 100-word floor on what "own style" accepts.

**What changed:** `SKILL.md`'s intake item 1 (Voice) now asks the own-style-or-default question directly rather than defaulting to a sample-or-adjectives request. Section 1 gained a new subsection, "The own-style-or-default gate," specifying: own style requires a real sample (essay, article, blog post, past social post, email) of at least 100 words, with an explicit instruction to ask for more if under that floor rather than build a fingerprint from too little data; default explicitly waives the personal fingerprint while keeping every plain-style and typographic default in force; adjectives alone no longer satisfy either path. The exception carried over unchanged: a real 100+ word sample pasted unprompted, or Section 8's fixed personal-voice skill, resolves the choice without asking.

**What this doesn't do:** no pattern in `plain-style-diagnostics.md` or `typographic-markers.md` changed, and Sections 2 through 9 are untouched. This is entirely an intake-mechanics change, tightening how the Voice question gets asked and validated, not what the skill does once Voice is answered.

## v2.2.1

**Trigger:** the skill was installed locally and run for the first time end-to-end (previous versions were validated by reading, not by invocation), specifically to produce a second worked example for `README.md` demonstrating Section 1 (voice fingerprint) and Section 4 (specificity test) on a short, unformatted personal narrative, layered under a separate fixed personal-voice skill per Section 8, rather than the mostly-structural/typographic before/after already in the README.

**What changed:** README-only. Added "Before / after example 2," a fictional, non-identifying short narrative (a Kuala Lumpur date that turns into a photoshoot) run through the actual installed skill rather than hand-written to spec, with the fixed personal-voice skill's rules (no em dashes, zero cap on unsupported facts, an acid test against real named entities, burstiness, grade 6-7 readability) standing in for Bespoke's generic Voice defaults. No change to `SKILL.md`'s instructions or to any pattern in `plain-style-diagnostics.md` or `typographic-markers.md`; version bumped for traceability of the README content change, matching this project's practice of logging every content change rather than only instruction changes.

## v2.2.0

**Trigger:** a full, line-by-line audit against `blader/humanizer`'s complete 33-pattern taxonomy (v2.9.1, the same version v2.1.0 was benchmarked against), requested to confirm Bespoke has no remaining coverage gap against it. v2.1.0 had closed the largest gap (typography, borrowed authority, decorative structure, borrowed register); this pass checked the rest pattern-by-pattern rather than assuming parity.

**What the audit found:** three patterns with no dedicated equivalent (significance/legacy inflation and promotional/brochure language, both content-level puffery; the full high-frequency AI-vocabulary list; passive voice and subjectless fragments as a named, concrete pattern rather than an implication of Orwell's Fault 2), two patterns present only as a side effect rather than a named, checkable item (filler phrases; excessive hedging), and one deliberate design difference worth tightening: the em-dash default was calibrated as "rare," where humanizer treats it as a hard zero-default constraint with an explicit pre-delivery scan. All were closed in this version. See the diff in `plain-style-diagnostics.md` and `typographic-markers.md` for specifics; summary below.

**What was added, and where it lives:**

- **Significance/legacy inflation and promotional/brochure language**: added as two named sub-families under Fault 1 (dying metaphors) in `plain-style-diagnostics.md`, since both are dying metaphors by mechanism, puffery reached for instead of stating the fact plainly, just with their own recognizable phrase sets (humanizer's patterns #1 and #4).
- **The high-frequency AI-vocabulary list** (additionally, align with, crucial, enhance, fostering, garner, interplay, intricate, key, landscape, pivotal, showcase, underscore, valuable, and more): added under Fault 3 (pretentious diction), explicitly tied back to Section 1's stylometry framing, that the tell is anomalous *rate*, not any single word, which is a more rigorous frame than a flat banned-word list (humanizer's pattern #7).
- **Passive voice and subjectless fragments**: given a named, concrete treatment with a before/after example under Fault 2, rather than left as an implication of "prefer active voice" (humanizer's pattern #13).
- **Filler phrases** ("in order to," "due to the fact that," "at this point in time," and similar): given an explicit stock-phrase list under Fault 2, alongside the verbal-false-limb mechanism that already covered the general case (humanizer's pattern #23).
- **Excessive hedging, generic positive conclusions, definitional throat-clearing openers, and recap/meta-commentary closings**: new Cluster D ("hedging, throat-clearing, and empty closes") in `plain-style-diagnostics.md`. The first two map to humanizer's patterns #24 and #25; the latter two have no equivalent there.
- **Uniform transition-word rotation and structural symmetry addiction**: new Cluster E ("mechanical uniformity"), patterns visible only across a whole document or section rather than in a single sentence. Neither has an equivalent in humanizer's taxonomy or, so far as this project's research turned up, in any comparable published AI-tell list.
- **Em dash default hardened**: from "treat as rare" to "none by default," with an explicit pre-delivery scan for `—`, `–`, spaced hyphens, and doubled hyphens, matching humanizer's hard-constraint treatment. The override principle is unchanged and, if anything, more explicit: a real voice sample showing regular em-dash use still wins over the default outright.
- **Presence, not just absence** (`SKILL.md` Section 9, new): a section with no humanizer equivalent by name, though humanizer's "PERSONALITY AND SOUL" gestures at the same problem. Removing every flagged pattern and adding nothing back produces sterile prose, a different failure with the same symptom (a reader who doesn't believe a person wrote it). Grounded in Section 3's existing formulaic-language argument rather than added as a bare directive: uneven rhythm, real stance, unresolved mixed feelings, and genuine self-correction, gated by the same content-type judgment Section 6 already applies to engagement tactics, and bounded by Section 4's no-fabrication rule throughout.
- **Invocation modes** (`SKILL.md` Section 10, new): pasted-text, file, and embedded modes, matching humanizer's functional coverage (added there in v2.9.0) but written to fit Bespoke's own intake-and-fingerprint workflow rather than adapted from humanizer's wording.
- **An explicit self-audit step**: Application workflow step 5 now asks two direct questions of the draft ("what still reads as generated," "does anything state a fact not in the source") before the final rewrite, matching the audit loop in humanizer's Process and Output section, applied to Bespoke's own specificity-test language rather than restated from humanizer's.
- **Expanded false-positive guidance**: `plain-style-diagnostics.md`'s "What NOT to flag" section grew from 4 items to 15, folding in humanizer's detection-guidance false-positive list (perfect grammar, mixed register, formal vocabulary alone, letter-style sign-offs, a single transition word, curly quotes alone, unsourced claims alone, secondhand/quoted text) alongside Bespoke's existing items.

**What this doesn't do:** none of the above required touching Sections 1 through 8 of `SKILL.md`, which still work exactly as v2.1.0 left them; every addition either extends an existing reference file or appends a new numbered section rather than restructuring what was already there. No pattern was removed or weakened to make room for a new one.

## v2.1.0

**Trigger:** a direct, critical comparison against `blader/humanizer` v2.9.1, requested after v2.0.0 shipped, turned up a real regression rather than a purely stylistic trade-off. Rebuilding away from humanizer's category structure to fix v1's architectural over-dependence (see v2.0.0 below) had also cut real coverage: roughly a third of humanizer's 33 named patterns, including em dashes, arguably the single most recognizable AI-writing tell, had no equivalent anywhere in v2.0.0.

**What was added, and where it lives:**

- **Typography and formatting** (em dashes, curly quotes, Title Case headings, boldface density, inline-header lists, hyphenated-compound overuse, emoji): new file `typographic-markers.md`, framed through Section 1's voice-fingerprint concept rather than as a flat ban list. The default (rare em dashes, sentence-case headings, and so on) is explicitly a calibration absent a sample, not a permanent rule; a real sample that contradicts the default wins.
- **Vague attribution, notability namedropping, persuasive authority tropes** ("borrowed authority," Cluster A in `plain-style-diagnostics.md`): grouped as ways a sentence implies credibility it hasn't earned, tied to both Orwell's pretentious diction and the specificity test in `SKILL.md` Section 4.
- **Synonym cycling, false ranges, negative parallelisms/tailing negations, fragmented headers, manufactured punchline runs, aphorism formulas** ("decorative structure," Cluster B): folded in alongside the patterns already present (rule-of-three, metaphor stacking, thesis repetition, copula avoidance, signposting).
- **Chatbot artifacts, sycophantic tone, conversational rhetorical openers** ("borrowed register," Cluster C): framed as correspondence-shaped or performed language leaking into content that isn't correspondence, cross-referenced from `SKILL.md` Section 5.
- **Cutoff disclaimers and speculative gap-filling**: not placed in the pattern-list file at all. Folded directly into `SKILL.md` Section 4 as a concrete example of what fails the specificity test, since dressing an unknown as narrative is a fabrication mechanism, not a phrasing tell, and belongs with the CBCA-based construction checklist rather than a word list.
- **The despite-challenges formula, diff-anchored writing, superficial "-ing" tack-ons**: added as paragraph-level instances of Orwell's verbal-false-limb pattern (Fault 2), since each pads a paragraph the way a verbal false limb pads a sentence.

**What this doesn't do:** revert to humanizer's own category names or numbering. Every addition above sits inside one of Bespoke's existing frames (the voice fingerprint, Orwell's four faults, the specificity test, borrowed authority/structure/register) rather than being appended as a flat, renumbered list. The goal was closing a real functional gap without reintroducing the structural mimicry v2.0.0 was built to fix.

**Also fixed:** a stale internal cross-reference in `SKILL.md`'s intro, which pointed to Section 5 for the AI-detector note when the actual content is in Section 7.

---

## v2.0.0

**Trigger for this rewrite:** v1.0.0 (below) was built after benchmarking against `blader/humanizer`, an existing open-source AI-tell removal skill. v1 organized its tell taxonomy under the same category scheme humanizer uses (content-level, grammar-level, structural, filler/hedging), and its packaging (`AGENTS.md`, `.claude-plugin/`, CI workflow) closely mirrored humanizer's actual repository structure, which had been fetched directly during development. The content was original, the wording was original, but the shape of the thing was a close structural echo of the tool it was benchmarked against.

**What changed and why:** rebuilt from independent research instead of from a comparative audit. The previous version's core weakness wasn't plagiarism, the words were original, it was architectural dependence: reasoning that starts from "here's what humanizer does, now do it better" produces something shaped like humanizer even when every sentence is new. v2 starts instead from four independent, established, verifiable bodies of research that have nothing to do with AI-tell removal as a category:

- **Stylometry and authorship attribution** (Mosteller and Wallace, 1964; Stamatatos, 2009) for what a real voice fingerprint actually consists of.
- **Orwell's "Politics and the English Language"** (1946) for a principled, pre-AI account of why prefabricated language reads as hollow, with a diagnosis ("gone some distance toward turning himself into a machine") more precise than any list of buzzwords.
- **Formulaic language psycholinguistics** (Alison Wray) for why eliminating all pre-formed phrasing is the wrong goal, and what the right one is instead.
- **Criteria-Based Content Analysis and Reality Monitoring** (Undeutsch; Steller and Köhnken, 1989), forensic-psychology research on what separates genuine, experience-based accounts from fabricated ones, repurposed here as a construction checklist rather than a detection tool.

Humanizer's 33-pattern taxonomy is real, useful, and covers ground worth covering. It's now one smaller supporting file (`plain-style-diagnostics.md`'s second section) folded under Orwell's four-fault framework rather than the organizing structure of the whole skill. The packaging (`AGENTS.md`, plugin manifests, CI) still follows the correct external schemas for Claude Code plugins and GitHub Actions, those are platform requirements, not humanizer's invention, but the wording was rewritten independently rather than adapted from humanizer's actual files.

**What this means concretely:** `SKILL.md`'s operational instructions no longer compare themselves to humanizer anywhere. The comparison lives in exactly one place, this file, as attribution for where the benchmarking started, not as the skill's ongoing frame of reference.

---

## v1.0.0

Initial build. See the v2.0.0 entry above for what was wrong with its approach and why it was rebuilt.

## Sources that shaped the original brief

1. `elite-communication-codex`, a prior skill whose structuring techniques informed early drafts.
2. A research document on AI-detection science (see `detection-science.md` for a citation-fabrication correction found in it).
3. A content-formula document on platform-favored writing patterns.
4. A "Content Refiner" persona prompt, the source of the four-input intake (Voice, Task, Audience, Intention) that still structures `SKILL.md`'s opening workflow.

## What was rejected or gated, and why

**The research document's specific statistics** (per-model buzzword frequencies, detection-evasion percentages, embedding-dimension figures) were excluded after two spot-checked citations turned out to be fabricated or mismatched. Full detail in `detection-science.md`.

**Deliberate-inaccuracy engagement tactics applied to published, audience-facing content** were gated rather than adopted by default. Full reasoning in `engagement-ethics.md`.

**Targeting a specific AI-detector score as the definition of success** was rejected as the skill's verification method, in favor of the specificity and voice-fidelity checks in `SKILL.md` Sections 1 through 4.

## Naming

Considered: Signature (fine, more generic). Idiolect (the linguistically precise term, and now a genuinely apt one given Section 1's grounding, but rejected again for being obscure and four syllables). Kept **Bespoke**: made to order for one specific person, not off a generic rack, which is the actual mechanism this skill now implements at every layer, not just a tagline.

## Note for this skill's original author

This skill was built in the same working session as two companion skills for personal use: a fixed brand-voice skill and a high-intensity live-communication skill. Bespoke is the general-purpose version of the underlying engine, with the private calibration stripped back out so it stands alone. See `SKILL.md` Section 8 for how to layer a fixed personal-voice skill on top of Bespoke if you maintain one; nothing in this repository requires it.
