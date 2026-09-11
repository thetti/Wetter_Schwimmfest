# User-Story 009: Wetterverteilungen vergleichen

## Status

Abgeschlossen.

## User Story

Als Nutzer möchte ich neben zeitlichen Verläufen auch typische Werte und deren
Verteilung sehen, damit einzelne Ausreisser die beiden Kandidatentage nicht
übermässig prägen.

## Sichtbares Ergebnis

Das Stundenprofil reicht bis 12:00 Uhr des Folgetags und verwendet historische
Medianwerte. Das Tagesdiagramm erhält rechts zwei schmale Boxplots. Früher und
später Kandidatentag haben in allen Darstellungen dieselben Blautöne.

## Umfang

- Stundenpositionen 1 bis 36 aus Kandidatentag und folgendem Vormittag bilden
- Median statt Mittelwert je Stundenposition berechnen und anzeigen
- Band zwischen 25. und 75. Perzentil beibehalten
- Tageslinien und zwei Boxplots in einer gemeinsamen Grafik kombinieren
- dunkelblaue Farbe für den früheren Kandidatentag verwenden
- hellblaue Farbe für den späteren Kandidatentag verwenden
- Beschriftungen und Dokumentation an die neue Statistik anpassen

## Nicht enthalten

- weitere Tage nach dem Folgetag um 12:00 Uhr
- andere auswählbare Quantile
- statistische Signifikanztests zwischen den Kandidatentagen

## Akzeptanzkriterien

- Das Stundenprofil enthält je Kandidatentag 36 Positionen.
- Stunde 24 ist die letzte Stunde des Kandidatentags; Stunden 25 bis 36 bilden
  01:00 bis 12:00 Uhr des Folgetags ab.
- Die Linie verwendet den Median und nennt ihn in Erklärung und Tooltip so.
- Das Schattenband bleibt das 25.–75. Perzentil.
- Das Tagesdiagramm enthält zwei Linien und zwei Boxplots mit gemeinsamer
  y-Achse.
- Die Farbzuordnung ist in beiden Diagrammen identisch.
- Automatische Tests prüfen Statistik, Folgezeitraum, Boxplots und Farben.

## Prüfung

- 21 automatische Tests erfolgreich
- Median, Perzentile und alle 36 Stundenpositionen geprüft
- gemeinsame y-Achse, Boxplot-Inhalte und durchgängige Farben geprüft
