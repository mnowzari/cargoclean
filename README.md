# Cargo Clean
## Script to quickly clean up my Rust project build artifacts

Script will run "cargo clean" on all projects under a provided --target_dir 

### Wishlist/to-do:
- _Improve how the script discovers Rust repos it can run "cargo clean" in. Currently it looks for a Cargo.toml, but only at the top level of the directory_
