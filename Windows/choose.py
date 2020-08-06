import os
import sys

"""
Author: Red Williams (Red-CS)
Email:  red.devcs@gmail.com

July 18, 2020
"""

def choose():
    """Chooses which file, remote.py or local.py, is to be run.
    Also parses optional parameters (as definied in the params dict)
    for additional options when creating a repoisotry remotely. The
    API allows for a multiple arguments, but I've included the most 
    used options. That is why this is meant to be dynamic: if you
    want to add more commands, simply create a new tag in the params
    dictionary, add it to the if/else block, add to args if necessary,
    and read it in the appropriate file (remote.py or local.py).
    """

    # create: Case where only the create command is called
    if len(sys.argv) == 1:
        general_usage()
        sys.exit(0)

    args = {                            # Example input: create "My repo name" -d "My repo description" -y
        "name" :            "",         # "My repo name"
        "description" :     "",         # "My repo description"
        "publicity" :       "Public",   # public
        "auto_confirm" :    False       # True
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

            # create -h / create --help / create help()
            if len(sys.argv) == 2:        
                general_usage()

            # create -d -p -h: User doesn't know how to use -h properly
            elif len(sys.argv) > 3:       
                help_usage()

            # create --description --help: Proper use for optional parameter
            else:  
                       
                # Retrieve help-requested parameter
                op_param = str(sys.argv[len(sys.argv) - i])

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
        elif str(sys.argv[i]) in params["local"]:
            
            # create -l: Cases where no name is included
            if len(sys.argv) == 2:
                print("Naming Error: Repository name not included.")
                sys.exit(1)

            # create --local "My Repo Name": Cases where local creation is used correctly
            elif len(sys.argv) == 3 and i == 2:
                os.system("python local.py \"{}\"".format(str(sys.argv[1]))) # Must inlcude quotes
            
            # create -l help(): Get help on using the local tag
            elif len(sys.argv) == 3 and str(sys.argv[i+1]) in params["help"]:
                local_usage()
        
            else:
                print("Syntax Error: Type \"create -l help()\" for usage.")     
            sys.exit(0)

        # Test for -d or --description
        elif str(sys.argv[i]) in params["description"]:

            try:
                # create -d --private: Cases where description tag is used, but no description included
                if not is_tag(tag=str(sys.argv[i+1]), dict=params):
                    args["description"] = str(sys.argv[i+1])    # If next parameter is a tag, leaves description empty

            except IndexError:
                # create --private -d: Cases where description tag is last, where sys.argv[i+1] will raise IndexError
                print("Unknown Option Error: A description tag was used but no description was provided.")
                sys.exit(1)

        # Test for -p or --private
        elif str(sys.argv[i]) in params["private"]:
            args["publicity"] = "Private"
        
        # Test for -y, --yes, or --auto-confirm
        elif str(sys.argv[i]) in params["auto_confirm"]:
            args["auto_confirm"] = True
        
        else:
            # TODO More tags/optional params for the future.
            # That's up to you, creator!
            pass
    
    # Presents confirmation message to user
    if not args["auto_confirm"]:
        if not confirm_info(args):
            sys.exit(0)
    
    # Execution, baby!
    os.system("python remote.py \"{name}\" \"{description}\" {publicity}".format(**args))

def general_usage():
    """Shows general usage of the create command, as well as the existence of
    the remove command. Shows optional paramters as well. Remember to add to this list
    and the corresponding usage function when adding new tags.
    """
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
    """Shows how to use the help tags."""
    print()
    print("Syntax Error: Help tag is used incorrectly.")
    print()
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
    """Shows how to use the description tags"""
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
    """Shows how to use the private tags"""
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
    """Shows how to use the local tags"""
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
    """Shows how to use to automatic confirm tags"""
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
    
def confirm_info(dict):
    """Confirms if the called arguments are correct. This method only calls when
    one of the automatic confirm tags aren't listed.
    """
    print()
    print("The following arguments will be passed:")
    print("  Name:                 {name}".format(**dict))
    print("  Description:          {description}".format(**dict))
    print("  Publicity:            {publicity}".format(**dict))
    print()
    usr = input("Is this information correct (y/n)? ")
    return usr.lower() == "y"

def is_tag(tag, dict):
    """Helper method testing if a passed paramter is a defined tag."""
    for key in dict:
	    if tag in dict[key]:
		    return True
    return False

if __name__ == "__main__":
    choose()