import sys
import os
import getpass
from github import Github

path = "~/Documents/Projects/MyProjects/"

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))
    isLogedIn = False
    
    while not isLogedIn:
        username = raw_input("Username for 'www.github.com': ")
        password = getpass.getpass("Password for '" + username + "@github.com': ")
        user = Github(username, password).get_user()
        try:
            user.login
            isLoggedIn = True
        except:
            print("Credentials are wrong.")

    repo = user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()
