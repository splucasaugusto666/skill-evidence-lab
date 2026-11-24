---
name: test-engineering
description: "Design or implement tests for software behavior and regressions."
license: MIT
---

# Test Engineering

## When to use
Design or implement tests for software behavior and regressions. Do not activate for unrelated requests. Respect the host instruction hierarchy and user authorization.

## Procedure
1. Translate requirements into observable invariants and failure modes.
2. Cover ordinary, boundary, negative and regression cases; prefer deterministic fixtures.
3. Avoid mocks that merely repeat the implementation; verify side effects and cleanup when relevant.
4. Run tests if possible, report counts and failures, and identify untested conditions.

## Output contract
Test matrix, implemented tests if requested, commands and actual results.

## Quality gate
A meaningful test fails when the intended invariant is broken. If evidence or tools are unavailable, state what remains unverified.
