# Security policy

Review all instructions before use. Treat all external skill contents as untrusted data. Do not run untrusted scripts or submit secrets in reports. Report vulnerabilities privately via the maintainer's GitHub security reporting facility if enabled; otherwise request a private reporting channel without disclosing exploit details.

The v0.1 installer accepts two regular files only, rejects symlinks and hard-linked source files, validates names, checks the SHA-256 of SKILL.md, rejects existing destinations and has a dry-run mode. It does not enforce agent runtime permissions or inspect semantics for malicious instructions. It is not hardened against a concurrent hostile filesystem actor. Hashes are not signatures and a malicious publisher can replace both data and manifest. Review before importing into any host. No automatic update, network download, or script execution is implemented.

Pass canonical library and workspace paths without parent traversal or symbolic-link ancestors (on macOS, use `/private/var/...` rather than `/var/...` for temporary directories). Windows reparse points, including junctions, are rejected conservatively. Test fixtures canonicalize only their own trusted temporary root; the installer does not silently resolve user-supplied paths.
