# Created by Zac the Wise
# This file is used to execute the tool's various
# help commands without clogging the main file.

class Help():

    BOLD = "\u001b[1m"
    RESET = "\033[0m"

    def __init__(self, cmd: str = None) -> None:
        self.cmd = cmd
        if cmd == "regular":
            self.regular()
            return None
        elif cmd == "shortcuts":
            self.shortcut()


    def regular(self):
        """Regular/standard help command"""
        print("")
        print("Git emoji/labeling tool created by Zac the Wise")
        print("")
        print(f"{Help.BOLD}Basic Usage:{Help.RESET}")
        print("")
        print("commit -m <commit message>")
        print("")
        print("      -h, --help              shows this command")
        print("")
        print("      -m \"<message>\"        commit message (required), quotation marks not required")
        print("")
        print(f"{Help.BOLD}Advanced Usage:{Help.RESET}")
        print("")
        print("ALTERNATE SELECT MENUS\nUsage:\ncommit [select menu option] -m <commit message>")
        print("")
        print("   -e, --extra    displays a select menu with other labels that are used less often")
        print("")
        print("   -s, --strict    displays a select menu strictly in line with the emoji log project by ahmad awais")
        print("")
        print("SHORTCUTS")
        print("The commit option can be omitted for shortcut commit messages:\n")
        print("commit -sh <shortcut>      puts the commit message for you as the value of 'shortcut'")
        print("")
        print("Available shortcuts:")
        print("ty     commit message defaults to: ✏️ FIX TYPO")
        print("cl     commit message defaults to: 🧹 CLEAN UP")
        print("in     commit message defaults to: 🎉 INITIAL COMMIT")
        print("ln     commit message defaults to: 🚨 FIX LINT WARNINGS")
        print("")
        print(f"SPECIAL OPTIONS\n")
        print("commit [special-options] [options] \"<commit message>\"")
        print("")
        print("       --add <file1> ...     git add specified files before committing")
        print("       --push                push after committing\n")
        print("       --add-push <file1>... git add and git push")
        print("Special options are placed before the menu and message related options")
        print("")
        print("SPECIAL UTILITIES")
        print("Usage:")
        print("commit [special utility]")
        print("")
        print("  -sa, --show-all             displays all select menu options and their related labels")
        print("")
        print("  -l,  --get-label -m <commit message>     returns the commit",
              "label without commiting anything\n",
              "                                          (can be used anywhere including  non-git repos)")
        print("")
        print("")
        print("Please submit any issues or bugs to https://github.com/TechWiz-3/git-commit-emojis/issues")
        print("")


    def shortcut(self):
        """Shortcuts help command"""
        print("")
        print("Shortcut usage: commit -sh shortcut")
        print("")
        print("Shortcuts use pre-prepared commit messages for simple commit messages, refer to them by their assigned abbreviation")
        print("")
        print("List of shortcuts:")
        print("")
        print("Value                           Message")
        print("cl or clean                     🧹 CLEAN UP")
        print("ty or typo                      ✏️  FIX TYPO")
        print("in or init or initial           🎉 INITIAL COMMIT")
        print("ln or lint or linter            🚨 FIX LINT WARNINGS")
        print("")
