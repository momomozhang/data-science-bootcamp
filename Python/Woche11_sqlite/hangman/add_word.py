import sqlite3


def main():
    connection = sqlite3.connect("database.db")
    cur = connection.cursor()

    while True:
        eingabe = input("Welches Wort soll der Datenbank hinzugefügt werden (oder EXIT)?\n")

        if eingabe.upper() == "EXIT":
            break

        wort = eingabe.upper()
        anzahl = len(wort)

        cur.execute("SELECT word FROM words WHERE word = ?", (wort,))
        exists = cur.fetchone()

        if exists:
            print(f"Das Wort {wort} befindet sich schon in Datenbank!")
        else:
            cur.execute("INSERT INTO words (word, letters) VALUES (?, ?)", (wort, anzahl))
            connection.commit()
            print(f"Das Wort {wort} wurde der Datenbank hinzugefügt")

    connection.close()


if __name__ == "__main__":
    main()
