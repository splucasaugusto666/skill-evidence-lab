---
name: debugging
description: "Diagnose reproducible software failures, errors or failing tests."
license: MIT
---

# Debugging

## When to use
Diagnose reproducible software failures, errors or failing tests. Do not activate for unrelated requests. Respect the host instruction hierarchy and user authorization.

## Procedure
1. Capture expected and actual behavior, version and minimal reproduction.
2. Rank plausible causes and design discriminating checks; avoid speculative rewrites.
3. Run the narrowest authorized diagnostic; isolate the root cause before changing code.
4. Apply a minimal fix, rerun reproduction and regression tests, and record residual uncertainty.

## Output contract
Root cause or ranked hypotheses, patch if authorized, and test evidence.

## Quality gate
Separate observed facts from hypotheses; preserve user changes. If evidence or tools are unavailable, state what remains unverified.
