# Zoo-Verwaltungssystem

## Projektbeschreibung

In diesem Projekt geht es darum, ein Zoo-Verwaltungssystem mit Hilfe der Objektorientierten Programmierung (OOP) in Python zu erstellen. Ziel ist es, verschiedene Tierklassen zu programmieren, die Konzepte wie Klassen, Instanzen und besonders die Vererbung nutzen. Dieses Projekt dient dazu, den Umgang mit OOP in Python zu vertiefen und praktisch anzuwenden.

### Struktur des Programms:

Das System soll aus mehreren Dateien bestehen, die verschiedene Tierklassen sowie eine Hauptklasse (`main.py`) umfassen:

- **main.py**: Das Hauptprogramm, das die verschiedenen Tierinstanzen initialisiert und mit ihnen interagiert.
- **tier.py**: Beinhaltet die Basisklasse `Tier`, von der alle spezifischen Tierklassen erben.
- **tiger.py**: Beinhaltet die spezifische Klasse `Tiger`, die von `Tier` erbt.
- **gorilla.py**: Beinhaltet die spezifische Klasse `Gorilla`, die von `Tier` erbt.
- ...weitere Tierklassen nach Wahl...

### Die Basisklasse `Tier`:

Die Klasse `Tier` dient als Grundlage für alle Tiere im Zoo und beinhaltet folgende Elemente:

- **Instanzattribute**:
  - `name`: Der Name des Tieres (String).
  - `sex`: Das Geschlecht des Tieres (Boolean, wobei `0` für männlich und `1` für weiblich steht).
  - `age`: Das Alter des Tieres (Integer).

- **Methoden**:
  - `eat()`: Gibt eine Nachricht aus, dass das Tier isst (z.B. "Max isst.").
  - `sleep()`: Gibt eine Nachricht aus, dass das Tier schläft (z.B. "Max schläft.").
  - `grow(years)`: Erhöht das Alter des Tieres um `years` Jahre und gibt eine Nachricht aus (z.B. "Max wurde 5 Jahre älter und ist jetzt 20 Jahre alt.").

### Die Kindklassen:

Jede Kindklasse erbt von `Tier` und implementiert spezifische Eigenschaften und Methoden:

- **Klassenattribute**:
  - `num_appendages`: Die Anzahl der Extremitäten (Integer).
  - `is_cold_blooded`: Gibt an, ob das Tier kaltblütig ist (Boolean).
  - `is_mammal`: Gibt an, ob das Tier ein Säugetier ist (Boolean).

- **Überschriebene Methoden**:
  - Spezifiziere für jede Tierklasse angepasste Nachrichten für `eat()`, `sleep()`, und `grow(years)`.

- **Spezifische Methoden**:
  - Überlege dir zusätzliche Funktionen für jede Kindklasse, wie z.B. `klettern()` für die Gorillaklasse.

### Abgabe:

Das fertige Programm soll als reiner Python-Code in mehreren Dateien (*.py) gespeichert werden. Jede Datei repräsentiert eine Klasse im Zoo-Verwaltungssystem. Erstelle eine **zip-Datei** namens **zoo_projekt.zip** und lade diese Datei hier auf dieser Seite hoch.
