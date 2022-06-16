#!/usr/bin/env python3

# Zac the Wise on 24 May
# Little script that adds emojis and labels for git commits
# More info: https://github.com/TechWiz-3/git-commit-emojis 

from sys import argv  # import cli arguement function
from sys import exit  # import exit function
from os import system

def help():
    """Help command"""
    BOLD = "\u001b[1m"
    RESET = "\033[0m"
    print(
        "\n"
        "Git emoji/labeling tool created by Zac the Wise"
        "\n\n"
        f"{BOLD}Basic Usage:{RESET}"
        "\n\n"
        "gc -m <commit message>"
        "\n\n"
        "      -h, --help      shows this command"
        "\n\n"
        "      -m <\"message\">     commit message (required), quotation marks not required"
        "\n\n"
        f"{BOLD}Advanced Usage:{RESET}"
        "\n\n"
        "ALTERNATE SELECT MENUS\nUsage:\ngc [select menu option] -m <commit message>"
        "\n\n   -e, --extras    displays a select menu with other labels that are used less often"
        "\n\n   -s, --strict    displays a select menu strictly in line with the emoji log project by ahmad awais"
        "\n\nSHORTCUTS"
        "\n\nThe commit option can be omitted for shortcut commit messages:\n"
        "\n\t-sh <shortcut>      puts the commit message for you as the value of 'shortcut'\n\n"
        "Available shortcuts:\n\n"
        "ty     commit message defaults to: ✏️ FIX TYPO\n"
        "cl     commit message defaults to: 🧹 CLEAN UP\n"
        "in     commit message defaults to: 🎉 INITIAL COMMIT\n"
        "\n\n"
    )

def get_opts():
    """Get cli options/arguements"""
    for arg in argv[1:]:  # gets arguements except the first one and assigns them
        if arg == "-m":  # message option
            commit_message = ""
            # get the argument for the option
            get_arg_index = argv.index('-m')  # find the index number for the option
            try:
                args_after_m = argv[get_arg_index+1:]
                for msg_word in args_after_m:
                    commit_message += f"{msg_word} "
                commit_message = commit_message[:-1]  # remove extra space from end
            except IndexError:
                return "error", "You didn't include the arguement for the commit message like so: -m \"my commit message\""
            else:
                if commit_message == "":  # if the commit message is empty
                    return "error", "Commit message cannot be empty"
                return "message only", commit_message
        elif arg == "-sh":
            get_arg_index = argv.index('-sh')  # find the index number for the option
            try:
                shortcut = argv[get_arg_index+1]  # get the arguement after the option and assign it
            except IndexError:
                return "error", "You didn't include the arguement for the shortcut type: -sh <shortcut value>"
            else:
                if shortcut == "":  # if the shortcut value is empty
                    return "error", "Shortcut value cannot be empty"
                elif shortcut == "ty" or shortcut == "typo":
                    commit_message = "✏️ FIX TYPO"
                    return "shortcut", commit_message
                elif shortcut == "cl" or shortcut == "clean":
                    commit_message = "🧹 CLEAN UP"
                    return "shortcut", commit_message
                elif shortcut == "in" or shorcut == "init" or shortcut == "initial":
                    commit_message = "🎉 INITIAL COMMIT"
                    return "shortcut", commit_message
                else:
                    return "error", "Unrecognized shortcut usage"
        elif arg in ("-s", "--strict"):  # strict select menu option
            commit_message = ""  # label + user input message
            message = ""  # raw user input message
            get_arg_index = argv.index(arg)
            try:
                args_after_s = argv[get_arg_index+1:]
                if args_after_s[0] == "-m":
                    try:
                        message = args_after_s[1]
                    except IndexError:
                        return "error", "You didn't include the arguement for the commit message like so: -m \"my commit message\""
                    else:
                        if message == "":
                            return "error", "Commit message cannot be empty"
                        else:
                            message = args_after_s[1:]
                            for word in message:
                                commit_message += f"{word} "
                            return "strict", commit_message
                elif args_after_s[0] == "":
                    return "error", "After the -s or --strict, add the commit message directly or with the -m switch"
                else:
                    message = args_after_s[0:]
                    for word in message:
                        commit_message += f"{word} "
                    return "strict", commit_message
            except IndexError:
                return "error", "You need to include your commit message after the -s or --strict option, you can do this directly after the option or use the -m <commit message> option"
            # ensure next argument is -m
            # get the emssage
            # ensure the message isn't empty or non-existant
            # assign commit_message
            # return "message only", commit_message
        elif arg == "-h" or arg == "--help":  # help option
            help()  # display help message
            return exit()  # stop the rest of the program from running

def select_menu():
    """Displays the select menu and returns the value to enter into the commit"""
    options = ["👌 Improvement", "📦 Addition", "📖 Documentation", "🐛 Bug-fix", "🔖 Version-tag", "🚪 Exit"]
    commit_label = ""
    for option in options:
        opt_no = options.index(option)
        print(f"{opt_no+1}) {option}")
    select_label = int(input("Enter the number corresponding to which type of change you made: "))
    if select_label == 1:
        commit_label = "👌 IMPROVE: "
    elif select_label == 2:
        commit_label="📦 NEW: "
    elif select_label == 3:
        commit_label="📖 DOC: "
    elif select_label == 4:
        commit_label="🐛 FIX: "
    elif select_label == 5:
        commit_label="🔖 "
    elif select_label == 6:
        print("Exiting, have a nice day...")
        exit()
    else:
        print("Unrecognised menu option, exiting...")
        exit()
    return commit_label


def second_menu():
    """Displays another select menu with more options that are used less often"""
    pass


def strict_menu():
    """Displays a select menu which strictly follows the labels specified by
    the emoji log project by ahmadawais"""
    options = ["👌 Improvement", "📦 Addition", "📖 Documentation", "🐛 Bug-fix", "🚀 Release", "🤖 Test", "‼️  Breaking", "🚪 Exit"]
    for option in options:
        opt_no = options.index(option)
        print(f"{opt_no+1}) {option}")
    select_label = int(input("Enter the number corresponding to which type of change you made: "))
    if select_label == 1:
        commit_label = "👌 IMPROVE: "
    elif select_label == 2:
        commit_label = "📦 NEW: "
    elif select_label == 3:
        commit_label = "📖 DOC: "
    elif select_label == 4:
        commit_label="🐛 FIX: "
    elif select_label == 5:
        commit_label = "🚀 RELEASE:  "
    elif select_label == 6:
        commit_label = "🤖 TEST: "
    elif select_label == 7:
        commit_label = "‼️ BREAKING: "
    elif select_label == 6:
        print("Exiting, have a nice day...")
        exit()
    else:
        print("Unrecognised menu option, exiting...")
        exit()
    return commit_label

if __name__ == "__main__":

    options = get_opts()
    if options == None:
        print("Incorrect usage. Refer to gc.py --help")
    else:
        typ, msg = options
        if typ == "message only":
            label = select_menu()
            system(f"git commit -m \"{label}{msg}\"")

        elif typ == "strict":
            label = strict_menu()
            system(f"git commit -m \"{label}{msg}\"")

        elif typ == "shortcut":
            system(f"git commit -m \"{msg}\"")

        elif typ == "error":
            print(f"Error occured: {msg}")

