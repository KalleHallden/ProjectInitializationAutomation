### Prerequisites
```bash
First of all, if you are in a Windows machine, you will have to instal the git bash
After this, install the latest version of python if you have not installed yet
Then install pip, a tool that you will need later to install the requirements
Download the webdriver of the browser that you mostly use
```

### Install: 
```bash
git clone "https://github.com/KalleHallden/ProjectInitializationAutomation.git"
cd ProjectInitializationAutomation
pip install -r requirements.txt
Now open the .env file with your favourite text editor and type your username, password, and the path where you want to create the project folder.
Now you will have to navigate to your computer usarname folder, and place the file named .my_commands.sh there
Then, in the same directory, your computer username folder, edit the .bashrc file with your text editor and type in the following "source ~/.my_commands.sh". If the file
.bashrc is not created, create it by yourself.

```

### Usage:
```bash
To run the create script type in 'create <name of the folder>'
To run the remove script type in 'delete <name of the folder>'
```

### Env File Format:
```bash
USERNAME="Username123"
PASSWORD="Password123"
FILEPATH="/project/path/" Notice that the path has to end with an "/" as I did in the example
```

### Important Note
```bash
1. Please read the comments in both delete.py and .my_commands files to set the scripts up correctly
2. The last line of the function create in the .my_commands file ("subl $1") is a custom alias that I have created by typing 'alias subl="/C/Program\ Files/Sublime\ Text\ 3/sublime_text.exe"'
int the .bashrc file, that opens Sublime Text, you can delete it or just change it if you use a different text editor, for example, if you use VSCode, replace the line with code .
3. You may have trouble with the ssh keys that gives you permission to acces the GitHub repositories, but you can solve it by yourself following this tutorial: "https://gist.github.com/adamjohnson/5682757"

```
