# Gewitter- und Schlechtwetterindikatoren für historische Festtage

Stand: 11. September 2026

## Fragestellung und wichtigste Unterscheidung

Diese Notiz untersucht, wie historische Wetterdaten für drei fachlich
verschiedene Aussagen genutzt werden können:

1. **Gewitterneigung:** Wie günstig war die meteorologische Umgebung für die
   Entstehung eines Gewitters, unabhängig davon, ob am Auswertungsort tatsächlich
   eines entstand?
2. **Gewitter beobachtet:** Gab es im festgelegten räumlichen Umfeld und
   Zeitfenster tatsächlich elektrische Gewitteraktivität?
3. **Allgemeine Schlechtwetterbelastung:** Wie ungünstig waren die länger
   anhaltenden Bedingungen für ein Fest, zum Beispiel wegen Kälte, Regen,
   fehlender Sonne oder Wind?

Diese Aussagen dürfen nicht zu früh vermischt werden. Ein heisser, sonniger und
schwüler Sommertag kann eine hohe Gewitterneigung besitzen und bis zum Abend
trotzdem trocken bleiben. Umgekehrt ist ein kalter, regnerischer Tag schlechtes
Festwetter, ohne dass ein Gewitter beteiligt sein muss. MeteoSchweiz definiert
den Beginn eines Gewitters technisch mit der ersten elektrischen Entladung,
auch wenn diese nur innerhalb der Wolke stattfindet
([MeteoSchweiz: Gewitter](https://www.meteoswiss.admin.ch/weather/weather-and-climate-from-a-to-z/thunderstorms.html)).

## Meteorologische Grundlage der Gewitterneigung

Für tiefe, feuchte Konvektion müssen mehrere **Zutaten gleichzeitig**
zusammenkommen:

- **Feuchte:** genügend Wasserdampf in der bodennahen Luft und möglichst auch in
  einer tiefen Schicht der Troposphäre; geeignete Grössen sind Taupunkt,
  spezifische Feuchte und niederschlagbares Wasser.
- **Labilität:** eine Luftmasse, in der ein angehobenes Luftpaket wärmer und
  leichter als seine Umgebung wird. CAPE beschreibt die dabei verfügbare
  Auftriebsenergie. CAPE ist jedoch nur ein Potenzial und kein Gewitternachweis.
- **Auslösung:** Hebung muss die Luft bis zum Niveau freier Konvektion bringen
  und eine allfällige Sperrschicht überwinden. CIN beschreibt die dazu nötige
  Energie. Mögliche Auslöser sind Fronten, Konvergenz, Gebirgshebungen und starke
  Tageserwärmung.
- **Organisation und mögliche Stärke:** Vertikale Windscherung unterstützt
  häufig langlebigere und organisiertere Zellen, sobald Konvektion ausgelöst
  wurde. Sie ist keine notwendige Bedingung für jedes gewöhnliche Gewitter und
  kann allein ebenfalls kein Gewitter erzeugen.

Der ECMWF Forecast User Guide hält ausdrücklich fest, dass weder CAPE noch ein
CAPE-Scherungs-Produkt allein Wolken oder Niederschlag nachweist; Feuchte sowie
das Überwinden von CIN beziehungsweise dynamische Hebung müssen zusätzlich
berücksichtigt werden
([ECMWF: Verwendung von CAPE, CIN und Scherung](https://confluence.ecmwf.int/spaces/FUG/pages/673551783/Section%2B9.6.4%2BUsing%2Bavailable%2Bforecast%2Bproducts)).
Auch die grundlegende „ingredients-based methodology“ für konvektiven Starkregen
trennt Aufstieg, Wasserdampf, Niederschlagseffizienz und Dauer
([Doswell, Brooks und Maddox 1996](https://doi.org/10.1175/1520-0434(1996)011%3C0560:FFFAIB%3E2.0.CO;2)).

### Besonderheiten der Schweiz

Die Schweizer Topografie verändert sowohl die Entstehung als auch die Zugbahn
von Gewittern. Am Alpennordrand, am Jura, in der Napfregion und auf der
Alpensüdseite kann erzwungene Hebung die Auslösung begünstigen; gleichzeitig
erzeugen Täler, Seen, Exposition und Höhenlage starke lokale Unterschiede.
MeteoSchweiz weist für 2000–2024 im Tessin im Mittel 20–30 Gewittertage pro Jahr,
im Wallis und Engadin dagegen weniger als zehn aus. In allen Regionen liegt das
Maximum im Sommer; die mittlere Blitzdichte ist auf Graten, Gipfeln und im
südlichen Tessin besonders hoch
([MeteoSchweiz: Gewitter- und Blitzhäufigkeit](https://www.meteoswiss.admin.ch/weather/weather-and-climate-from-a-to-z/thunderstorms/thunderstorm-and-lightning-frequency-in-switzerland.html)).

Eine europäische Untersuchung, die Blitzdaten, Bodenbeobachtungen,
Radiosondierungen und Reanalyse vergleicht, findet die Alpen als Schwerpunkt
sommerlicher Gewitteraktivität. Sie zeigt zugleich, dass Blitzdaten die
objektivste direkte Stichprobe liefern, während Reanalysen längere Reihen
ermöglichen, aber in Gebieten mit starken räumlichen Gradienten und Gebirgen an
Auflösung und Modellfehlern leiden
([Taszarek et al. 2019](https://doi.org/10.1175/JCLI-D-18-0372.1)).
Damit ist ein fixer, schweizweit gleicher Grenzwert aus blossen Bodenmessungen
fachlich nicht ausreichend.

## Vorschlag A: Indikator „Gewitterneigung“

### Beabsichtigte Aussage

Der Indikator soll auf einer Skala von 0 bis 100 ausdrücken, wie häufig unter
vergleichbaren meteorologischen Bedingungen **im gewählten Raum und
Zeitfenster** ein Blitz beobachtet wurde. Er ist weder der Nachweis eines
Gewitters noch eine operative Vorhersage für ein künftiges Fest.

Die fachlich beste Zielgrösse ist daher eine **empirisch kalibrierte
Wahrscheinlichkeit**:

> Anteil historischer Vergleichsfälle mit mindestens einer elektrischen
> Entladung im definierten Umkreis und Zeitfenster, bei vergleichbarer Feuchte,
> Labilität, Auslösung, Scherung, Jahreszeit und örtlicher Lage.

Eine Bezeichnung wie „37 von 100 vergleichbaren Fällen“ ist verständlicher als
ein scheinbar exakter, aber unkalibrierter Gewitterindex.

### Eingangsdaten und transparente Teilwerte

Für jede Stunde sollten mindestens vier Teilwerte sichtbar bleiben:

| Teilwert | Geeignete Grössen | Aussage | Wichtige Grenze |
| --- | --- | --- | --- |
| Feuchte | Taupunkt oder spezifische Feuchte nahe Boden; niederschlagbares Wasser | Ist genug Wasserdampf für tiefe feuchte Konvektion vorhanden? | Hohe relative Feuchte am Boden allein genügt nicht. |
| Labilität | bevorzugt MUCAPE oder eine ähnlich klar definierte CAPE-Variante | Wie viel Auftriebsenergie könnte freigesetzt werden? | CAPE kann vorhanden sein, ohne dass sie ausgelöst wird; die Definition hängt vom Luftpaket ab. |
| Auslösbarkeit | CIN, grossräumige Vertikalbewegung, bodennahe Konvergenz, Front-/Drucktendenz; Geländehebung | Kann die Sperrschicht überwunden werden? | Ein Reanalysegitter bildet lokale Tal- und Hangzirkulationen nur unvollständig ab. |
| Organisation | 0–6-km-Bulk-Scherung, optional CAPE × Scherung | Begünstigt die Umgebung organisierte oder stärkere Zellen? | Scherung ist eher ein Stärke- als ein reiner Entstehungsindikator. |

Statt universeller Stützpunkte sollten die Zutaten zunächst gegenüber der
**lokalen und saisonalen Klimatologie** eingeordnet werden, zum Beispiel als
Perzentile für Ort, Monat und Tageszeit. Das berücksichtigt, dass derselbe
CAPE- oder Taupunktwert im Tessin, Mittelland oder in einem inneralpinen Tal
nicht dieselbe Bedeutung haben muss. Danach wird das Modell gegen beobachtete
Blitze kalibriert. Orographische Merkmale wie Höhe, Hangneigung, Exposition und
Distanz zu typischen Entstehungsgebieten dürfen die örtliche Grundrate
mitbestimmen, aber nicht von Jahr zu Jahr wechseln.

Als methodisch einfache und nachvollziehbare erste Fassung empfiehlt sich eine
logistische Kalibrierung mit wenigen physikalisch begründeten Variablen. Eine
reine gewichtete Summe ist ungünstig, weil sehr hohe CAPE fehlende Feuchte oder
eine starke Sperrschicht nicht „kompensieren“ sollte. Falls vor der Kalibrierung
eine regelbasierte Vorstufe nötig ist, sollten Feuchte, Labilität und
Auslösbarkeit deshalb als notwendige Tore kombiniert werden; Scherung wirkt
anschliessend als Verstärker der möglichen Organisation. Dieser Rohwert darf
nur „Zutatenindex“, nicht „Wahrscheinlichkeit“, heissen.

MeteoSchweiz kombiniert in seinen operationellen Nowcasting-Systemen ebenfalls
mehrere Informationsarten: Radar, Blitzmessungen, Orographie sowie optional
Modell- und Satellitendaten. Messstationen beschreiben danach lokale Folgen wie
Böen oder Starkregen
([MeteoSchweiz: Nowcasting](https://www.meteoswiss.admin.ch/weather/warning-and-forecasting-systems/nowcasting.html)).
Eine Schweizer Studie zum Nowcasting fand je nach Ziel zusätzlichen Nutzen aus
Radar-, Satelliten-, Blitz-, Modell- und Topografiedaten
([Hamann, Germann und Mecikalski 2022](https://doi.org/10.5194/nhess-22-577-2022)).

### Stunden- und Tagesdefinition

- **Stundenwert:** kalibrierte Wahrscheinlichkeit für mindestens eine Entladung
  im räumlichen Umfeld während der örtlichen Stunde. Die Anwendung muss
  ausdrücklich entscheiden, ob ein Wert die laufende Stunde oder die folgende
  Stunde beschreibt.
- **Tageswert:** nicht der Mittelwert aller 24 Stunden. Für ein Fest sind der
  höchste Stundenwert im Festzeitfenster und zusätzlich die Zahl der Stunden
  mit erhöhter Neigung aussagekräftiger. Soll genau eine Tageswahrscheinlichkeit
  gezeigt werden, muss sie direkt auf Tagesfälle kalibriert werden; die Formel
  `1 - Produkt(1 - Stundenwahrscheinlichkeit)` wäre wegen der starken
  Abhängigkeit benachbarter Stunden ohne zusätzliche Kalibrierung zu hoch.
- **Historische Darstellung:** Median und Perzentile des Stundenwertes über die
  Jahre können typische Tagesgänge zeigen. Für einen einzelnen historischen
  Tag bleibt der tatsächlich rekonstruierte Stundenwert sichtbar.

### Geeignete historische Quelle für die atmosphärische Umgebung

Eine Reanalyse ist einer einzelnen Bodenstation überlegen, weil sie die
vertikale Struktur rekonstruiert. ERA5 verbindet Beobachtungen mit einem
Wettermodell und stellt seit 1940 stündliche Schätzungen auf einem globalen
Gitter bereit. Die Standardauflösung der Atmosphäre beträgt ungefähr 31 km
beziehungsweise 0,25 Grad
([ECMWF: ERA5](https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5)).
Sie ist damit für die grossräumige Umgebung geeignet, nicht für die genaue
Position einer sommerlichen Gewitterzelle in einem Schweizer Tal. Zudem warnt
die ERA5-Dokumentation vor gelegentlich unrealistisch grossen CAPE-Werten
([ECMWF: bekannte ERA5-Probleme](https://confluence.ecmwf.int/pages/viewpage.action?pageId=216495524)).

Radiosondierungen liefern die reale vertikale Struktur hochwertiger, stammen in
der Schweiz aber regulär nur zweimal täglich aus Payerne. Sie sind deshalb eine
wichtige Referenz und Validierungsquelle, jedoch kein stündliches lokales Feld
für beliebige Festorte
([MeteoSchweiz: Radiosondierungen](https://opendatadocs.meteoswiss.ch/b-data-atmosphere/b1-radio-sounding)).

## Vorschlag B: Indikator „Gewitter beobachtet“

### Primäre Definition über elektrische Entladungen

Die unmittelbarste historische Definition lautet:

> **Stunde mit beobachtetem Gewitter:** mindestens eine registrierte
> Wolken-Boden- oder Wolkenentladung innerhalb des festgelegten Umkreises und
> Stundenintervalls. **Gewittertag:** mindestens eine solche Gewitterstunde im
> Tages- oder Festzeitfenster.

Das entspricht der meteorologischen Definition über elektrische Aktivität.
MeteoSchweiz bezieht Blitzdaten von Météorage; pro Ereignis sind unter anderem
Zeit, Koordinaten, Blitzart, Polarität und Intensität vorhanden. Die typische
Ortsgenauigkeit liegt laut MeteoSchweiz bei etwa 1 km. Rund 95 % der
Wolken-Boden-Blitze und bis zu 70 % der Wolkenentladungen werden erfasst. Für
SwissMetNet-Stationen berechnet MeteoSchweiz bereits Summen innerhalb von 3 km
sowie zwischen 3 und 30 km
([MeteoSchweiz: Blitzmessnetz](https://www.meteoswiss.admin.ch/weather/measurement-systems/atmosphere/lightning-detection-network.html)).

Für das Dashboard sollten keine Entladungen als voneinander unabhängige
„Gewitter“ gezählt werden. Sinnvoll sind vielmehr diese getrennten Ergebnisse:

- `Gewitter beobachtet`: ja/nein/keine Daten;
- Zahl der Gewitterstunden im Festzeitfenster;
- Zeitpunkt der ersten und letzten registrierten Entladung;
- kleinste Entfernung zum Auswertungsort;
- Zahl der Entladungen, getrennt nach Wolken-Boden und Wolkenentladungen;
- räumliche Stufen, beispielsweise **am Ort** (0–3 km) und **im Umfeld**
  (3–30 km), angelehnt an die MeteoSchweiz-Aggregation.

Die räumliche Bezugsfläche ist Teil der Definition. Ein grösserer Radius findet
mehr Gewitter, beantwortet aber eine andere Frage. Für die Fest-Sicherheit kann
ein weiterer Umkreis relevant sein als für die Frage, ob es auf dem Gelände
regnete. Die Wahl muss deshalb fachlich begründet und im Dashboard sichtbar
sein. Fehlende Blitzdaten bedeuten **unbekannt**, nicht „kein Gewitter“.

### Radar als zweite Beobachtungsebene

Radar ergänzt Blitzdaten, weil es konvektive Zellen, intensiven Niederschlag und
Hagel räumlich hochaufgelöst erfasst und bereits vor der ersten Entladung
auffällig werden kann. Das MeteoSchweiz-System TRT verfolgt einzelne
Gewitterzellen aus Radarreflektivität
([MeteoSchweiz: Thunderstorms Radar Tracking](https://www.meteoswiss.admin.ch/about-us/research-and-cooperation/projects/en/2002/trt.html)).
Die Schweizer Radare erzeugen etwa alle fünf Minuten ein Volumen; Hagelprodukte
wie POH werden auf einem 1-km-Raster berechnet. Hochwertige Rohdaten liegen seit
2002 vor, allerdings ist die Reihe für seltene lokale Ereignisse kurz und durch
Generationenwechsel nicht vollständig homogen
([MeteoSchweiz: Daten und Methoden der Hagelklimatologie](https://www.meteoswiss.admin.ch/climate/the-climate-of-switzerland/hail-climatology/data-and-methods.html)).

Radar allein beweist jedoch keine elektrische Entladung: Ein kräftiger Schauer
kann ohne Gewitter auftreten. Umgekehrt kann eine Blitzortung den elektrisch
aktiven Teil einer Zelle erst später in ihrem Lebenszyklus erfassen. Die beste
historische Ereigniskennzeichnung ist deshalb:

1. Blitz = primärer Gewitternachweis;
2. TRT-/Radarzelle = räumliche und zeitliche Zuordnung sowie Vor- und Nachphase;
3. Radar-Hagelprodukte, 10-Minuten-Niederschlag und Stationsböen = beobachtete
   Auswirkungen, nicht Ersatz für den Blitznachweis.

Die Open-Data-Übersicht führt Niederschlags- und Hagelradarprodukte, während
Konvektionsprodukte noch ausstehend sind; längere Archive sind teilweise nur
auf Anfrage verfügbar
([MeteoSchweiz Open Data: Radardaten](https://opendatadocs.meteoswiss.ch/de/d-radar-data)).
Eine wissenschaftliche Untersuchung Schweizer Zellen bestätigt zudem, dass
Wolken- und Wolken-Boden-Aktivität nicht linear zusammenhängen und empfiehlt
probabilistische, polarimetrische Radaransätze
([Figueras i Ventura et al. 2019](https://doi.org/10.5194/amt-12-5573-2019)).

### Was Bodenstationsdaten leisten – und was nicht

Stündlicher oder 10-minütiger Starkregen, eine abrupte Böe, Druckänderungen und
gegebenenfalls Hagel sind starke Hinweise auf den **lokalen Durchgang** einer
konvektiven Zelle. Sie sind wertvolle Wirkungsindikatoren. Keine Kombination
dieser Werte kann aber zuverlässig feststellen, ob eine elektrische Entladung
stattfand. Ein entferntes Gewitter kann am Ort keinen Stationsausschlag
erzeugen; ein Schauer oder eine Frontböe kann umgekehrt ähnlich aussehen.
Ohne Blitz- oder geeignete visuelle Beobachtung muss das Ergebnis deshalb
„gewitternahes Ereignis vermutet“ statt „Gewitter beobachtet“ heissen.

## Vorschlag C: „Allgemeine Schlechtwetterbelastung“

### Ziel und Skala

Vorgeschlagen wird eine vom Gewitter getrennte Skala von **0 bis 100**:

- 0 = keine allgemeine Schlechtwetterbelastung im Festzeitfenster;
- 100 = sehr starke, anhaltende oder sicherheitsrelevante Belastung;
- der Wert beschreibt historische Festbedingungen und ist kein amtlicher
  Gefahrenwert.

Die Berechnung sollte nach Möglichkeit aus Stunden- oder 10-Minuten-Werten im
tatsächlichen Festzeitfenster erfolgen. Ein Tagesmaximum oder eine Tagessumme
kann nicht unterscheiden, ob ein Ereignis während des Festes oder nachts
auftrat.

### Empfohlene Belastungsgruppen

| Gruppe | Abgeleitete Kennzahlen im Festzeitfenster | Bewertungslogik |
| --- | --- | --- |
| Nässe | Niederschlagssumme, Anteil nasser Zeitabschnitte, höchste Kurzzeitsumme | Dauer und Intensität getrennt werten; ein kurzer Schauer und Dauerregen sind verschieden störend. |
| Temperatur | Dauer unter einer unteren Komfortgrenze; Dauer über einer Hitzegrenze; Extremwerte | Kälte und Hitze als zwei Richtungen derselben Gruppe; orts- und veranstaltungsspezifische Grenzen. |
| Himmel/Sonne | relative Sonnenscheindauer oder Verhältnis der gemessenen zur möglichen Strahlung | Bewölkung belastet moderat, darf aber nicht als Sicherheitsgefahr erscheinen. |
| Wind | Dauer erhöhten Mittelwinds und höchste Böe | Böen als Sicherheitsaspekt stärker und nicht durch Windstille zu anderer Zeit ausgleichen. |
| Feuchte/Schwüle | Taupunkt oder ein thermischer Belastungsindex zusammen mit Temperatur | Hohe relative Feuchte allein ist bei Kälte und Hitze nicht gleich zu interpretieren. |

Innerhalb jeder Gruppe werden stark zusammenhängende Messgrössen nicht einfach
doppelt gewichtet. Beispielsweise können mittlerer Wind und Böe zu einem
gemeinsamen Windteilwert verbunden werden, wobei die Böe eine Untergrenze der
Belastung setzt. Gleiches gilt für Temperaturmittel und -maximum. Erst danach
werden die fünf Gruppenteilwerte kombiniert. Als diskutierbarer Startpunkt für
ein Schwimmfest eignen sich **Nässe 35 %, Temperatur 25 %, Wind 20 %,
Himmel/Sonne 15 % und Feuchte/Schwüle 5 %**. Diese Gewichte sind eine
Produktentscheidung, keine meteorologische Naturkonstante, und müssen mit
Veranstaltern sowie historischen Beispieltagen geprüft werden.

Die Stützpunkte sollten fest, sichtbar und asymmetrisch sein. Ein Sicherheits-
Schwellenwert darf nicht durch schönes Wetter in einer anderen Kategorie
weggewichtet werden. Amtliche Warnschwellen eignen sich zur Orientierung für
hohe Belastungsstufen, aber nicht unverändert als Komfortgrenzen eines Fests:
MeteoSchweiz warnt beispielsweise bei Gewittern unter anderem anhand von
30–50 mm/h, Böen von 90–120 km/h und Hagel von 2–4 cm für Stufe 3; Stufe 4
beginnt bei noch höheren Ausprägungen
([MeteoSchweiz: Gefahrenstufen Gewitter](https://www.meteoswiss.admin.ch/weather/hazards/explanation-of-the-danger-levels/thunderstorms.html)).
Allgemeine Windwarnungen beginnen im Flachland bei 70–90 km/h, während
Dauerregen-Schwellen regional zwischen Alpennord- und Alpensüdseite
unterschiedlich sind
([Wind](https://www.meteoswiss.admin.ch/weather/hazards/explanation-of-the-danger-levels/wind.html),
[Regen](https://www.meteoswiss.admin.ch/weather/hazards/explanation-of-the-danger-levels/rain.html)).

### Gewitter nicht in einem Mittelwert verschwinden lassen

Zur allgemeinen Belastung kommen zwei separate konvektive Angaben:

- **Gewitterneigung 0–100** für das Potenzial;
- **Gewitter beobachtet ja/nein** mit Entfernung und Zeit für das Ereignis.

Falls später unbedingt ein einziger Gesamtwert nötig ist, sollte akute Gefahr
nicht linear kompensierbar sein. Eine verständliche mögliche Regel wäre:

`Gesamtbelastung = 100 × (1 - (1 - allgemeine Belastung / 100) × (1 - konvektive Belastung / 100))`

Zusätzlich kann ein beobachtetes Gewitter im definierten Sicherheitsumkreis den
Gesamtwert auf eine festgelegte Mindestbelastung setzen. Die konkrete
Sicherheitsdistanz und Abbruchregel ist jedoch eine betriebliche Entscheidung
des Veranstalters und soll nicht aus einer historischen Wetteranalyse abgeleitet
werden. Operativ ersetzen historische Indikatoren niemals aktuelle amtliche
Warnungen; MeteoSchweiz betont, dass Ort, Zeitpunkt und Stärke schwerer Gewitter
selbst mit modernen Methoden nicht mehrere Stunden im Voraus genau bestimmbar
sind
([MeteoSchweiz: Gefahrenstufen Gewitter](https://www.meteoswiss.admin.ch/weather/hazards/explanation-of-the-danger-levels/thunderstorms.html)).

## Einordnung des bestehenden Fest-Indikators

Der gegenwärtige Fest-Indikator beantwortet die umgekehrte, positiv formulierte
Frage: **Wie günstig war der gesamte Tag gemäss sechs ausgewählten
Bodenmessungen?** Er vergibt 0 bis 100 Punkte, wobei 100 besonders günstiges
Festwetter bedeutet.

Jede Messgrösse wird über offen sichtbare Stützpunkte in einen Teilwert von
0 bis 100 übersetzt; zwischen den Stützpunkten wird linear interpoliert. Danach
entsteht ein gewichtetes Mittel:

```text
Fest-Indikator = 0,30 × Niederschlagspunkte + 0,25 × Mitteltemperaturpunkte
+ 0,15 × Böenpunkte + 0,10 × Höchsttemperaturpunkte
+ 0,10 × Windpunkte + 0,10 × Feuchtepunkte
```

| Teilwert | Gewicht | Aktuelle Stützpunkte Messwert → Punkte |
| --- | ---: | --- |
| Tagesniederschlag | 30 % | 0 mm → 100; 0,5 → 90; 2 → 70; 5 → 40; 10 → 10; 20 → 0 |
| Tagesmitteltemperatur | 25 % | 5 °C → 0; 12 → 20; 16 → 60; 20–26 → 100; 30 → 60; 35 → 0 |
| stärkste Tagesböe | 15 % | 0–30 km/h → 100; 50 → 60; 70 → 20; 90 → 0 |
| Tageshöchsttemperatur | 10 % | 10 °C → 0; 18 → 50; 22–30 → 100; 35 → 50; 40 → 0 |
| mittlerer Tageswind | 10 % | 0–10 km/h → 100; 20 → 70; 30 → 30; 40 → 0 |
| mittlere relative Feuchte | 10 % | 0 % → 50; 20 → 70; 35–65 → 100; 75 → 80; 85 → 40; 95–100 → 0 |

Messwerte zwischen zwei Stützpunkten erhalten einen linear dazwischenliegenden
Punktwert; ausserhalb der Tabelle gilt jeweils der erste oder letzte Punktwert.
Bei sonst idealen Teilwerten ergeben beispielsweise 5 mm Tagesniederschlag
noch 82 Gesamtpunkte. Selbst eine stärkste Tagesböe von 90 km/h ergibt bei fünf
sonst idealen Teilwerten noch 85 Gesamtpunkte. Diese Beispiele zeigen, warum
die heutige Mittelung Komfortbedingungen gut zusammenfassen kann, akute
Gefahren aber nicht zuverlässig abbildet.

Fehlt eine der sechs Kernmessungen, bleibt der Fest-Indikator leer. Diese Logik
ist leicht erklärbar, zeitlich und zwischen Stationen stabil und bewahrt die
amtlichen Einzelwerte. Sie hat aber vier fachliche Grenzen:

1. **Tagesbezug:** Sie sagt nicht, ob Regen oder Böen während des Fests auftraten.
2. **Kompensation:** Ein sehr schlechter Teilwert kann durch fünf gute Teilwerte
   ausgeglichen werden; für Blitz, Hagel oder gefährliche Böen ist das
   ungeeignet.
3. **Kein Himmelsteilwert:** Bewölkung, Sonnenschein und Strahlung bleiben wegen
   kürzerer Messreihen ausserhalb des Scores. Ein grauer, trockener Tag kann
   deshalb ähnlich gut erscheinen wie ein sonniger.
4. **Keine Gewitterdiagnose:** Tagesregen, Tagesböe und Feuchte können Folgen
   eines Gewitters enthalten, unterscheiden aber weder Gewitterneigung noch
   tatsächliche elektrische Aktivität.

Als einfache Beziehung gilt derzeit näherungsweise:
`allgemeine Schlechtwetterbelastung = 100 - Fest-Indikator`. Für die neue
fachliche Zielsetzung reicht diese Umkehrung jedoch nicht, weil die aktuelle
Zusammensetzung weder Festzeit noch Bewölkung erfasst und akute Gefahren
kompensierbar macht.

## Empfohlene Zielstruktur für das Dashboard

Die klarste Lösung besteht aus vier nebeneinander verständlichen Aussagen:

1. **Festtauglichkeit 0–100:** positiv formulierter Komfort- und
   Nutzbarkeitswert; Weiterentwicklung des bestehenden Fest-Indikators.
2. **Allgemeine Schlechtwetterbelastung 0–100:** negative Darstellung derselben
   länger anhaltenden Grundbedingungen im konkreten Festzeitfenster.
3. **Gewitterneigung 0–100:** empirisch kalibriertes Potenzial aus Feuchte,
   Labilität, Auslösung, Scherung, Saison und örtlicher Lage.
4. **Gewitter beobachtet:** ja/nein/keine Daten sowie Zeit, Entfernung und
   beobachtete Folgen.

Die beiden ersten Skalen sind teilweise redundant; langfristig sollte die
Oberfläche vorzugsweise eine davon prominent zeigen und die andere nur als
erklärende Gegenperspektive verwenden. Gewitterneigung und Gewitternachweis
müssen dagegen separat bleiben. Für die nächste fachliche Entscheidung sollten
zuerst Festzeitfenster und räumlicher Sicherheitsbezug festgelegt werden; erst
danach sind konkrete Kalibrierung, Schwellen und Datenbeschaffung sinnvoll.

## Datenquellen, räumlicher und zeitlicher Bezug

| Quelle | Geeignete Rolle | Raum/Zeit | Umgang mit Lücken und Grenzen |
| --- | --- | --- | --- |
| Météorage-Blitzdaten bei MeteoSchweiz | direkter Gewitternachweis und Kalibrierziel | Ereigniszeit und -koordinate; laut MeteoSchweiz etwa 1 km Ortsgenauigkeit; Schweizer Reihe seit 2000 | Erfassungsgrad und Netzänderungen je Zeitraum dokumentieren; fehlende Daten nie als null zählen; Zugang und Nutzungsrecht vor Umsetzung klären. |
| MeteoSchweiz-Radar, TRT, POH/MESHS, CombiPrecip | Zellen und lokale Auswirkungen | typischerweise 5 Minuten, Radar-/Hagelprodukte auf etwa 1-km-Raster; hochwertige Reihe seit 2002 | Abschattung und technische Generationen berücksichtigen; Archive teilweise auf Anfrage; Radar ist kein alleiniger Blitznachweis. |
| ERA5-Reanalyse | lange, räumlich vollständige Umgebungsdaten für Zutaten | stündlich ab 1940, ungefähr 31 km/0,25 Grad | Modell-/Reanalysedaten als solche kennzeichnen; für lokale Schweizer Konvektion zu grob; bekannte CAPE-Ausreisser prüfen. |
| Radiosondierung Payerne | gemessene vertikale Referenz für Labilität, Feuchte und Wind | 00 und 12 UTC an einem Ort | nicht auf beliebige Orte oder Stunden übertragen; eher Validierung als lokaler Dashboardwert. |
| SwissMetNet | lokale Auswirkungen und allgemeines Festwetter | Punktmessung, 10 Minuten/Stunde/Tag je Parameter | Station ist nicht identisch mit Auswertungsort; Zeitintervall, Höhe, Datenbeginn und Lücken pro Parameter zeigen. |

Alle abgeleiteten Werte müssen daher Quelle, Einheit, räumlichen Radius,
Zeitintervall, Zeitzone, verfügbare Periode und fehlende Daten sichtbar
ausweisen. Historische Änderungen der Messsysteme und eine mögliche
Nichtstationarität des Klimas sind bei Vergleichen über viele Jahrzehnte als
zusätzliche Einschränkung zu nennen.
