import sys
import os
from github import Github
from dotenv import load_dotenv
import pygit2
load_dotenv()

path = os.getenv("FILEPATH")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def create():
    folderName = str(sys.argv[1])
    user = Github(username, password).get_user()
    repo = user.create_repo(folderName)
    repo.create_file("README.md", "Initial commit","")
    repoClone = pygit2.clone_repository(repo.git_url, path + str(folderName))
    print(f"Succesfully created repository {folderName}")
    os.chdir(path+str(folderName))
    os.system("code .")

if __name__ == "__main__":
    create()
