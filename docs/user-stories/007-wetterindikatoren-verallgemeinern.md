# User-Story 007: Wetterindikatoren verallgemeinern

## Status

Abgeschlossen. Die allgemeinen Projektdokumente trennen Auswertungsort,
Wetterstation, Indikator und Zeitauflösung. Der allgemeine Katalog enthält
Tages- und Stundenindikatoren unabhängig von ihrer Verfügbarkeit in Cham.

## User Story

Als Nutzer möchte ich Wetterindikatoren unabhängig von der ersten Orts- und
Stationswahl verstehen, damit das Dashboard später unterschiedliche Orte,
Stationen und zeitliche Perspektiven sinnvoll unterstützen kann.

## Sichtbares Ergebnis

Die Projektdokumentation unterscheidet klar zwischen dem allgemeinen
Produktziel und der ersten Konfiguration Zug/Cham. Ein allgemeiner,
quellenbasierter Katalog beschreibt hilfreiche Wetterindikatoren auf Tages- und
Stundenbasis. Auch fachlich sinnvolle Indikatoren mit kurzer oder fehlender
Messreihe in Cham bleiben darin erhalten.

## Umfang

- allgemeine Dokumente auf unnötige Festlegungen zu Zug und Cham prüfen
- Auswertungsort, Wetterstation und Stationszuordnung sauber unterscheiden
- Tagesindikatoren über die ersten beiden Messgrössen hinaus beschreiben
- Stundenindikatoren für Auswertungen innerhalb eines Festzeitfensters ergänzen
- stationsabhängige Verfügbarkeit getrennt von der fachlichen Eignung bewerten
- bestehende Zug/Cham-Recherche als nachvollziehbare Fallstudie kennzeichnen

## Nicht enthalten

- neue Indikatoren in der Anwendung implementieren
- freie Orts- oder Stationswahl in der Oberfläche implementieren
- Stundenwerte herunterladen oder darstellen
- einen Gesamtwert für „gutes Festwetter“ festlegen

## Akzeptanzkriterien

- Zug und Cham sind in der allgemeinen Spezifikation nur als erste
  Konfiguration bezeichnet.
- Abgeschlossene User Stories dürfen Zug/Cham weiterhin als damaligen
  Umsetzungsstand dokumentieren.
- Der Indikatorenkatalog enthält fachlich hilfreiche Tages- und
  Stundenindikatoren mit Einheit, Nutzen und Einschränkungen.
- Kurze oder fehlende Messreihen an einer einzelnen Station schliessen einen
  Indikator nicht aus dem allgemeinen Katalog aus.
- Die Dokumentation erklärt, dass Verfügbarkeit und maximaler Zeitraum für jede
  Kombination aus Station, Indikator und Zeitauflösung neu bestimmt werden.
- Aussagen zu amtlichen Parametern sind mit primären MeteoSchweiz-Quellen
  belegt.
