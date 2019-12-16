# git-create

[![Build Status](https://travis-ci.org/Justintime50/git-create.svg?branch=master)](https://travis-ci.org/Justintime50/git-create)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

Automate creating a Github project with a single command. `git-create` creates a new directory on your machine, initializes a Github repo with a README and pushes it to the configured Github account.

## Installation
This project requires Python3 and PIP. You'll also need to ensure your SSH keys are stored in Github for the machine you're creating projects from.

1) Run `cp .env.example .env` add your Github key.
2) **Optional**: [Setup VS Code launch from cli](https://code.visualstudio.com/docs/setup/mac)
3) Install project dependencies:

```bash
pip install -r requirements.txt
```

4) Add `create_repo.sh` to your path or add an alias.

```bash
alias git-create='/path/to/this/project/git-create/create_repo.sh'
```

5) Finally, reload your profile `source ~/.zshrc`, or start a new terminal session.

## Usage
Run the following command in any directory. It will clone your new Github project in the path specified as the parameter
```
git-create <path to project>
```

## Example
Create repo `foobar`, and clone it into `~/Desktop/foobar` 
```
git-create ~/Desktop/foobar
```
