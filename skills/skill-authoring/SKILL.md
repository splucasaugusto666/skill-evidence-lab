---
name: skill-authoring
description: "Create or revise portable Agent Skills with activation descriptions, instructions and tests."
license: MIT
---

# Skill Authoring

## When to use
Create or revise portable Agent Skills with activation descriptions, instructions and tests. Do not activate for unrelated requests. Respect the host instruction hierarchy and user authorization.

## Procedure
1. Define task, activation and non-activation cases, required inputs, tools and success criteria.
2. Check the target host specification; use standard frontmatter and separate optional project metadata.
3. Write concise steps with decision points, failure paths and a precise output contract; move reference material out of the main file.
4. Create positive and negative test cases; distinguish static validation from behavioral evidence.

## Output contract
A SKILL.md, optional references, tests, and a compatibility statement.

## Quality gate
Directory and name match; no unsupported host capabilities or untested performance claims. If evidence or tools are unavailable, state what remains unverified.
