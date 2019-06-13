### Install: 
```bash
git clone "https://github.com/KalleHallden/ProjectInitializationAutomation.git"
cd ProjectInitializationAutomation
```
Then go to ```.env.example``` rename it to ```.env``` then set:
- ```PROJECTS_PATH```: As your projects path.
- ```USERNAME```: Your github username.
- ```PASSWORD```: Your github password. <br />
You are able to leave the password empty and the shell will ask you to enter it when running the command. <br />

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
