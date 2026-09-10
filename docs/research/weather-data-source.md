# Recherche: historische Wetterdaten für den ersten Meilenstein

Stand: 8. September 2026

## Geltungsbereich

Dieses Dokument hält die Datenquellenentscheidung für die **erste
Konfiguration Zug/Cham** fest. Stationswahl, konkrete Parameter und Startjahr
sind eine nachvollziehbare Fallstudie, aber keine allgemeine Einschränkung des
Dashboards. Für andere Auswertungsorte müssen Stationszuordnung,
Parameterverfügbarkeit und Zeitraum neu geprüft werden.

## Kurzempfehlung für die erste Konfiguration

Für den ersten Meilenstein sollten die **amtlichen Tageswerte der automatischen
MeteoSchweiz-Station Cham (CHZ)** verwendet werden. Sie sind als einfache
CSV-Dateien frei zugänglich und enthalten in derselben Datei sowohl die
Tageshöchsttemperatur als auch zwei amtlich definierte
Niederschlagstagessummen. Für beide gewünschten Indikatoren reicht die
gemeinsame Messreihe ab **11. Juni 1993**.

Im Dashboard muss der Auswertungsort deshalb zunächst transparent als
**„Zug, repräsentiert durch MeteoSchweiz-Station Cham (CHZ), ca. 5,9 km
Luftlinie vom amtlichen Gemeindetreffer Zug“** bezeichnet werden. Es handelt
sich um eine punktuelle Stationsmessung, nicht um einen flächigen Wert für die
Stadt oder Gemeinde Zug.

Als Niederschlagsindikator ist für den einfachen Einstieg `rka150d0`
(00:00–00:00 UTC) geeigneter als `rre150d0` (06:00–06:00 UTC des Folgetags),
weil sein Zeitfenster näher am ausgewählten Kalendertag liegt. Es ist im August
dennoch gegenüber dem lokalen Schweizer Kalendertag um zwei Stunden verschoben.
Diese fachliche Einschränkung muss sichtbar bleiben. Die Verwendung von
`rka150d0` wurde als bewusste Produktentscheidung bestätigt.

## Empfohlene Quelle und Zugang

