#!/usr/bin/env python3

# Zac the Wise on 24 May
# Little script that adds emojis and labels for git commits
# More info: https://github.com/TechWiz-3/git-commit-emojis 

from sys import argv  # import cli arguement function
from sys import exit  # import exit function
from os import system

def help():
    """Help command"""
    print(
        "\n\n"\
        "Git emoji/labeling tool created by Zac the Wise"\
        "\n\n"\
        "Basic Usage:",
        "\n\n"\
        "gc -m <commit message>"\
        "\n\n"\
        "      -h, --help      shows this command"\
        "\n\n"\
        "      -m <\"message\">     commit message (required), use quotation marks"\
        "\n\n"\
        "Advanced Usage:"\
        "\n\n"\
        "The commit option can be omitted for shortcut commit messages:"\
        "\n\n"\
        "       -sh <shortcut>      puts the commit message for you as the value of 'shortcut'"\
        "\n\n"\
        "Shortcuts:\n\n"\
        "ty     commit message defaults to: ✏️ FIX TYPO\n\n"\
        "cl     commit message defaults to: 🧹 CLEAN UP\n\n"\
        "in     commit message defaults to: 🎉 INITIAL COMMIT\n"\
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
        elif typ == "shortcut":
            system(f"git commit -m \"{msg}\"")
        elif typ == "error":
            print(f"Error occured: {msg}")
