from os.path import exists
from os import system

class CommitUtils:

    def __init__(self):
        pass

    @classmethod
    def add_files(cls, args_after_add):
        """Takes in the arguements after an
        add command and git adds the files"""
        # supports -add and --add-push
        recognised_options = ["-m", "--push", "-e", "--extra", "-sh", "-s", "--strict"]
        for arg in args_after_add:
            if arg in recognised_options:
                break
            file_exists = exists(arg)
            if file_exists:
                system(f"git add {arg}")
            else:
                usr_opt = input(f"Error, '{arg}' file not found. Continue? [y/n] ")
                if (usr_opt.lower() in ( "y", "yes", "")):
                    pass
                else:
                    print("Exiting, have a nice day...")
                    print("")
                    exit()

