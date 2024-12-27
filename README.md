# Cargo Clean
## Script to quickly clean up Rust project build artifacts

Script will run "cargo clean" on all projects under a provided --target-dir.
Will also accept the "--release" flag to pass along to "cargo clean".

### Wishlist/to-do:
- _Possibly implement other "cargo clean" flags and arguments such as --dry-run, --doc, --verbose, --quiet, etc_
- _Improve how the script discovers Rust repos it can run "cargo clean" in. Currently it looks for a Cargo.toml, but only in the top level of the directories it finds_
