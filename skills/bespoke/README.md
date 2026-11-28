# Bespoke

A portable agent skill that builds writing from a specific person's real voice, grounded in four established, independent bodies of research rather than a fixed list of banned phrases:

- **Stylometry and authorship attribution** for what an individual's actual linguistic fingerprint consists of (function words, sentence-length variance, recurring phrase patterns), the same class of evidence used in forensic authorship analysis since the statistical study of the disputed Federalist Papers.
- **Orwell's plain-style diagnostics**, from "Politics and the English Language" (1946), for a principled account of why prefabricated phrasing reads as hollow, eight decades before anything resembling AI-generated text existed.
- **Formulaic-language psycholinguistics**, for why the goal is swapping shared, generic phrasing for a writer's own recurring language, not eliminating pre-formed phrasing altogether.
- **Forensic content-analysis criteria** (Criteria-Based Content Analysis and Reality Monitoring) for what distinguishes genuine, specific, lived detail from plausible-sounding invention.

It is plain Markdown with zero external dependencies: no API keys, no build step, nothing to install to use it. Full sourcing for all four is in `references/`.

## Installation

### Skills CLI

Install with the cross-agent [skills CLI](https://www.npmjs.com/package/skills):

```bash
npx skills add blisse-code/bespoke --global
```

Update an existing install:

```bash
npx skills update bespoke --global
```

To install into every supported agent harness on your machine:

```bash
npx skills add blisse-code/bespoke --global --agent '*'
```

Omit `--global` for a project-local install that can be committed and shared with collaborators.

### Claude Code plugin

```
/plugin marketplace add blisse-code/bespoke
/plugin install bespoke@bespoke
```

The skill is then invoked as `/bespoke:bespoke`.

### Manual

Any agent harness can use the skill directly because the runtime artifact is `SKILL.md`. Copy it, and the `references/` folder alongside it, into wherever your harness expects skill directories:

```bash
git clone https://github.com/blisse-code/bespoke.git /path/to/your/skills/bespoke
```

Or, if you already have this repo cloned:

```bash
mkdir -p /path/to/your/skills/bespoke
cp -r SKILL.md references /path/to/your/skills/bespoke/
```

### Claude.ai

Upload `SKILL.md` and the `references/` folder as a `.skill` file (zip the repo, excluding `.git`, `.github`, and `.claude-plugin`) through Settings → Capabilities → Skills.

## Usage

Invoke however your harness exposes installed skills. Common forms:

```
/bespoke

Write in my voice: [paste a LinkedIn post topic]
```

```
Humanize this: [paste AI-sounding text]
```

The skill opens with a short intake if it doesn't already know your voice, platform, audience, and intention for the piece. Voice is an explicit choice, your own style or Bespoke's default, not a request for adjectives:

```
Voice: own style
[paste at least 100 words of your own past writing, an essay,
 article, post, or email you actually wrote]
Task: LinkedIn post about a product launch delay
Audience: my team and a few clients who are already annoyed
Intention: own the delay without sounding defensive
```

From a real sample like that, Bespoke reads sentence-length pattern, function-word habits, and recurring phrases (Section 1) rather than working from a self-description. The profile that comes out of one might read, in Bespoke's own shorthand, as something like "direct, a little dry, no corporate hedging", but that's Bespoke's inference from your material, not something you type in yourself. Under 100 words, it'll ask for more before building anything from it. Say `Voice: default` instead to skip a personal fingerprint entirely and get Sections 2 through 4's plain-style discipline without one.

## Before / after example 1: structural and typographic tells

*(Illustration note: the "before" is a representative generic-AI-written passage, not a real product announcement. The "after" applies the voice profile from the intake example above, direct, a little dry, no corporate hedging, and adds a few concrete specifics, like "three teams asked" and "check Settings," that stand in for the kind of real detail a user would supply in an actual session. Bespoke doesn't invent those in practice; it asks for them or leaves the sentence plain. See Section 4's specificity test.)*

**Before (generic AI-written text):**

> ## 🚀 Introducing Smart Scheduling: A Game-Changer for Your Workflow
>
> We're thrilled to announce the launch of Smart Scheduling, a feature that stands as a testament to our commitment to innovation, efficiency, and user delight. This pivotal update marks a key turning point in our platform's evolving landscape.
>
> **Intelligent Automation:** Intelligent automation ensures your calendar stays perfectly organized.
> **Seamless Integration:** Seamless integration means Smart Scheduling works effortlessly with the tools you already love.
> **Real-Time Sync:** Real-time sync keeps everyone — teammates, clients, and stakeholders — on the exact same page.
>
> In order to fully leverage this robust new capability, users simply need to enable it in Settings. It could potentially possibly make a meaningful difference for teams juggling multiple calendars.
>
> Additionally, Smart Scheduling isn't just a tool — it's a philosophy. It's not about saving time, it's about giving that time back to what truly matters. Whether you're a solo founder, a growing startup, or an established enterprise, Smart Scheduling has something for everyone.
>
> We hope this helps streamline your day! Let us know if you have any questions — we'd love to hear from you. 🎉
>
> Overall, we're incredibly excited about what this means for the future. The road ahead looks bright, and we can't wait to see what you build next.

**After (Bespoke rewrite):**

> Smart Scheduling is live. Check Settings to turn it on.
>
> It syncs your calendar with the tools you're already using, so teammates, clients, and anyone else on the invite are looking at the same times. No import step, no separate app to check.
>
> We built it because three teams asked for the same thing in one month: stop making them reconcile two calendars by hand. If that's not your problem, you probably won't notice this update, and that's fine.
>
> Turn it on and tell us what breaks.

Every pattern in the "before" maps to a specific rule this skill applies: the heading trades Title Case and an emoji for plain sentence case with no decoration; "stands as a testament to... innovation, efficiency, and user delight" (a dying metaphor stacked with rule-of-three padding) becomes nothing, because the fact that the feature exists doesn't need a legacy claim; the bolded inline-header list collapses into two plain sentences; "in order to fully leverage this robust... capability" (a filler phrase plus pretentious diction) becomes "so"; "could potentially possibly" (stacked hedging) becomes a specific, sourced reason instead of a hedge; the em dashes are gone; and the closing "Overall, we're incredibly excited..." (a generic positive conclusion) is replaced by an actual next step. See [Coverage](#coverage-against-wikipedias-signs-of-ai-writing-guide) below for where each pattern lives in the skill.

## Before / after example 2: voice and specificity, layered with a fixed personal-voice skill

The first example shows structural and typographic tells getting removed from a formatted document. This one shows the other half of the skill, Sections 1 and 4, working on a short, unformatted personal narrative, and demonstrates Section 8: layering Bespoke under a separate, fixed personal-voice skill rather than using Bespoke's generic defaults.

*(Illustration note: this is a fictional narrative written to demonstrate the skill, not a real account, and doesn't depict any real, identifiable person. The "before" is a short, deliberately generic AI-written passage. For the "after," Bespoke's own intake (Section "The intake") was pre-filled per Section 8 by an existing fixed-voice skill, no em dashes, zero cap on unsupported facts, an "acid test" against real named entities, burstiness, grade 6-7 readability, restrained tone, no performed vulnerability, a quiet close over a dramatic one, rather than by a fresh sample. The specific narrative details below, the street name, the dialogue, the dead flash, are illustrative texture standing in for what a real user's own material would supply; see Section 4's specificity test for why a rewrite shouldn't invent this kind of detail about something that actually happened.)*

**Before (generic AI-written text, 199 characters):**

> Nestled in the vibrant heart of Kuala Lumpur, an unofficial date with a stunning model blossomed into an unforgettable, impromptu photoshoot, a testament to genuine chemistry and effortless artistry.

**After (Bespoke rewrite, voice layered from a fixed personal-voice skill):**

> Met her at a rooftop bar off Jalan Alor on a Tuesday, the kind of humid Kuala Lumpur night that turns any jacket into a mistake by nine. She modeled part-time, she said, mostly for local streetwear brands. I brought a camera out of habit, not intent.
>
> Two drinks in, she picked it up, turned it over, and said, "so are you going to use this or just carry it around."
>
> We ended up on the street outside for maybe twenty minutes, I didn't check. Streetlights and a wet road did most of the work. My flash died halfway through. Neither of us minded.

What changed and why: "nestled in the vibrant heart of," "blossomed into," and "a testament to genuine chemistry and effortless artistry" (Fault 1's dying metaphors and promotional-language sub-family) are gone entirely rather than trimmed, because the plain fact underneath them, two people met, ended up taking pictures, doesn't need a frame telling the reader how to feel about it. In their place: a specific street and night (Section 4's contextual embedding), reproduced dialogue instead of summary ("she asked about the camera" would be the generic version), an unexpected complication a smooth invented account wouldn't think to include (the dead flash), and an admitted gap ("I didn't check") rather than false precision. Sentence length varies sharply, one long scene-setting sentence, then short and medium ones, per the layered skill's burstiness rule and Section 9's presence principle, rather than settling into the uniform mid-length rhythm generated text defaults to. Zero em dashes, per both the layered skill's hard rule and Section 1's typographic default. The close is a flat, quiet fact instead of a generic positive conclusion (Cluster D), which is the layered skill's own "solution is the hero, not the victim" instinct doing the same work Section 9 asks for from a different direction.

## What it does

- **An explicit own-style-or-default choice**, not a default assumption. Choosing your own style requires a real writing sample of at least 100 words, an essay, article, post, or email you actually wrote; under that, the skill says so and asks for more rather than guessing from a fragment. Adjectives alone ("direct, a little dry") don't satisfy either path. Choosing default skips the personal fingerprint and keeps every plain-style and typographic default in force.
- **A stylometric voice fingerprint**, not a one-shot style match: function-word habits, sentence-length variance, opening patterns, and the writer's own recurring bigrams and trigrams, read from a real sample and kept for the rest of the conversation.
- **Orwell's plain-style check**, applied as a live diagnostic: dying metaphors, verbal false limbs, pretentious diction, and meaningless words, the same four faults named in 1946, with current examples.
- **Five clusters of structural patterns beyond Orwell's essay**: borrowed authority, decorative structure, borrowed register, hedging and throat-clearing, and mechanical uniformity, covering everything from significance inflation and promotional language to stacked hedging, throat-clearing openers, and uniform transition-word rotation across a whole document. See [Coverage](#coverage-against-wikipedias-signs-of-ai-writing-guide) below for the full pattern list.
- **A hard zero-default on em and en dashes**, not just "use sparingly": the finished draft is scanned for `—`, `–`, and their spaced/doubled-hyphen equivalents before delivery, unless a real voice sample shows the writer actually uses them, in which case the sample wins outright.
- **A formulaic-language swap, not a ban.** Pre-formed phrasing is normal and necessary for fluent writing; the skill directs it toward the writer's own recurring phrases instead of shared clichés.
- **A specificity test drawn from forensic content analysis**: contextual embedding, unexpected complications, reproduced (not summarized) conversation, and admitted gaps, the actual criteria used to distinguish genuine accounts from fabricated ones, repurposed as a construction checklist.
- **Presence, not just absence.** Stripping every flagged pattern out and putting nothing back produces sterile prose, a different failure with the same symptom. Once a voice fingerprint exists, the skill writes toward it: uneven rhythm, real stance, unresolved mixed feelings, genuine self-correction, gated by content type and bounded by the no-fabrication rule throughout.
- **Platform-specific structure**: Context-Core-Connect for LinkedIn and Substack, hook-plus-white-space for X and Threads, tight distillation for email and Slack.
- **Three invocation modes**: pasted text (draft plus notes on what changed), file mode (rewrites a file in place, prose only), and embedded mode (bare final text for another agent or task using this skill as one step of a larger job).
- **An honest engagement gate.** Rapport techniques that work by being honest are always available. Techniques that work by deceiving the reader are gated to disclosed, consensual contexts, not applied by default to published, audience-facing content. See `references/engagement-ethics.md`.
- **Verified detection science, not fabricated statistics.** `references/detection-science.md` documents a citation-fabrication finding caught and excluded during research, and why current classifier-based detectors make surface-level evasion a weaker strategy than genuine specificity.

## Coverage against Wikipedia's "Signs of AI writing" guide

The primary source for Bespoke's pattern taxonomy is Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide, maintained by [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) from real examples observed across Wikipedia articles, drafts, and comments. See [References](#references) below. That guide is broader than Bespoke's scope in one direction, it documents Wikipedia-specific markup and citation mechanics (broken wikitext, invalid DOIs, `utm_source` parameters, non-existent templates, skipped heading levels, and similar), none of which apply to general prose and none of which Bespoke checks. The table below covers the guide's Content, Language and Grammar, Style, and Communication sections, the parts that generalize to any writing, and where each lives in Bespoke.

### The guide's general-prose patterns, and where they live in Bespoke

| Wikipedia's pattern | Where it lives in Bespoke |
|---|---|
| Undue emphasis on significance, legacy, and broader trends | `plain-style-diagnostics.md`, Fault 1, "Significance and legacy inflation" |
| Canned emphasis on notability, attribution, and media coverage | `plain-style-diagnostics.md`, Cluster A, "Notability namedropping" |
| Superficial analyses | `plain-style-diagnostics.md`, "Padding at the paragraph level" |
| Promotional and advertisement-like language | `plain-style-diagnostics.md`, Fault 1, "Promotional and brochure language" |
| Vague attributions and overgeneralization of opinions | `plain-style-diagnostics.md`, Cluster A, "Vague attribution" |
| Outline-like conclusions about challenges and future prospects | `plain-style-diagnostics.md`, "Padding at the paragraph level" |
| High density of "AI vocabulary" words | `plain-style-diagnostics.md`, Fault 3, tied to `SKILL.md` Section 1's frequency framing |
| Avoidance of basic copulatives ("is"/"are") | `plain-style-diagnostics.md`, Cluster B, "Copula avoidance" |
| Negative parallelisms (three subtypes) | `plain-style-diagnostics.md`, Cluster B |
| Rule of three | `plain-style-diagnostics.md`, Cluster B |
| Lexical diversity / elegant variation | `plain-style-diagnostics.md`, Cluster B, "Synonym cycling" |
| Title case | `typographic-markers.md` |
| Overuse of boldface | `typographic-markers.md` |
| Inline-header vertical lists | `typographic-markers.md` |
| Overuse of em dashes | `typographic-markers.md` — hard zero-default, not "use sparingly" |
| Emoji as formatting | `typographic-markers.md` |
| Curly quotation marks | `typographic-markers.md` |
| Collaborative communication | `plain-style-diagnostics.md`, Cluster C, "Chatbot artifacts" |
| Knowledge-cutoff disclaimers | `SKILL.md` Section 4, folded into the specificity test rather than a word list |
| Phrasal templates and placeholder text | `SKILL.md` Section 4, the specificity test's placeholder guidance |

A few of the guide's Style-section items are Wikipedia-article conventions with no general-prose analog (title-heading formatting, skipped heading levels, level-1-heading overuse, thematic breaks between sections, unusual table use) and aren't in the table above for that reason, not because they're uncovered by oversight.

### Patterns and features Bespoke has beyond the Wikipedia guide

- **Definitional throat-clearing openers** ("X refers to..." used to warm up a paragraph before the real point) — `plain-style-diagnostics.md`, Cluster D.
- **Recap and meta-commentary closings** ("In summary," "to conclude," restating what a piece already said) — Cluster D.
- **Uniform transition-word rotation** (mechanically cycling However / Moreover / Furthermore / Additionally across paragraphs) — Cluster E.
- **Structural symmetry addiction** (every section forced to the same paragraph count regardless of what the content needs) — Cluster E.
- **Frequency-based AI-vocabulary detection tied to stylometry.** The wider AI-vocabulary list under Fault 3 is explicitly framed as an anomalous-rate signal connected to `SKILL.md` Section 1's function-word fingerprinting, not a flat banned-word list, so a single instance of a listed word isn't treated as a violation on its own.
- **Presence, not just absence** (`SKILL.md` Section 9). Removing every flagged pattern and adding nothing back is a different failure with the same symptom as generated prose. Once a voice fingerprint exists, the skill actively writes toward it: uneven rhythm, real stance, unresolved mixed feelings, genuine self-correction, bounded by the no-fabrication rule throughout.
- **A stylometric voice fingerprint built from a real sample**, kept and updated across a whole conversation rather than applied once per rewrite (`SKILL.md` Section 1), grounded in the same authorship-attribution research used in forensic linguistics.
- **A specificity test from forensic content-analysis criteria** (CBCA, Reality Monitoring) for distinguishing genuine detail from plausible-sounding invention, not just an AI-tell scan (`SKILL.md` Section 4).
- **An honest-engagement gate** on rapport techniques that work by deceiving the reader, restricted to disclosed, consensual contexts rather than applied by default (`references/engagement-ethics.md`).
- **Verified, sourced detection science**, including a documented citation-fabrication finding caught and excluded during this project's own research (`references/detection-science.md`).

## Repository structure

```
bespoke/
├── SKILL.md                        # the skill itself; source of truth
├── README.md                       # this file
├── AGENTS.md                       # guidance for agents/contributors editing this repo
├── LICENSE                         # MIT
├── .claude-plugin/
│   ├── plugin.json                 # Claude Code plugin manifest
│   └── marketplace.json            # single-repo marketplace entry
├── .github/workflows/validate.yml  # CI: runs the same checks below on every push
├── scripts/
│   └── validate_package.py         # dependency-free sync checks (stdlib only)
└── references/
    ├── plain-style-diagnostics.md
    ├── typographic-markers.md
    ├── detection-science.md
    ├── engagement-ethics.md
    └── changelog.md
```

## Validating a local copy

```bash
python3 scripts/validate_package.py
```

Stdlib only, no `pip install` required. Checks that `SKILL.md`'s name and version match `.claude-plugin/plugin.json`, that every file `SKILL.md` points to under `references/` actually exists, and that the marketplace entry resolves.

## Version history

- **2.4.0** — Corrected the pattern taxonomy's primary-source attribution: `references/plain-style-diagnostics.md`'s Clusters A through C now cite Wikipedia's "Signs of AI writing" guide directly, verified against the live page, rather than being attributed by way of `blader/humanizer`, which is itself downstream of that same guide. New README "References" section citing the Wikipedia guide and WikiProject AI Cleanup, its maintaining organization, without claiming any project affiliation beyond citation. The "Coverage" section is rebuilt against the guide's own Content, Language and Grammar, Style, and Communication sections (with its Wikipedia-specific markup and citation items explicitly noted as out of scope) rather than humanizer's numbered list. `blader/humanizer` now appears only in Credits, as the tool early development was benchmarked against. See `references/changelog.md`.
- **2.3.0** — Made the Voice intake an explicit own-style-or-default choice rather than a default sample-or-adjectives request. Choosing own style now requires a real writing sample of at least 100 words, with an explicit ask for more if under that floor; adjectives alone no longer satisfy either path. Choosing default explicitly waives a personal fingerprint while keeping every plain-style and typographic default in force. New "The own-style-or-default gate" subsection in `SKILL.md` Section 1; intake item 1 and the Usage/"What it does" sections of this README updated to match. No change to any pattern in `plain-style-diagnostics.md` or `typographic-markers.md`. See `references/changelog.md`.
- **2.2.1** — Added "Before / after example 2" to this README: a short, fictional, non-identifying personal narrative run through the installed skill with Voice pre-filled by a separate fixed personal-voice skill per Section 8, demonstrating Sections 1 and 4 (voice fingerprint, specificity test) on unformatted prose rather than the mostly structural/typographic first example. README-only; no change to `SKILL.md` or any pattern file. See `references/changelog.md`.
- **2.2.0** — Full audit against `blader/humanizer` v2.9.1's complete 33-pattern taxonomy (see [Coverage](#coverage-against-wikipedias-signs-of-ai-writing-guide) above). Closed every remaining gap: significance/legacy inflation and promotional/brochure language (Fault 1), the full high-frequency AI-vocabulary list tied to Section 1's stylometry framing (Fault 3), passive voice and subjectless fragments as a named pattern (Fault 2), filler phrases as an explicit stock list (Fault 2), and two new clusters, D (hedging, throat-clearing, and empty closes) and E (mechanical uniformity), the latter with no equivalent in humanizer's taxonomy. Hardened the em-dash default from "rare" to a zero-default with a pre-delivery scan, matching humanizer's hard-constraint treatment while keeping the sample-override principle. Added `SKILL.md` Section 9 ("Presence, not just absence") on actively writing toward the voice fingerprint rather than only scrubbing tells, Section 10 (invocation modes: pasted text, file, embedded), and an explicit two-question self-audit step in the Application workflow. Expanded `plain-style-diagnostics.md`'s false-positive guidance from 4 items to 15. Added a before/after example and the coverage table above to this README. See `references/changelog.md` for the full audit account.
- **2.1.0** — Closed a coverage gap found during a direct comparison against the tool this skill was originally benchmarked against: added typography and formatting as voice-fingerprint markers (`references/typographic-markers.md`) and three clusters of structural patterns (borrowed authority, decorative structure, borrowed register) to `references/plain-style-diagnostics.md`. Also fixed a stale internal section cross-reference. See `references/changelog.md` for the specific patterns added and why each was placed where it was.
- **2.0.0** — Rebuilt around independent research (stylometry, Orwell's plain-style diagnostics, formulaic-language psycholinguistics, forensic content-analysis criteria) rather than a comparative audit of an existing tool. See `references/changelog.md` for the full account of what changed and why.
- **1.0.0** — Initial release, built after benchmarking against an existing AI-tell removal tool. Superseded by 2.0.0's independent research base.

## License

MIT. See `LICENSE`.

## References

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — primary source for the pattern taxonomy in `references/plain-style-diagnostics.md`'s Clusters A through C and `references/typographic-markers.md`. See [Coverage](#coverage-against-wikipedias-signs-of-ai-writing-guide) above for the section-by-section mapping.
- [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) — the Wikipedia project that maintains the guide above.

## Credits

Early development benchmarked against [blader/humanizer](https://github.com/blader/humanizer) (MIT), an existing open-source AI-tell removal skill that itself cites the Wikipedia guide above as its own primary source. Bespoke's current structure is built from independent research (see `references/changelog.md`); this credit reflects where the project started, not its present design or its present sourcing.
