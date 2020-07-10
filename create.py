import sys
import os
from github import Github 
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("FILEPATH")
password = os.getenv("PASSWORD")
username = os.getenv("USERNAME")

def create():
	folderName = str(sys.argv[1])
	os.makedirs(path + str(folderName))
	gh = Github(username, password)
	user = gh.get_user()	
	repo = user.create_repo(folderName)
	print("The repository {} has been created successfully".format(folderName))


if	__name__ == "__main__":
	create()