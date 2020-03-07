__author__ = "wikyprash"
__copyright__ = "Copyright 2007, The Cogent Project"
__credits__ = ["wikyprash", "KalleHallden"]
__license__ = "MIT"
__version__ = "0.0.2"
__maintainer__ = "wikyprash"
__email__ = "wikyprash@gmail.com"
__status__ = "development"


import argparse
import os
from github import Github


def local():
    try:
        if os.path.exists(path):
            os.chdir(path)
        else:
            print('Cannot create a file when that file already exists')
            exit()
        
        commands = ['git init',
                    f'echo "# {foldername}" > README.md',
                    'git add README.md',
                    'git commit -m "Initial commit"']

        os.mkdir(_dir)
        os.chdir(_dir)
        for c in commands:
            os.system(c)

        print(f'{foldername} created locally')
        os.system('code .')

    except Exception as e:
        print(e)


def remote():
    try:
        token = os.environ.get('gt')            # add github token to the env vars
        g = Github(token)
        user = g.get_user()
        login = user.login
        user.create_repo(foldername)
    except Exception as e:
        print(e)

    commands = [f'echo # {foldername} > README.md',
                'git add .',
                'git commit -m "Initial commit"',
                'git push -u origin master']

    try:
        # os.mkdir(_dir)
        os.chdir(path)
        
        print(f'{foldername} initialized')
        os.system(f"git clone https://github.com/{login}/{foldername}.git")
        os.chdir(_dir)
        for c in commands:
            os.system(c)

        os.system('code .')

    except Exception as e:
        print(e)


if __name__ == "__main__":

    p = argparse.ArgumentParser()
    p.add_argument('name', help='name of the project')
    p.add_argument('--operation', '-o', default='l', help='type of initialization')
    args = p.parse_args()

    UserProfile = os.environ.get('USERPROFILE')
    path = f'{UserProfile}\\Desktop'
    foldername = args.name
    _dir = path + '\\' + foldername


    if args.operation == 'l':
        local()
    elif args.operation == 'r':
        remote()
    else:
        print('error...')
