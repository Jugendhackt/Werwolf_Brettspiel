import random
import time

ar = ["Werwolf", "Seher", "Hexe", "Bewohner"]  # Alle rollen die existieren

rollen_spiel = [ar[0], ar[0], ar[1], ar[2], ar[3], ar[3], ar[3], ar[3]]  # Jede EINZELNE Rolle in der Runde


Rollennummer = 1  # Spieler ID
gesamt_spieler = []  # Ort zum Sammeln aller Spielernamen
spieler_nummer = {}  # Ort zum Sammeln von Spieler ID und zugewiesener Spieler

for x in range(0, 8):  # 8 Spieler eingeben

    spielername = input("Was ist ihr Spielername? ")  # Spielernamen eingeben
    spieler_nummer[Rollennummer] = spielername  # Dict spieler_nummer key Rollennummer und value spielername hinzufügen
    Rollennummer = Rollennummer + 1  # Spieler ID ist einzigartig
    gesamt_spieler.append(spielername)  # Liste gesamtspieler spielername hinzufügen

spieler_nummer_const = spieler_nummer  # konstantes Dict erstellen, um das andere zu verändern
gesamt_spieler_const = gesamt_spieler  # konstantes Dict erstellen, um das andere zu verändern

spieler_rollen = {}  # Ort zum Sammeln von Spielern und ihren Rollen
tode_rollen = []

def rollen_zuteilung():
    zufällige_rolle = random.choice(rollen_spiel)  # Zufällige Rolle aus Liste rollen_spiel heraussuchen und in Variable speichern
    rollen_spiel.remove(zufällige_rolle)  # herausgesuchte Rolle löschen, da diese Rolle nur einmal vergeben werden soll
    print(zufällige_rolle)  # nicht notwendig

    zufälliger_spieler = gesamt_spieler[0]  # Zufälligen Spieler aus Liste gesamt_spieler herraussuchen und in Variable speichern
    gesamt_spieler.remove(zufälliger_spieler)  # herausgesuchten Spieler löschen, da nur einmal Rolle erhalten soll
    print(zufälliger_spieler)  # nicht notwendig

    spieler_rollen[zufälliger_spieler] = zufällige_rolle  # Dict spieler_rollen key zufälliger Spieler und value zufällige Rolle hinzufügen
    print(spieler_rollen)  # nicht notwendig
    print(gesamt_spieler)  # nicht notwendig
    print(rollen_spiel)  # nicht notwendig

for i in range(0, 8):  # ( Spielern müssen Rollen zugeteil werden
    rollen_zuteilung()  # Funktion aufrufen


#def Bot_zu_Seher():
#    seher_DE = ["Wähle einen Spieler aus , dessen Identität du überprüfen möchtest.",              # Liste mit Sprüchen (Spruch 1)
#                "Wessen wahre Identität möchtest du durch deine Fähigkeit in Erfahrung bringen?"]  # (Spruch 2)
#
#    seher_spruch = random.randint(0, 2)  # zufallszahl 1 oder 2 generieren
#
#    if seher_spruch == 1:  # wenn zufallszahl 1 ist
#        seher_checkt = int(input(seher_DE[0]))  # Spruch 1 schreiben
#
#    if seher_spruch == 2:  # wenn zufallszahl 2 ist
#        seher_checkt = int(input(seher_DE[1]))  # Spruch 2 schreiben
#



def tod():
    vote = input("Wen möchtest du Tod sehen? ")
    stimme = spieler_rollen[vote]
    print(stimme)
    print(spieler_rollen)
    tode_rollen.append(stimme)
    spieler_rollen.pop(vote)
    print(spieler_rollen)
    print(tode_rollen)

def seher():
    time.sleep(1)
    seher_DE = ["Wähle einen Spieler aus , dessen Identität du überprüfen möchtest.",              # Liste mit Sprüchen (Spruch 1)
                "Wessen wahre Identität möchtest du durch deine Fähigkeit in Erfahrung bringen?"]  # (Spruch 2)

    seher_spruch = random.randint(0, 2)  # zufallszahl 1 oder 2 generieren

    if seher_spruch == 1:  # wenn zufallszahl 1 ist
        seher_checkt = int(input(seher_DE[0]))  # Spruch 1 schreiben

    if seher_spruch == 2:  # wenn zufallszahl = 2
        seher_checkt = int(input(seher_DE[1]))  # Spruch 2 schreiben

    seher_checkt_name = spieler_nummer_const.get(seher_checkt)  # ermitteln des an seher_checkt zugeordneten values
    print(seher_checkt_name)

    seher_checkt_rolle = spieler_rollen.get(seher_checkt_name)
    print(seher_checkt_rolle)

    print("Dieser Spieler ist ", seher_checkt_rolle)  # Seher über Rolle informieren


seher()  # Funktion aufrufen
