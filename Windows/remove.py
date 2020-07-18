import os
import stat
import sys

from colorama import init, Fore, Style
from github import Github

"""
Author: Red Williams (Red-CS)
Email:  red.devcs@gmail.com

July 18, 2020
"""

def remove():
    """Removes first a remote repository, then a local one. If a local
    repository isn't found, it will abort (since this is mainly for GitHub)
    Note that the argument called is os.environ.get() can be anything, as
    long as it is definied in your user variable list.
    """
    # Setup

    # Activiate color mode!
    init()

    if len(sys.argv) == 1:
        general_usage()
        sys.exit(0)

    elif len(sys.argv) > 2:
        print(f"Syntax Error: Command requires only one argument, {int(len(sys.argv) - 1)} were given.")
        general_usage()
        sys.exit(1)

    # Log in
    token = os.environ.get("PWFA-Token")
    g = Github(token)
    user = g.get_user()
    login = user.login

    list = ["-l", "--list"]

    # Remove remote repository

    # remove -l, --list
    if str(sys.argv[1]) in list:
        repo_number = 0
        print()
        for repo in user.get_repos():
            repo_number += 1
            print(f"  {repo_number}.   {repo.name}")
        print()      
        sys.exit(0)
    else:
        try:

            git_url = "https://github.com/"

            # remove -X
            if (
                str(sys.argv[1]).startswith("-") and 
                str(sys.argv[1])[1:].isnumeric()
               ):
                passed_int = int(str(sys.argv[1])[1:])
                local_repo_name = user.get_repos()[passed_int - 1].name
                repo_url =  "{}{}".format(git_url, 
                                          user.get_repos()[passed_int - 1].full_name)
                
                # Confirm deletion
                if ask_delete_repo(repo_url):
                    user.get_repos()[passed_int - 1].delete()
                    print(f"Deleted repository {repo_url}")
                else:
                    print("Remote repository not deleted.")
            else:
            # remove repoName
                passed_str = str(sys.argv[1])
                local_repo_name = passed_str
                repo_url = "{}{}".format(git_url, 
                                         user.get_repo(passed_str).full_name)

                # Confirm deletion
                if ask_delete_repo(repo_url):
                    user.get_repo(passed_str).delete()
                    print(f"Deleted repository {repo_url}")
                else:
                    print("Remote repository not deleted.")
        except:
            # TODO Run refactor local to test other possible repo name
            print(f"Naming Error: Error in finding remote repository \"{local_repo_name}\"")
            sys.exit(1)

    # Move on to local or exit
    if not ask_continue_local():
        sys.exit(0)
    
    # Remove local repository

    path = os.environ.get("PWFA-Path")

    # Search local repos with dashes
    if os.path.isdir(f"{path}\\\\{local_repo_name}"):

        path += "\\\\" + local_repo_name

        # Delete if selected
        if ask_delete_repo(local_repo_name):
            remove_local_directory(path, local_repo_name)
        else:
            print("Local repository not deleted.\n")

    # Search local repos with spaces
    elif os.path.isdir(f"{path}\\{refactor_local(local_repo_name)}"):

        local_repo_name = refactor_local(local_repo_name)
        path += "\\\\" + local_repo_name

        # Delete if selected
        if ask_delete_repo(path):
            remove_local_directory(path, local_repo_name)
        else:
            print("Local repository not deleted.\n")

    # Local repository not found
    else:
        print("A directory with that name could not be found.")

def ask_delete_repo(repo_name):
    """Prompts the user if they are sure they want to delete the
    repository. Used for both deleting the local and remote repository.
    There is no auto confirm tag since this is a special process, I don't
    want anyone to accidentally delete a repository.
    """
    print()
    print(Fore.RED)
    print(f"Warning! Executing this command would remove {repo_name}")
    print("Are you sure you want to delete this repository (y/n)? ", end=Style.RESET_ALL)
    usr = input()
    return usr.lower() == "y"

def ask_continue_local():
    """Prompts the user if they want to continue to search for and delete
    a local repository after being asked to delete a remote repository.
    """
    print()
    print()
    usr = input("Continue to search for and delete a local repository (y/n)? ")
    return usr.lower() == "y"

def refactor_local(repo_name):
    """Changes the name of the repository staged for remote deletion to 
    test if it was saved under a slightly different name locally. For example
    and as you know, GitHub repository names have dashes instead of spaces.
    This project allows for repository names with spaces. Thus, a remote name
    could be "Remote-Repository" while a local name could be "Remote Repository"
    This method changes the passed repo_name by replacing dashes with spaces.
    Note that repository names with apostrophes (') also appear with dashes,
    so don't use those when creating a repository with this project.
    """
    local_name = ""
    for char in repo_name:
        if char == "-":
            local_name += " "
        else:
            local_name += char
    return local_name

def remove_local_directory(directory_path, directory_name):
    """Removes all files, directories, and sub directories of a 
    local repository, printing what is deleted with every iteration.
    Note some files initialized with git are read only and can't be 
    deleted normally. This gives access and deletes the proper files,
    giving a better output if there is an error.
    """
    print()
    for root_path, directories, files in os.walk(directory_path, topdown=False):
        relative_path = root_path[root_path.index(directory_name):]
        for name in files:
            filename = os.path.join(root_path, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
            print("  Deleted File:        {}\\{}".format(relative_path, name))
        for name in directories:
            os.rmdir(os.path.join(root_path, name))
            print("  Deleted Directory:   {}\\{}".format(relative_path, name))
    os.rmdir(directory_path) 
    print()
    print(f"  Deleted Parent Directory:    {directory_path}")
    print()

def general_usage():
    """Prints general usage of the remove command"""
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
