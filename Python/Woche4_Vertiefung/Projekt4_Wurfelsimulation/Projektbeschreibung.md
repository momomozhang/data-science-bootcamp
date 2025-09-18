# Projekt 4: Würfelsimulation

## Projektbeschreibung

In diesem Projekt wirst du die Aufgabe übernehmen, das Werfen eines fairen Würfels zu simulieren. Ziel ist es, die geworfenen Augenzahlen zu sammeln und daraus den Mittelwert zu berechnen, um den theoretischen Erwartungswert eines Würfels zu überprüfen.

Die Schritte deines Programms umfassen:

- Simuliere N Würfe eines fairen Würfels.
- Speichere die Ergebnisse dieser Würfe in einer Liste.
- Berechne den Mittelwert der geworfenen Augenzahlen.
- Vergleiche den empirischen Mittelwert mit dem theoretischen Erwartungswert von 3,5.
- Analysiere, wie sich die Annäherung an den Erwartungswert ändert, wenn du die Anzahl der Würfe (N) erhöhst oder verringerst.

## Hinweise zur Implementierung

- Verwende die Funktion `randint` aus dem `random` Modul, um einen Wurf zu simulieren: `from random import randint`.
- Mit dem Befehl `wurf = randint(1, 6)` kannst du eine zufällige Augenzahl zwischen 1 und 6 generieren.
- Denke daran, den empirischen Mittelwert zu berechnen, indem du die Summe aller Würfe durch die Anzahl der Würfe (N) teilst.

## Abgabe

Das endgültige Programm muss als reiner Python-Code unter dem Namen `dicesimulator.py` eingereicht werden. Ein erster Prototyp kann in einem Jupyter Notebook entwickelt werden, muss aber für die Abgabe in eine Python-Datei (*.py) für die Ausführung außerhalb des Notebooks, beispielsweise in VS Code oder Spyder, übertragen werden.

## Beispiel
===============================================
WÜRFELSIMULATOR 3000
===============================================
Wie viele Würfe sollen simuliert werden?
10000
===============================================
Simuliere 10000 Würfe...
===============================================
Berechneter Mittelwert: 3.511
Theoretischer Mittelwert: 3.5
===============================================
Noch einmal? (j/n)
