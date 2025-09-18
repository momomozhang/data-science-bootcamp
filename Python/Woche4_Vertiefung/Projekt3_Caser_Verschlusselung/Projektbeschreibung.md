# Projekt 3: Cäsar-Verschlüsselung

## Projektbeschreibung

In diesem Projekt wirst du ein Programm zur Cäsar-Verschlüsselung erstellen. Dieses historische Verschlüsselungsverfahren verändert Buchstaben eines Textes basierend auf einer festgelegten Verschiebungszahl.

Der Ablauf deines Programms wird folgendermaßen gestaltet:

- Aufforderung zur Eingabe eines Textes, der nur Kleinbuchstaben enthält.
- Aufforderung zur Eingabe einer Verschiebungszahl, die angibt, um wie viele Stellen jeder Buchstabe im Alphabet verschoben wird.
- Der eingegebene Text wird gemäß der Cäsar-Verschlüsselung mit der gewählten Verschiebungszahl verschlüsselt.
- Ausgabe des verschlüsselten Textes in der Konsole.
- Optional: Ermögliche die Rückverschlüsselung des Textes, um die ursprüngliche Nachricht zu erhalten.

## Abgabe

Das endgültige Programm muss als reiner Python-Code unter dem Namen `caesar.py` eingereicht werden. Ein erster Prototyp kann in einem Jupyter Notebook entwickelt werden, muss aber für die Abgabe in eine Python-Datei (*.py) für die Ausführung außerhalb des Notebooks, beispielsweise in VS Code oder Spyder, übertragen werden.

## Tipps für die Umsetzungn

- Nutze `ord()` um ein Zeichen in seinen entsprechenden ASCII-Wert umzuwandeln und `chr()` um den ASCII-Wert zurück in ein Zeichen zu konvertieren.
- Verwende den Modulo-Operator `%` um sicherzustellen, dass die Verschiebung innerhalb des Bereichs der Kleinbuchstaben bleibt. Dies ermöglicht es, bei 'z' wieder bei 'a' anzufangen.
- Denke daran, dass die ASCII-Werte für Kleinbuchstaben von 97 ('a') bis 122 ('z') laufen.

## Beispiel

Hier ist ein Beispiel, wie dein verschlüsselter Text in der Konsole aussehen könnte:
