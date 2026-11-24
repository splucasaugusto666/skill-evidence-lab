# Compatibility and evidence levels

Specification reference: https://agentskills.io/specification (reviewed 2026-11-23). Required name/description, directory naming, and concise body are implemented in the project profile. A full official reference-validator conformance run is pending.

Vendor references: https://developers.openai.com/plugins/concepts/skills ; https://github.com/huggingface/skills ; https://geminicli.com/docs/cli/skills/ ; https://cursor.com/docs/skills ; https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills ; https://code.claude.com/docs/en/skills (last URL not independently opened in this iteration).

Codex, Claude Code, Gemini CLI, Cursor and Copilot have documented or upstream-reported skill support; actual runtime behavior and installed version remain UNVERIFIED for every bundled skill. Filesystem placement alone is not native activation. ChatGPT uses its own skill/plugin packaging, not the local project installer. Other hosted and local models, Windsurf, Continue, OpenCode, Meta AI, DeepSeek, Grok, Mistral, Qwen: runtime UNVERIFIED. Manual Markdown reading is a fallback, not evidence of support. MCP is a tool/context integration protocol, not a skill file format.
