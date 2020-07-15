import sys
import os
from github import Github

# Set variables
repo_name = str(sys.argv[1])
repo_description = str(sys.argv[2])
if str(sys.argv[3]) == "public":
    repo_publicity = False
else:
    repo_publicity = True


path = "[Path to workspace here]"
_dir = path + '\\' + repo_name

token = "[GitHub Token here]"

g = Github(token)
user = g.get_user()
login = user.login
repo = user.create_repo(name=repo_name, 
                        description=repo_description,
                        private=repo_publicity)

os.mkdir(_dir)
os.chdir(_dir)

commands = [f'echo # {repo.name} >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{repo.name}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

for c in commands:
    os.system(c)

print(f'Repository "{repo_name}" created locally and pushed to GitHub!')
print(f"Check it out at https://github.com/{login}/{repo.name}.git")
os.system('code .')