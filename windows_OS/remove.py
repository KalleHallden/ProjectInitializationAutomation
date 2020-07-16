import os
import sys
from github import Github

if len(sys.argv) != 2:
    print("Syntax incorrect")
    sys.exit(1)

# Log in
token = os.environ.get("PWFA-Token")

g = Github(token)
user = g.get_user()
login = user.login

list = ["-l", "--list"]

def remove():
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
                # remove -3
                if str(sys.argv[1]).startswith("-") and str(sys.argv[1])[1:].isnumeric():
                    passed_int = int(str(sys.argv[1])[1:])
                    repo_url =  "{}{}".format(git_url, user.get_repos()[passed_int - 1].full_name)
                    if delete_repo(repo_url):
                        user.get_repos()[passed_int - 1].delete()
                        print(f"Deleted repository {repo_url}")
                else:
                # remove repoName
                    passed_str = str(sys.argv[1])
                    repo_url = "{}{}".format(git_url, user.get_repo(passed_str).full_name)
                    if delete_repo(repo_url):
                        user.get_repo(passed_str).delete()
                        print(f"Deleted repository {repo_url}")
            except:
                print("Error in processing request")
            print()

def delete_repo(repo_name):
    for x in range(0, 3): print()
    print("Warning!")
    print(f"  Executing this command would remove {repo_name}")
    print()
    usr = input("Are you sure you want to delete this repository (y/n)? ")
    return usr.lower() == "y"

def general_usage():
    pass
    
if __name__ == "__main__":
    remove()
