import random

tote_spieler = {}
votes = []
Rollennummer = 1  # Spieler ID
gesamt_spieler = []  # Ort zum Sammeln aller Spielernamen
spieler_nummer = {}  # Ort zum Sammeln von Spieler ID und zugewiesener Spieler
Zeit_w = (120) # Hier landet die Zeit zum Wählen, wenn sie vom Spieler modifiziert wurde

for x in range(0, 4):  # 4 Spieler eingeben

    spielername = input("Was ist ihr Spielername? ")  # Spielernamen eingeben
    spieler_nummer[Rollennummer] = spielername  # Dict spieler_nummer key Rollennummer und value spielername hinzufügen
    Rollennummer = Rollennummer + 1  # Spieler ID ist einzigartig
    gesamt_spieler.append(spielername)  # Liste gesamtspieler spielername hinzufügen

spieler_nummer_const = spieler_nummer  # konstantes Dict erstellen, um das andere zu verändern
gesamt_spieler_const = gesamt_spieler  # konstantes Dict erstellen, um das andere zu verändern


aufgang_de = ["Mit dem Dorf wacht ihr alle auf.",
        "Alle Lebenden sind erwacht.",
        "Die Sonne geht auf und ihr alle erwacht."
        "Du wurdest von einem komischen Gestank aufgeweckt...",]

print(random.choice(aufgang_de))

def Stimmabgabe():

    voting_de = ["Für welchen Spieler möchtest du abstimmen ?",  # Liste mit Sprüchen (Spruch 1)
                "Wen möchtest du tot sehen ?"]  # (Spruch 2)

    stimme = int(input(random.choice(voting_de)))  # Spruch 2 schreiben

    votes.append(stimme)



def Stimmen_Auszaehlen():
    global killed_player
    global most_votes

    votes_pro_spieler = {}

    rollennummer = 0

    for i in range(0, len(gesamt_spieler_const)):
        stimmen_zaehler = 0
        rollennummer = rollennummer + 1

        if rollennummer in votes:

            for x in range(0, len(votes)):

                if rollennummer == votes[x]:
                    stimmen_zaehler = stimmen_zaehler + 1
                    votes_pro_spieler[rollennummer] = stimmen_zaehler

                    print(votes_pro_spieler)


    print(max(votes_pro_spieler.values()))

    highest = max(votes_pro_spieler.values())

    most_votes = [key for key in votes_pro_spieler if votes_pro_spieler[key] == highest]

    keys = list(votes_pro_spieler.keys())
    values = list(votes_pro_spieler.values())
    print(keys[values.index(highest)])

    voted_player = keys[values.index(highest)]
    killed_player = spieler_nummer.get(voted_player)
    print("Voted Player = ", voted_player)
    print(most_votes)
    print(voted_player)
    print(spieler_nummer)
    Tod = {voted_player: killed_player}
    tote_spieler.update(Tod)
    print(tote_spieler)


def Werwolf_Abstimmergebnis(most_votes: list, killed_player: int) -> None:

    if len(most_votes) == 1:

        print(killed_player, "ist getötet worden. ")


Stimmabgabe()
Stimmabgabe()
Stimmabgabe()
Stimmen_Auszaehlen()
#print(stimmen_zaehler)
#print(most_votes)
Werwolf_Abstimmergebnis(most_votes, killed_player)
