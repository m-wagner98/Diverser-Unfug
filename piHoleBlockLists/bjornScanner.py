from googlesearch import search
import re
import requests

# Ggf. anpassen
#######################################################################################################################
piHoleRegExDomain = 'https://raw.githubusercontent.com/m-wagner98/Diverser-Unfug/master/piHoleBlockLists/regexp.txt'
#######################################################################################################################


# Filtere @param linksammlung nach Einträgen, die noch nicht von
# PiHole RegEx Filtern erkannt werden. Rückgabe erhält keine doppelten Werte
def extrahiereNeueDomains(linksammlung):
    piHoleRegexFilters = requests.get(piHoleRegExDomain).text.splitlines()
    regex = 'https?://(www)?.*[.][^/]*/'

    neueDomains = set()
    for zeile in linksammlung:
        result = re.search(regex, zeile).group(0)[:-1]  # "/" am Ende entfernen, sonst RegEx match Probleme
        matched = False
        # Nur merken, wenn der Eintrag noch nicht von den aktiven RegEx Filtern erkannt wird
        for regExFilter in piHoleRegexFilters:
            if re.search(regExFilter, result) is not None:
                matched = True
        if not matched:
            # Nur wenn noch nicht von PiHole blockiert (gravity Listen)
            try:
                response = requests.get(result)
                if response.status_code == 200 and 'Pi-hole' not in response.text:  # HTTP wird von Pi-Hole mit 200 beantwortet
                    neueDomains.add(result)  # Noch nicht in die Datei schreiben, da es sonst Duplikate gibt
            except Exception:
                pass
    return neueDomains


# **********************************************Beginn******************************************************************
print('Starte Websuche...')
query = input('Suchwort: ')

links = open('links.txt', 'w')
htmlLinks = search(query, num=200, stop=200, pause=0.5)
# Alle Links aus der Antwort in eine Datei schreiben
for link in htmlLinks:
    links.write(link + "\n")
links.close()

# Ergebnisse nach domains filtern
print('Extrahiere domains...')
links = open('links.txt', "r")
domains = extrahiereNeueDomains(links)
links.close()

# Schreibe verbliebene eindeutige Werte in neue Datei
ergebnisListe = open('bjorn.txt', 'w')
for bjorn in domains:
    ergebnisListe.write(bjorn + '\n')
ergebnisListe.close()

print('Fertig!')
print(len(domains).__str__() + ' neue Domains gefunden!')
print('Bjorn Liste liegt im aktuellen Verzeichnis.')
