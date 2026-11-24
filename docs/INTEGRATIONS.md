# Ecosystem integration design (not implemented)

SkillParity (https://github.com/splucasaugusto666/skillparity) compares actual file paths and bytes between skill directories. It is complementary to this project's catalog and installation. Proposed integration: run its read-only parity check on the source and installed copies, using the published interface after checking the selected version. No dependency or modification is made.

OpenActionProof (https://github.com/splucasaugusto666/OpenActionProof) explores independent outcome verification and evidence receipts. Proposed integration: evaluate external actions against predeclared expected outcomes with a separate observer; distinguish outcome satisfaction from proof of causality. The current project has no runtime adapter and does not claim third-party attestations.
