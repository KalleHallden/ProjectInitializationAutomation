### Install: 
```bash
git clone "https://github.com/KalleHallden/ProjectInitializationAutomation.git"
cd ProjectInitializationAutomation
```
Then go to .my_commands.sh and set the path, username and password to be your path, username and password.
To use the command on the current terminal session run this command into the terminal.
```bash
source ~/.my_commands.sh
```
To use the command global add this command to your .bash_profile
```bash
source cloned_project_path/ProjectInitializationAutomation/.my_commands.sh
```
Then run this command into your terminal to start using the script
```bash
source .bash_profile
```
### Note: Global use may change from os to another

### Usage:
To run the script type in 
```bash
project <name>
```
To delete the project
```bash
project -d <name>
```
