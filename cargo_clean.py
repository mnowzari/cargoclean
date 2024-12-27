'''
Script to automatically clean up Rust project
build artifacts via 'cargo clean'
'''
# pylint: disable=broad-except, no-value-for-parameter

import os
import subprocess as subpop
import glob
import click

HEADER = "\n==| Rust Auto Clean |=="
FOOTER = "\n--| Script Complete |--\n"

def exec_cmd(cmd: list) -> bool:
    '''
    Function to run a given command
    The cmd list we receive maps as follows:
    [0] -> the project directory we need to cd to
    [1:] -> the "cargo clean" command and any passed flags
    '''
    try:
        print(f"Current directory: {cmd[0]}")
        os.chdir(cmd[0])
        clean_command = " ".join(cmd[1:])
        print(f"     Command: {clean_command}")
        subpop.check_output(clean_command, shell=True)
        return True
    except Exception as e_msg:
        print(f"Exception {e_msg} occurred during the runtime of cmd {cmd}")
        return False


def cmd_cargo_clean(project_dir: str, options: list) -> bool:
    '''
    Function for forming and running commands
    '''
    try:
        cmd = [project_dir, "cargo", "clean"]
        if options:
            cmd.extend(options)
        return exec_cmd(cmd)
    except Exception as e_msg:
        print(f"Exception {e_msg} occurred during func cmd_cargo_clean()")
        return False


def glob_and_clean(target_dir: str, release: bool) -> bool:
    '''
    Glob through given Rust projects directory and run 'cargo clean'
    in each directory
    '''
    search_pattern = os.path.join(target_dir, "*", "Cargo.toml")

    print(f"\n:: Searching for {search_pattern} ::")

    for cargo_toml_dir in glob.glob(search_pattern):
        proj_dir = os.path.dirname(cargo_toml_dir)
        print(f"\n{proj_dir}")
        options = []
        if release:
            options.append("--release")
        cmd_cargo_clean(proj_dir, options)
    return True

@click.command()
@click.option('--target-dir',
        type=click.Path(),
        required=True,
        help='The directory of Rust projects you want cleaned.')
@click.option('--release', is_flag=True)
def main(target_dir, release):
    ''' main '''
    print(f"{HEADER}")
    if release:
        print("\n--release was passed. \
                \nArtifacts under ../target/release/ will be deleted!.")

    glob_and_clean(target_dir, release)
    print(f"{FOOTER}")

if __name__=='__main__':
    main()
