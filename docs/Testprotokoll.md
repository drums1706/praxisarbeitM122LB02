Skript 1 

| Testfall | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - |
| Skript aufruf | Alle Repos repos werden aus einem File gelesen und danach geklont<pre>python3 git_clone_update_repos.py repos</pre> | Alle Repos repos werden aus einem File gelesen und danach geklont | Alle Repos repos werden aus einem File gelesen und danach geklont | Ricardo Hengartner | Datum: 14.07.2022 Status: Bestanden
| Übergabe GIT-Repo-URLs |Die Zielverzeichnisse werden in einem File als Liste übergeben | Die GIT-Repo-URLs und ihre Zielverzeichnisse werden in einem File als Liste übergeben werden können. | Die GIT-Repo-URLs und ihre Zielverzeichnisse werden in einem File als Liste übergeben werden können. | Ricardo Hengartner | Datum: 14.07.2022 Status: Bestanden
| Clone Git-Repos |Git clone https://github.com/drums1706/praxisarbeitM122LB02 | Es müssen alle geklonten Git-Repos die nicht mehr gebraucht werden (da sie nicht mehr im input file sind), gelöscht werden. | Es müssen alle geklonten Git-Repos die nicht mehr gebraucht werden (da sie nicht mehr im input file sind), gelöscht werden. | Ricardo Hengartner | Datum: 14.07.2022 Status: Bestanden
| Logging und Logfile |Es wurde ein File namens logfile.log erstellt | Die Logs haben folgendes Format: DateTime:Loglevel:Message | 2022-07-14 23:22:51,069:INFO | Ricardo Hengartner | Datum: 14.07.2022 Status: Bestanden |

Skript 2

| Testfall | Testdaten | erwartetes Testresultat | erhaltenes Testresultat | Tester | Testdatum und Teststatus |
|  - | - | - | - | - | - |
| Skript aufruf | Alle Repos repos werden aus einem File gelesen und danach geklont<pre>python3 git_extract_commits_m122.py -d repos</pre> | Alle Repos aus ~/PATH/ werden gelesen und ein File /PATH/gitCommits.csv per default erstellt | Alle Repos aus ~/PATH/ werden gelesen und ein File /PATH/gitCommits.csv per default erstellt | Issaya Tubniyom | Datum: 14.07.2022 Status: Bestanden
| CSV mit Commits wird erstellt | CSV File mit angegebenen Filenamen wurde erstellt, also der definierte Pfad | Es kann unter dem definierten Pfad und definiertem Namen ein CSV File vorgefunden werden, welches alle Commits darin enthält. | Es kann unter dem definierten Pfad und definiertem Namen ein CSV File vorgefunden werden, welches alle Commits darin enthält. | Issaya Tubniyom | Datum: 14.07.2022 Status: Bestanden
| CSV Format und Header | M122_LB2,20220714,7fb40cbaacae6d9e1d598b030560117ccad28d63, Ricardo Hengartner | Der Header ist im CSV File oben in der richtigen Reihenfolge zusehen, darunter folgen die Commits welche dem genannten Format entsprechen. | Es kann unter dem definierten Pfad und definiertem Namen ein CSV File vorgefunden werden, welches alle Commits darin enthält. | Issaya Tubniyom | Datum: 14.07.2022 Status: Bestanden
| Logging und Logfile | Es wurde ein File namens logfile.log erstellt | Die Logs haben folgendes Format: DateTime:Loglevel:Message | Es kann unter dem definierten Pfad und definiertem Namen ein CSV File vorgefunden werden, welches alle Commits darin enthält. | Issaya Tubniyom | Datum: 14.07.2022 Status: Bestanden
