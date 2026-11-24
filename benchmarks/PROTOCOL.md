# Behavioral evaluation protocol (unexecuted)

Question: does a skill improve task success for the same model and tool configuration?

A: no skill; B: short specialization instruction; C: original skill; D: revised skill. Use matched tasks across conditions, randomize order, freeze model version, tools, permissions, scoring criteria and token/time budgets. Separate development tasks (the 12 included seed cases) from new, privately held-out tasks. Record prompt and skill hashes, model identifier, run seed when supported, tool availability, token usage, elapsed time, completion status and judge version. Predefine correctness as primary outcome and safety, efficiency and completeness as secondary outcomes. Use deterministic tests where possible and blinded independent rubric review otherwise; record disagreement. Estimate paired differences and uncertainty by task, account for repeated runs, and report missing runs and negative findings. No results exist until runs actually occur.

The seed prompts are examples, not a validated benchmark dataset or scored cases. Do not use them alone to claim generalization. Each JSON contains a provisional acceptance rubric; refine into anchored scoring before execution. Publish exact methodology and eligible artifacts, preserving privacy.
