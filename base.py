# module
import random

###############################################################################################################

ar = ["Werwolf", "Seher", "Hexe", "Bewohner"]  # Alle rollen die existieren
gute_rollen = ["Seher", "Bewohner", "Hexe"]  # alle guten rollen
boese_rollen = ["Werwolf"]  # alle boesen Rollen die existieren
unbekannte_rollen = []  # alle unbekannten Rollen die existieren
votes = {}

###############################################################################################################

tote_rollen = []
rollen_spiel = [ar[0], ar[0], ar[1], ar[2], ar[3], ar[3], ar[3], ar[3]]  # Jede EINZELNE Rolle in der Runde
rollen_spiel_const = rollen_spiel
print(rollen_spiel, rollen_spiel_const)

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


spieler_rollen = {spielername: rollen_spiel[0]} #,
# : rollen_spiel[1],
# : rollen_spiel[2],
# : rollen_spiel[3],
# : rollen_spiel[4],
# : rollen_spiel[5],
# : rollen_spiel[6],
# : rollen_spiel[7]}

def rollen_zuteilung():
    zufällige_rolle = random.choice(rollen_spiel)
    print(zufällige_rolle)

    zufälliger_spieler = random.choice(gesamt_spieler)
    print(zufälliger_spieler)

    spieler_rollen.__setitem__(zufälliger_spieler, zufällige_rolle)



#
rollen_zuteilung()
# print(random.choice(rollen_spiel))
# print(rollen_spiel)
# random.shuffle(rollen_spiel)
# print(rollen_spiel)
print(gesamt_spieler)

# spielername = key; ar[] = value #Dict
#spielername = key; nummer = value
spieler_nummer = {spielername : 1} # , : 2, : 3, : 4, : 5, : 6, : 7, : 8 }
# Rolle = key; Beschreibung = value
rollen_beschreibung = {ar[0]: "Der Werwolf kann pro Nacht einen Spieler töten. (Team: Werwölfe)",
ar[1]: "Der Seher kann jede Nacht die Rolle eines Spielers sehen. (Team: Dorf)",
ar[2]: "Die Hexe hat einen Heiltrank und einen Todestrank, der in der ersten Nacht nicht eingesetzt werden kann. "
"Der Heiltrank wird nur verbraucht , wenn der damit geschützte Spieler angegriffen wird. (Team: Dorf)",
ar[3]: "Der Dorfbewohner hat noch keine spezielle Fähigkeit. (Team: Dorf)"}
print(spieler_rollen.values())
print(spieler_rollen.keys())

def Voting():



    Voting_DE = ["Für welchen Spieler möchtest du abstimmen ?",  # Liste mit Sprüchen (Spruch 1)
                "Wen möchtest du tot sehen ?"]  # (Spruch 2)

    voting_spruch = random.randint(0, 2)  # zufallszahl 1 oder 2 generieren

    if voting_spruch == 1:  # wenn zufallszahl 1 ist
        stimme = int(input(Voting_DE[0]))  # Spruch 1 schreiben

    if voting_spruch == 2:  # wenn zufallszahl = 2
        stimme = int(input(Voting_DE[1]))  # Spruch 2 schreiben

    votes.append(stimme)


def Stimmen_Auszählen():

    votes_pro_spieler = {}

    Rollennummer = 0

    for i in range(0, len(gesamt_spieler_const)):
        stimmen_zaehler = 0
        Rollennummer = Rollennummer + 1

        if Rollennummer in votes:

            for x in range(0, len(votes)):

                if Rollennummer == votes[x]:
                    stimmen_zaehler = stimmen_zaehler + 1
                    votes_pro_spieler[Rollennummer] = stimmen_zaehler

                    print(votes_pro_spieler)

                else:
                    None

        else:
            None

    print(max(votes_pro_spieler.values()))

    highest = max(votes_pro_spieler.values())
    print([key for key in votes_pro_spieler if votes_pro_spieler[key] == highest])

    most_votes = [key for key in votes_pro_spieler if votes_pro_spieler[key] == highest]

    if len(most_votes) == 1:
        print("Das Dorf hat ", [key for key in votes_pro_spieler if votes_pro_spieler[key] == highest], "getötet. ")

    else:
        print("Das Dorf konnte sich nicht entscheiden. ")


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

def Tod():


def seher():
    Bot_zu_Seher()
    # seher_checkt = Person zum pruefen
    spieler_rollen.get(spielername)  # ermitteln des an spielernamen zugeordneten values
    print("Dieser Spieler ist ", spieler_rollen.get(spielername))

def übergang():

print(spieler_rollen.get(spielername))  # Rolle des Spielers printen
seher()
hexe()
