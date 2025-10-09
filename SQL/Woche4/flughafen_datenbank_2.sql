----------------------------------------------------------------------------------------------------
--- Aufgabe 1.
--- Ermittle den minimalen, maximalen und durchschnittlichen Preis der Buchungen.
----------------------------------------------------------------------------------------------------
SELECT
	MIN(preis) AS preis_min,
	MAX(preis) AS preis_max,
	ROUND(AVG(preis),2) AS preis_avg
FROM
	buchung;


----------------------------------------------------------------------------------------------------
--- Aufgabe 2
--- Finde die Namen der Reisenden mit den höchsten Buchungskosten.
----------------------------------------------------------------------------------------------------
SELECT
	p.vorname,
	p.nachname,
	p.passagier_id,
	b.preis
FROM
	passagier p
	JOIN buchung b
		ON p.passagier_id = b.passagier_id
WHERE
	b.preis = (SELECT MAX(preis) FROM buchung)
ORDER BY
	p.passagier_id;


----------------------------------------------------------------------------------------------------
--- Aufgabe 3
--- Bestimme die Fluglinie mit den durchschnittlich teuersten Tickets.
----------------------------------------------------------------------------------------------------

SELECT
	f.fluglinie_id,
	f.fluglinie_name AS company,
	SUM(b.preis) AS total_sum_of_bookings,
	COUNT(*) AS no_of_bookings,
	AVG(b.preis) AS average_price_of_bookings
FROM
	fluglinie f
	INNER JOIN flug ON f.fluglinie_id = flug.fluglinie_id
	INNER JOIN buchung b ON flug.flug_id = b.flug_id
GROUP BY
	f.fluglinie_id,
	f.fluglinie_name
ORDER BY
	AVG(b.preis) DESC;

----------------------------------------------------------------------------------------------------
--- Aufgabe 4
--- Ermittle die Flugzeuge mit der höchsten Kapazität, die vom Flughafen ALTAMIRA abgeflogen sind.
----------------------------------------------------------------------------------------------------
SELECT
	DISTINCT flugzeug.flugzeug_id,
	flughafen.flughafen_name,
	ft.bezeichnung,
	flugzeug.kapazitaet,
	fluglinie.fluglinie_name
FROM
	flug
	INNER JOIN flughafen ON flug.von = flughafen.flughafen_id
	INNER JOIN fluglinie ON flug.fluglinie_id = fluglinie.fluglinie_id
	INNER JOIN flugzeug ON flug.flugzeug_id = flugzeug.flugzeug_id
	INNER JOIN flugzeug_typ ft ON flugzeug.typ_id = ft.typ_id
WHERE
	flughafen.flughafen_name = 'ALTAMIRA'
ORDER BY
	flugzeug.kapazitaet DESC

----------------------------------------------------------------------------------------------------
--- Aufgabe 5
--- Zähle, wie viele Personen die Spain Airlines
--- im Zeitraum vom 06.06.2015 bis zum 08.06.2015 transportiert hat.
--- Dabei zählen wir die Personen, die in diesem Zeitraum abgeflogen sind,
--- auch wenn sie erst später ankommen.
----------------------------------------------------------------------------------------------------
SELECT
	fluglinie.fluglinie_name,
	COUNT(*) AS anzahl_passagiere
FROM
	fluglinie
	INNER JOIN flug ON fluglinie.fluglinie_id = flug.fluglinie_id
	INNER JOIN buchung b ON flug.flug_id = b.flug_id
WHERE
	fluglinie.fluglinie_name = 'Spain Airlines' AND
	flug.abflug BETWEEN '2015-06-06' AND '2015-06-08'
GROUP BY
	fluglinie.fluglinie_name;


----------------------------------------------------------------------------------------------------
--- Aufgabe 6
--- Erstelle für jeden Flug eine Auflistung mit Flugnummer,
--- Kapazität des Flugzeugs und der Anzahl der Buchungen.
--- Füge eine Spalte hinzu, die anzeigt,
--- ob der Flug mehr als 5% ausgelastet war (basierend auf der Kapazität und der Anzahl der Buchungen).
--- Da wir nur ein Sample der Buchungen für das Projekt nutzen entspricht die Anzahl nicht der Realität.
----------------------------------------------------------------------------------------------------
SELECT
	flug.flug_id,
	flug.flugnr,
	flugzeug.kapazitaet,
	COUNT(b.buchung_id) AS anzahl_buchungen,
	CASE
		WHEN COUNT(b.buchung_id) > (flugzeug.kapazitaet * 0.05) THEN 'Yes'
		ELSE 'No'
	END AS ausgelastet_über_5_prozent
