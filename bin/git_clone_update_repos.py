import argparse
import os
import configparser
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import sys


# assign base folder to the variable 'directory'
directory = sys.argv[1]

myfile = 'git_clone_update_repos_input.txt'


with open(myfile, "r", encoding='utf-8') as f:
    for line in f.read():
        githublink, folderName = line.split(' ')
        if githublink.startswith('https'):
            mode = 'https'
            # KEY

        else:
            # KEY
            mode = 'ssh'