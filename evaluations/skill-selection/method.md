# Selection and loading method

These experiments distinguish four questions:

1. Is the skill package valid and independently installable?
2. Does an agent choose the intended purpose from only the catalogue descriptions?
3. On a normal authoring request, which available skill and supporting files does the agent actually read?
4. Does a particular native client discover and activate the skill correctly?

The local experiments address the first three. They do not substitute for the fourth.

For catalogue selection, create an isolated input containing only each skill's
name and description, plus the ordinary prompts from `cases.json` without its
assessment fields. Give fresh-context responders that input, and require a
choice of primary skill, optional companions or none. Preserve the exact input
and raw output. Score afterward against the retained assessment criteria.

For behaviour and loading, copy the complete collection into a unique isolated
run directory. Generate a catalogue containing names, descriptions and the local
paths to their instructions. Provide one ordinary marketing or decision-record
request and its invented source facts. Do not name a skill or provide an expected
answer. Tell the responder to use the supplied catalogue and relevant guidance,
then complete the requested work. Exclude prior outputs and the scoring rubric.

Start `read_monitor.py` before the responder reads the isolated catalogue and
skills. It records Linux file-access events, not document contents. Stop the
monitor when the responder finishes. Count unique accessed files and their word
counts afterward. A process reading a file does not prove every byte entered the
model's context, nor does manual catalogue selection demonstrate native client
activation. Report those limits with the results.

Record source-file hashes at snapshot time rather than describing an uncommitted
skill as the base Git revision. Keep output hashes and prompts so subsequent runs
can be compared. Review factual accuracy, reader navigation, uncertainty and the
next action independently of file-load counts. Lower context is valuable only
when the intended behaviour survives.

The monitor was smoke-tested locally against a known read: one file-access event
was captured. It is an evaluation aid for Linux, not part of any installed skill
or a cross-platform runtime dependency.
