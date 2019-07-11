# git-create
Automate creating a Github project with a single command. `git-create` creates a new directory on your machine, initializes a Github repo with a README and pushes it to the configured Github account.

## Installation
This project requires Python3 and PIP. You'll also need to ensure your SSH keys are stored in Github for the machine you're creating projects from.

### Setup
1) Clone this project
2) Navigate to the this project directory
3) Copy the `.env.example` file to a new `.env` file and update the values.
4) **Optional**: [Setup VS Code launch from cli](https://code.visualstudio.com/docs/setup/mac)
5) Run each of the following commands:

```
pip install -r requirements.txt
	
source .my_commands.sh
```

## Usage
To run the script type in `create <name of your project>`
