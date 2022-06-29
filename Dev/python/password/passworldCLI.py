import argparse
from datetime import datetime
import pyperclip

from libs.password import Password as pwd

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

    passwords = []
    for _ in range(args.num):
        password = pwd(length=args.length, has_digits=args.digits, has_specials=args.specials)
        if not args.export:
            print(password)
        passwords.append(password)

    if args.export:
        if args.num == 1:
            password = str(passwords[0])
            pyperclip.copy(password)
            print(f"The password {password} was copied on the clipboard")

        else:
            time = datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"{time}-password.txt"
            with open(filename, "w") as file:
                for password in passwords:
                    file.write(str(password))
                    file.write("\n")
            print(f"The file {filename} was generate with {args.num} passwords")