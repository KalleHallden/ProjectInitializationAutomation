import os
import sys

from colorama import init, Fore, Style
from github import Github

"""
Author: Red Williams (Red-CS)
Email:  red.devcs@gmail.com

July 18, 2020
"""

"""Creates and pushes a repository locally and remotely with the passed arguments"""

# Color is beautiful!
init()

# Set passed repository attributes
repo_name = str(sys.argv[1])
repo_description = str(sys.argv[2])
if str(sys.argv[3]) == "Public":
    repo_publicity = False
else:
    repo_publicity = True


_dir = "{}\\\\{}".format(os.environ.get("PWFA-Path"), repo_name)

# Login to GitHub
token = os.environ.get("PWFA-Token")
g = Github(token)
user = g.get_user()
login = user.login

# Create remote repository
repo = user.create_repo(name=repo_name, 
                        description=repo_description,
                        private=repo_publicity)

# Create local directory and change into said directory
if not os.path.isdir(_dir):
    os.mkdir(_dir)
os.chdir(_dir)

# TODO Add README.md commit message parameter in choose.py
commands = [f'echo # {repo.name} >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{repo.name}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

# Initialize local repository and push to GitHub 
for command in commands:
    os.system(command)

print(Fore.GREEN)
print(f"Created \"{_dir}\" locally and pushed to GitHub!")
print(f"Check it out at https://github.com/{login}/{repo.name}.git")
print(Style.RESET_ALL)
os.system('code .') # TODO Add if/else block and os.environ.get for setting code editor preference, or another tag