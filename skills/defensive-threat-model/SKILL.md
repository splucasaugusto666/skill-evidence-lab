---
name: defensive-threat-model
description: "Threat model an authorized system, assess defensive controls or supply-chain risk."
license: MIT
---

# Defensive Threat Model

## When to use
Threat model an authorized system, assess defensive controls or supply-chain risk. Do not activate for unrelated requests. Respect the host instruction hierarchy and user authorization.

## Procedure
1. Define assets, actors, trust boundaries and authorized scope.
2. Trace data flows and identify abuse cases including prompt injection, credential exposure and unsafe dependencies.
3. Rank threats by impact and likelihood with assumptions; propose preventive and detective controls.
4. Define safe validation tests, residual risk and owners; do not execute untrusted artifacts.

## Output contract
Threat register, mitigations, verification plan and residual risk.

## Quality gate
No unauthorized exploitation or claims of complete security. If evidence or tools are unavailable, state what remains unverified.
