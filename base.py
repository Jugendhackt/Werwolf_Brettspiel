# module
import random

###############################################################################################################

ar = ["Werwolf", "Seher", "Hexe", "Bewohner"]  # Alle rollen die existieren
gute_rollen = ["Seher", "Bewohner", "Hexe"]  # alle guten rollen
boese_rollen = ["Werwolf"]  # alle boesen Rollen die existieren
unbekannte_rollen = []  # alle unbekannten Rollen die existieren

###############################################################################################################

tote_rollen = []
rollen_spiel = [ar[0], ar[0], ar[1], ar[2], ar[3], ar[3], ar[3], ar[3]]  # Jede EINZELNE Rolle in der Runde

spielername = input("Was ist ihr Spielername? ")  # Spielernamen eingeben
gesamt_spieler = []  # Ort zum Sammeln aller Spielernamen
Rollenarten = [ar[0], ar[1], ar[2], ar[3]]  # Jede Rollenart in der Runde
max_spieler = 8  # Maximale Spieleranzahl
min_spieler = 5  # Minimale Spieleranzahl
spieleranzahl = 0  # Spieleranzahl in der Runde

if spieleranzahl == 8:  # Ueberpruefen ob max. Spieler Limit erreicht ist
    exit(0)
#
elif spieleranzahl < 8:
    gesamt_spieler.append(spielername)
random.randint(0, spieleranzahl)


#
def rollen_zuteilung():
    random.choice(rollen_spiel)


#
rollen_zuteilung()
# print(random.choice(rollen_spiel))
# print(rollen_spiel)
# random.shuffle(rollen_spiel)
# print(rollen_spiel)
print(gesamt_spieler)

# spielername = key; ar[] = value
spieler_rollen = {spielername: rollen_spiel[0]}  # , : ar[0], : ar[1], : ar[2], : ar[3], : ar[3], : ar[3], : ar[3] }  # Dict
#spielername = key; nummer = value
spieler_nummer = {spielername : 1} # , : 2, : 3, : 4, : 5, : 6, : 7, : 8 }

print(spieler_rollen.values())
print(spieler_rollen.keys())

# def Chat_Bot():
heiltrank = 1
todestrank = 1

def Trank():
    Hexe_spieler = int(input("Für wen möchtest du den Trank verwenden? "))

def Bot_zu_Hexe():
    hexe_DE = int(input("Du kannst einen Spieler auswählen, den du retten oder umbringen möchtest. (retten=2; töten=1; nichts machen=0) "))
    if hexe_DE == 0:
        print("Du hebst deinen Trank für einen passenderen Zeitpunkt auf.")
        #nichts machen
    if hexe_DE == 1:
        Trank()
        #töten
    if hexe_DE == 2:
        Trank()
        
        #retten
    #hexe_DE = ["Du kannst einen Spieler auswählen, den du retten oder umbringen möchtest."]
    # Hexe tut irgendwas

def hexe():
    Bot_zu_Hexe()

    #if antwort = 

    # Hexe tut irgendwas

    # falls Hexe töten will:
    # todestrank = 0

    # falls Hexe retten will:
    #     falls Trank geholfen hat :
    #         heiltrank = 0
    #     sonst:
    #         heiltrank = 1


def Bot_zu_Seher():
    seher_DE = ["Wähle einen Spieler aus , dessen Identität du überprüfen möchtest.",
                "Wessen wahre Identität möchtest du durch deine Fähigkeit in Erfahrung bringen?"]

    seher_spruch = random.randint(0, 2)

    if seher_spruch == 1:
        print(seher_DE[0])

    if seher_spruch == 2:
        print(seher_DE[1])


def seher():
    Bot_zu_Seher()
    # seher_checkt = Person zum pruefen
    spieler_rollen.get(spielername)  # ermitteln des an spielernamen zugeordneten values
    print("Dieser Spieler ist ", spieler_rollen.get(spielername))


print(spieler_rollen.get(spielername))  # Rolle des Spielers printen
seher()
hexe()
