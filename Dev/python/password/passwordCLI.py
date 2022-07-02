"""
Password Generator
    The software is maid to generate password,
    You can generate password in bulk and export them in a txt file
"""
import argparse
from datetime import datetime
from pathlib import Path

import pyperclip
from rich.console import Console

from libs.password import Password as pwd

def dir_path(path):
    """
    The function check if the path is a valide directory
    If it is, it add a generic file name to it with the datetime
    If not, it assume that the path is a file name
    """

    p = Path(path)
    if p.is_dir():
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{time}-password.txt"
        p = p / filename
    return p

def write_file(password, path):
    """
    This function open the file pass in argument, 
    if the file exist, it will erase it, 
    if the file dont exist, it will be created

    If password is a string (just one password),
    the function, wrote it in the file.

    If password is not a string, it assume it's an array
    of password and loop trough it to write every line in
    the file
    """
    with open(path, "w") as file:
        if type(password) == str:
            file.write(str(password))
        else :
            for el in password:
                file.write(str(el))
                file.write("\n")
    console.print(f"[green][bold][+][/] The file [bold underline]{path}[/] was generate")
    
if __name__ == "__main__":
    # --- Build the command line tool ---
    parser = argparse.ArgumentParser(description="Generate a password")
    parser.add_argument(
        "--length",
        "-l",
        type=int,
        default=12,
        help="Length of the password"
    )
    parser.add_argument(
        "--digits",
        "-d", 
        action="store_false",
        help="Add digits to the password",
    )
    parser.add_argument(
        "--specials",
        "-s",
        action="store_true",
        help="Add specials to the password",
    )
    parser.add_argument(
        "--num",
        "-n",
        type=int,
        default=1,
        help="Number of password to generate",
    )
    parser.add_argument(
        "--export",
        "-e",
        dest="path",
        type=dir_path,
        help="Export the password on an text file or clipboard",
    )
    args = parser.parse_args()

    # --- Initialize Rich console ---
    console = Console()
    
    print("")
    # If one password is asked
    if args.num == 1:
        # Generate the password with the arguments passed via the command line
        gen_pwd = str(pwd(length=args.length, has_digits=args.digits, has_specials=args.specials))
        # Put the password in the clipboard
        pyperclip.copy(gen_pwd)
        console.print("[green][bold][+][/] The password was copied to the clipboard")
        # If it's not an export, print the password on the console
        if not args.path:
            console.print(f"[bold white]{gen_pwd}")
    # If more then one password is asked
    else:
        gen_pwd = []
        # Generate the number of password passed in the parameters
        for _ in range(args.num):
            # Generate the password with the arguments passed via the command line
            password = pwd(length=args.length, has_digits=args.digits, has_specials=args.specials)
            # Add the password the the list
            gen_pwd.append(password)
            # If it's not an export, print the password on the console
            if not args.path:
                console.print(f"[bold white]{password}",)
    # If it's an export, write the file
    if args.path:
        write_file(gen_pwd, args.path)
    print("")