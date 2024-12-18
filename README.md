# Cargo Auto-Clean
## Script to quickly clean up my Rust project build artifacts

Script will run "cargo clean" on all projects under "/rust_projects"

Feel free to modify this script as needed to target different directories.

### Wishlist/to-do:
- _Make this more command-line-friendly with click_
- _Improve how the script discovers Rust repos it can run "cargo clean" in. Currently it looks for a Cargo.toml, but only at the top level of the directory
