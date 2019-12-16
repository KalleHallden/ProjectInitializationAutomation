""" Import Required Modules """
import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITTOKEN")

def create():
    """ Create Git Repo """
    path = sys.argv[1]
    name = sys.argv[2]

    # folderName = str(firstArg)
    os.makedirs(path)
    github = Github(TOKEN)
    user = github.get_user()

    repo = user.create_repo(name=name, auto_init=True)

    print(repo.git_url.replace("git://github.com/", "git@github.com:"))

if __name__ == "__main__":
    create()
    sys.exit(0)
