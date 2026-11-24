# APEX Infinity: prospective competitive protocol v2

This protocol supersedes the four-dimension weighting only for future comparisons. Preserve the earlier baseline, and never rescore historical results retroactively. No aggregate rank until comparable thresholds, measures and observations are available.

| Dimension | Weight | Planned measurement |
|---|---:|---|
| Technology | 30 | 15 held-out task success; 8 package conformance; 7 efficiency |
| Security and quality | 15 | 10 authorized adversarial cases; 5 regressions and stability |
| Innovation | 15 | 10 independently measured added value over prior art; 5 documented research contributions |
| Experience and adoption | 15 | 5 first-use success; 5 actual host activation; 5 independent usability |
| Recognition and distribution | 15 | 5 public discovery; 5 comparable download/install figures; 5 independent referrals |
| Authority and sustainability | 10 | 4 independent replication; 3 transparency; 3 independent contributors and maintenance |

Before a formal comparison, freeze quantitative thresholds, versions, sample, dates and normalization. Store per measure: own value, peer value, URL/artifact, timestamp, method, confidence, gap, next action. Null is unknown, not zero. Do not compute a global score with missing criteria or compare unrelated product categories as though identical.

## New direct evaluation references

SkillsBench v1.1: https://www.skillsbench.ai/blogs/skillsbench-1-1 (87 tasks, paired evaluations); NVIDIA SkillEvaluator: https://github.com/NVIDIA/SkillEvaluator (documented security and live evaluation); SWE-Skills-Bench: https://arxiv.org/abs/2603.15401 (deterministic SWE verification). No competitor code was executed. Our offline paired aggregator is a narrow complement, not evidence of superiority.

## Checkpoint

PR #2 passed all six CI jobs and merged. PR #3 contains the expanded original matrix; keep it independent of this change. Local evaluator candidate: 29 unittest tests passed, 12 skills statically validated, synthetic paired example ran. Real agent execution, actual task score verification, uncertainty estimation and independent replication remain unverified. Next: validate this PR in CI, implement deterministic task scoring and version-pinned runner, then perform an authorized paired model experiment. A connector release-publishing operation is not currently available.