Das Angebot **„Automatische Wetterstationen – Messwerte“** stammt direkt vom
Bundesamt für Meteorologie und Klimatologie MeteoSchweiz. SwissMetNet umfasst
rund 160 automatische Stationen. Pro Station stehen 10-Minuten-, Stunden-,
Tages-, Monats- und Jahreswerte bereit. MeteoSchweiz empfiehlt ausdrücklich,
für Tagesauswertungen die bereits aggregierte Tagesgranularität zu verwenden,
statt sie selbst aus Rohwerten zu berechnen
([MeteoSchweiz-Dokumentation: automatische Wetterstationen](https://opendatadocs.meteoswiss.ch/de/a-data-groundbased/a1-automatic-weather-stations)).

Der maschinelle Zugang erfolgt über die STAC-REST-API der Bundesgeodaten-
Infrastruktur:

- [STAC-Collection der automatischen Wetterstationen](https://data.geo.admin.ch/api/stac/v1/collections/ch.meteoschweiz.ogd-smn)
- [STAC-Eintrag der Station Cham (CHZ)](https://data.geo.admin.ch/api/stac/v1/collections/ch.meteoschweiz.ogd-smn/items/chz)
- [historische Tageswerte CHZ als CSV](https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/chz/ogd-smn_chz_d_historical.csv)
- [Tageswerte des laufenden Jahres CHZ als CSV](https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/chz/ogd-smn_chz_d_recent.csv)

Die API ist kein eigenes proprietäres MeteoSchweiz-Format, sondern folgt dem
OGC-STAC-API-Standard. MeteoSchweiz beschreibt zudem ETag/`If-None-Match` als
vorgesehenes Verfahren, um eine Datei nur bei Änderungen erneut zu laden
([MeteoSchweiz-Dokumentation: Daten herunterladen](https://opendatadocs.meteoswiss.ch/de/general/download)).

## Ortsbezug und Stationsauswahl im Beispiel Zug/Cham

### Amtliche Koordinaten

Der [MeteoSchweiz-Stationskatalog](https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/ogd-smn_meta_stations.csv)
weist für Cham (CHZ) folgende Angaben aus:

| Merkmal | Wert |
| --- | --- |
| Stationsname und Kürzel | Cham (CHZ) |
| WGS84 | 47.188278° N, 8.464642° E |
| LV95 | E 2'677'759 m, N 1'226'878 m |
| Stationshöhe | 443 m ü. M. |
| Exposition | Anhöhe, 30–100 m über Talsohle |
| allgemeiner Datenbeginn laut Stationskatalog | 1. Januar 1961 |

Als nachvollziehbarer Referenzpunkt für „Zug“ dient der
[Gemeindetreffer Zug (ZG) des amtlichen geo.admin.ch-Suchdienstes](https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=Zug&type=locations&origins=gg25&sr=2056&limit=20).
Er liefert 47.151554° N, 8.521273° E. Der Suchdienst umfasst unter anderem
Städte und Gemeinden
([Dokumentation des geo.admin.ch SearchServer](https://api3.geo.admin.ch/services/sdiservices.html#search)).

Aus den beiden WGS84-Koordinaten ergibt sich mit der Haversine-Formel und einem
mittleren Erdradius von 6'371,0088 km eine Luftlinie von **5,916 km**. Dieselbe
Suche über alle 158 Stationskoordinaten des amtlichen Katalogs ergibt Cham als
nächste automatische MeteoSchweiz-Station; Oberägeri (AEG) folgt mit rund
6,87 km. Die Distanz sagt nichts über Höhenlage, Gelände oder lokales Mikroklima
aus. Genau deshalb sollen Stationsname, Höhe und Distanz in der Anwendung
sichtbar sein.

### Warum nicht „Wetter in Zug“ behaupten?

Cham misst das Wetter an einem konkreten Punkt auf 443 m ü. M. Das ist eine
plausible und einfache Repräsentation für den ersten Meilenstein, aber kein
Messwert für jede Stelle in Zug. Eine spätere Ortswahl sollte entweder wieder
eine Station mit offengelegter Zuordnung verwenden oder auf amtliche
Rasterdaten umgestellt werden.

## Parameter, Einheit und Zeitbezug

Der amtliche [Parameterkatalog](https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/ogd-smn_meta_parameters.csv)
und die CHZ-Tagesdateien enthalten die benötigten Parameter:

| Kennung | Bedeutung | Einheit | Zeitfenster |
| --- | --- | --- | --- |
| `tre200dx` | Lufttemperatur 2 m über Boden; Tagesmaximum | °C | Tagesaggregation; Referenzzeit in UTC |
| `rka150d0` | Niederschlag; Tagessumme | mm | 00:00 UTC bis 00:00 UTC |
| `rre150d0` | Niederschlag; Tagessumme | mm | 06:00 UTC bis 06:00 UTC des Folgetags |

MeteoSchweiz verwendet für alle Referenzzeitstempel UTC; bei Tageswerten
bezeichnet der Zeitstempel den Beginn des Intervalls. Für Niederschlag und
Schnee nennt die allgemeine Dokumentation als historisch konsistentes
Standardintervall 06:00 UTC bis zum Folgetag
([Zeitstempel und Intervalle](https://opendatadocs.meteoswiss.ch/de/general/download#how-datetime-time-intervals-and-missing-values-are-represented)).
Die zusätzliche Niederschlagskennung `rka150d0` definiert dagegen ausdrücklich
den UTC-Kalendertag.

Für `tre200dx` besteht eine zu klärende Dokumentationsnuance: Die allgemeine
Download-Dokumentation beschreibt die meisten Tageswerte als Aggregation des
jeweiligen UTC-Tages. Die amtliche Seite zur Datenaufbereitung nennt jedoch vor
2018 ein leicht anderes Aggregationsfenster (23:50 des Vortags bis 23:40 des
Tages) und ab 2018 00:10 bis 00:00 des Folgetags
([MeteoSchweiz: Datenaufbereitung](https://www.meteoswiss.admin.ch/wetter/messsysteme/datenmanagement/datenaufbereitung.html)).
Vor einer fachlich exakten Tagesdefinition sollte diese Semantik direkt mit
MeteoSchweiz geklärt oder zumindest als Quellenbeschränkung dokumentiert werden.

## Zeitliche Abdeckung und Aktualisierung

Der allgemeine Stationskatalog nennt für Cham Daten seit 1961. Entscheidend ist
aber das parameterspezifische
[Dateninventar](https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/ogd-smn_meta_datainventory.csv):
Für `tre200dx`, `rka150d0` und `rre150d0` beginnt die gemeinsame Reihe erst am
**11. Juni 1993**; ein Enddatum ist nicht gesetzt. Der heruntergeladene
historische Tagesdatensatz reicht mit Stand dieser Recherche bis 31. Dezember
2025. Damit sind für den August-Vergleich die vollständigen Vergleichsjahre
1993 bis 2025 historisch verfügbar; das laufende Jahr kommt aus der
`recent`-Datei.

Eine Stichprobe über den tatsächlichen ersten Use-Case ist ebenfalls positiv:
Für alle 66 frühen und späten Kandidatentage der 33 Vergleichsjahre 1993–2025
enthält die am 8. September 2026 geladene historische CHZ-Datei Werte für
`tre200dx`, `rka150d0` und `rre150d0`. Das garantiert keine allgemeine
Lückenfreiheit; die Anwendung muss leere Felder weiterhin korrekt behandeln.

MeteoSchweiz trennt die Aktualisierung wie folgt
([offizielle Aktualisierungsfrequenzen](https://opendatadocs.meteoswiss.ch/de/general/download#update-frequency)):

- `historical`: Messbeginn bis 31. Dezember des Vorjahres, jährliche
  Aktualisierung;
- `recent`: 1. Januar des laufenden Jahres bis gestern, täglich um 12:00 UTC;
- `now`: nur für Stunden- und 10-Minuten-Werte, daher für diesen Meilenstein
  nicht erforderlich.

## Format und fehlende Werte

Die Stationsdaten sind CSV-Dateien mit

- Semikolon als Spaltentrenner,
- Punkt als Dezimaltrenner,
- Windows-1252 als Zeichenkodierung und
- Zeitstempeln im Format `dd.mm.yyyy HH:MM`.

Dies ist amtlich in der
[MeteoSchweiz-Download-Dokumentation](https://opendatadocs.meteoswiss.ch/de/general/download#how-csv-files-are-structured)
beschrieben. Die erste Spalte enthält das Stationskürzel, die zweite den
Referenzzeitstempel und die weiteren Spalten die Parameterkennungen.

Fehlende Werte sind **leere Felder**. Eine leere Zelle darf daher niemals als
0 mm Niederschlag oder 0 °C interpretiert werden. Die Anwendung sollte sie als
fehlend einlesen, im Diagramm als Lücke zeigen und Linien nicht unbemerkt über
die Lücke hinweg verbinden. Leere Spalten können ausserdem bedeuten, dass ein
Parameter an einer Station gar nicht gemessen wird.

## Qualität und Umgang mit Korrekturen

Bodenmessdaten sind bei der ersten Veröffentlichung noch nicht vollständig
qualitätsgesichert. MeteoSchweiz prüft sie in einem rollenden Zeitraum von fünf
Tagen automatisch und manuell; manuell geprüfte Daten werden in der Regel nach
fünf Tagen publiziert. Tägliche und monatliche Niederschlagswerte bilden eine
Ausnahme und werden erst gegen Ende des Folgemonats manuell geprüft
([MeteoSchweiz-FAQ zur Qualitätskontrolle](https://opendatadocs.meteoswiss.ch/de/general/faq#what-about-the-quality-control-of-data)).

Für die Anwendung folgt daraus:

1. Für abgeschlossene historische Jahre wird die jährlich erneuerte
   `historical`-Datei verwendet.
2. Daten des laufenden Jahres werden aus `recent` geladen, aber für
   Niederschlag erst nach Ende des Folgemonats als abschliessend kontrolliert
   behandelt.
3. Bereits gespeicherte Daten müssen durch neuere amtliche Dateien ersetzbar
   sein, damit nachträgliche Korrekturen ankommen.
4. In den am 8. September 2026 geprüften CHZ-Tages-CSV-Dateien ist keine eigene
   Spalte für Qualitätsflags enthalten. Die Anwendung kann daher den
   Kontrollstatus nicht je Einzelwert anzeigen, sondern nur aus Dateityp und
   Alter ableiten.

MeteoSchweiz beschreibt ausserdem Vollständigkeits- und Plausibilitätsprüfungen
sowie automatische und manuelle Interpolation. Diese Bearbeitungen werden
intern mit Mutationsinformationen gekennzeichnet
([MeteoSchweiz: Datenaufbereitung](https://www.meteoswiss.admin.ch/wetter/messsysteme/datenmanagement/datenaufbereitung.html));
diese Informationen sind in der untersuchten öffentlichen Tagesdatei jedoch
nicht als Spalten enthalten.

Die CHZ-Reihe ist eine Stationsmessreihe und **nicht homogenisiert**.
Stationsverschiebungen, Instrumentenwechsel oder veränderte Umgebung können
langfristige Vergleiche beeinflussen. MeteoSchweiz empfiehlt für Aussagen über
langfristige klimatische Entwicklungen homogene Reihen. Das Dashboard soll
deshalb historische Einzeljahre vergleichen, aber aus CHZ-Rohwerten keine
unbelegte Aussage über einen Klimatrend ableiten.

## Lizenz und Nutzungsbedingungen

MeteoSchweiz veröffentlicht die Open Data unter **CC BY 4.0**. Teilen,
Bearbeiten und auch kommerzielle Nutzung sind erlaubt. Bei Wiedergabe oder
Weiterverbreitung ist die Angabe **„Quelle: MeteoSchweiz“** erforderlich.
MeteoSchweiz schliesst Gewähr für Richtigkeit, Genauigkeit, Aktualität,
Zuverlässigkeit und Vollständigkeit aus. Unverhältnismässige Zugriffe oder das
hochfrequente erneute Herunterladen derselben Dateien sind untersagt
([vollständige Nutzungsbedingungen](https://opendatadocs.meteoswiss.ch/de/general/terms-of-use)).

Das Dashboard sollte daher die Quellenangabe sichtbar führen und Dateien lokal
zwischenspeichern beziehungsweise per ETag nur bei Änderungen erneut laden.

## Relevante amtliche Alternativen

### Homogene Klimareihen (Swiss NBCN)

Homogene Reihen korrigieren Einflüsse etwa durch Stationsverschiebungen oder
Instrumentenwechsel und sind für langfristige Klimaentwicklungen die bessere
Quelle. Der nächste NBCN-Standort zum verwendeten Zug-Referenzpunkt ist nach
derselben Distanzberechnung Luzern (LUZ), rund 21,0 km entfernt. Das
NBCN-Inventar bietet dort ein homogenes Tagesmaximum `ths200dx` ab 1886, aber
den homogenen Niederschlag nur monatlich und jährlich. Damit erfüllt dieses
Angebot den ersten Use-Case mit **beiden Indikatoren auf Tagesebene an einem
nahen gemeinsamen Standort nicht**
([MeteoSchweiz-Dokumentation: homogene Klimareihen](https://opendatadocs.meteoswiss.ch/de/c-climate-data/c1-climate-stations_homogeneous),
[NBCN-Dateninventar](https://data.geo.admin.ch/ch.meteoschweiz.ogd-nbcn/ogd-nbcn_meta_datainventory.csv)).

### Räumliche Klimaanalysen auf 1-km-Raster

Die amtlichen räumlichen Klimaanalysen enthalten täglichen Niederschlag sowie
tägliche Mittel-, Minimal- und Maximaltemperatur auf einem 1-km-Raster für die
ganze Schweiz. Sie könnten einen Wert näher am eigentlichen Veranstaltungsort
liefern und sind deshalb für eine spätere freie Ortswahl attraktiv. Es sind
jedoch statistisch aus Stations-, Radar- und Satellitendaten geschätzte
„Pseudo-Beobachtungen“ und keine direkte Punktmessung; die Dateien sind NetCDF
und die Wahl eines Rasterpixels bringt zusätzliche fachliche und technische
Schritte mit sich. Für den bewusst einfachen ersten Meilenstein ist das weniger
geeignet, sollte aber als spätere Ausbaustufe erhalten bleiben
([MeteoSchweiz-Dokumentation: räumliche Klimaanalysen](https://opendatadocs.meteoswiss.ch/de/c-climate-data/c3-ground-based-climate-data)).

## Bestätigter Umgang mit dem Temperaturintervall

Das amtliche Tagesmaximum `tre200dx` wird unverändert übernommen und nicht aus
feiner aufgelösten Messwerten neu berechnet. Die abweichenden amtlichen
Beschreibungen der Tagesaggregation vor und ab 2018 bleiben als Einschränkung
der Datenquelle dokumentiert.

Der Vergleichszeitraum wurde inzwischen fachlich festgelegt: Es werden stets
so viele Daten wie für die gewählte Station und die ausgewählten Indikatoren
verfügbar verwendet. Für CHZ und die ersten beiden Indikatoren ist 1993 der
früheste gemeinsame Beginn. Neuere Werte aus `recent` können einbezogen werden,
sobald die ausgewählten Kalendertage vorliegen; ihr Qualitätsstand bleibt
sichtbar.

## Übertragung auf weitere Orte und Stationen

Für einen neuen Auswertungsort wird die Zug/Cham-Zuordnung nicht kopiert,
sondern derselbe transparente Prüfprozess wiederholt:

1. mögliche amtliche Stationen mit Koordinaten, Höhe und Exposition ermitteln;
2. die gewählte Stationszuordnung und ihren räumlichen Bezug offenlegen;
3. das amtliche Dateninventar je Indikator und Zeitauflösung prüfen;
4. den maximal nutzbaren Zeitraum für die konkrete Auswahl bestimmen;
5. fehlende Werte und kurze Reihen sichtbar machen.

Die blosse Nähe einer Station garantiert keine Repräsentativität für das lokale
Gelände. Ebenso darf der allgemeine Stationsbeginn nicht als Datenbeginn jedes
Parameters verstanden werden. Ein fachlich sinnvoller Indikator bleibt Teil
des allgemeinen Katalogs, wenn er an einer konkreten Station fehlt; dort wird
er als nicht verfügbar ausgewiesen oder durch eine andere geeignete amtliche
Datenquelle ergänzt.
