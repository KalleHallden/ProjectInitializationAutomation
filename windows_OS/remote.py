# remote.py

import sys
import os
from github import Github

def create_repository(username, password, foldername):
    # Authenticate to GitHub
    g = Github(username, password)
    user = g.get_user()

    # Create a new repository on GitHub
    repo = user.create_repo(foldername)

def create_local_repository(foldername):
    # Set file path from an environment variable
    path = os.environ.get('mp')

    # Construct the full path to the new folder
    _dir = path + '/' + foldername

    # Create the new folder and change the current working directory to it
    os.mkdir(_dir)
    os.chdir(_dir)

    # Initialize a Git repository and add a README file
    os.system('git init')
    os.system(f'echo "# {foldername}" > README.md')
    os.system('git add README.md')
    os.system('git commit -m "first commit"')

    # Print a success message and open the folder in Visual Studio Code
    print(f'{foldername} created locally')
    os.system('code .')

def remote():
    # Extract folder name and GitHub credentials from command line arguments
    foldername = str(sys.argv[1])
    username = sys.argv[2]
    password = sys.argv[3]

    # Create the repository on GitHub
    create_repository(username, password, foldername)

    # Create the local repository
    create_local_repository(foldername)

if __name__ == "__main__":
    remote()
