# Betriebsdokumentation
[[_TOC_]]
## Einführungstext 

Es sollen 2 Skripts erstellt werden. Das erste Skript soll alle GIT-Repos mit GIT-Kommandos klonen und in einen Verzeichnis ablegen. Das zweite Skript soll von allen GIT-Repos in diesem Verzeichnis alle Commits auslesen und in einem File speichern.

## Installationsanleitung für Administratoren

### Vorinstallation
* Ubuntu 20.04.4 LTS

### Installation

1. Das Repository Clonen
````
git clone https://github.com/drums1706/praxisarbeitM122LB02.git
````

2. Das verzeichnis wechseln
````
cd praxisarbeitM122LB02/bin
````

3. Python und PIP installieren
````
sudo apt install python 3
````

````
sudo apt install python3-pip
````

## Bedienungsanleitung Benutzer

### User Input File

Für das Script git_clone_update_repos.py muss man nun alles im folgenden Format für das git_clone_update_repos_input.txt eingeben:

````
<github url> <foldername>
````

## Bediensanleitung Benutzer

### Repository klonen

````
git clone https://github.com/drums1706/praxisarbeitM122LB02.git
````
### Das Script git_clone_update_repos.py aufrufen

````
python3 git_clone_update_repos.py <inputfile name> <foldername>
````
