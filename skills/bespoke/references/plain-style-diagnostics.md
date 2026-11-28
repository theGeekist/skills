# Plain-style diagnostics

Orwell's "Politics and the English Language" (1946) is the primary source for the four-fault section below. It's cited by name and quoted briefly in `SKILL.md` Section 2. Clusters A through C's empirical grounding, what specific phrases and structures actually recur in AI-generated text, traces to a different primary source: Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide, maintained by [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup), drawn from real examples the project has observed across Wikipedia articles, drafts, and comments. See `README.md`'s References section. Clusters D and E go past what that guide documents at the time of writing: hedging-and-throat-clearing patterns at the sentence and paragraph level, and mechanical uniformity patterns at the structural level, both real failure modes that word-list-based tools miss because they're about *rhythm and shape across a passage*, not a single flagged phrase. Typography and formatting (em dashes, curly quotes, heading case, and the rest) live in the companion file `typographic-markers.md`, since they're a different kind of signal, closer to Section 1's voice-fingerprint concept than to word choice.

---

## Orwell's four faults, expanded

### 1. Dying metaphors

**The mechanism:** a figure of speech reused so often it stops evoking the image it's built on. Orwell's own examples: "toe the line," "ride roughshod over," "no axe to grind," "grist to the mill." His diagnostic test: writers who mix incompatible metaphors, or misuse one slightly (his example: "toe the line" written as "tow the line"), are proof the phrase was never really evoking anything for them. It was retrieved as a unit, not composed as an image.

**Current instances of the same mechanism:** "delve into," "a tapestry of," "stands as a testament to," "unlock your potential," "navigate the complexities of." Different decade, same failure: a phrase retrieved whole because thinking up a real image is more effort than reaching for the available one.

**Two sub-families worth naming on their own,** because each has its own recognizable shape and its own common phrases, even though both are dying metaphors by mechanism:

- **Significance and legacy inflation.** Puffing up an ordinary fact by attaching it to a bigger story it doesn't need: "marks a pivotal moment," "a key turning point," "sets the stage for," "shapes the evolving landscape of," "leaves an indelible mark," "deeply rooted in," "a focal point for," "underscores its significance," "reflects a broader trend," "contributing to the ongoing," "symbolizing its enduring." The fact usually stands fine on its own; the inflation is doing the work a real detail should be doing.
- **Promotional and brochure language.** The travel-writing and marketing register, applied to things that aren't being sold: "boasts a," "rich cultural heritage," "nestled in," "in the heart of," "renowned for," "breathtaking," "must-visit," "stunning," "a true gem," "showcasing," "exemplifies," "a testament to its commitment to." Recognizable because it reads like copy even when the subject is a zoning ordinance or a quarterly report.

**The fix:** if the metaphor is doing real work, keep it, once. If it's there because it's the phrase that comes to mind fastest, that's the tell that it's not doing real work. Say the plain thing instead. For both sub-families above, the plain thing is almost always the fact itself, stated once, without the frame that tells the reader how to feel about it.

### 2. Operators, or verbal false limbs

**The mechanism:** replacing a plain verb with a longer phrase built around it, almost always in a way that also invites the passive voice. Orwell's examples: "render inoperative" for "stop," "militate against" for "hurt," "have the effect of" for "cause," "give rise to" for "cause."

**Current instances:** "serves as," "functions to enable," "has the ability to," "is in a position to." The added length doesn't add precision; it adds distance between the writer and a direct claim.

**Stock filler versions of the same move,** common enough to name directly: "in order to" for "to," "due to the fact that" for "because," "at this point in time" for "now," "in the event that" for "if," "it is important to note that" (cut entirely, then check whether the sentence still needs the words that followed it), "with regard to" for "about," "in the process of" for a plain present-tense verb.

**Passive voice and subjectless fragments belong here too**, not as a separate fault but as the grammatical form this one most often hides in: dropping or burying the actor is Fault 2's mechanism applied to the whole sentence instead of one phrase. "No configuration file needed" and "the results are preserved automatically" both hide who's doing what. Rewrite as "You don't need a configuration file" and "the system saves the results automatically" when naming the actor makes the sentence clearer, which it usually does; genuinely actor-irrelevant statements (most instructions, most process documentation) are a legitimate exception, not the default.

