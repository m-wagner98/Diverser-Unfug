# Author: Martin Wagner
# Datum: 01.05.2021
import string

chiffre = "VIXJDALRASVGWKKXHTHFJAIGAEUDZAGCWLMLWTANVEGAWIWDFEGUGRTTKGXRWTSSOIKCVALRVEKFWHXHEELBZLNDKSXKNOKCWRXHYEGS" \
          "DIVGWNGZUHKHUHMDFUXAWRMQSGNMYBXQWIMRRWBRUHXMKEGCWRNMVEFOXAXMYEKZMSZDLANRUHMVMRWDSLLNTEBCWNIZJTXHWNUDCAGML" \
          "ILS"
chiffre = chiffre.replace(" ", "").upper()
offsets = []


# @return Den Wert, um den der übergebene Block verschoben wurde.
# @param subtext: Der Text, auf dem die Häufigkeitsanalyse durchgeführt werden soll
# Das Ergebnis wird mittels Häufigkeitsanalyse ermittelt.
def frequency_analysis(subtext):
    # konvertiere list in einen string
    subtext = ''.join(subtext)
    hashmap = {}
    # Hashmap befüllen
    for i in range(0, 26):
        b = chr(ord('A') + i)
        hashmap[b] = 0
    # Häufigkeiten zählen
    idx = 0
    while idx < len(subtext):
        buchstabe = subtext[idx]
        if buchstabe in string.ascii_uppercase:
            hashmap[buchstabe] += 1
        idx += 1
    # Häufigkeiten ausgeben
    max_key = max(hashmap, key=hashmap.get)
    if max_key in string.ascii_uppercase:
        offset = (ord(max_key) - ord('E')) % 26
    else:
        offset = (ord(max_key) - ord('e')) % 26
    offsets.append(offset)
    return offset


# @param k: Schlüssellänge
# @return : dechiffrierten Text
def kryptanalyse(k):
    # Chiffre in Einzelalphabete (Gruppen) teilen, Schlüssellänge k ist bekannt
    gruppen = []
    iteration = 0
    while iteration < k:
        # Alle Buchstaben jeweils im Abstand k in eine Gruppe einfügen
        gruppe = []
        index = iteration
        while index < len(chiffre):
            gruppe.append(chiffre[index])
            index += k
        gruppen.append(gruppe)
        iteration += 1
    # Jede Gruppe wurde mit dem gleichen Schlüsselbuchstaben verschoben (caesar cipher)
    # --> Häufigkeitsanalyse innerhalb einer Gruppe möglich
    for g in gruppen:
        frequency_analysis(g)
    # Baue Schlüssel zusammen
    key_ = ''
    for o in offsets:
        key_ += chr(ord('A') + o)

    return key_


def decrypt(key):
    m = ''
    for counter, c in enumerate(chiffre):
        # Chiffretext Buchstaben - Schlüsselwortbuchstaben % 26
        key_idx = counter % 4
        buchstabe = ((ord(c)-ord('A')) - (ord(key[key_idx]) - ord('A'))) % 26  # Anzahl Buchstaben im Alphabet
        m += chr(ord('A') + buchstabe)
    return m


# ************************+**  Beginn  *******************************
schluessel_laenge = 4
print('Schlüssellänge: ' + str(schluessel_laenge))
schluessel = kryptanalyse(schluessel_laenge)
print('Schlüssel: ' + schluessel)
print('Text: ' + decrypt(schluessel))
