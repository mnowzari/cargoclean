'''
Script to automatically clean up my Rust project
build artifacts via 'cargo clean'

@author mnowzari
'''
# pylint: disable=broad-except
import click
import glob
import subprocess as subpop

HEADER = "\n==| Rust Auto Clean |=="
FOOTER = "\n--| Script Complete |--\n"

def run(cmd: list) -> bool:
    '''
    Function to run a given command
    '''
    try:
        # print(f"  Command {cmd}\n")
        # shell=True is not great but wtv
        subpop.check_output(" ".join(cmd), shell=True)
        return True
    except Exception as e_msg:
        print(f"Exception {e_msg} occurred during the runtime of cmd {cmd}")
        return False


def cmd_cargo_clean(project_dir: str, options: list) -> bool:
    '''
    Function for forming and running the cargo clean command
    '''
    try:
        cmd = [f"cd {project_dir};", "cargo", "clean"]
        if options:
            cmd.extend(options)
        run(cmd)
        return True
    except Exception as e_msg:
        print(f"Exception {e_msg} occurred during func cmd_cargo_clean()")
        return False


def glob_and_clean(target_dir) -> bool:
    '''
    Glob through my Rust projects directory and run 'cargo clean'
    in each directory
    '''
    search_pattern = '/'.join([f"{target_dir}", "*", "Cargo.toml"])

    print(f"\n:: Searching {search_pattern} ::")

    for cargo_toml_dir in glob.glob(search_pattern):
        proj_dir = "/".join(cargo_toml_dir.split("/")[:-1])
        print(f"\n{proj_dir}")
        cmd_cargo_clean(proj_dir, [])
    return True

@click.command()
@click.option('--target_dir',
        type=click.Path(),
        required=True,
        help='The directory of Rust projects you want cleaned.')
def main(target_dir):
    print(f"{HEADER}")
    glob_and_clean(target_dir)
    print(f"{FOOTER}")

if __name__=='__main__':
    main()
