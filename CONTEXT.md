# Wettervergleich Schwimmfest

Dieses Fachgebiet beschreibt historische Wettervergleiche für frei wählbare
Kalendertage und Zeiträume. Der erste Use-Case vergleicht zwei mögliche Samstage
für ein Schwimmfest in Bezug auf den Schulstart der Stadt Zug.

## Language

**Schulstart**:
Der erste Montag, der kalendarisch nach dem 15. August eines Vergleichsjahres
liegt.
_Avoid_: Referenzdatum

**Später Kandidatentag**:
Der Samstag direkt vor dem Schulstart eines Vergleichsjahres.
_Avoid_: erster Samstag, Referenzsamstag

**Früher Kandidatentag**:
Der Samstag genau eine Woche vor dem späteren Kandidatentag.
_Avoid_: zweiter Samstag, anderer Samstag

**Vergleichsjahr**:
Ein Kalenderjahr, in dem dieselbe Kalenderauswahl mit historischen
Wetterbeobachtungen verbunden wird.

**Kalenderauswahl**:
Einzelne Kalendertage, mehrere frei gewählte Kalendertage oder ein
zusammenhängender Zeitraum, die innerhalb eines Vergleichsjahres ausgewertet
werden.
_Avoid_: Kandidatentage, wenn die Tage keine möglichen Veranstaltungstermine sind

**Auswertungsort**:
Der geografische Ort, auf den sich der Wettervergleich bezieht; anfänglich ist
dies Zug, später kann ein anderer Ort gewählt werden.
_Avoid_: Wetterstation

**Tagesindikator**:
Eine Wetterkennzahl, die sich auf einen ganzen Kalendertag bezieht, etwa die
Niederschlagssumme oder die Höchsttemperatur.
_Avoid_: Wetterwert

**Historischer Vergleich**:
Die Auswertung derselben Kalenderauswahl und Wetterindikatoren über mehrere
Vergleichsjahre; sie kann einzelne Tage gegenüberstellen oder den Verlauf eines
zusammenhängenden Zeitraums zeigen.
