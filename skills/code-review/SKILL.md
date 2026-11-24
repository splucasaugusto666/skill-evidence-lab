---
name: code-review
description: "Review a code change for defects, regressions, maintainability or secure implementation."
license: MIT
---

# Code Review

## When to use
Review a code change for defects, regressions, maintainability or secure implementation. Do not activate for unrelated requests. Respect the host instruction hierarchy and user authorization.

## Procedure
1. Identify intended behavior and changed paths; inspect nearby callers and tests before conclusions.
2. Trace boundary inputs, failure paths, concurrency and authorization where relevant.
3. Find concrete regressions with reproducible scenarios; distinguish defects from stylistic suggestions.
4. Prioritize findings by impact, cite file and line, propose focused tests and avoid unrelated rewrites.

## Output contract
Prioritized findings, reproduction steps, suggested fixes and verification status.

## Quality gate
Do not claim tests passed unless executed; no invented line numbers. If evidence or tools are unavailable, state what remains unverified.
