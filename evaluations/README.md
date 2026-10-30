# Evaluation records

This directory contains test inputs, generated outputs and assessments for the published skill collection. Deliberately flawed text and unsuccessful runs are retained as evidence; they are not current product guidance.

## Find a result

| Concern | Records |
| --- | --- |
| Skill selection and resource loading | [Selection cases](skill-selection/), [observed file access](skill-selection/) |
| Architecture behaviour | [Architecture cases](architecture/), [split/loading cases](architecture-split/) |
| Project terminology and writing | [Public project pilot](pilots/llm-core/), [editorial task trials](editorial-v1.6.0/) |
| Evidence gaps and handoffs | [Uncertainty cases](uncertainty/) |
| Portable packaging and offline analysis | [Portability checks](portability/) |

Read the case's README or assessment alongside its inputs and outputs. A single generated answer establishes only the recorded case result. Package checks, agent judgement, native client activation and human comprehension are different evidence types; the [validation guide](../docs/language-system/validation-results.md) explains their scope.

## Replay conventions

Some outputs contain relative links to staged skill copies. Follow the case's replay instructions to recreate those directories; the skill package may be represented by a source revision or hash manifest instead of duplicated files. Raw outputs keep their original text, including defects identified by an assessment.
