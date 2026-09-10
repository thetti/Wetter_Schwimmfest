# Projektziel und erster Use-Case

## Ausgangslage

Vor dem Schwimmfest wird wiederholt diskutiert, ob es am Samstag direkt vor dem
Schulstart der Stadt Zug oder eine Woche früher stattfinden soll. Historische
Wetterdaten sollen diese Diskussion mit nachvollziehbaren Fakten unterstützen.

## Ziel

Die Anwendung wird ein Dashboard, das historische Wetterdaten für einen frei
wählbaren Auswertungsort lädt, auswertet und aus mehreren Perspektiven
darstellt. Nutzer sollen einzelne Kalendertage, mehrere Tage oder einen
zusammenhängenden Zeitraum auswählen und über mehrere Jahre untersuchen können.
Eine historische Auswertung kann Hinweise geben, ist aber keine sichere
Vorhersage für einen zukünftigen Zeitraum.

Die beiden Kandidatentage im August bilden den ersten konkreten Use-Case. Das
Dashboard als Ganzes bleibt für weitere Kalenderauswahlen und Darstellungen
offen.

## Orte und Wetterstationen

Der Auswertungsort und der Messstandort sind zwei verschiedene Dinge. Ein frei
gewählter Ort kann zunächst durch eine passende amtliche Wetterstation
repräsentiert werden. Dabei müssen Stationsname, Höhe und räumlicher Bezug zum
Auswertungsort sichtbar bleiben.

Zug mit der zugeordneten MeteoSchweiz-Station Cham ist nur die erste
Konfiguration. Das spätere Dashboard soll andere Orte und Stationen nach
demselben Prinzip unterstützen. Welche Indikatoren und Jahre nutzbar sind, wird
für jede Station und Zeitauflösung aus dem amtlichen Dateninventar bestimmt und
nicht aus der Verfügbarkeit in Cham abgeleitet.

## Kalenderregel des ersten Use-Cases

Für jedes Vergleichsjahr gelten folgende Schritte:

1. Bestimme den ersten Montag nach dem 15. August als Schulstart.
2. Bestimme den unmittelbar vorhergehenden Samstag als späteren Kandidatentag.
3. Bestimme den Samstag sieben Tage davor als früheren Kandidatentag.

„Nach dem 15. August“ ist strikt zu verstehen: Fällt der 15. August selbst auf
einen Montag, liegt der Schulstart am darauffolgenden Montag.

Beispiele:

| Vergleichsjahr | Schulstart | Später Kandidatentag | Früher Kandidatentag |
| --- | --- | --- | --- |
| 2026 | Montag, 17. August | Samstag, 15. August | Samstag, 8. August |
| 2027 | Montag, 16. August | Samstag, 14. August | Samstag, 7. August |
| 2028 | Montag, 21. August | Samstag, 19. August | Samstag, 12. August |

## Erste Darstellung in der initialen Konfiguration

Das erste Diagramm zeigt einen auswählbaren Tagesindikator über mehrere Jahre:

- x-Achse: Vergleichsjahr
- y-Achse: Wert des Tagesindikators mit sichtbarer Einheit
- Linie 1: später Kandidatentag
- Linie 2: früher Kandidatentag

Die ersten implementierten Tagesindikatoren sind:

- Niederschlagssumme `rka150d0` eines Tages in Millimetern
- Höchsttemperatur `tre200dx` eines Tages in Grad Celsius

Das Diagramm soll Einzelwerte nachvollziehbar anzeigen und fehlende Werte nicht
unbemerkt überbrücken. Auswertungsort, Datenquelle, Zeitraum und Einheit müssen
erkennbar sein.

Der dargestellte Vergleichszeitraum nutzt so viele verfügbare Daten wie
möglich. Er passt sich an die ausgewählte Station und die ausgewählten
Indikatoren an. Daten des laufenden Jahres können einbezogen werden, sobald die
betreffenden Kalendertage vorliegen; ihr noch vorläufiger Qualitätsstand muss
dann erkennbar sein.

## Weitere Tagesindikatoren

Für die Beurteilung eines Veranstaltungstags kommen neben Niederschlagssumme
und Höchsttemperatur insbesondere folgende Messgrössen infrage:

- Tagesmittel- und Tagestiefsttemperatur
- mittlere Windgeschwindigkeit und maximale Böe
- relative Luftfeuchtigkeit
- Sonnenscheindauer und relative Sonnenscheindauer
- Globalstrahlung
- je nach amtlichem Angebot weitere verständliche Grössen wie Bewölkung oder
  Sichtweite

Die fachliche Eignung eines Indikators wird unabhängig davon beschrieben, ob
er an der zuerst verwendeten Station bereits lange verfügbar ist. In der
Anwendung müssen Kennung, Einheit, Messintervall, tatsächlicher Datenbeginn,
Datenende und Lücken für die gewählte Station nachvollziehbar sein. Eine kurze
Reihe kann für eine ergänzende Ansicht sinnvoll sein, auch wenn sie keinen
langen historischen Vergleich erlaubt.

## Stundenbasierte Indikatoren

Tageswerte beschreiben einen ganzen Tag, beantworten aber nicht zuverlässig,
wie das Wetter während der Veranstaltung war. Für ein frei wählbares örtliches
Festzeitfenster sollen deshalb später insbesondere folgende Stundenwerte
ausgewertet werden können:

- Niederschlagssumme je Stunde
- mittlere, minimale und maximale Temperatur je Stunde
- mittlere Windgeschwindigkeit und maximale Böe je Stunde
- mittlere relative Luftfeuchtigkeit je Stunde
- Sonnenscheindauer oder Strahlung je Stunde, sofern an der Station verfügbar

Eine Stundenansicht kann Einzelstunden zeigen oder Werte innerhalb des
Festzeitfensters verständlich zusammenfassen. Amtliche UTC-Zeitstempel müssen
dabei korrekt in die lokale Zeit am Auswertungsort umgerechnet werden,
einschliesslich Sommerzeit. Tages- und Stundenwerte bleiben getrennte
Perspektiven, weil sie unterschiedliche Fragen beantworten.

Grundlage: [Allgemeiner Wetterindikatorenkatalog](research/weather-indicator-catalog.md)

## Weitere Kalenderauswahlen und Darstellungen

Später soll eine Auswertung nicht auf genau zwei Kandidatentage beschränkt
sein. Vorgesehen sind insbesondere:

- Vergleich von mehr als zwei frei gewählten Kalendertagen
- Auswahl eines zusammenhängenden Zeitraums, zum Beispiel des ganzen Septembers
- Darstellung des Wetterverlaufs innerhalb eines solchen Zeitraums
- Vergleich desselben Zeitraums über mehrere Jahre
- durchschnittlicher Tagesverlauf der Temperatur
- zeitlicher Verlauf des Niederschlags
- Windstärke und Windverlauf
- Auswertung eines örtlichen Festzeitfensters mit Stundenwerten
- weitere Wetterindikatoren und Vergleichsperspektiven

Diese Erweiterungen gehören noch nicht zum ersten Umsetzungsschritt. Fachliche
Begriffe und spätere technische Entscheidungen sollen sie jedoch nicht
unnötig erschweren.

## Erfolg des ersten fachlichen Meilensteins

Der fachliche Entwurf ist bereit für die Umsetzung, wenn die offenen Fragen in
`DECISIONS.md` soweit geklärt sind, dass Datenquelle, Ortsbezug, Zeitraum und
erste Darstellungsform eindeutig feststehen.
