#! /bin/python3

from git import Repo
from datetime import datetime
import csv
import os
import argparse
import logging 

# Change Default Logging Level
logging.basicConfig(filename='logfile.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

HEADER = ["Zielverzeichnis", "Datum", "Commit-Hash", "Author"] # M122_LB2,20220714,7fb40cbaacae6d9e1d598b030560117ccad28d63, Ricardo Henagrtner
TARGET_DIR = '' 
lines = []

# Parser for Target Dir and Output Location and Filename of CSV
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--Output", help="Output location and filename", default="gitCommits.csv")
parser.add_argument("-d", "--Directory", help="Target Directory -> Git Repos are in there", required=True)  
args = parser.parse_args()

OUTPUT_LOC = args.Output # Example: -o ~/PATH/GitHub/
logging.info("Output Location and Filename " + OUTPUT_LOC + " defined")

TARGET_DIR = args.Directory # Example: -d ~/PATH/filename.csv
logging.info("Target Directory " + TARGET_DIR + " defined")


# Create the date String; Example: YYYYMMDD - 14072022
def dateToDateString(now):
    date = now.strftime("%m%d%Y")
    return(date)
    
# Check if directory or not
def validateTargetDir(targetDir):
    if os.path.isfile(targetDir) == True:
        print(targetDir + "is not a directory, exit")
        logging.warning("The Repository: " + targetDir + " is not a directory")
        exit()

validateTargetDir(TARGET_DIR)

# Put SubDirs from TARGET_DIR in list
subTargetDirs = os.listdir(TARGET_DIR)


# Go trough each SubRepo and look if is valid git Repo
for subdir in subTargetDirs:
    directory = TARGET_DIR +"/"+ subdir #PATH of Sub Dir
    if os.path.isdir(directory):
        try:
            # Create a new Repo instance if is valid git repo. Add all the Git Repos. 
            Repo(directory) # GitPython
            logging.info("Succesfully added: " + directory)

        except Exception: 
            # Skip if not valid Git repo
            print(subdir, "is not a Git repository, skipping")
            logging.warning("The Git Repository: " + subdir + "; is not valid, going to the next one")
            continue
        
        # Create list and put Commits inside
        repos = Repo(directory)
        commits = list(repos.iter_commits()) # GitPython - take each commit from each repo
        logging.info("Commits from Repo: " + subdir + "; successfully written into unformatted List")

        # Format each commit in list
        for commit in commits:
            # Format: # Directory,Date in YYYYMMDD,Commit Hash, Commit Author
            lines.append([subdir, dateToDateString(commit.authored_datetime), commit.hexsha, commit.author])

    else:
        print(f"Not a directory: {directory}")
# Write List into CSV @stackoverflow
with open(str(OUTPUT_LOC), 'w') as file:
    write = csv.writer(file)
    write.writerow(HEADER)
    write.writerows(lines)

logging.info("Commits succesfully written into formatted CSV \n")