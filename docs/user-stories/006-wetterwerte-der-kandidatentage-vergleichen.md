# User-Story 006: Wetterwerte der Kandidatentage vergleichen

## Status

Umgesetzt und geprüft.

## Story

Als Nutzer möchte ich die echten Wetterwerte beider Kandidatentage über alle
verfügbaren Vergleichsjahre in einem Diagramm sehen, damit ich Niederschlag
oder Höchsttemperatur der beiden Termine unmittelbar vergleichen kann.

## Sichtbares Ergebnis

Das bisherige Demo-Diagramm wird durch das erste fachliche Diagramm ersetzt.
Es zeigt pro Vergleichsjahr zwei Linien mit den amtlichen Werten der Station
Cham: eine für Datum 1 und eine für Datum 2.

## Umfang

- vollständige Vergleichsjahre aus dem verfügbaren Wetterzeitraum bestimmen
- Kandidatentage jedes Jahres mit den amtlichen Tageswerten verbinden
- Niederschlagssumme oder Höchsttemperatur auswählbar darstellen
- tatsächliches Datum eines Punkts beim Darüberfahren anzeigen
- fehlende Messwerte als Lücke erhalten und nicht verbinden
- Werte aus der Datei des laufenden Jahres als vorläufig kennzeichnen
- Datenquelle, Station, Zeitraum, Parameter und Einheit sichtbar machen
- künstliches Demo-Diagramm und seinen Test entfernen
- Aufbereitung und Diagramm mit lokalen Daten automatisch prüfen

## Nicht enthalten

- Gewinner, Mittelwerte oder Wahrscheinlichkeiten berechnen
- eine Empfehlung für einen Veranstaltungstermin aussprechen
- andere Orte, Stationen oder frei gewählte Kalenderzeiträume anbieten
- Tagesverläufe oder weitere Wetterindikatoren darstellen

## Akzeptanzkriterien

- Das Diagramm enthält genau zwei benannte Linien.
- Die x-Achse zeigt alle vollständig verfügbaren Vergleichsjahre.
- Die y-Achse zeigt den ausgewählten Parameter mit korrekter Einheit.
- Der Wechsel des Wetterindikators verwendet die jeweils richtigen Werte.
- Das genaue Kandidatendatum ist am Datenpunkt erkennbar.
- Fehlende Werte werden nicht als null behandelt und nicht überbrückt.
- Werte aus dem laufenden Jahr sind als vorläufig erkennbar.
- Für 2025 erscheinen die direkt kontrollierten amtlichen Werte:
  - Datum 1: 32,6 °C und 0,0 mm
  - Datum 2: 29,9 °C und 0,4 mm
- Das Dashboard enthält keine künstlichen Wetterwerte mehr.

## Umsetzungsergebnis

- Die Kalenderauswahl und die amtlichen Tageswerte werden unabhängig von der
  Darstellung zu einer Vergleichstabelle verbunden.
- Das echte Plotly-Diagramm zeigt zwei Linien für 34 vollständige
  Vergleichsjahre von 1993 bis 2026 und insgesamt 68 Tageswerte.
- In diesen 68 Werten bestehen aktuell weder beim Tagesmaximum noch bei der
  Niederschlagssumme Messwertlücken; spätere Lücken würden unterbrochen
  dargestellt.
- Der Tooltip zeigt Vergleichsjahr, genaues Datum, Messwert und Datenstand.
- Die Werte des laufenden Jahres haben offene Markierungen und den Hinweis
  „vorläufig“.
- Die amtliche Stichprobe für 2025 bestätigt 32,6 °C und 0,0 mm für Datum 1
  sowie 29,9 °C und 0,4 mm für Datum 2.
- Das Dashboard wurde mit beiden Indikatoren und dem Tooltip für 2026 im
  Browser geprüft.
- Alle dreizehn automatischen Tests bestehen ohne Internetzugriff.
