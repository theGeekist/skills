# Detection science: what's actually verified

The uploaded research document ("Comprehensive Deconstructed Analysis of AI-Generated Writing Indicators in Latest LLMs") reads like a serious literature review, with numbered citations throughout. On inspection, it isn't reliable as a source of specific facts, and this file exists to separate what's real from what isn't before any of it gets encoded into a skill as if it were verified.

---

## What was checked, and what was found

Two of the document's central citations were checked directly against the source it names.

**"Liu et al., 2023, arXiv:2303.11156," cited for the foundational definition of perplexity and burstiness.** The arXiv ID is real, but the paper at that address is Sadasivan et al., "Can AI-Generated Text be Reliably Detected?" (2023), a different set of authors than cited, and its actual subject is adversarial robustness of detectors against paraphrasing attacks, not a foundational definition of perplexity or burstiness. The citation pairs a real identifier with a fabricated author and a mismatched description of the paper's content.

**"Clark et al., 2025, Journal of Artificial Intelligence Research, Vol. 82," cited for embedding intrinsic-dimension figures of "2.2-2.8" for AI text versus "3.0-4.0" for human text.** No such paper was found. The real, underlying research on this exact technique is Tulchinskii et al., "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts" (NeurIPS 2023, arXiv:2306.04723), which reports entirely different figures: average intrinsic dimension around 9 for human text in most alphabet-based languages (around 7 for Chinese), with AI-generated text running about 1.5 lower, using a different method (Persistence Homology Dimension) than the one implied in the document. The general concept the document describes is real and grounded in real research. The specific numbers attached to it are not from that research, or from any located source.

Given two fabricated or mismatched citations found on direct inspection, out of a document with 27 numbered references and dozens of specific percentages (detection accuracy rates, per-model buzzword frequencies, evasion rates), the responsible move is to treat the document's specific statistics as unverified across the board, not to spot-fix the two that happened to get checked. What follows is what's actually verified, from sources checked directly.

---

## What's real and can be used

**Perplexity and burstiness are real, established concepts** in the AI-detection literature, described accurately at a conceptual level in the source document even where its citations aren't reliable: perplexity measures how statistically predictable a text is; burstiness measures how much sentence-level unpredictability varies across a document. Human writing tends toward higher perplexity variance and higher burstiness than early-generation AI text.

**These are not how modern detectors actually work, and haven't been for a while.** GPTZero's own current documentation states it moved away from perplexity and burstiness to a deep-learning classifier architecture in autumn 2023. Building a humanization strategy primarily around perplexity and burstiness targets a method that the most recognizable detector in this space no longer uses as its core approach.

**Intrinsic dimension analysis is real** (Tulchinskii et al., NeurIPS 2023): human-written text occupies a higher-dimensional embedding manifold than AI-generated text, a difference that holds up across languages and generator models. This is conceptually sound and worth knowing. The specific numbers in the source document for it are not.

**Modern classifier-based detectors are trained specifically to catch "humanized" evasion.** Pangram, the detector now used directly on Substack (see below), is trained on large corpora of human and AI text and states explicitly that its adversarial training targets paraphrasing and rewriting tools used to evade detection, reporting around 97% accuracy against that specific evasion pattern in its own published claims. This is the single most important practical fact for how this skill should work: a strategy built around surface-level rewriting to dodge a heuristic is fighting a detector generation that was built specifically to catch surface-level rewriting. Genuine specificity and a real voice profile are a stronger strategy not because they're more virtuous, but because they're not the exact pattern the newest detectors were trained against.

**Substack's own AI-detection stance has changed since the source document's citation.** The document quotes a Substack support statement (dated December 2024, "updated 2025") saying Substack doesn't proactively monitor content for AI origin. As of July 2026, Substack has a live, reader-facing AI-detection feature, powered by Pangram, that lets any reader scan a post, note, or comment and see an estimated AI-generated percentage. Anything published to Substack can now be checked by any reader in a few taps, which is a materially different posture than the one the source document describes.

---

## What this means for how Bespoke should work

Don't target a detector score. Build genuine specificity from the voice profile and the plain-style and specificity checks in `SKILL.md` Sections 1 through 4, and treat a low detector score as a plausible side effect of doing that well, not as the goal being optimized. See `SKILL.md` Section 7.

Don't repeat the source document's model-specific behavioral statistics (per-model buzzword-frequency percentages, specific evasion rates for GPT-5, Claude, Gemini, or Grok) as fact anywhere. They weren't verifiable, and the two spot-checked citations that were supposed to support this kind of claim didn't hold up.
