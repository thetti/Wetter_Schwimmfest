# Wettervergleich Schwimmfest

Dieses Fachgebiet beschreibt historische Wettervergleiche für frei wählbare
Orte, Kalendertage und Zeiträume. Der erste Use-Case vergleicht zwei mögliche
Samstage für ein Schwimmfest in Bezug auf den Schulstart der Stadt Zug. Zug und
die zunächst zugeordnete Wetterstation Cham sind eine erste Konfiguration und
keine fachliche Begrenzung des Dashboards.

## Language

**Schulstart**:
Der erste Montag, der kalendarisch nach dem 15. August eines Vergleichsjahres
liegt.
_Avoid_: Referenzdatum

**Datum 1**:
Der Samstag genau eine Woche vor Datum 2.
_Avoid_: früher Kandidatentag, erstes Datum

**Datum 2**:
Der Samstag direkt vor dem Schulstart eines Vergleichsjahres.
_Avoid_: später Kandidatentag, zweites Datum

**Vergleichsjahr**:
Ein Kalenderjahr, in dem dieselbe Kalenderauswahl mit historischen
Wetterbeobachtungen verbunden wird.

**Verfügbarer Vergleichszeitraum**:
Die grösstmögliche zeitliche Abdeckung, für welche die gewählte Station und die
ausgewählten Wetterindikatoren Daten anbieten. Einzelne Messwertlücken bleiben
innerhalb dieses Zeitraums als Lücken sichtbar.
_Avoid_: festes Startjahr

**Kalenderauswahl**:
Einzelne Kalendertage, mehrere frei gewählte Kalendertage oder ein
zusammenhängender Zeitraum, die innerhalb eines Vergleichsjahres ausgewertet
werden.
_Avoid_: Kandidatentage, wenn die Tage keine möglichen Veranstaltungstermine sind

**Auswertungsort**:
Der geografische Ort, auf den sich der Wettervergleich bezieht. Er ist nicht
zwingend identisch mit dem Standort einer Wetterstation.
_Avoid_: Wetterstation

**Wetterstation**:
Ein konkreter Messstandort, dessen Beobachtungen einem Auswertungsort zugeordnet
werden können. Stationsname, Höhe und räumlicher Bezug zum Auswertungsort
bleiben nachvollziehbar.
_Avoid_: Auswertungsort

**Stationszuordnung**:
Die transparente Verbindung zwischen einem Auswertungsort und der für ihn
verwendeten Wetterstation. Eine nahe Station ist nicht automatisch für jedes
Gelände gleich repräsentativ.

**Indikatorverfügbarkeit**:
Der Zeitraum, in dem ein bestimmter Wetterindikator an einer bestimmten Station
und in einer bestimmten Zeitauflösung tatsächlich verfügbar ist.
_Avoid_: allgemeiner Stationsbeginn

**Zeitauflösung**:
Die Länge der Zeitabschnitte, auf die sich Wetterwerte beziehen, beispielsweise
ein Tag oder eine Stunde.

**Festzeitfenster**:
Der örtliche Zeitraum innerhalb eines Veranstaltungstags, der für eine
stundenbasierte Auswertung betrachtet wird, beispielsweise 10:00–18:00 Uhr.

**Stundenindikator**:
Eine Wetterkennzahl, die sich auf eine einzelne Stunde bezieht. Mehrere
Stundenwerte können den Verlauf innerhalb eines Festzeitfensters zeigen.

**Tagesindikator**:
Eine Wetterkennzahl, die sich auf einen ganzen Kalendertag bezieht, etwa die
Niederschlagssumme oder die Höchsttemperatur.
_Avoid_: Wetterwert

**Fest-Indikator**:
Eine transparente Bewertung der Anwendung von 0 bis 100, die mehrere
Tagesindikatoren mit festen Regeln und Gewichten zusammenfasst. Sie ist kein
amtlicher Wetterwert; 100 steht für besonders günstige und 0 für sehr
ungünstige Bedingungen gemäss diesen Regeln.
_Avoid_: amtlicher Festwert, Wettervorhersage

**Typische Bandbreite**:
Der Bereich zwischen dem 25. und 75. Perzentil historischer Stundenwerte. Er
enthält die mittlere Hälfte der beobachteten Werte und ist kein Minimum-
Maximum-Bereich.
_Avoid_: Unsicherheit, Prognoseband

**Stundenposition**:
Die fortlaufende Stunde innerhalb des 36-stündigen Vergleichsfensters. Die
Positionen 1–24 gehören zum gewählten Datum, 25–36 zum Folgetag bis 12:00 Uhr.
_Avoid_: Uhrzeit, wenn der Folgetag nicht eindeutig wäre

**Typischer Stundenverlauf**:
Die Folge der historischen Medianwerte je Stundenposition, ergänzt durch die
typische Bandbreite. Er beschreibt eine Verteilung vergangener Beobachtungen
und keine Vorhersage.
_Avoid_: durchschnittlicher Tagesverlauf

**Niederschlagssumme**:
Die während eines ausdrücklich genannten Zeitintervalls aufsummierte
Niederschlagsmenge in Millimetern. Tages- und Stundensummen beantworten
unterschiedliche Fragen und dürfen nicht ohne Angabe des Intervalls vermischt
werden.
_Avoid_: Regenmenge ohne Angabe des Zeitfensters

**Historischer Vergleich**:
Die Auswertung derselben Kalenderauswahl und Wetterindikatoren über mehrere
Vergleichsjahre; sie kann einzelne Tage gegenüberstellen oder den Verlauf eines
zusammenhängenden Zeitraums zeigen.
