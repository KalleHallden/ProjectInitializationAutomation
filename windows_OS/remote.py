import sys
import os
from github import Github


if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Invalid syntax.\n")
    
    print("Usage:")
    print("  create <repo_name> [options]\n")

    print("Commands:")
    print("  create\t\t\t\tCreate a repository.")
    print("  remove\t\t\t\tRemove a repository.")
    print()
    print("Optional Parameters:")
    print("  -h, --help")
    print("  -d, --description\t\t\t\tAdd a description to the remote repository.")
    print("  -")
    sys.exit(1)

repo_name = str(sys.argv[1])

try:
    repo_description = str(sys.argv[2])
except IndexError:
    print("No description will be included")
    repo_description = ""
sys.exit(0)
path = "Be sure to add a path"
_dir = path + '\\' + repo_name

token = "Be sure to add a token"

g = Github(token)
user = g.get_user()
login = user.login
repo = user.create_repo(name=repo_name, description=repo_description)

os.mkdir(_dir)
os.chdir(_dir)

commands = [f'echo "# {repo.name}" >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{repo.name}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']



for c in commands:
    os.system(c)

print(f'Repository "{repo_name}" created locally')
os.system('code .')