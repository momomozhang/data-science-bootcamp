In diesem Projekt setzen wir die gelernten Inhalte der Woche praktisch um. Wir erstellen ein einfaches Interface, welches die Interaktion mit der Konsole ermöglicht und dabei die Eingaben der Nutzer überprüft (Inputvalidierung).
Inputvalidierung ist ein essenzieller Schritt bei der Softwareentwicklung. Man kann (leider) nicht immer davon ausgehen, dass Benutzer korrekte Eingaben machen, sei es versehentlich oder absichtlich. Eine unsachgemäße Eingabeüberprüfung kann zu Sicherheitslücken führen, die von Angreifern ausgenutzt werden können.
Das fertige Programm soll als reine Python-Datei mit der Endung `*.py` abgegeben werden. Verwende dafür den Namen `input_validation.py`.


Struktur des Programms:
Das Programm läuft in einer `while`-Schleife und verarbeitet Nutzereingaben. Die Schleife wird erst durch die Eingabe von `q` beendet.


Funktionen:
main(): Steuert den Programmablauf und ruft die Validierungsfunktionen auf.
check_email(input_email): Validiert die eingegebene Emailadresse.
check_age(input_age): Validiert das eingegebene Alter.


Inputvalidierung:
Implementiere die Überprüfung der Nutzereingaben und stelle sicher, dass nur gültige Daten akzeptiert werden.
Nutze Debug- und Infonachrichten, um die Funktionalität der Anwendung zu protokollieren.


Eingabeoptionen:
`?`: Gibt die Docstrings der verfügbaren Funktionen mithilfe des Attributs `__doc__` aus.
`w`: Lässt den Nutzer seine Emailadresse und sein Alter eingeben. Sollte ein Fehler vorkommen, wird der Nutzer nach neuen Werten gefragt.
`q`: Beendet das Programm.


Beispiel:
Drücke '?' um Hilfe zu bekommen.
Drücke 'q' um die App zu verlassen.
Drücke 'w' um weiterzumachen.

> test
2023-10-04 16:08:56,205 - ERROR - Bitte gib einen korrekten Input an!

Drücke '?' um Hilfe zu bekommen.
Drücke 'q' um die App zu verlassen.
Drücke 'w' um weiterzumachen.

> ?
check_email:
Die Funktion checkt, ob der String ‘input_email‘ eine valide Adresse darstellt.

Parameters: input_email (str)
Returns: str

check_age:
Die Funktion checkt, ob der String ‘input_age‘ ein valides Alter darstellt.

Parameters: input_age (str)
Returns: int

Drücke '?' um Hilfe zu bekommen.
Drücke 'q' um die App zu verlassen.
Drücke 'w' um weiterzumachen.

> w
Wie lautet deine Email?
> fake-mail.com
2023-10-04 16:09:47,155 - DEBUG - Eingegebene Email ist fake-mail.com.
2023-10-04 16:09:47,156 - INFO - Funktion 'check_email' wurde aufgerufen.
2023-10-04 16:09:47,156 - ERROR - Bitte gib eine korrekte Email an!

Drücke '?' um Hilfe zu bekommen.
Drücke 'q' um die App zu verlassen.
Drücke 'w' um weiterzumachen.

> w
Wie lautet deine Email?
> name@mail.com
2023-10-04 16:10:07,332 - DEBUG - Eingegebene Email ist name@mail.com.
2023-10-04 16:10:07,332 - INFO - Funktion 'check_email' wurde aufgerufen.

Wie alt bist du?
> abc
2023-10-04 16:10:24,085 - DEBUG - Eingegebenes Alter ist abc.
2023-10-04 16:10:24,085 - INFO - Funktion 'check_age' wurde aufgerufen.
2023-10-04 16:10:24,095 - ERROR - Bitte gib ein korrektes Alter an!

Drücke '?' um Hilfe zu bekommen.
Drücke 'q' um die App zu verlassen.
Drücke 'w' um weiterzumachen.

> w
Wie lautet deine Email?
> name@mail.com
2023-10-04 16:10:31,649 - DEBUG - Eingegebene Email ist name@mail.com.
2023-10-04 16:10:31,649 - INFO - Funktion 'check_email' wurde aufgerufen.

Wie alt bist du?
> 27
2023-10-04 16:10:35,748 - DEBUG - Eingegebenes Alter ist 27.
2023-10-04 16:10:35,748 - INFO - Funktion 'check_age' wurde aufgerufen.

Drücke '?' um Hilfe zu bekommen.
Drücke 'q' um die App zu verlassen.
Drücke 'w' um weiterzumachen.

> q
2023-10-04 16:10:39,969 - DEBUG - Die Schleife wurde beendet.
