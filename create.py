import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("FILEPATH")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))
    user = Github(username, password).get_user()
    repo = user.create_repo(folderName)
    # f strings 
    print(f"Succesfully created repository {folderName}")

if __name__ == "__main__":
    create()
