#! /bin/python3
import argparse
import os
import configparser
from xml.dom.expatbuilder import parseString
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import sys
import git
import shutil

#Must point to input file with Github repositorys
myfile = 'git_clone_update_repos_input.txt'

directory = ""

#set base directory
if len(sys.argv) == 2:
    directory = sys.argv[1] 
else:
    directory = os.getcwd()

visited = []

#Pull repository from file
with open(myfile, "r", encoding='utf-8') as f:
    for line in f:
        (githublink, folderName) = line.split(' ')
        completePath = os.path.join(directory, folderName).strip()

        visited.append(completePath)
        try:      
            if (os.path.exists(completePath)):
                repo = git.Repo(completePath)
                o = repo.remotes.origin
                o.pull()
                repo.close()
                continue
            else:
                git.Repo.clone_from(githublink, completePath)
        except:
            print(f"Invalid Github repository: {githublink}")

#Delete unused repositorys
allSubDirectorys = os.listdir(directory)
for cDir in allSubDirectorys:
    delete = os.path.join(directory, cDir).strip()
    print(delete)
    if cDir not in visited: 
        shutil.rmtree(delete)