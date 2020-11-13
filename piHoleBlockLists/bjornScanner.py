from googlesearch import search
import re

#***Beginn*****************************************************************************************
query = input('Suchwort: ')

print('Starte Websuche...')

links = open('links.txt', 'w')
htmlLinks = search(query, num=200, stop=200, pause=0.5)
# Alle Links aus der Antwort in eine Datei schreiben
for link in htmlLinks:
    links.write(link + "\n")
links.close()

# Ergebnisse nach domains filtern
print('Extrahiere domains...')

regex = 'https?://(www)?.*[.][^/]*/'
links = open('links.txt', "r")
domainArray = set()

for zeile in links:
    d = re.search(regex, zeile)
    domainArray.add(d.group(0))  # Noch nicht in die Datei schreiben, da es sonst Duplikate gibt
links.close()

# Schreibe eindeutige Werte in neue Datei
domains = open('bjorn.txt', 'w')
for bjorn in domainArray:
    domains.write(bjorn + '\n')
domains.close()

print('Fertig!')
print('Bjorn Liste liegt im aktuellen Verzeichnis.')
