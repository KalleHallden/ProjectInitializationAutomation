# create.py

import sys
import os
from github import Github

def create_repository(username, password, foldername):
    # Authenticate to GitHub
    g = Github(username, password)
    user = g.get_user()

    # Create a new repository on GitHub
    repo = user.create_repo(foldername)

def create():
    # Extract folder name and file path from command line arguments
    foldername = str(sys.argv[1])
    file_path = str(sys.argv[2])

    # Set GitHub credentials from command line arguments
    username = sys.argv[3]
    password = sys.argv[4]

    # Create the repository on GitHub
    create_repository(username, password, foldername)

    # Print a success message
    print(f'Successfully created repository {foldername}')

if __name__ == "__main__":
    create()
