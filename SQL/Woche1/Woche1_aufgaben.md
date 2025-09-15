![Employee DB ERD](image.png)

1. Wie viele salary-Werte hat die angestellte Fachkraft mit der Nummer emp_no '100001' erhalten?


2. Wie viele unterschiedliche Titel gibt es in dem Unternehmen?
Hinweis: Experimentiere mit dem Befehl DISTINCT


3. Wie viele Personen haben am 17. August Geburtstag? Versuche das einmal mit `birth_date::text LIKE ...` und einmal mit der Funktion `date_part`.


4. Wie lauten die Nachnamen aller Angestellten, die eine emp_no kleiner als 20.000 haben, Uri mit Vornamen heißen, weiblich sind und, entweder zwischen 1957-05-23 und 1958-01-01 Geburtstag haben oder zwischen 1989-02-10 und 1990-01-01 eingestellt wurden.
Hinweis: Für ein Datumsintervall kannst du BETWEEN benutzen.


5. Gibt es weitere Mitarbeiter, die die gleichen Kriterien wie die in Aufgabe 4 erfüllen, jedoch nicht den Namen Uri tragen, sondern einen Vornamen mit drei Buchstaben haben, der mit U beginnt?


![DVD Rental ERD](image-1.png)

1. Du möchtest gerne einen Film ausleihen, der länger als drei Stunden dauert. Welche Filme stehen dir zur Auswahl?


2. Wie viele unterschiedliche Schauspieler*in sind in unserer Videothek gelistet?


3. Wie viele Action-Filme haben wir gelistet? Überleg dir, wie du an die Information Action von categories kommst.


4. Wir wollen ein Special-Offer für alle Kunden anbieten, die aus Ländern kommen, die entweder mit A anfangen oder mit L aufhören. Welche Länder wären das?
