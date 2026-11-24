---
name: skill-review
description: "Review skills for clarity, security, portability and testability."
license: MIT
---

# Skill Review

## When to use
Review skills for clarity, security, portability and testability. Do not activate for unrelated requests. Respect the host instruction hierarchy and user authorization.

## Procedure
1. Read the files without executing scripts; inventory tools, network, credentials and write permissions.
2. Check specification, activation scope, contradictions, file references and external input handling.
3. Identify unsupported claims and score gaps with evidence; propose minimal edits.
4. Separate findings by severity and prescribe regression cases for each material flaw.

## Output contract
Review with evidence locations, severity, remediation and test plan.

## Quality gate
Do not certify safety or behavioral quality from a static scan alone. If evidence or tools are unavailable, state what remains unverified.
