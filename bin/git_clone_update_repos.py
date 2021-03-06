#! /bin/python3
import argparse
import os
import configparser
from xml.dom.expatbuilder import parseString
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import sys
import git  
import shutil
import logging 

#Logging
logging.basicConfig(filename='logfile.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

#Must point to input file with Github repositorys
inputFile = ""

directory = ""

#set base file
if len(sys.argv) >= 2:
    inputFile = sys.argv[1]

#set base directory
if len(sys.argv) >= 3:
    directory = sys.argv[2]
else:
    directory = os.getcwd()

#list for used repository
visited = []

#Pull repository from file
with open(inputFile, "r", encoding='utf-8') as f:
    for line in f:
        (githublink, folderName) = line.split(' ')
        folderName = folderName.strip()
        completePath = os.path.join(directory, folderName)
        visited.append(folderName)
        try:      
            if (os.path.exists(completePath)):
                repo = git.Repo(completePath)
                o = repo.remotes.origin
                o.pull()
                repo.close()
                print("Git repositorys pulled")
                continue
            else:
                git.Repo.clone_from(githublink, completePath)
        except:
            logging.info(f"Invalid Github repository: {githublink}")

#Delete unused repositorys
allSubDirectorys = os.listdir(directory)
for cDir in allSubDirectorys:
    deletePath = os.path.join(directory, cDir).strip()
    if cDir not in visited: 
        shutil.rmtree(deletePath)
        logging.info(f"Deleted unused directorys: {deletePath}")