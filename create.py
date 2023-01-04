import sys
import os
import configparser
from github import Github

def create_repository(token, foldername):
    # Authenticate to GitHub with a personal access token
    g = Github(token)
    user = g.get_user()

    # Create a new repository on GitHub
    repo = user.create_repo(foldername)

def create_local_repository(foldername, file_path):
    # Construct the full path to the new folder
    _dir = file_path + '/' + foldername

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

def create():
    # Extract folder name and file path from command line arguments
    foldername = str(sys.argv[1])
    file_path = str(sys.argv[2])

    # Read the personal access token from a configuration file
    config = configparser.ConfigParser()
    config.read(file_path)
    token = config['github']['token']

    # Create the repository on GitHub
    create_repository(token, foldername)

    # Create the local repository
    create_local_repository(foldername, file_path)

if __name__ == "__main__":
    create()
