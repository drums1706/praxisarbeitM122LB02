#! /bin/python3

from git import Repo
from datetime import datetime
import csv
import os
import argparse
import logging 

#Logging
logging.basicConfig(filename='logfile.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

header = ["Zielverzeichnis", "Datum", "Commit-Hash", "Author"]
targetDirectory = '' 
lines = []

# Parse Parameter
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--Output", help="Output location and filename", default="gitCommits.csv")
parser.add_argument("-d", "--Directory", help="Target Directory -> Git Repos are in there", required=True)  
args = parser.parse_args()

output = args.Output
#logging.info("Output Location and Filename " + output + " defined")

targetDirectory = args.Directory
#logging.info("Target Directory " + targetDirectory + " defined")


# Create Date: YYYYMMDD - 14072022
def dateToDateString(now):
    date = now.strftime("%m%d%Y")
    return(date)
    
# Directory validator
def validateTargetDir(targetDir):
    if os.path.isfile(targetDir) == True:
        print(targetDir + "is not a directory, exit")
        logging.warning("The Repository: " + targetDir + " is not a directory")
        exit()

validateTargetDir(targetDirectory)

#Create List
subTargetDirectorys = os.listdir(targetDirectory)


#Loop through repository
for subdir in subTargetDirectorys:
    directory = targetDirectory +"/"+ subdir #PATH of Sub Dir
    if os.path.isdir(directory):
        try:
            # Create a new Repo
            Repo(directory)
            logging.info("Succesfully added: " + directory)

        except Exception: 
            # Skip
            print(subdir, "is not a Git repository, skipping")
            logging.warning("The Git Repository: " + subdir + "; is not valid, going to the next one")
            continue
        
        # Create list
        repos = Repo(directory)
        commits = list(repos.iter_commits()) # GitPython - take each commit from each repo
        logging.info("Commits from Repo: " + subdir + "; successfully written into unformatted List")

        # Format
        for commit in commits:
            lines.append([subdir, dateToDateString(commit.authored_datetime), commit.hexsha, commit.author])
    else:
        print(f"Not a directory: {directory}")
# Write List into CSV @stackoverflow
with open(str(output), 'w') as file:
    write = csv.writer(file)
    write.writerow(header)
    write.writerows(lines)

logging.info("Commits succesfully written into formatted CSV \n")