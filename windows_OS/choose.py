import os
import sys

def choose():
    print(f"sys.argv --> {str(sys.argv)}")

    if len(sys.argv) == 1:
        general_usage()
        sys.exit(0)

    args = {                            # Example input:
        "name" :            "",         # "My repo name"
        "description" :     "",         # "My repo description"
        "publicity" :       "public",   # public
        "auto_confirm" :    "false"     # true
    }
    args["name"] = str(sys.argv[1])

    params = {
        "help" :            ["-h", "--help", "help()"],
        "description" :     ["-d", "--description"],
        "private" :         ["-p", "--private"],
        "local" :           ["-l", "--local"],
        "auto_confirm" :    ["-y", "--yes", "--auto-confirm"]
    }

    for i in range(1, len(sys.argv)):

        # Test for -h, --help, or help()
        if str(sys.argv[i]) in params["help"]:

            if len(sys.argv) == 2:                              # "create -h" prints general usage
                general_usage()

            elif len(sys.argv) > 3:                             # "create -d -p -h" user doesn't know how to use -h properly
                help_usage()

            else:                                               # "create --description --help" proper use for option parameter
                op_param = str(sys.argv[len(sys.argv) - i]) # len(sys.argv) is 3, checking non help or create param

                if op_param in params["description"]:
                    description_usage()

                elif op_param in params["private"]:
                    private_usage()

                elif op_param in params["local"]:
                    local_usage()

                elif op_param in params["auto_confirm"]:
                    auto_confirm_usage()

                else:
                    print(f"Unknown Option Error: \"{op_param}\" is not recognized")
                    sys.exit(1)

            sys.exit(0)

        # Test for -l or --local
        if str(sys.argv[i]) in params["local"]:
            if len(sys.argv) == 2:      # No name is included ("create -l")
                print("Naming Error: Repository name not included.")
                sys.exit(1)
            elif len(sys.argv) == 3 and i == 2:
                # TODO Run local.py with name parameter
                print("Here I am, running local.py with the name parameter.")
            elif len(sys.argv) == 3 and str(sys.argv[i+1]) in params["help"]:
                local_usage()
            else:
                print("Syntax Error: Type \"create -l help()\" for usage.")     
            sys.exit(0)

        # Test for -d or --description
        if str(sys.argv[i]) in params["description"]:
            # TODO Add description
            try:
                if not is_tag(tag=str(sys.argv[i+1]), dict=params):
                    args["description"] = str(sys.argv[i+1])
            except IndexError:
                print("Unknown Option Error: A description tag was used but no description was provided.")
                sys.exit(1)
            
            print(f"Added your description: {str(sys.argv[i+1])}")

        # Test for -p or --private
        if str(sys.argv[i]) in params["private"]:
            # TODO Set repo to private
            args["publicity"] = "private"
            print("Setting repo to private and continuing")
        
        # Test for -y, --yes, or --auto-confirm
        if str(sys.argv[i]) in params["auto_confirm"]:
            # TODO Set repo to push automatically
            args["auto_confirm"] = "true"
            print("Set repo to automatically, without confirmation message.")
    
    print("Here I am, we finished!!!")
    print("Oh, and here are the passed arguments:")
    print(str(args))


def general_usage():
    print()
    print("Usage:")
    print("  create <repository name> [options]\n")

    print("Commands:")
    print("  create\t\t\t\tCreate a repository.")
    print("  remove\t\t\t\tRemove a repository.")
    print()
    print("Optional Parameters:")
    print("  -h, --help\t\t\t\tPrints general usage or usage of a specific option.")
    print("  -d, --description\t\t\tAdd a description to the remote repository.")
    print("  -p, --private\t\t\t\tSet remote repository to private.")
    print("  -l, --local\t\t\t\tCreate a local repository; does not push to Github.")
    print("\t\t\t\t\tUse only a repository name and this parameter.")
    print("  -y, --yes, --auto-confirm\t\tAutomatically initialize repository without confirmation message.")
    print()

def help_usage():
    print()
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
    print()

def description_usage():
    print()
    print("Usage:")
    print("  create <repository name> -d \"[repository description]\"")
    print("  create <repository name> --description \"[repository description]\"")
    print()
    print("  create <repository name> -d \"[repository description]\" [option]")
    print("  create <repository name> --description \"[repository description]\" [option]")
    print()
    print("Description:")
    print("  The description tag adds a descripiption to the remote repository.")
    print("  NOTE: Multi-word descriptions need to be surrounded by quotation marks (\"\")")
    print()

def private_usage():
    print()
    print("Usage:")
    print("  create <repository name> -p")
    print("  create <repository name> --private")
    print()
    print("  create <repository name> [option] -p")
    print("  create <repository name> [option] --private")
    print()
    print("Description:")
    print("  The private tag sets the remote repository to private, as it is")
    print("  defaulted to public.")
    print("  NOTE: The local tag must not be included, as local repositories")
    print("  cannot be public or private.")
    print()

def local_usage():
    print()
    print("Usage:")
    print("  create <repository name> -l")
    print("  create <repository name> --local")
    print()
    print("Description:")
    print("  The local tag is used to create a repository locally, not")
    print("  pushing to GitHub.")
    print("  NOTE: To create a local project, only include the project name")
    print("  (in quotation marks if it is multi-word), otherwise you will")
    print("  recieve an error.")
    print()

def auto_confirm_usage():
    print()
    print("Usage:")
    print("  create <repository name> -y")
    print("  create <repository name> --yes")
    print("  create <repository name> --auto-confirm")
    print()
    print("  create <repository name> [options] -y")
    print("  create <repository name> [options] --yes")
    print("  create <repository name> [options] --auto-confirm")
    print()
    print("Description:")
    print("  The auto-confirmation tag is used to automatically create a remote")
    print("  repository without confirming that the details are correct.")
    print()
    

def is_tag(tag, dict):
    for key in dict:
	    if tag in dict[key]:
		    return True
    return False

if __name__ == "__main__":
    choose()