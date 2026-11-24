# APEX competitive baseline — 2026-11-23

Public GitHub page snapshots, rounded counts. These are discovery signals, not users, scientific quality, or evidence of organic origin.

| Reference | Stars | Forks | Observable positioning |
|---|---:|---:|---|
| [mattpocock/skills](https://github.com/mattpocock/skills) | 331.3k | 27.8k | Focused engineering workflows |
| [obra/superpowers](https://github.com/obra/superpowers) | 325.0k | 28.8k | Composable development methodology |
| [anthropics/skills](https://github.com/anthropics/skills) | 199.4k | 23.3k | Vendor reference implementation |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | 40.6k | 3.6k | Installer and skills.sh discovery |
| Skill Evidence Lab | unknown | unknown | Offline validation, integrity, installation and evaluation research |

This is a selected peer set, not an exhaustive market ranking. Downloads, active users, retention, comparative security and behavioral performance remain unknown.

## Measurement framework

- Technology (40%): reproducible same-task evaluation, feature conformance, platform CI, adversarial tests.
- Experience (20%): successful first-run task, time to first value, documented installation, host activation.
- Discovery (25%): timestamped public stars, forks, independent referrals and downloads when accessible.
- Authority (15%): reproducible reports, independent reproductions, contributor and maintenance history.

No aggregate score until comparable evidence and normalization rules exist. Unknown is not zero. Freeze criteria before evaluating results.

## First experiment

Hypothesis: an offline demo that shows both successful installation and rejected modification improves first-use comprehension. Run python demo.py on a clean clone; record success and time separately. Invite independent users to reproduce without collecting telemetry. Do not infer adoption or uplift from automated tests. The demo is a synthetic filesystem experiment, not an agent benchmark.

Next: validate host activation, make a runnable paired evaluation protocol, and test compatibility with established distribution tools without executing external skills.

## Capability matrix (documented evidence; 2026-11-23)

D = documented capability (not independently tested here); V = locally/CI verified in our scope; P = planned; U = unknown/not investigated; N/A = outside primary scope. Unknown does not mean absent. No external skills were executed.

| Capability | Evidence Lab | Matt Pocock | Superpowers | Anthropic | Vercel |
|---|---|---|---|---|---|
| Reusable skill library | V: 12 | D | D | D | N/A: primarily installer |
| Engineering workflow composition | P | D | D | U | N/A |
| Documented host integration | D: file targets only | D | D | D | D |
| Verified host activation in this audit | U | U | U | U | U |
| Local package SHA-256 check | V: SKILL.md | U | U | U | U |
| Safe local copy demonstration | V: isolated demo | U | U | U | D: installer |
| Behavioral evaluation harness | P: protocol only | U | D: drill harness | U | N/A |
| Security audit of instruction semantics | P | U | U | U | D: partner audit integration |
| Public catalog / distribution channel | V: JSON catalog | D: plugin/skills.sh | D: plugins | D: marketplace | D: skills.sh |
| Independent replication of efficacy | U | U | U | U | U |

### Evidence anchors

- [Matt Pocock README](https://github.com/mattpocock/skills/blob/main/README.md): reusable model-invoked and user-invoked skills, setup workflow and distribution.
- [Superpowers repository](https://github.com/obra/superpowers): development methodology, host plugins and behavior test harness.
- [Anthropic Skills repository](https://github.com/anthropics/skills): reference examples, specification links and Claude plugin marketplace.
- [Vercel CLI documentation](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) and [repository](https://github.com/vercel-labs/skills): skill installation, supported hosts, directory discovery and audit requests.
- [Evidence Lab PR #2](https://github.com/splucasaugusto666/skill-evidence-lab/pull/2) and [CI run](https://github.com/splucasaugusto666/skill-evidence-lab/actions/runs/45315497843): six successful matrix jobs for the demo release candidate.

## Prespecified scoring rubric v1

Score each subcriterion 0–4 only after a comparable measurement: 0 = measured failure, 1 = prototype with partial success, 2 = documented reproducible baseline meeting minimum, 3 = benchmarked against peers and meeting target, 4 = independently reproduced target with no material regression in the measured scope. Mark unavailable measurements null, not zero. Publish evidence links, dates, version and coverage. Do not compute an overall rank with missing subcriteria. This is a proposed rubric, not an independent certification.

| Dimension | Subcriterion | Weight (points) | Measurement |
|---|---|---:|---|
| Technology | Behavioral task success | 15 | Same held-out tasks, model, tool access and budget; paired success delta and uncertainty |
| Technology | Package conformance | 8 | Shared valid/invalid fixtures, acceptance and rejection accuracy |
| Technology | Security | 10 | Authorized adversarial fixtures, false positives/negatives, threat-model scope |
| Technology | Efficiency | 7 | Tokens, latency and failures under identical conditions |
| Experience | First-use success | 8 | Independent clean-install and first-task completion |
| Experience | Host activation | 7 | Version-pinned real agent runs, not directory copies |
| Experience | Documentation usability | 5 | Independent task-based review |
| Recognition | GitHub discovery | 10 | Dated stars/forks and 30-day deltas, not user counts |
| Recognition | Distribution | 10 | Verified installs/downloads with comparable windows and definitions |
| Recognition | Independent references | 5 | Deduplicated, verifiable third-party links |
| Authority | Reproducibility | 7 | Independent reruns with evidence |
| Authority | Community sustainability | 5 | Distinct external contributors and maintenance responsiveness |
| Authority | Research transparency | 3 | Versioned methods, data, negative results and limitations |

A numeric score, if all criteria are observed under a frozen comparison protocol, is sum(weight * level / 4). Quantitative thresholds and normalization (especially popularity) must be preregistered before scoring; the generic scale does not itself establish those thresholds. Report dimensions separately and do not use popularity as a proxy for scientific superiority.

## Prioritized gap register

| Priority | Gap | Acceptance evidence |
|---|---|---|
| P0 | No actual behavioral evaluation | Runnable paired evaluator with versioned outputs and synthetic unit tests, then real authorized model runs |
| P0 | No real host activation | At least one recorded clean activation per claimed platform; record versions and negative tests |
| P1 | No established installer integration | Dry-run/discovery plus isolated install via an established tool, compare actual bytes using SkillParity |
| P1 | Narrow two-file package profile | Document conformance boundaries; expand only with safe fixtures and spec validation |
| P1 | No semantic security audit | Separate static risk indicators from proven vulnerabilities; report false positives |
| P2 | Unmeasured discovery | Capture repository counts via authorized source, record time and repeat with identical definitions |
| P2 | No independent reproductions | Publish reproduction guide and accept independently submitted evidence |

Repository-specific star/fork counts were not exposed by the connected metadata response; public fetch of Evidence Lab was unavailable. Keep them unknown. The peer snapshots above are rounded and were rechecked on 2026-11-23. This matrix does not establish a global top-1 position.
