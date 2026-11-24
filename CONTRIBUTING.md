# Contributing

Propose an observable user problem, activation and non-activation examples, and acceptance criteria. Write a concise original SKILL.md in the existing flat frontmatter profile; document sources and any licensed material. Add a manifest with the same name and SHA-256, and a benchmark seed case. The v0.1 format intentionally rejects scripts and arbitrary additional files.

Run `python skilllab.py validate`, regenerate `catalog.json` with `python skilllab.py catalog`, update the catalog-count test when adding a skill, and run `python -m unittest discover -s tests -v`. Include test outputs and distinguish planned behavioral experiments from actual runs. Use reviewable PRs. Do not fabricate results or copy unlicensed instructions.
