import random

votes = []
stimme = None
Rollennummer = 1  # Spieler ID
gesamt_spieler = []  # Ort zum Sammeln aller Spielernamen
spieler_nummer = {}  # Ort zum Sammeln von Spieler ID und zugewiesener Spieler

for x in range(0, 4):  # 4 Spieler eingeben

    spielername = input("Was ist ihr Spielername? ")  # Spielernamen eingeben
    spieler_nummer[Rollennummer] = spielername  # Dict spieler_nummer key Rollennummer und value spielername hinzufügen
    Rollennummer = Rollennummer + 1  # Spieler ID ist einzigartig
    gesamt_spieler.append(spielername)  # Liste gesamtspieler spielername hinzufügen

spieler_nummer_const = spieler_nummer  # konstantes Dict erstellen, um das andere zu verändern
gesamt_spieler_const = gesamt_spieler  # konstantes Dict erstellen, um das andere zu verändern

def Voting():

    stimme = None

    Voting_DE = ["Für welchen Spieler möchtest du abstimmen ?",  # Liste mit Sprüchen (Spruch 1)
                "Wen möchtest du tot sehen ?"]  # (Spruch 2)

    voting_spruch = random.randint(1, 2)  # zufallszahl 1 oder 2 generieren

    if voting_spruch == 1:  # wenn zufallszahl 1 ist
        stimme = int(float(input(Voting_DE[0])))  # Spruch 1 schreiben

    if voting_spruch == 2:  # wenn zufallszahl = 2
        stimme = int(float(input(Voting_DE[1])))  # Spruch 2 schreiben

    votes.append(stimme)
    spieler_wahl = spieler_nummer.get(stimme)
    print("Du hast", spieler_wahl,"gewählt.")


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
        key = int(str(most_votes)[1:-1])
    else:
        None

    if len(most_votes) == 1:
        voted_player = spieler_nummer.get(key)
        print("Das Dorf hat ", [key for key in votes_pro_spieler if votes_pro_spieler[key] == highest], "getötet. ")
        print(key for key in votes_pro_spieler if votes_pro_spieler[key] == highest)
        print("Das Dorf hat ", voted_player, "getötet. ")

    else:
        print("Das Dorf konnte sich nicht entscheiden. ")
print(spieler_nummer)
Voting()
Voting()
Voting()
Stimmen_Auszählen()
