import sys
import os

# Extract folder name from command line arguments
foldername = str(sys.argv[1])

# Set the file path from an environment variable
path = os.environ.get('mp')

# Construct the full path to the new folder
_dir = path + '/' + foldername

try:
    # Create the new folder and change the current working directory to it
    os.mkdir(_dir)
    os.chdir(_dir)

    # Initialize a Git repository and add a README file
    os.system('git init')
    os.system(f'echo "# {foldername}" > README.md')
    os.system('git add README.md')
    os.system('git commit -m "first commit"')

    # Print a success message and open the folder in Visual Studio Code
    print(f'{foldername} created locally')
    os.system('code .')

except:
    # Print an error message if the folder could not be created
    print(f'Error: Could not create folder {_dir}')