**The fix:** find the verb hiding inside the phrase and use it. "Has the ability to process" is "processes."

### 3. Pretentious diction

**The mechanism:** reaching for a Latinate, technical, or foreign-derived word to imply expertise the sentence hasn't earned. Orwell's examples: "phenomenal," "categorical," "epoch-making," "veritable."

**Current instances:** "leverage" (verb), "utilize," "facilitate," "robust" (as filler), "holistic," "ecosystem" (metaphorical), "paradigm." None of these are wrong words. They're wrong when a plainer word already covers the meaning and the fancier one is there to sound credentialed instead.

**A wider, related list worth flagging as a group:** additionally, actually (as a throat-clearing opener, not the genuine "actually, I was wrong" correction), align with, crucial, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate / intricacies, key (as a reflexive intensifying adjective: "a key factor," "a key role"), landscape (as an abstract noun: "the competitive landscape," not an actual landscape), pivotal, showcase, underscore (verb), valuable. Individually these are ordinary words with legitimate uses; connect this list back to Section 1 of `SKILL.md`, because that's exactly why it belongs under stylometry as much as under Orwell. The tell isn't any single word on this list, it's the rate: this specific set of words co-occurs and repeats at a frequency well outside how any individual writer's function-word habits actually behave, the same statistical signature Section 1 uses to fingerprint an author, just running in the opposite direction. One "pivotal" in a page is a writer's ordinary word choice. Three AI-vocabulary words from this list in one paragraph is a frequency anomaly, not a coincidence.

**The fix:** Orwell's own test, adapted: could a person actually say this out loud to a colleague without it sounding like a memo? If not, it's probably pretentious diction, not precision. For the wider list, the fix is the frequency check above, not word-by-word substitution: a single instance is rarely worth flagging on its own.

### 4. Meaningless words

**The mechanism:** words with no stable, checkable definition, used because the reader is expected to nod rather than ask what they mean. Orwell's field for this was art criticism; his examples: "vital," "natural," "human," "romantic," "values."

**Current instances:** "authentic," "vibrant," "seamless" (as filler, not describing an actual seam), "impactful," "holistic" again (it does double duty). The test: could two people disagree about whether something qualifies, with no way to settle it? If so, the word isn't describing anything, it's vouching for something.

**The fix:** replace with the specific, checkable claim the vague word was standing in for.

---

## Five clusters of pre-formed shape, beyond Orwell's four faults

