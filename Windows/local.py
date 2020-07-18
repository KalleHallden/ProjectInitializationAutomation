import os
import sys

from colorama import init, Fore, Style

"""
Author: Red Williams (Red-CS)
Email:  red.devcs@gmail.com

July 18, 2020
"""

# The world is dark enough, let's add some color!
init()

# Get repository name
repo_name = str(sys.argv[1])

# Set directory
_dir = "{}\\\\{}".format(os.environ.get("PWFA-Path"), repo_name)

# Create local repository
if not os.path.isdir(_dir):
    os.mkdir(_dir)
os.chdir(_dir)

# Test if git is initialzed
if os.path.isdir(f"{_dir}\\.git"):
    usr = input("Git is already initialized. Reinitialize git (y/n)? ")
    if not usr.lower() == "y":
        sys.exit(0)

# Initialize git
os.system('git init')
os.system(f'echo # {repo_name} > README.md')
os.system('git add README.md')
os.system('git commit -m "Initial commit"')

# Rejoice Hallelujah!
print(Fore.GREEN)
print(f"Created \"{repo_name}\" locally!")
print(Style.RESET_ALL)
os.system('code .')