## Installation and usage


### Clone the repository:
```bash
git clone "https://github.com/KalleHallden/ProjectInitializationAutomation.git"
cd ProjectInitializationAutomation
```

### Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Create a configuration file (e.g. config.ini) with the following format:
```bash
[github]
username = your_github_username
password = your_github_password

[local]
file_path = /path/to/local/folder
```

### Run create.py or remote.py with the desired arguments:
```bash
python create.py <folder_name> <config_file_path>
```

### To create a repository only on GitHub using remote.py, run the following command:
```bash
python remote.py <folder_name> <config_file_path>
```
