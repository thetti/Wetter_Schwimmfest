# User-Story 010: Dashboard mobil verwenden

## Status

Abgeschlossen.

## User Story

Als Nutzer möchte ich die Wettervergleiche auch auf einem Mobiltelefon gut
lesen und bedienen können, damit ich das Dashboard unabhängig vom Gerät nutzen
kann.

## Sichtbares Ergebnis

Das Dashboard zeigt nur noch die Wetterauswertung. Die beiden Vergleichstage
heissen Datum 1 und Datum 2. Jahresverlauf und Verteilung stehen auf breiten
Bildschirmen nebeneinander und auf schmalen Bildschirmen untereinander.

## Umfang

- Ansicht „Kalenderregel prüfen“ vollständig aus dem Dashboard entfernen
- Kalenderberechnung im Hintergrund beibehalten
- sichtbare Bezeichnungen auf Datum 1 und Datum 2 vereinheitlichen
- Tagesdiagramm responsiv in Verlauf und Verteilung aufteilen
- Stundenachse, Legenden und Diagrammränder für kleine Bildschirme verdichten
- automatische Tests und eine visuelle Prüfung in Desktop- und Mobilbreite

## Nicht enthalten

- Änderung der Kalenderregel
- neue auswählbare Vergleichsdaten
- eigenes Frontend oder zusätzliche UI-Bibliothek

## Akzeptanzkriterien

- Die Kalenderprüfsektion, ihre Eingabe und ihre Kennzahlen sind nicht sichtbar.
- Datum 1 ist dunkelblau und Datum 2 hellblau.
- Auf einem Mobiltelefon werden Jahresverlauf und Boxplots untereinander lesbar.
- Das Stundenprofil hat eine lesbare Achse und eine platzsparende Legende.
- Tabellen bleiben innerhalb ihres verfügbaren Bereichs bedienbar.
- Alle automatischen Tests sind erfolgreich.

## Prüfung

- Die automatische Testsuite umfasst 21 erfolgreiche Tests.
- Die Darstellung wurde bei 1280 Pixel und bei einer mobilen Breite von
  390 Pixel im Browser geprüft.
- Bei mobiler Breite stehen Jahresverlauf und Verteilung untereinander; das
  Stundenprofil und die Datentabelle bleiben innerhalb der Seitenbreite.
