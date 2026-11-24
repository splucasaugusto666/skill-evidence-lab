# Local test record

Executed in the build environment; not GitHub Actions or agent runtime tests.

```text
Python 3.13.5
12 skills statically validated
test_catalog (test_skilllab.TestLab.test_catalog) ... ok
test_catalog_snapshot (test_skilllab.TestLab.test_catalog_snapshot) ... ok
test_dry_run (test_skilllab.TestLab.test_dry_run) ... ok
test_duplicate_manifest_keys (test_skilllab.TestLab.test_duplicate_manifest_keys) ... ok
test_empty_library (test_skilllab.TestLab.test_empty_library) ... ok
test_extra_script (test_skilllab.TestLab.test_extra_script) ... ok
test_install_all_targets (test_skilllab.TestLab.test_install_all_targets) ... ok
test_manifest_name_mismatch (test_skilllab.TestLab.test_manifest_name_mismatch) ... ok
test_missing_skill (test_skilllab.TestLab.test_missing_skill) ... ok
test_no_overwrite (test_skilllab.TestLab.test_no_overwrite) ... ok
test_symlink_destination (test_skilllab.TestLab.test_symlink_destination) ... ok
test_symlink_source (test_skilllab.TestLab.test_symlink_source) ... ok
test_tamper (test_skilllab.TestLab.test_tamper) ... ok
test_traversal (test_skilllab.TestLab.test_traversal) ... ok
test_unknown_permission (test_skilllab.TestLab.test_unknown_permission) ... ok

----------------------------------------------------------------------
Ran 15 tests in 0.078s

OK
```

## Portability correction (release candidate)

Initial GitHub Actions run [45313593280](https://github.com/splucasaugusto666/skill-evidence-lab/actions/runs/45313593280): Ubuntu Python 3.13 passed; macOS Python 3.13 failed because the trusted temporary fixture was accessed through `/var`; four jobs were cancelled by fail-fast. The fixture now resolves its own trusted root. User-supplied symbolic-link ancestors remain rejected, parent traversal and Windows reparse points are rejected, and CI fail-fast is disabled. Python 3.13.5 local rerun: 12 skills validated; all 18 unittest cases passed, including workspace alias, parent traversal and simulated reparse-point classification. The latter is a mock, not a real Windows junction test. Remote matrix confirmation and real agent activation remain separate gates.
