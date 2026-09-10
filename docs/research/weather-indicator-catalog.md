# Stationsunabhängiger Katalog von Wetterindikatoren für ein Outdoor- und Schwimmfest

Stand: 10. September 2026

## Fragestellung

Welche amtlichen Wetterindikatoren eignen sich, um historische Tage oder
Zeitfenster im Hinblick auf ein Outdoor- und Schwimmfest zu beurteilen?

Der Katalog ist bewusst **nicht auf einen bestimmten Ort oder eine bestimmte
Station zugeschnitten**. Ein Parameter kann an einer Station über Jahrzehnte,
an einer anderen erst seit kurzer Zeit oder überhaupt nicht verfügbar sein.
MeteoSchweiz veröffentlicht deshalb neben dem
[Parameterkatalog](https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/ogd-smn_meta_parameters.csv)
ein
[Dateninventar](https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/ogd-smn_meta_datainventory.csv)
mit Start- und Enddatum jeder Kombination aus Station und Parameter. Die
Anwendung muss die tatsächlich verfügbare Kombination prüfen und den
Vergleichszeitraum dynamisch bestimmen.

## Datengrundlage und zeitliche Bedeutung

Das automatische Messnetz SwissMetNet umfasst laut MeteoSchweiz rund 160
Stationen und misst Temperatur, Niederschlag, Wind, Sonnenschein,
Luftfeuchtigkeit, Strahlung und Luftdruck. Stationsdateien werden unter anderem
als Stunden- (`h`) und Tageswerte (`d`) angeboten. MeteoSchweiz empfiehlt,
amtlich aggregierte Stunden- und Tagesdaten zu verwenden und diese nicht selbst
aus 10-Minuten-Werten nachzubilden. Historische Korrekturen können nur in den
höheren Aggregationsstufen enthalten sein. Quellen:
[automatische Wetterstationen](https://opendatadocs.meteoswiss.ch/de/a-data-groundbased/a1-automatic-weather-stations),
[Datengranularität und Zeitintervalle](https://opendatadocs.meteoswiss.ch/de/general/download#data-granularity).

Alle Zeitstempel beziehen sich auf UTC. Bei Stundenwerten bezeichnet der
Zeitstempel das Ende des Intervalls, bei Tageswerten den Beginn des Tages.
Stundenwerte vor 2018 wurden nach einem anderen, am SYNOP-Takt orientierten
Zeitfenster berechnet als heutige Stundenwerte. Das muss bei fein aufgelösten
Langzeitvergleichen als methodischer Bruch erkennbar sein. Fehlende Werte sind
in den CSV-Dateien leere Felder und dürfen in Diagrammen nicht stillschweigend
überbrückt werden. Quelle:
[Darstellung von Zeitintervallen und fehlenden Werten](https://opendatadocs.meteoswiss.ch/de/general/download#how-datetime-time-intervals-and-missing-values-are-represented).

## Tagesindikatoren

### Hohe Aussagekraft für Festwetter

| Kennung | Amtliche Bedeutung | Einheit | Nutzen für ein Fest | Grenze der Aussage |
| --- | --- | --- | --- | --- |
| `rka150d0` | Niederschlag; Tagessumme 0 UTC bis 0 UTC | mm | Direkter Hinweis, ob ein Tag trocken oder nass war; für den Vergleich gleicher Kalendertage gut verständlich. | Der UTC-Tag stimmt im Sommer nicht mit dem lokalen Kalendertag überein. Der Wert zeigt nicht, ob es während der Feststunden, nachts oder nur kurz stark regnete. |
| `tre200dx` | Lufttemperatur 2 m über Boden; Tagesmaximum | °C | Zeigt, ob ein Tag warm genug oder möglicherweise sehr heiss war. | Eine kurze Spitze beschreibt nicht die Temperatur während des ganzen Festes. |
| `tre200d0` | Lufttemperatur 2 m über Boden; Tagesmittel | °C | Robuster Überblick über das Temperaturniveau des Tages. | Kann einen kühlen Vormittag und heissen Nachmittag zu einem unauffälligen Mittelwert vermischen. |
| `sre000d0` | Sonnenscheindauer; Tagessumme | min | Sehr anschauliches Merkmal für sonniges, freundlich wahrgenommenes Wetter. | Die mögliche Tageslänge ändert sich mit Datum und Ort; die Uhrzeit des Sonnenscheins bleibt unbekannt. |
| `sremaxdv` | Sonnenscheindauer relativ zur absolut möglichen Tagessumme | % | Erleichtert Vergleiche zwischen Jahreszeiten und Orten mit unterschiedlicher möglicher Sonnenscheindauer. | Gibt ebenfalls nicht an, wann die Sonne schien; nicht an jeder Station verfügbar. |
| `fu3010d1` | Böenspitze (Sekundenböe); Tagesmaximum | km/h | Sicherheitsrelevant für Zelte, Sonnenschirme, Dekoration und lose Gegenstände. | Eine einzelne Spitze sagt wenig über Dauer und Zeitpunkt des Windes aus. |
| `fu3010d0` | Windgeschwindigkeit skalar; Tagesmittel | km/h | Zeigt, ob es über längere Zeit windig und dadurch unangenehm war. | Kurze gefährliche Böen können im Mittelwert verschwinden; daher zusammen mit `fu3010d1` betrachten. |
| `ure200d0` | Relative Luftfeuchtigkeit 2 m über Boden; Tagesmittel | % | Ergänzt die Temperatur und hilft, schwüle oder feucht-kühle Tage einzuordnen. | Relative Feuchte hängt stark von der Temperatur ab; allein ist sie kein eindeutiges Komfortmass. |
| `gre000d0` | Globalstrahlung; Tagesmittel | W/m² | Physikalisches Mass für die am Boden eintreffende kurzwellige Strahlung; ergänzt Sonnenscheindauer auch bei wechselnder Bewölkung. | Weniger intuitiv als Sonnenminuten und **kein UV-Index**. |

Für Wind gibt es gleichwertige Kennungen in m/s (`fkl010d0` für das
Tagesmittel und `fkl010d1` für die maximale Sekundenböe). Die Anwendung sollte
eine einheitliche Anzeigeeinheit wählen und nicht Messreihen mit verschiedenen
Einheiten vermischen. Sämtliche amtlichen Bezeichnungen und Einheiten stammen
aus dem
[MeteoSchweiz-Parameterkatalog](https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/ogd-smn_meta_parameters.csv).

### Ergänzend oder nur für bestimmte Fragestellungen

| Kennung | Amtliche Bedeutung | Einheit | Möglicher Nutzen | Grenze der Aussage |
| --- | --- | --- | --- | --- |
| `tre200dn` | Lufttemperatur 2 m über Boden; Tagesminimum | °C | Relevant für frühen Aufbau und späten Abbau. | Für die üblichen Feststunden oft weniger aussagekräftig als Stundenwerte. |
| `dkl010d0` | Windrichtung; Tagesmittel | ° | Nützlich, wenn Exposition, Schutzbauten oder Ausrichtung des Geländes bekannt sind. | Ohne lokale Geländekenntnis kaum als „gut“ oder „schlecht“ bewertbar; wechselnde Richtungen werden stark vereinfacht. |
| `pva200d0` | Dampfdruck 2 m über Boden; Tagesmittel | hPa | Ergänzende physikalische Feuchtegrösse. | Für Besucher weniger verständlich als relative Feuchte oder Taupunkt. |
| `erefaod0` | Referenzverdunstung nach FAO; Tagessumme | mm/d | Kann trocknende Bedingungen und Wasserverlust beschreiben. | Für Festkomfort nur indirekt und nicht als einzelnes Qualitätsmerkmal geeignet. |
| `prestad0`, `pp0qffd0`, `pp0qnhd0` | verschiedene Tagesmittel des Luftdrucks | hPa | Können Wetterlagen meteorologisch einordnen. | Sagen kaum direkt aus, ob ein Festtag angenehm, trocken oder sicher war. |

Strahlungsgrössen wie Diffusstrahlung (`ods000d0`), langwellige Ein- und
Ausstrahlung (`oli000d0`, `olo000d0`) oder reflektierte kurzwellige Strahlung
(`osr000d0`) sind amtlich verfügbar, aber für ein allgemein verständliches
Festwetter-Dashboard zu spezialisiert. Boden- und bodennahe Temperaturen,
Schneehöhe, Heiz- und Kühlgradzahlen sowie der Föhnindex sind nur bei besonderen
Orts-, Saison- oder Betriebsfragen sinnvoll. Sie sollten den Kernkatalog nicht
überladen.

### Zwei verschiedene amtliche Niederschlagstage

Neben `rka150d0` führt der Katalog `rre150d0` als Tagessumme von 6 UTC bis
6 UTC des Folgetags. Diese beiden Werte beziehen sich nicht auf dasselbe
Zeitfenster und dürfen nicht ohne Kennzeichnung ausgetauscht oder gemeinsam als
einheitliche Tagesreihe behandelt werden. Für jede Darstellung muss das
Messintervall sichtbar sein.

## Stundenindikatoren

Stundenwerte sind für ein Fest häufig aussagekräftiger als Tageswerte, weil ein
konkretes lokales Veranstaltungsfenster untersucht werden kann. Beispielsweise
ist Regen in der Nacht anders zu bewerten als Regen während des Wettkampfs.

| Kennung | Amtliche Bedeutung | Einheit | Nutzen für ein Fest | Grenze der Aussage |
| --- | --- | --- | --- | --- |
| `rre150h0` | Niederschlag; Stundensumme | mm | Zeigt Zeitpunkt, Dauer und Intensität des Regens innerhalb der Festzeit. Daraus lassen sich Festzeit-Summe, Zahl nasser Stunden und höchste Stundensumme ableiten. | Der Zeitstempel ist UTC und bezeichnet das Intervallende. Eine „nasse Stunde“ benötigt einen transparent festgelegten Schwellenwert. |
| `tre200h0` | Lufttemperatur 2 m über Boden; Stundenmittel | °C | Zeigt den erlebbaren Temperaturverlauf während Aufbau, Anlass und Abbau. | Innerhalb einer Stunde auftretende Extreme werden geglättet. |
| `tre200hn`, `tre200hx` | Lufttemperatur 2 m über Boden; Stundenminimum beziehungsweise Stundenmaximum | °C | Ergänzen den Stundenmittelwert um Hitze- oder Kältespitzen. | Für eine kompakte Übersicht nicht immer beide nötig. |
| `sre000h0` | Sonnenscheindauer; Stundensumme | min | Zeigt, ob die Sonne gerade während der Feststunden schien. | Stations- und parameterabhängige Verfügbarkeit; Schatten am konkreten Gelände wird nicht erfasst. |
| `gre000h0` | Globalstrahlung; Stundenmittel | W/m² | Beschreibt den Tagesgang der einfallenden Strahlung und ergänzt Sonnenminuten. | Kein UV-Index und für Laien erklärungsbedürftig. |
| `fu3010h0` | Windgeschwindigkeit skalar; Stundenmittel | km/h | Zeigt anhaltenden Wind während der relevanten Stunden. | Muss mit Böenspitzen kombiniert werden. |
| `fu3010h1` | Böenspitze (Sekundenböe); Stundenmaximum | km/h | Zeigt sicherheitsrelevante Windspitzen zeitlich wesentlich genauer als der Tageswert. | Eine Sekundenspitze beschreibt nicht die Dauer. |
| `dkl010h0` | Windrichtung; Stundenmittel | ° | Kann zusammen mit einem bekannten Geländeplan zeigen, wann Wind ungeschützt auf das Fest trifft. | Ohne lokale Exposition nur begrenzt interpretierbar. |
| `ure200h0` | Relative Luftfeuchtigkeit 2 m über Boden; Stundenmittel | % | Macht den Feuchteverlauf während heisser oder kühler Stunden sichtbar. | Temperaturabhängig und allein kein Komfortindex. |
| `tde200h0` | Taupunkt 2 m über Boden; Stundenmittel | °C | Physikalisch gut geeignete Ergänzung zur Beurteilung feuchter oder schwüler Luft. | Für viele Nutzer weniger geläufig; Komfortgrenzen wären eine eigene fachliche Festlegung und kein amtlicher Messwert. |

Auch bei Stundenwind existieren parallele Kennungen in m/s
(`fkl010h0`, `fkl010h1`). Die amtlichen Bedeutungen und Einheiten stehen im
[Parameterkatalog](https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/ogd-smn_meta_parameters.csv).

### Sinnvolle abgeleitete Festzeit-Kennzahlen

Aus den amtlichen Stundenwerten können für ein klar angegebenes lokales
Zeitfenster zusätzliche Kennzahlen berechnet werden:

- Niederschlagssumme während der Festzeit aus `rre150h0`
- Anzahl Stunden mit messbarem Niederschlag; der Schwellenwert muss sichtbar
  und konfigurierbar sein
- höchste Stundensumme des Niederschlags innerhalb der Festzeit
- kälteste, mittlere und wärmste Temperatur während der Festzeit
- Sonnenminuten während der Festzeit
- mittlerer Wind und stärkste Böe während der Festzeit
- Anteil der Feststunden, in denen zuvor definierte günstige Bedingungen
  gleichzeitig erfüllt waren

Diese Werte sind **abgeleitete Kennzahlen der Anwendung**, keine zusätzlichen
amtlichen MeteoSchweiz-Parameter. Sobald Schwellen oder günstige Bedingungen
festgelegt werden, entsteht daraus zusätzlich eine Bewertung der Anwendung.
Zeitzone, Sommerzeit, Schwellenwerte und Umgang mit unvollständigen Stunden
müssen nachvollziehbar dokumentiert werden.

## Verfügbarkeit darf die fachliche Auswahl nicht vorwegnehmen

Ein fachlich guter Indikator bleibt Teil des Katalogs, auch wenn er an einer
zuerst betrachteten Station fehlt oder nur eine kurze Reihe besitzt. Das gilt
insbesondere für Sonnenscheindauer, relative Sonnenscheindauer,
Globalstrahlung, Taupunkt und einzelne Windparameter.

Für jede konkrete Auswertung sollte die Anwendung daher:

1. die nächstgelegenen oder fachlich repräsentativen Stationen ermitteln,
2. im Dateninventar die Verfügbarkeit jedes gewünschten Parameters prüfen,
3. Stationsname, Distanz beziehungsweise räumlichen Bezug sowie Messhöhe zeigen,
4. pro Parameter den tatsächlich verfügbaren Zeitraum und Lücken ausweisen,
5. nicht automatisch alle Diagramme auf den kleinsten gemeinsamen Zeitraum
   beschneiden, wenn eine getrennte Darstellung mehr Information bewahrt,
6. einen Stationswechsel oder den Verzicht auf einen Parameter transparent
   machen.

Die Existenz einer Kennung im Parameterkatalog bedeutet ausdrücklich nicht,
dass sie an jeder Station gemessen wird. Quelle:
[Metadaten und Dateninventar der automatischen Wetterstationen](https://opendatadocs.meteoswiss.ch/de/a-data-groundbased/a1-automatic-weather-stations#metadaten).

## Wichtige Aspekte ausserhalb der normalen Stationsparameter

### Räumliche Klimaanalysen als mögliche Ergänzung

Fehlt ein fachlich wichtiger Stationsparameter am gewünschten Ort, kann später
eine räumliche Klimaanalyse eine Alternative sein. MeteoSchweiz bietet für die
gesamte Schweiz 1-km-Raster mit täglichen Analysen von Niederschlag,
Minimal-, Mittel- und Maximaltemperatur sowie relativer Sonnenscheindauer an.
Die tägliche relative Sonnenscheindauer trägt die Produktkennung `SrelD`, wird
in Prozent angegeben und reicht laut aktueller Produktdokumentation von 1971
bis heute.

Diese Werte sind statistisch aus Stationen, Satelliten und Radar geschätzte
**Pseudo-Beobachtungen** für ein Rasterpixel, keine Messung einer einzelnen
Station. Sie dürfen deshalb nicht unmarkiert mit Stationswerten zu einer
scheinbar einheitlichen Messreihe verbunden werden. Quellen:
[räumliche Klimaanalysen für Niederschlag, Temperatur und Sonnenschein](https://opendatadocs.meteoswiss.ch/de/c-climate-data/c3-ground-based-climate-data),
[Produktdokumentation `SrelD`](https://www.meteoswiss.admin.ch/dam/jcr:981891db-30d1-47cc-a2e1-50c270bdaf22/ProdDoc_SrelD.pdf).

Weitere räumliche Produkte zu Sonneneinstrahlung, Strahlungsbilanz und
Wolkenbedeckung werden aus Meteosat- und Bodenmessungen abgeleitet und als
Stunden- und Tagesdaten angeboten. Das aktuell kontrollierte Open-Data-Archiv
beginnt dort mit 2025; ältere Archivdaten sollen schrittweise ergänzt werden.
Diese Produkte sind daher fachlich interessant, zurzeit aber noch kein
gleichwertiger Ersatz für jede lange historische Stationsreihe. Quelle:
[räumliche Klimaanalysen für Strahlung und Wolken](https://opendatadocs.meteoswiss.ch/de/c-climate-data/c4-satellite-based-climate-data).

### Gewitter, Blitz und amtliche Warnungen

Ein Gewitter ist für ein Schwimmfest sicherheitskritisch, lässt sich aber nicht
aus einem einzelnen Tages- oder Stundenparameter der normalen Stationsdatei
zuverlässig ablesen. MeteoSchweiz nennt Blitz, Starkregen, Hagel und extreme
Böen als mögliche Gewittergefahren. Gewitter sind stark lokal und kurzfristig;
lokale Warnungen werden deshalb im Nowcasting erst nach Bildung einer Zelle mit
kurzer Vorlaufzeit herausgegeben. Für den Betrieb eines konkreten Fests gehören
aktuelle amtliche Warnungen somit in einen separaten Sicherheitsprozess, nicht
in einen historischen Stationsindikator. Quellen:
[Gefahrenstufen für Gewitter](https://www.meteoswiss.admin.ch/weather/hazards/explanation-of-the-danger-levels/thunderstorms.html),
[Gewitterwarnungen](https://www.meteoswiss.admin.ch/weather/weather-and-climate-from-a-to-z/thunderstorms/thunderstorm-warnings.html).

### Flächenhafter Niederschlag und Hagel

Stationsmessungen gelten für einen Messpunkt. Für kleinräumigen Niederschlag
und Hagel bietet MeteoSchweiz gesonderte Radarprodukte an. CombiPrecip verbindet
Radar- mit Stationsdaten und liefert stündliche Niederschlagssummen auf einem
Raster; die analysierte Fassung wird acht Tage später nachkorrigiert. Hagel wird
als `POH` (Hagelwahrscheinlichkeit beliebiger Grösse, %) und `MESHS`
(geschätzte maximale Grösse von starkem Hagel über 2 cm, mm) angeboten. Beide
Hagelprodukte werden nur vom 1. April bis 30. September berechnet. Diese
Produkte haben eigene Formate, räumliche Raster und Archive und sollten als
eigene Datenquelle modelliert werden.
Quellen:
[Niederschlags-Radarprodukte](https://opendatadocs.meteoswiss.ch/de/d-radar-data/d1-precipitation-radar-products),
[Hagel-Radarprodukte](https://opendatadocs.meteoswiss.ch/de/d-radar-data/d3-hail-radar-products),
[radarbasierte Hagel-Klimatologie](https://opendatadocs.meteoswiss.ch/de/c-climate-data/c5-radar-based-climate-data).

### UV-Index

Globalstrahlung ist nicht mit UV-Belastung gleichzusetzen. MeteoSchweiz
berechnet einen täglichen UV-Index als Vorhersage aus einem Strahlungsmodell
unter Einbezug der Bewölkung; er bezieht sich auf die maximale Intensität etwa
zwischen 11 und 15 Uhr und dient dem Gesundheitsschutz. Er ist deshalb für die
operative Festplanung sinnvoll, aber kein gewöhnlicher historischer
SwissMetNet-Tages- oder Stundenparameter. Quelle:
[UV-Index von MeteoSchweiz](https://www.meteoswiss.admin.ch/weather/weather-and-climate-from-a-to-z/uv-index.html).

### Wassertemperatur

Für ein Schwimmfest ist die Wassertemperatur fachlich wichtig, sie stammt aber
nicht aus den automatischen Wetterstationsdateien von MeteoSchweiz. Das
Bundesamt für Umwelt misst die Wassertemperatur an Flüssen und ausgewählten Seen
in einem eigenen hydrologischen Messnetz. Eine spätere Einbindung braucht daher
eine zweite Stationszuordnung, eine eigene Verfügbarkeitsprüfung und eine klare
Quellenangabe. Quelle:
[Wassertemperatur der Flüsse und Seen beim BAFU](https://www.hydrodaten.admin.ch/de/seen-und-fluesse/messstationen-temperatur).

## Fachliche Empfehlung für die weitere Produktentwicklung

Eine stationsunabhängige erste Erweiterung sollte nicht einfach möglichst viele
Spalten anzeigen, sondern zwei Ebenen anbieten:

1. **Tagesvergleich:** Niederschlag, Tagesmaximum und Tagesmittel der
   Temperatur, Sonnenscheindauer, relative Sonnenscheindauer,
   Globalstrahlung, mittlerer Wind, Böenspitze und relative Luftfeuchtigkeit.
2. **Festzeit-Verlauf:** stündlicher Niederschlag, Temperatur, Sonnenschein,
   Globalstrahlung, mittlerer Wind, Böenspitze, Luftfeuchtigkeit und Taupunkt.

Die Anwendung sollte gute Parameter auch dann nennen, wenn sie am gewählten Ort
nicht verfügbar sind, und die Einschränkung verständlich anzeigen. Eine spätere
Gesamtbewertung wie „gutes Festwetter“ darf erst aus transparenten,
veränderbaren Regeln entstehen. Sie darf nicht als amtlicher Wetterwert
erscheinen und sicherheitskritische Warnungen nicht ersetzen.
