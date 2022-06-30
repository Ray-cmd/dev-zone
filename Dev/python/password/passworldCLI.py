"""
Password Generator
    The software is maid to generate password,
    You can generate password in bulk and export them in a txt file

TODO
    - Add posibility to input a path with the --export flag
        This feature will allow to chose in wich directory 
        the file will be created. It will also allow to chose
        the name of the file
        EXEMPLE : passworldCLI.py -s -l32 -n100 --export ~/Documents/password  


        test
"""
import argparse
from datetime import datetime
import pyperclip
from rich.console import Console

from libs.password import Password as pwd

def write_file(password):
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{time}-password.txt"
    with open(filename, "w") as file:
        if type(password) == str:
            file.write(str(password))
        else :
            for el in password:
                file.write(str(el))
                file.write("\n")
    console.print(f"[bold][+][/] The file [bold underline green]{filename}[/] was generate", style="green")
    
if __name__ == "__main__":
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
        action="store_true",
        help="Export the password on an text file or clipboard",
    )
    args = parser.parse_args()

    console = Console()
    print("")
    if args.num == 1:
        gen_pwd = str(pwd(length=args.length, has_digits=args.digits, has_specials=args.specials))
        if not args.export:
            print(gen_pwd)
            print("")
        pyperclip.copy(gen_pwd)
        console.print("[bold][+][/] The password was copied to the clipboard", style="green")
    else:
        gen_pwd = []
        for _ in range(args.num):
            password = pwd(length=args.length, has_digits=args.digits, has_specials=args.specials)
            gen_pwd.append(password)
            if not args.export:
                print(password)

    if args.export:
        write_file(gen_pwd)
    print("")