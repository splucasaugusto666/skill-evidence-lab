---
name: experiment-design
description: "Design controlled experiments, benchmarks, ablations or reproducibility protocols."
license: MIT
---

# Experiment Design

## When to use
Design controlled experiments, benchmarks, ablations or reproducibility protocols. Do not activate for unrelated requests. Respect the host instruction hierarchy and user authorization.

## Procedure
1. State a falsifiable hypothesis, unit of analysis, outcome and practical effect threshold before observing results.
2. Specify baseline, treatment, randomization or pairing, sample size rationale, confounders and stopping rule.
3. Separate development cases from held-out cases; lock scoring rubrics and record model/tool versions.
4. Choose uncertainty estimates appropriate to the unit; report failures, missing runs and limitations.

## Output contract
Preregisterable experiment plan with metrics, data schema and analysis plan.

## Quality gate
No outcome-dependent changes to primary metrics; claims cannot exceed the design. If evidence or tools are unavailable, state what remains unverified.
