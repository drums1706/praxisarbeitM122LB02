import argparse
import os
import configparser
from xml.dom.expatbuilder import parseString
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import sys
import git

myfile = 'git_clone_update_repos_input.txt'

directory = ""

if len(sys.argv) == 2:
    directory = sys.argv[1]
else:
    directory = os.getcwd()

with open(myfile, "r", encoding='utf-8') as f:
    for line in f.read():
        githublink, folderName = line.split(' ')
        completePath = os.path.join(directory, folderName).strip()

        if (os.path.exists(completePath)):
            repo = git.Repo(completePath)
            o = repo.remotes.origin
            o.pull()
            repo.close()
            continue
        else:
            git.Repo.clone_from(githublink, completePath)