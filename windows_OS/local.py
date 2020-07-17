import os
import sys

# Get repository name
repo_name = str(sys.argv[1])

# Set directory
_dir = "{}\{}".format(os.environ.get("PWFA-Path"), repo_name)

# Create local repository
if not os._isdir(_dir):
    os.mkdir(_dir)
os.chdir(_dir)
os.system('git init')
os.system(f'echo # {repo_name} > README.md')
os.system('git add README.md')
os.system('git commit -m "Initial commit"')

# Rejoice Hallelujah!
print(f'{repo_name} created locally!')
os.system('code .')