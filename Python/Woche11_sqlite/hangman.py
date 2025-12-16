import sqlite3
import sys
from random import choice

MAX_VERSUCHE = 5


def main():
    connection = sqlite3.connect("database.db")
    cur = connection.cursor()

    print("Eine neue Runde Hangman!")
    prompt = (
        "Wähle die Anzahl der Buchstaben, welche das Wort enthalten soll.\n"
        "Oder gib EXIT ein, wenn das Spiel beendet werden soll.\n"
    )
    anzahl_buchstaben = int(input(prompt))

    cur.execute("SELECT word FROM words WHERE letters = ?", (anzahl_buchstaben,))
    woerter = cur.fetchall()

    if not woerter:
        print("Keine Wörter gefunden...")
        connection.close()
        sys.exit()

    wort = choice(woerter)[0]

    print("\nEin Wort wurde ausgewählt...")
    print("Die Raterunde beginnt!")
    print("Errate das Wort, das Wort rauszufinden!\nViel Spaß!\n")

    geratene_buchstaben = set()
    versuche = 0

    while versuche < MAX_VERSUCHE:
        anzeige = ""
        for buchstabe in wort:
            if buchstabe in geratene_buchstaben:
                anzeige += buchstabe
            else:
                anzeige += "_"

        print(f"Wort: {anzeige}")

        if "_" not in anzeige:
            print("\nGeschafft!")
            print("Eine neue Runde Hangman!")
            break

        print(f"Verbleibende Anzahl Versuche: {MAX_VERSUCHE - versuche}")
        eingabe = input("Welchen Buchstaben wählst du?\n").upper()

        if eingabe in geratene_buchstaben:
            print(f"{eingabe} wurde bereits gewählt!")
            continue

        geratene_buchstaben.add(eingabe)

        if eingabe not in wort:
            print(f"{eingabe} ist leider nicht vorhanden....\n")
            versuche += 1
        else:
            print(f"{eingabe} ist vorhanden!\n")

    if versuche >= MAX_VERSUCHE:
        print(f"\n{anzeige}")
        print("Gescheitert!")
        print("Keine Wörter gefunden...")

    connection.close()


if __name__ == "__main__":
    main()
