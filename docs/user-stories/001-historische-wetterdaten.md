# User-Story 001: Historische Wetterdaten auswählen

## Status

Abgeschlossen. MeteoSchweiz, die Station Cham (CHZ), `rka150d0` und die Regel
des maximal verfügbaren Vergleichszeitraums sind als Datengrundlage bestätigt.

Ergebnis: [Recherche zur historischen Wetterdatenquelle](../research/weather-data-source.md)

## Story

Als Organisator des Schwimmfests möchte ich wissen, welche amtlichen
historischen Wetterdaten wir für Zug verwenden können, damit spätere Vergleiche
der Kandidatentage auf einer nachvollziehbaren und langfristig verfügbaren
Datengrundlage beruhen.

## Umfang

- eine geeignete offizielle Schweizer Datenquelle bestimmen
- eine repräsentative Wetterstation für Zug vorschlagen
- Verfügbarkeit von täglicher Niederschlagssumme und Tageshöchsttemperatur prüfen
- historischen Zeitraum, Einheiten, Dateiformat und Aktualisierung klären
- Lizenz, Qualitätsangaben und fehlende Messwerte berücksichtigen
- Stationsname und Distanz zum Auswertungsort später sichtbar machen

Nicht Teil dieser User-Story sind das Herunterladen der vollständigen Daten,
Python-Code und das Dashboard.

## Akzeptanzkriterien

- Die Empfehlung ist durch direkte Links auf amtliche Quellen belegt.
- Datenquelle, Station, Parameter und bekannte Einschränkungen sind dokumentiert.
- Offene Fragen sind von bestätigten Fakten getrennt.
- Der Nutzer kann die vorgeschlagene Datengrundlage vor der Implementierung
  bestätigen oder anpassen.
