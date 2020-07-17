import os
import sys
from github import Github



if len(sys.argv) != 2:
    print("Syntax Error")
    sys.exit(1)

# Log in
token = os.environ.get("PWFA-Token")

g = Github(token)
user = g.get_user()
login = user.login

list = ["-l", "--list"]

def remove():

    """Remove remote repository"""

    # remove -l, --list
    if str(sys.argv[1]) in list:
        pos = 0
        print()
        for repo in user.get_repos():
            pos += 1
            print(f"  {pos}.   {repo.name}")
        print()
            
        sys.exit(0)
    else:
        try:
            git_url = "https://github.com/"
            # remove -X
            if str(sys.argv[1]).startswith("-") and str(sys.argv[1])[1:].isnumeric():
                passed_int = int(str(sys.argv[1])[1:])
                l_repo_name = user.get_repos()[passed_int - 1].name # For removing local
                repo_url =  "{}{}".format(git_url, user.get_repos()[passed_int - 1].full_name)
                if delete_repo(repo_url):
                    user.get_repos()[passed_int - 1].delete()
                    print(f"Deleted repository {repo_url}")
            else:
            # remove repoName
                passed_str = str(sys.argv[1])
                l_repo_name = passed_str    # For removing local
                repo_url = "{}{}".format(git_url, user.get_repo(passed_str).full_name)
                if delete_repo(repo_url):
                    user.get_repo(passed_str).delete()
                    print(f"Deleted repository {repo_url}")
        except:
            # TODO Run refactor local to test other possible repo name
            print(f"Naming Error: Error in finding remote repository \"{l_repo_name}\"")
            sys.exit(1)

    if not continue_local():
        sys.exit(0)
    
    """Remove local repository"""

    path = os.environ.get("PWFA-Path")

    # Try searching for a local Repos with spaces or dashes
    if os.path.isdir(f"{path}\\{l_repo_name}"):
        if delete_repo(l_repo_name):
            delete_local(path, l_repo_name)
    elif os.path.isdir(f"{path}\\{refactor_local(l_repo_name)}"):
        l_repo_name = refactor_local(l_repo_name)
        if delete_repo(l_repo_name):
            delete_local(path, l_repo_name)
    else:
        print("Nope, DNE")




def delete_repo(repo_name):
    print()
    print()
    print("Warning!")
    print(f"  Executing this command would remove {repo_name}")
    print()
    print()
    usr = input("Are you sure you want to delete this repository (y/n)? ")
    return usr.lower() == "y"

def continue_local():
    print()
    print()
    usr = input("Continue to search for and delete a local repository (y/n)? ")
    return usr.lower() == "y"

def refactor_local(repo_name):
    local_name = ""
    for char in repo_name:
        if char == "-":
            local_name += " "
        else:
            local_name += char
    return local_name

def delete_local(path_stem, path_head):
    print()
    for dirpath, dirnames, filename in os.walk((path_stem + "\\" + path_head), topdown=False):
        for file in filename:
            try:
                os.remove("{}\\{}".format(dirpath, file))
            except:
                print(f"Failed with removing {dirpath}\\{file}")
                print("Passed:")
                print("  {}\\{}".format(dirpath, file))
                sys.exit(1)
            else:
                # TODO Fix issue where subdirectories containing files aren't shown
                print(f"  Deleted:   {path_head}\\{file}")
    print("Next step is to delete local repo")



def general_usage():
    print()
    print("Usage:")
    print("  remove <options>\n")

    print("Commands:")
    print("  create\t\t\t\tCreate a repository.")
    print("  remove\t\t\t\tRemove a repository.")
    print()
    print("Required Parameters:")
    print("  -l, --list\t\t\t\tPrints a list of your remote repositories.")
    print("  -X        \t\t\t\tRemoves the Xth repository. View list by typing \"remove -l\".")
    print("  <repository name> \t\t\tRemoves the remote repository with the given name.")
    print()
    
if __name__ == "__main__":
    remove()
