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
- Linie 1: früher Kandidatentag, durchgehend dunkelblau
- Linie 2: später Kandidatentag, durchgehend hellblau
- rechts: ein schmaler Boxplot je Kandidatentag mit denselben Messwerten und
  derselben y-Achse

Das Tagesdiagramm bietet an:

- Niederschlagssumme `rka150d0` eines Tages in Millimetern
- Höchsttemperatur `tre200dx` eines Tages in Grad Celsius
- Tagesmittel- und Tagestiefsttemperatur
- mittlere Windgeschwindigkeit und maximale Böe
- relative Luftfeuchtigkeit
- Sonnenscheindauer und relative Sonnenscheindauer
- Globalstrahlung
- den aus sechs Kernmessungen berechneten Fest-Indikator von 0 bis 100

Das Diagramm soll Einzelwerte nachvollziehbar anzeigen und fehlende Werte nicht
unbemerkt überbrücken. Auswertungsort, Datenquelle, Zeitraum und Einheit müssen
erkennbar sein.

Der dargestellte Vergleichszeitraum nutzt so viele verfügbare Daten wie
möglich. Er passt sich an die ausgewählte Station und die ausgewählten
Indikatoren an. Daten des laufenden Jahres können einbezogen werden, sobald die
betreffenden Kalendertage vorliegen; ihr noch vorläufiger Qualitätsstand muss
dann erkennbar sein.

## Tagesindikatoren und Fest-Indikator

Die fachliche Eignung eines Indikators wird unabhängig davon beschrieben, ob
er an der zuerst verwendeten Station bereits lange verfügbar ist. In der
Anwendung müssen Kennung, Einheit, Messintervall, tatsächlicher Datenbeginn,
Datenende und Lücken für die gewählte Station nachvollziehbar sein. Eine kurze
Reihe kann für eine ergänzende Ansicht sinnvoll sein, auch wenn sie keinen
langen historischen Vergleich erlaubt.

Der Fest-Indikator fasst sechs besonders relevante, lang verfügbare Messgrössen
mit festen Gewichten zusammen:

| Teilwert | Gewicht |
| --- | ---: |
| Niederschlag | 30 % |
| Tagesmitteltemperatur | 25 % |
| stärkste Böe | 15 % |
| Höchsttemperatur | 10 % |
| mittlerer Wind | 10 % |
| relative Luftfeuchtigkeit | 10 % |

Jeder Teilwert wird über sichtbare Stützpunkte auf 0 bis 100 Punkte abgebildet;
dazwischen wird linear gerechnet. Die Anwendung zeigt die vollständigen
Stützpunkte direkt beim Diagramm. Fehlt eine Kernmessung, bleibt der
Fest-Indikator für diesen Tag leer. Sonnenschein und Globalstrahlung bleiben
separate Messgrössen, damit kurze Reihen die Zusammensetzung des Scores nicht
zwischen Jahren verändern.

## Stundenbasierte Indikatoren

Tageswerte beschreiben einen ganzen Tag, beantworten aber nicht zuverlässig,
wie das Wetter während der Veranstaltung war. Das separate Stundendiagramm
bietet deshalb folgende Messgrössen an:

- Niederschlagssumme je Stunde
- mittlere, minimale und maximale Temperatur je Stunde
- mittlere Windgeschwindigkeit und maximale Böe je Stunde
- mittlere relative Luftfeuchtigkeit je Stunde
- Sonnenscheindauer oder Strahlung je Stunde, sofern an der Station verfügbar

Für die 36 fortlaufenden Stunden vom Beginn des Kandidatentags bis 12:00 Uhr
des Folgetags zeigt es je Kandidatentag den Median über alle verfügbaren Jahre.
Ein Schatten vom 25. bis zum 75. Perzentil zeigt die typische Bandbreite.
Amtliche UTC-Zeitstempel werden korrekt in lokale Zeit am Auswertungsort
umgerechnet, einschliesslich Sommerzeit. Tages- und Stundenwerte bleiben
getrennte Perspektiven, weil sie unterschiedliche Fragen beantworten.

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
- weitere Wetterindikatoren und Vergleichsperspektiven

Diese Erweiterungen gehören noch nicht zum ersten Umsetzungsschritt. Fachliche
Begriffe und spätere technische Entscheidungen sollen sie jedoch nicht
unnötig erschweren.

## Erfolg des ersten fachlichen Meilensteins

Der fachliche Entwurf ist bereit für die Umsetzung, wenn die offenen Fragen in
`DECISIONS.md` soweit geklärt sind, dass Datenquelle, Ortsbezug, Zeitraum und
erste Darstellungsform eindeutig feststehen.
