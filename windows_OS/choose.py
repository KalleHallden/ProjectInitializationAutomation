import os
import sys

def choose():
    print(f"sys.argv --> {str(sys.argv)}")

    args = {}
    try:
        args["name"] = str(sys.argv[1])
    except IndexError:
        print("Index error, need name. Showing usage")

    for i in range(1, len(sys.argv)):

        # Test for -h or --help
        if str(sys.argv[i]) == "-h" or str(sys.argv[i]) == "--help" or str(sys.argv[i]) == "help()":
            if len(sys.argv) != 3:
                help_usage()
                sys.exit()
            
            print("Print either general usage or usage for next arg, exiting this program")

        # Test for -l or --local
        if str(sys.argv[i]) == "-l" or str(sys.argv[i]) == "--local":
            print("testing if only a name is included")
            if len(sys.argv) != 3:
                print("you didn't include a name, showing usage and exiting")
            print("Running local, exiting this program")
        
        # Test for -d or --description
        if str(sys.argv[i]) == "-d" or str(sys.argv[i]) == "--description":
            print(f"Adding your description: {str(sys.argv[i+1])}")

        # Test for -p or --private
        if str(sys.argv[i]) == "-p" or str(sys.argv[i]) == "--private":
            print("Setting repo to private and continuing")


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
    



if __name__ == "__main__":
    choose()