Orwell's essay is from 1946 and, understandably, doesn't cover typography (that's `typographic-markers.md`) or a handful of structural moves more common in web and social writing than in the print prose he was diagnosing. These sit in the same family as his four faults, a shape reached for instead of a thought, and organize into five clusters. Keep this section a secondary tool in practice: the plain-style check above is primary, this is the backup pass.

### Cluster A: borrowed authority

Ways a sentence implies credibility it hasn't earned, close cousins of pretentious diction applied to sourcing rather than vocabulary.

- **Vague attribution.** "Experts believe," "studies show," without naming who or which. Either name the source or cut the claim. This is also a specificity-test failure; see `SKILL.md` Section 4.
- **Notability namedropping.** Listing outlets or follower counts as a stand-in for an actual point ("featured in X, Y, Z"). Say the specific thing one of those sources actually said, or drop the list.
- **Persuasive authority tropes.** "At its core," "the real question is," "what really matters is," performing the act of cutting through noise instead of doing it. The sentence that follows is usually an ordinary point in ceremonial dress.

### Cluster B: decorative structure

Shapes reached for because they're available, not because the content calls for them.

- **Rule-of-three padding.** "Innovation, inspiration, and insight" fails a simple test: does each item carry distinct, checkable weight, or would the sentence lose nothing with two items or four? Real triads pass.
- **Synonym cycling (elegant variation).** Renaming the same referent every sentence to avoid repeating a word ("the founder... the entrepreneur... the visionary..."). Repeating the plainest word is more natural than cycling synonyms.
- **False ranges.** "From X to Y" used to sound sweeping when X and Y aren't actually on a meaningful scale. List the real things instead.
- **Negative parallelisms and tailing negations.** "It's not just X, it's Y" as a reflexive structure, and its smaller cousin, a clipped negative fragment tacked onto a sentence's end ("no guessing," "no wasted motion") instead of written as a real clause.
- **Manufactured metaphor stacking.** One vivid comparison, earned, lands. Three across one short piece reads as trying, retrieved for effect rather than because each one clarifies something new.
- **Mechanical repetition of a thesis.** Restating the same point three times in different words isn't reinforcement, it's the same idea wearing different clothes. Real reinforcement adds a new angle or new evidence each time.
- **Manufactured punchline runs.** One short declarative sentence for emphasis lands. Three or more in a row, each performing the same dramatic beat, is the tell, regardless of how true each individual line is.
- **Fragmented headers.** A heading immediately followed by a one-line paragraph that just restates the heading before real content starts. Cut the restatement.
- **Aphorism formulas.** "X is not a Y, it's a Z," "X is the language of Y," a template that makes an ordinary claim sound profound because it's portable across any topic with the nouns swapped. Replace with the actual mechanism the claim is gesturing at.
- **Copula avoidance.** "Serves as," "boasts," "features" used where "is" or "has" would be plainer, a close cousin of Orwell's verbal false limbs (Fault 2), specifically about avoiding a simple "to be."
- **Signposting instead of doing.** "Let's dive into how this works" announces the move instead of making it. If a phrase can be cut, cut it, per Orwell's third rule, and an announcement of what's about to happen is almost always cuttable.

### Cluster C: borrowed register

Language that belongs to a different kind of exchange, leaking into content where it doesn't fit.

- **Chatbot artifacts.** "I hope this helps," "let me know if you'd like me to expand," correspondence-shaped language pasted into content that isn't correspondence.
- **Sycophantic tone.** "Great question!", "you're absolutely right," warmth performed as a reflex rather than felt, a specific instance of Orwell's insincerity diagnosis: the tone doing work the content isn't backing up.
- **Conversational rhetorical openers.** "Honestly?", "Look,", "here's the thing," used as a standalone theatrical pause before an ordinary point. The tell is the pause-and-reveal structure, not the words themselves; "honestly" used mid-sentence in ordinary speech is fine.

### Cluster D: hedging, throat-clearing, and empty closes

Ways a sentence or paragraph avoids committing to a claim, or avoids starting and ending on one.

- **Stacked hedging.** One qualifier is normal caution. Stacking them ("could potentially possibly be argued that," "it may perhaps somewhat suggest") isn't extra precision, it's the sentence refusing to land anywhere. Pick the one qualifier the evidence actually supports and cut the rest: "could potentially possibly be argued that the policy might have some effect" is "the policy may affect outcomes."
- **Definitional throat-clearing openers.** Starting a section or paragraph by restating what the subject is before saying anything new about it: "X refers to...," "X can be defined as...," "X is a concept that..." If the reader already knows what X is, this is dead air before the actual point; if they don't, define it inline as part of the first real sentence instead of as a separate warm-up sentence.
- **Generic positive conclusions.** A vague, upbeat send-off with no new information: "the future looks bright," "exciting times lie ahead," "this represents a major step forward." Distinct from the despite-challenges close below in that it doesn't need a preceding challenges paragraph to show up, it's the default AI closing move for almost any topic. The fix is usually deletion: end on the last concrete fact instead of a send-off, or replace it with a real, sourced claim about what happens next.
- **Recap and meta-commentary closings.** "In summary," "to conclude," "overall," followed by a restatement of points already made in the piece. If a reader who skipped straight to the closing paragraph learns nothing they couldn't get from the headings, the recap isn't adding anything. Cut it, or replace it with the one thing the piece hasn't said yet.

### Cluster E: mechanical uniformity

Patterns visible only at the level of a whole document or section, where the tell isn't any single sentence but the fact that every sentence, paragraph, or section is shaped the same way.

- **Uniform transition-word rotation.** Opening consecutive paragraphs with "However," then "Moreover," then "Furthermore," then "Additionally," one per paragraph, in mechanical rotation rather than because each one reflects the actual logical relationship to what came before. A real writer repeats "but" or "and" far more than a style guide would predict, because the relationship between two ideas is usually simpler than a thesaurus of connectives. Check each transition word against what it's actually claiming (contrast, addition, consequence); if a plainer, more repeated connective says the same thing, use it.
- **Structural symmetry addiction.** The document-level cousin of rule-of-three padding (Cluster B): every section exactly three paragraphs, every paragraph exactly three sentences, every list exactly three items, regardless of what each part of the content actually needs. Real writing is lumpy: some points need a sentence, some need a page. Uniform symmetry at the structural level is a shape imposed on the content rather than a shape the content produced.

### Padding at the paragraph level

Orwell's verbal false limbs (Fault 2) operate on the sentence. These are the same move at the level of a whole paragraph.

- **The formulaic "despite challenges, continues to thrive" close.** A challenges paragraph that resolves into vague optimism instead of a specific outcome. Replace with the actual trade-off made.
- **Diff-anchored writing.** Narrating what changed instead of describing what a thing is now, in a document that isn't itself a changelog. "This was added to replace the old approach, which caused problems" makes the reader reconstruct history to understand the present. Describe what it is; the history is context, not the lead.
- **Superficial "-ing" tack-ons.** A claim followed by a present-participle clause that restates it with false depth ("...reflecting the region's resilience," "...showcasing years of craft"). Adds a decorative clause, not a second real idea.

## What NOT to flag

A distinctive writer hits several of the above on purpose, and that's not a problem to fix. Before rewriting, sanity-check against this list; the goal is catching generated prose, not gutting legitimate writing that happens to share a surface feature with it.

- A single vivid metaphor that's actually doing work. Orwell's own distinction, "iron resolution" is technically a dead metaphor and reads fine because it's used as a plain word now, not reached for as an image.
- A short sentence that lands a real point. The tell above is a run of three or more manufactured punches in a row, not the existence of one.
- Domain-necessary technical vocabulary. "Cross-functional" in a genuine description of a real team structure isn't pretentious diction; it's the accurate term.
- A real triad where each item actually differs. Check the test above before assuming three items is automatically padding.
- Perfect grammar and consistent style. Most published writing is professionally edited. Polish isn't evidence of anything.
- Mixed casual and formal registers within one piece. Often a signal of a technical-field writer, a younger writer, or an idiosyncratic personal style, not a chatbot switching modes.
- Plain or unadorned prose on its own. The patterns above are specific; generic dryness without any of them is just dry writing, not a tell.
- Formal or academic vocabulary in general. Fault 3 flags *specific* words used to sound credentialed, not all Latinate or technical vocabulary. Don't flatten "ostensibly" or "constituent" just because they're long.
- A letter-style greeting or sign-off on genuine correspondence. Salutations predate language models by centuries; Cluster C's borrowed-register flag is about correspondence phrasing leaking into content that isn't correspondence, not about actual correspondence.
- A single instance of a common transition word. "However," "moreover," and "consequently" are ordinary connectives. Cluster E's rotation pattern requires an actual rotation across consecutive paragraphs, not one appearance.
- Curly quotes alone. Most consumer text editors auto-curl by default; this is only worth noting as one signal in a larger cluster, never on its own.
- Em dashes alone, from a writer whose sample shows they use them regularly. See `typographic-markers.md`'s calibration note: the default is a default, not a ban, and a real sample overrides it.
- Unsourced claims, by themselves. Most everyday writing isn't footnoted. Absence of citation doesn't establish anything about origin.
- Text inside quotation marks, titles, or proper names that happens to contain a watched phrase. Don't rewrite a phrase that's being quoted or discussed rather than used as the writer's own words.
