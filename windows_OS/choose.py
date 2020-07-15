import os
import sys

def choose():
    print(f"sys.argv --> {str(sys.argv)}")

    args = {}
    try:
        args["name"] = str(sys.argv[1])
    except IndexError:
        print("Index error, need name. Showing usage")
        general_usage()

    params = {
        "help" :            ["-h", "--help", "help()"],
        "description" :     ["-d", "--description"],
        "private" :         ["-p", "--private"],
        "local" :           ["-l", "--local"],
        "auto_confirm" :    ["-y", "--yes"]
    }

    for i in range(1, len(sys.argv)):

        # Test for -h or --help
        if str(sys.argv[i]) in params["help"]:

            if len(sys.argv) == 2:                              # "create -h" prints general usage
                general_usage()

            elif len(sys.argv) > 3:                             # "create -d -p -h" user doesn't know how to use -h properly
                help_usage()

            else:                                               # "create --description --help" proper use for option parameter
                print("Showing optional usage:\n\n")
                op_param = str(sys.argv[len(sys.argv) - i]) # len(sys.argv) is 3, checking non help or create param

                if op_param in params["description"]:
                    print("Showing description usage")

                elif op_param in params["private"]:
                    print("Showing private usage")

                elif op_param in params["local"]:
                    print("Showing local usage")

                elif op_param in params["auto_confirm"]:
                    print("Showing auto confirm usage")

                else:
                    print("That option is not recognized")
                    sys.exit(1)

            sys.exit(0)

        # Test for -l or --local
        if str(sys.argv[i]) in params["local"]:
            print("testing if only a name is included")
            if len(sys.argv) != 3:
                print("you didn't include a name, showing usage and exiting")
            print("Running local, exiting this program")
            # TODO Can't exit here, case "create --local help()"
        
        # Test for -d or --description
        if str(sys.argv[i]) in params["description"]:
            print(f"Adding your description: {str(sys.argv[i+1])}")

        # Test for -p or --private
        if str(sys.argv[i]) in params["private"]:
            print("Setting repo to private and continuing")
        
        # Test for -y or --yes
        if str(sys.argv[i]) in params["auto_confirm"]:
            print("Will initialize repo automatically, without confirmation message.")


def general_usage():
    print("Usage:")
    print("  create <repo_name> [options]\n")

    print("Commands:")
    print("  create\t\t\t\tCreate a repository.")
    print("  remove\t\t\t\tRemove a repository.")
    print()
    print("Optional Parameters:")
    print("  -h, --help\t\t\t\tPrints general usage or usage of a specific option.")
    print("  -d, --description\t\t\t\tAdd a description to the remote repository.")
    print("  -p, --private\t\t\t\tSet remote repository to private.")
    print("  -l, --local\t\t\t\tCreate a local repository; does not push to Github.")
    print("\t\t\t\t\tUse only a repository name and this parameter")
    print("  -y, --yes\t\t\t\tAutomatically initialize repository without confirmation message.")

def help_usage():
    print("Syntax is incorrect.")
    print("Usage:")
    print("  create -h")
    print("  create --help")
    print("  create help()")
    print()
    print("  create [option] -h")
    print("  create [option] --help")
    print("  create [option] help()")
    print()
    print("Description:")
    print("  Explains usage of the \"create\" command and its options")

def description_usage():
    pass

def private_usage():
    pass

def local_usage():
    pass

def auto_confirm_usage():
    pass
    



if __name__ == "__main__":
    choose()