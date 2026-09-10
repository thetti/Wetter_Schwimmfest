# User-Story 008: Festwetter differenziert vergleichen

## Status

Abgeschlossen. Das Dashboard bietet elf Tagesperspektiven einschliesslich
Fest-Indikator sowie zehn Stundenindikatoren mit Mittelwertlinien und typischer
Bandbreite für beide Kandidatentage.

Geprüft am 10. September 2026:

- 21 automatische Tests bestanden;
- echte Tagesdateien mit 12'000 Zeilen geladen;
- vier echte Stunden-Jahrzehntdateien und die laufende Datei mit zusammen
  288'304 Zeilen geladen;
- Fest-Indikator für alle 68 verfügbaren Kandidatentage berechnet;
- beide Stundenprofile enthalten alle lokalen Stunden 1 bis 24.

## User Story

Als Nutzer möchte ich weitere Tageswerte, einen verständlichen Fest-Indikator
und typische Stundenverläufe vergleichen, damit ich die beiden Kandidatentage
aus mehreren nachvollziehbaren Perspektiven beurteilen kann.

## Sichtbares Ergebnis

Das bestehende Jahresdiagramm bietet zusätzliche Tagesindikatoren und den
Fest-Indikator von 0 bis 100 an. Ein separates Diagramm zeigt für einen
ausgewählten Stundenindikator je Kandidatentag den Mittelwert jeder lokalen
Stunde über alle verfügbaren Jahre sowie die typische Bandbreite als Schatten.

## Umfang

- Tagesmittel- und Tagestiefsttemperatur ergänzen
- mittleren Wind, maximale Böe und relative Luftfeuchtigkeit ergänzen
- Sonnenscheindauer, relative Sonnenscheindauer und Globalstrahlung ergänzen
- Fest-Indikator mit fest dokumentierten Teilwerten und Gewichten berechnen
- amtliche Stundenwerte für die erste Station laden
- Niederschlag, Temperatur, Sonne, Strahlung, Wind, Böe, Luftfeuchtigkeit und
  Taupunkt als Stundenindikatoren anbieten
- Stundenwerte in lokale Zeit und Stundenintervalle 1 bis 24 übersetzen
- Mittelwert sowie 25. und 75. Perzentil je Stunde und Kandidatentag darstellen

## Nicht enthalten

- freie Orts- oder Stationswahl
- nutzerdefinierte Gewichte oder Schwellenwerte für den Fest-Indikator
- 10-Minuten-Werte
- operative Wetterwarnungen oder Vorhersagen

## Akzeptanzkriterien

- Alle ausgewählten amtlichen Tages- und Stundenparameter werden mit Einheit
  und Zeitbezug angezeigt.
- Kurze oder fehlende Messreihen bleiben als solche erkennbar.
- Die Berechnung des Fest-Indikators ist im Code und im Dashboard vollständig
  nachvollziehbar.
- Der Fest-Indikator wird bei fehlenden Kernmessungen nicht teilweise oder mit
  veränderten Gewichten berechnet.
- Das Stundendiagramm hat die lokalen Stunden 1 bis 24 auf der x-Achse.
- Beide Kandidatentage besitzen je eine Mittelwertlinie und ein eigenes Band
  vom 25. bis zum 75. Perzentil.
- Automatische Tests prüfen Datenimport, Score, Stundenaggregation,
  Diagramme und Dashboard-Start.
