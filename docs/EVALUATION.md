# Paired evaluation: offline outcome aggregator

This tool accepts externally supplied binary outcomes. It does not run models, inspect outputs, authenticate the caller or verify scores. The bundled example is synthetic, not evidence of skill efficacy.

```sh
python evaluate.py benchmarks/synthetic-plan.json
python evaluate.py benchmarks/synthetic-plan.json benchmarks/synthetic-records.json
```

The first command prints the SHA-256 of canonical plan JSON (sorted keys, compact separators, ASCII escapes). Freeze the plan and record its digest before collecting outputs. Record that digest on each observation. Hash actual configuration, prompt/skill bytes, tasks and output artifacts using a documented method; keep those artifacts and independent scoring evidence separately. Hashes here are consistency identifiers, not signatures. Plan and record files are UTF-8 JSON; duplicate keys are rejected. The conditions are A (no skill), B (brief instruction, optional), C (skill) and D (revised skill, optional). Use identical model, tools, task, budgets and scoring rubric; randomize execution order outside this tool. Repetitions are predetermined. `success` is strictly boolean for a completed record; an error has null success and output hash. Missing and error outcomes are not silently treated as failure.

The example has one complete pair with a positive difference, and one incomplete pair. The complete-pair delta is +1.0 (100 percentage points); the all-planned-pair bounds are [0, 0.5]. These are constructed fixtures, not model results. Bounds use the best and worst possible missing outcomes conditional on known scores; they are not statistical confidence intervals. Report the denominator, missing pairs and bounds alongside the complete-case estimate. Each planned task has the same repetition count, but incomplete pairs may unbalance complete-case estimates. Do not use repeated trials as independent tasks for inferential statistics.

## Prior art and scope

- [SkillsBench v1.1](https://www.skillsbench.ai/blogs/skillsbench-1-1): 87 tasks, paired evaluations, published leaderboard and skill invocation measurements.
- [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401): requirements-driven software-engineering tasks and execution-based verification.
- [NVIDIA SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator): documents tiered quality, security, compatibility and live agent evaluation.

These references already address skill evaluation; we do not claim novelty for paired comparisons. This implementation is a small offline aggregation component emphasizing explicit missing-data bounds and plan-linked records. No comparative superiority or real model performance has been demonstrated. Future work: deterministic task verifiers, compatible importers, a version-pinned host runner, independent reproducibility and statistical uncertainty by task.
