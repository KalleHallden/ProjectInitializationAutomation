import os
import sys

from colorama import init, Fore, Style
from github import Github

init()

# Set passed repository attributes
repo_name = str(sys.argv[1])
repo_description = str(sys.argv[2])
if str(sys.argv[3]) == "Public":
    repo_publicity = False
else:
    repo_publicity = True


_dir = "{}\\{}".format(os.environ.get("PWFA-Path"), repo_name)

# Login to GitHub
token = os.environ.get("PWFA-Token")
g = Github(token)
user = g.get_user()
login = user.login
# Create remote repository
repo = user.create_repo(name=repo_name, 
                        description=repo_description,
                        private=repo_publicity)

# Create local directory and cd
if not os.path.isdir(_dir):
    os.mkdir(_dir)
os.chdir(_dir)

commands = [f'echo # {repo.name} >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{repo.name}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

# Initialize local repo and push 
for c in commands:
    os.system(c)

# TODO Add file path instead of "created locally"
print(Fore.GREEN)
print(f'Repository "{repo_name}" created locally and pushed to GitHub!')
print(f"Check it out at https://github.com/{login}/{repo.name}.git")
print(Style.RESET_ALL)
os.system('code .')