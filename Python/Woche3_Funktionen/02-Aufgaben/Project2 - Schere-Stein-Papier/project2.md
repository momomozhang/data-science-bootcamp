# Projekt 2: Schere-Stein-Papier

## Projektbeschreibung

In diesem Projekt entwickelst du ein Schere-Stein-Papier-Spiel gegen den Computer. Du und der Computer wählen gleichzeitig eine der folgenden Optionen:
- Schere
- Stein
- Papier
- (optional: Brunnen)

Es gibt mehrere mögliche Kombinationen mit unterschiedlichen Ergebnissen:

| Teilnehmende | Schere          | Stein            | Papier           |
|--------------|-----------------|------------------|------------------|
| Schere       | Unentschieden   | Stein gewinnt    | Schere gewinnt   |
| Stein        | Stein gewinnt   | Unentschieden    | Papier gewinnt   |
| Papier       | Schere gewinnt  | Papier gewinnt   | Unentschieden    |

### Spielablauf

- Dir wird über die Konsole die Wahl zwischen Schere, Stein und Papier geboten. Es besteht zusätzlich die Option, das Spiel zu beenden.
- Bei Wahl des Spielabbruchs wird das Ergebnis angezeigt und das Spiel beendet.
- Andernfalls simuliert das Spiel die Computerwahl und ermittelt die gewinnende Partei für die Punktevergabe.
- Nach jeder Runde wird der aktuelle Punktestand ausgegeben.
- Dieser Prozess wiederholt sich, bis du das Spiel beendest.

### Die Wahl des Computers simulieren (1)

Um ein faires Spiel zu gewährleisten, wird die Entscheidung des Computers zufällig simuliert.

Hierfür nutzen wir die Funktionalität von Python zur Erzeugung (pseudo-)zufälliger Zahlen. Mit dem Befehl `randint(a, b)` kann eine zufällige ganze Zahl zwischen a und b (inklusive) generiert werden.

Für die Zuweisung könnten die Zahlen dann wie folgt festgelegt werden:
- 1 für Stein
- 2 für Schere
- 3 für Papier
Die spezifische Auswahl der Zuweisung ist selbstverständlich anpassbar.

Am Anfang des Programms muss dazu folgende Zeile eingefügt werden:
