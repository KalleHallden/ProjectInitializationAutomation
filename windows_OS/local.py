import sys
import os

foldername = str(sys.argv[1])
path = os.environ.get('mp')
_dir = path + '/' + foldername

os.mkdir(_dir)
os.chdir(_dir)
print(f'{foldername} created locally')
os.system('code .')