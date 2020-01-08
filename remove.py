import sys
import getpass
from github import Github

reponame = sys.argv[1]

def remove():
    username = raw_input("Username for 'www.github.com': ")
    password = getpass.getpass("Password for '" + username + "@github.com': ")
    user = Github(username, password)
    try:
        repo = user.get_repo(username + "/" + reponame)
        repo.delete()
        print("Repository deleted.")
    except:
        print("No repo found!")

if __name__ == "__main__":
    remove()
