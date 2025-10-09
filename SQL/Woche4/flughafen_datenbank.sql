----------------------------------------------------------------------------------------------------
--- Benenne die Tabelle `buchung_sample` zu `buchung` um.
----------------------------------------------------------------------------------------------------

ALTER TABLE IF EXISTS buchung_sample RENAME TO buchung;


----------------------------------------------------------------------------------------------------
--- Füge eine neue Person in die Tabelle `passagier` ein,
--- wobei die ID automatisch generiert werden soll.
--- Notiere, welche ID der neuen Zeile zugewiesen wurde.
----------------------------------------------------------------------------------------------------

INSERT INTO passagier (passnummer, vorname, nachname)
VALUES ('EK3879J28', 'Panda', 'Shifu');


----------------------------------------------------------------------------------------------------
--- Füge der Tabelle passagier eine neue Spalte `staatsangehörigkeit` hinzu.
----------------------------------------------------------------------------------------------------

ALTER TABLE passagier ADD COLUMN staatsangehörigkeit VARCHAR(30);

----------------------------------------------------------------------------------------------------
--- Weise der zuvor erstellten Person eine Nationalität zu.
----------------------------------------------------------------------------------------------------

UPDATE passagier
SET staatsangehörigkeit = 'deutsch'
WHERE passnummer = 'EK3879J28';

----------------------------------------------------------------------------------------------------
--- Entferne die Spalte `staatsangehörigkeit` aus der Tabelle `passagier`.
----------------------------------------------------------------------------------------------------

ALTER TABLE passagier DROP COLUMN IF EXISTS staatsangehörigkeit;
