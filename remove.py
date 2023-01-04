import sys
import os
import requests

# Extract repository name and GitHub credentials from command line arguments
reponame = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]

# Set up authentication for the GitHub API
auth = (username, password)
headers = {'Accept': 'application/vnd.github+json'}

# Delete the repository using the GitHub API
response = requests.delete(f'https://api.github.com/repos/{username}/{reponame}', auth=auth, headers=headers)

# Check the status code of the response
if response.status_code == 204:
    print(f'Successfully deleted repository {reponame}')
else:
    print(f'Failed to delete repository {reponame}')