FROM
	flug
	INNER JOIN flugzeug ON flug.flugzeug_id = flugzeug.flugzeug_id
	INNER JOIN buchung b ON flug.flug_id = b.flug_id
GROUP BY
	flug.flug_id,
	flug.flugnr,
	flugzeug.kapazitaet
ORDER BY
	flug.flug_id,
	flug.flugnr;


----------------------------------------------------------------------------------------------------
--- Aufgabe 7
--- Identifiziere die Fluglinien, die am häufigsten zum Flughafen KAGOSHIMA fliegen.
----------------------------------------------------------------------------------------------------
SELECT
	flughafen.flughafen_name AS ziel_flughafen,
	fluglinie.fluglinie_name,
	COUNT(flug.flug_id) AS anzahl_fluege
FROM
	flug
	INNER JOIN flughafen ON flug.nach = flughafen.flughafen_id
	INNER JOIN fluglinie ON flug.fluglinie_id = fluglinie.fluglinie_id
WHERE
	flughafen.flughafen_name = 'KAGOSHIMA'
GROUP BY
	flughafen.flughafen_name,
	fluglinie.fluglinie_name
ORDER BY
	COUNT(flug.flug_id) DESC ;


----------------------------------------------------------------------------------------------------
--- Aufgabe 8
--- Bestimme die Flugzeuge einer Fluglinie mit einem italienischen Flughafen als Basis,
--- die die meisten Flüge durchgeführt haben, und gib deren Typ an.
----------------------------------------------------------------------------------------------------
SELECT
	flugzeug.flugzeug_id,
	fluglinie.fluglinie_name AS firmenname,
	fluglinie.heimat_flughafen_id,
	flughafen.flughafen_land,
	flugzeug_typ.bezeichnung,
	COUNT(flug.flug_id) AS anzahl_fluege
FROM
	flug
	INNER JOIN flugzeug ON flug.flugzeug_id = flugzeug.flugzeug_id
	INNER JOIN fluglinie ON flug.fluglinie_id = fluglinie.fluglinie_id
	INNER JOIN flughafen ON fluglinie.heimat_flughafen_id = flughafen.flughafen_id
	INNER JOIN flugzeug_typ ON flugzeug.typ_id = flugzeug_typ.typ_id
WHERE
	flughafen.flughafen_land ILIKE '%italy%'
GROUP BY
	flugzeug.flugzeug_id,
	fluglinie.fluglinie_name,
	fluglinie.heimat_flughafen_id,
	flughafen.flughafen_land,
	flugzeug_typ.bezeichnung
ORDER BY
	COUNT(flug.flug_id) DESC;

----------------------------------------------------------------------------------------------------
--- Aufgabe 9
--- Berechne die gesamten Anteile aller Buchungen je nach Flugzeugtyp in Prozent.
----------------------------------------------------------------------------------------------------
DROP TABLE IF EXISTS total_buchungen;
CREATE TEMPORARY TABLE total_buchungen AS (
	SELECT COUNT(*) AS total_count FROM buchung
);

SELECT
	flugzeug_typ.bezeichnung AS flugzeugtyp,
	COUNT(b.buchung_id) AS anzahl_buchungen,
	ROUND((COUNT(b.buchung_id) * 100.0 / (SELECT total_count FROM total_buchungen)), 2) AS anteil_prozent
FROM
	flugzeug_typ
	INNER JOIN flugzeug ON flugzeug_typ.typ_id = flugzeug.typ_id
	INNER JOIN flug ON flugzeug.flugzeug_id = flug.flugzeug_id
	INNER JOIN buchung b ON flug.flug_id = b.flug_id
GROUP BY
	flugzeug_typ.bezeichnung
ORDER BY
	COUNT(b.buchung_id) DESC;
