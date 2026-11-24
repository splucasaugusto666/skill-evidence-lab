# Skill Evidence Lab

**Ship agent skills with evidence, not promises.**

An offline-first research prototype for authoring, validating, discovering and safely copying instruction-only Agent Skills. Part of the independent research direction *Reliable, Interoperable & Verifiable AI Systems*.

## Why this exists

A valid skill file is not evidence that an agent performs better. This project separates format and package integrity from actual behavioral evaluation. v0.1.0 includes 12 original skills, an offline CLI, a reproducible catalog, and 12 unexecuted evaluation seed cases.

## Quick start

Python 3.10+; no third-party runtime packages. From the extracted project directory:

```sh
python skilllab.py validate
python skilllab.py list
python skilllab.py search research
python skilllab.py info code-review
python skilllab.py install code-review --platform codex --workspace . --dry-run
python skilllab.py install code-review --platform codex --workspace .
python -m unittest discover -s tests -v
```

The installer copies two files into an existing workspace. It never runs skill code or contacts the network. Review instructions before activating a skill. Remove the installed skill directory manually to reverse the copy; do not remove unrelated files. `catalog` prints reproducible JSON to stdout. To verify the checked-in snapshot, run the tests.

## Library

| Skill | Domain |
|---|---|
| evidence-research | Research |
| experiment-design | Research |
| context-engineering | AI |
| skill-authoring | Meta |
| skill-review | Meta |
| code-review | Engineering |
| debugging | Engineering |
| test-engineering | Engineering |
| defensive-threat-model | Security |
| product-discovery | Business |
| ethical-growth-copy | Marketing |
| fitness-programming | Fitness |

## Platforms

The directories below are project-relative installation targets. Local copy and integrity tests passed for all six targets, **not actual agent activation**. See [compatibility](docs/COMPATIBILITY.md).

| Target | Directory | Evidence |
|---|---|---|
| Codex | `.agents/skills` | Local copy only |
| Claude Code | `.claude/skills` | Local copy only |
| Gemini CLI | `.gemini/skills` | Local copy only |
| Cursor | `.cursor/skills` | Local copy only |
| GitHub Copilot | `.github/skills` | Local copy only |
| Manual | `skills` | Local copy only |

## Architecture

```text
SKILL.md + manifest.json
        | strict package-profile validation
        v
SHA-256 integrity check -> catalog -> search / info
        | explicit target + no-overwrite policy
        v
local workspace installation
        |
        v
agent activation and controlled evaluation (future)
```

The manifest is a project-specific sidecar, not a new Agent Skills standard. The validator intentionally supports only the flat YAML subset used by this library. It is not a general-purpose validator for arbitrary third-party skills.

## Evaluation

[Protocol](benchmarks/PROTOCOL.md) and 12 seed cases are provided. **No LLM behavioral runs have been conducted.** No claim of uplift, cross-model reliability, token savings or scientific certification is made. See [local test record](docs/TEST-RESULTS.md).

## Security

A matching hash checks consistency with the supplied manifest, not authenticity or safety. The permission declaration is informational, not a host-enforced sandbox. Only the two-file instruction-only profile is accepted. The local filesystem checks assume a trusted, non-concurrent workspace. See [SECURITY.md](SECURITY.md).

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). See [research landscape](research/LANDSCAPE.md), [roadmap](ROADMAP.md), and [integration design](docs/INTEGRATIONS.md).

MIT license. No affiliation with model vendors is implied.
