Aufgabe 1 - Erstelle ein ER-Diagramm
Analysiere die Excel-Datei und identifiziere die relevanten Entitäten, Attribute und Beziehungen. Zeichne ein ERD, das die logische Struktur der Daten zeigt. Achte darauf, die Beziehungen zwischen den Entitäten korrekt zu modellieren. Verwende dafür ein Tool deiner Wahl oder zeichne es von Hand.

﻿
Jedes Buch besitzt eine BookID (einen eindeutigen Bezeichner) und einen Titel. Jedes Buch ist mit einer  AuthID verknüpft. Zu jedem*r Autor*in sind außerdem der Name, das Geburtsdatum, das Wohnsitzland und die durchschnittliche Anzahl an Schreibstunden pro Tag gespeichert.

Manche Bücher haben Preise gewonnen. Zu jeder Auszeichnung sind der Name des Preises (Award Name) und das Jahr, in dem der Preis gewonnen wurde (Year Won) vermerkt.

Außerdem enthält die Datei Informationen zu der Edition selbst, wie die eindeutige ISBN, das Format (z.B. Hardcover, Paperback), das Veröffentlichungsdatum, die Seitenzahl, die Auflagenhöhe in Tausend Stück (Print Run Size (k)) und den Preis.

Jede Edition wird von einem Verlag veröffentlicht. Der Verlag hat eine eigene PubID (Verlags-ID), einen Namen (Publishing House) sowie Angaben zum Sitz: Stadt, Bundesland (State), Land (Country), das Gründungsjahr (Year Established) und auch deren Marketingausgaben (Marketing Spend).


Deine Aufgabe in diesem Schritt ist es, aus diesen Daten ein ER-Diagramm zu entwickeln. 

Überlege dir dafür:

Welche Entitäten (z.B Book, Author, Edition, usw.) kannst du aus diesen Daten ableiten?
Welche Attribute gehören zu welcher Entität?
Wie hängen die Entitäten zusammen?
Gibt es 1:n- oder n:m-Beziehungen?

Achte darauf, dass die Beziehungen immer zwischen den richtigen Feldern hergestellt werden. Eine Beziehung zwischen AuthID und BookID wäre nicht sinnvoll, da diese beiden Felder unterschiedliche Dinge repräsentieren. Stattdessen sollten Beziehungen über gemeinsame Felder erfolgen, wie z.B. die AuthID in der Author und Book Tabelle.

Dein ERD soll die Daten so strukturieren, dass jede Information nur einmal gespeichert wird und die Redundanzen der Excel-Datei aufgelöst werden.