'''
Script to automatically clean up my Rust project
build artifacts via 'cargo clean'

@author mnowzari
'''
# pylint: disable=broad-except
import glob
import subprocess as subpop

DIRECTORY_TO_SEARCH = "/home/mattnowzari/Documents/rust_projects"

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


def glob_and_clean() -> bool:
    '''
    Glob through my Rust projects directory and run 'cargo clean'
    in each directory
    '''
    search_pattern = '/'.join([f"{DIRECTORY_TO_SEARCH}", "*", "Cargo.toml"])

    print(f"\n:: Searching {search_pattern} ::")

    for cargo_toml_dir in glob.glob(search_pattern):
        proj_dir = "/".join(cargo_toml_dir.split("/")[:-1])
        print(f"\n{proj_dir}")
        cmd_cargo_clean(proj_dir, [])
    return True


if __name__ == "__main__":
    HEADER = "\n==| Rust Auto Clean |=="
    FOOTER = "\n--| Script Complete |--\n"
    print(f"{HEADER}")
    glob_and_clean()
    print(f"{FOOTER}")
