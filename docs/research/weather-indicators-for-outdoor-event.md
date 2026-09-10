# Recherche: Wetterindikatoren für ein Schwimmfest

Stand: 10. September 2026

## Kurzempfehlung

Für die Frage, ob ein Tag aus Sicht eines Schwimmfests „gutes Wetter“ hatte,
sollten mehrere **amtliche Messwerte getrennt sichtbar** bleiben. MeteoSchweiz
liefert die Beobachtungen; die Beurteilung „gut“ oder „schlecht“ ist dagegen
eine Produktbewertung und kein amtlicher Messwert.

Zusätzlich zu den bereits verwendeten Grössen Niederschlag (`rka150d0`) und
Höchsttemperatur (`tre200dx`) sind für Cham vor allem sinnvoll:

1. **Tagesmitteltemperatur `tre200d0`**: ergänzt die kurze Temperaturspitze um
   das Temperaturniveau des ganzen Tages;
2. **maximale Sekundenböe `fu3010d1`**: zeigt windbedingte Risiken etwa für
   Zelte, Sonnenschirme und leichte Gegenstände;
3. **mittlere Windgeschwindigkeit `fkl010d0`**: beschreibt, ob es über den Tag
   hinweg anhaltend windig war;
4. **mittlere relative Luftfeuchtigkeit `ure200d0`**: ergänzt die Temperatur
   um einen groben Hinweis auf Schwüle beziehungsweise feucht-kühles Empfinden.

Alle vier reichen an der Station Cham ungefähr gleich weit zurück wie die
bisherigen Indikatoren. Sonnenscheindauer wäre für Menschen besonders
verständlich, ist in Cham aber erst ab Oktober 2022 vorhanden und deshalb für
den historischen Vergleich 1993–2026 vorerst ungeeignet. Globalstrahlung ist
ab Juli 2014 verfügbar und kann als ergänzender Helligkeits-/Strahlungshinweis
dienen, ist aber weniger anschaulich als Sonnenminuten.

Die tatsächlichen CHZ-Dateien enthalten für alle 68 frühen und späten
Kandidatentage von 1993 bis 2026 Werte für Tagesmitteltemperatur, relative
Luftfeuchtigkeit, mittleren Wind und maximale Sekundenböe. Diese Ergänzungen
würden den bestehenden Vergleich aktuell weder verkürzen noch Lücken einführen.

## Amtliche Datengrundlage

Die Untersuchung verwendet ausschliesslich das Angebot „Automatische
Wetterstationen – Messwerte“ von MeteoSchweiz:

- [amtlicher Parameterkatalog](https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/ogd-smn_meta_parameters.csv)
- [amtliches Dateninventar je Station und Parameter](https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/ogd-smn_meta_datainventory.csv)
- [historische CHZ-Tageswerte](https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/chz/ogd-smn_chz_d_historical.csv)
- [CHZ-Tageswerte des laufenden Jahres](https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/chz/ogd-smn_chz_d_recent.csv)

Der Parameterkatalog erklärt für jede Kennung Bedeutung, Granularität und
Einheit ([Katalogbeschreibung auf opendata.swiss](https://opendata.swiss/de/dataset/automatische-wetterstationen-messwerte/resource/b0ff8b49-06e4-41e0-a6b1-6a4daa87b53a)).
MeteoSchweiz empfiehlt für Tagesauswertungen die amtlich aggregierten
Tageswerte
([Dokumentation der automatischen Wetterstationen](https://opendatadocs.meteoswiss.ch/de/a-data-groundbased/a1-automatic-weather-stations)).

Die unten genannten Startdaten stammen aus dem amtlichen Dateninventar und
wurden gegen die tatsächlich gefüllten Spalten der beiden CHZ-Tagesdateien
geprüft. Leere Einzelwerte bleiben mögliche Messlücken. Der allgemeine
Stationsbeginn ist deshalb nicht mit der Verfügbarkeit eines bestimmten
Parameters gleichzusetzen.

## Besonders hilfreiche Indikatoren

| Kennung | Amtliche Bedeutung | Einheit | CHZ seit | Nutzen und Grenze für das Fest |
| --- | --- | --- | --- | --- |
| `rka150d0` | Niederschlag; Tagessumme 00:00–00:00 UTC | mm | 11.06.1993 | Direkter Hinweis auf Regen. Eine Tagessumme zeigt aber weder Zeitpunkt noch Dauer; im August entspricht das Fenster ungefähr 02:00–02:00 Uhr lokaler Zeit. |
| `tre200dx` | Lufttemperatur 2 m über Boden; Tagesmaximum | °C | 11.06.1993 | Zeigt, ob der Tag überhaupt warm oder sehr heiss wurde. Eine kurze Spitze sagt wenig über den ganzen Veranstaltungszeitraum. |
| `tre200d0` | Lufttemperatur 2 m über Boden; Tagesmittel | °C | 11.06.1993 | Beschreibt das Temperaturniveau stabiler als das Maximum, schliesst aber Nachtstunden ein. |
| `fu3010d1` | Böenspitze (Sekundenböe); Tagesmaximum | km/h | 11.06.1993 | Wichtig für Sicherheit und Komfort bei Zelten, Sonnenschirmen und leichten Gegenständen. Der Tageshöchstwert kann ausserhalb der Festzeit aufgetreten sein. |
| `fkl010d0` | skalare Windgeschwindigkeit; Tagesmittel | m/s | 11.06.1993 | Zeigt anhaltenden Wind. Die Einheit m/s ist für viele Nutzer weniger eingängig als km/h. |

Für das nächste kleine Produktinkrement wären `tre200d0`, `fu3010d1` und
`fkl010d0` die stärkste Ergänzung: Sie sind für die Veranstaltung relevant und
verkürzen die historische Zeitreihe nicht. Für eine leicht verständliche
Oberfläche könnte eine Umrechnung von m/s in km/h angezeigt werden; diese wäre
dann klar als von der Anwendung umgerechneter Wert zu kennzeichnen.

## Hilfreiche Ergänzungen mit Einschränkungen

| Kennung | Amtliche Bedeutung | Einheit | CHZ seit | Einordnung |
| --- | --- | --- | --- | --- |
| `ure200d0` | relative Luftfeuchtigkeit 2 m über Boden; Tagesmittel | % | 11.06.1993 | Unterstützt die Komfortbeurteilung. Der Mittelwert verdeckt aber besonders schwüle Stunden; zusammen mit Temperatur interpretieren. |
| `tre200dn` | Lufttemperatur 2 m über Boden; Tagesminimum | °C | 11.06.1993 | Relevant für frühen Aufbau oder späten Abbau, für ein Fest am Nachmittag meist weniger wichtig. |
| `dkl010d0` | Windrichtung; Tagesmittel | Grad | 11.06.1993 | Kann bei bekannter Ausrichtung des Festgeländes helfen. Ohne Gelände- und Infrastrukturbezug wenig aussagekräftig. |
| `gre000d0` | Globalstrahlung; Tagesmittel | W/m² | 01.07.2014 | Objektiver Hinweis auf ein helles/strahlungsreiches Tagesbild. Nur rund zwölf Jahre Abdeckung und für Laien weniger intuitiv. |
| `sre000d0` | Sonnenscheindauer; Tagessumme | min | 04.10.2022 | Sehr anschaulich für „sonnig“, aber für einen langen historischen Vergleich in Cham noch viel zu kurz. |
| `sremaxdv` | Sonnenscheindauer relativ zur absolut möglichen Tagessumme | % | 04.10.2022 | Erleichtert Vergleiche über Jahreszeiten, hat aber dieselbe kurze CHZ-Abdeckung. |

Sonnenscheindauer ist fachlich attraktiv, sollte im Dashboard aber erst als
zusätzliche Kurzzeitansicht angeboten werden. Eine Linie ab 2022 neben Reihen
ab 1993 könnte sonst fälschlich gleich belastbar wirken.

## Eher wenig hilfreiche Tagesindikatoren

Diese Parameter sind in den CHZ-Tagesdateien tatsächlich befüllt, beantworten
die Festwetterfrage aber nur indirekt oder redundant:

| Gruppe / Kennungen | Amtliche Bedeutung und Abdeckung | Warum nachrangig |
| --- | --- | --- |
| `pva200d0` | Dampfdruck; Tagesmittel, seit 11.06.1993, mit deutlich mehr Lücken als die relative Feuchte | Fachlich brauchbar für Feuchte, aber schwerer verständlich als `ure200d0`. |
| `prestad0`, `pp0qffd0`, `pp0qnhd0` | verschiedene Tagesmittel des Luftdrucks; ab 1993, 1999 beziehungsweise 1996 | Luftdruck allein sagt Besuchern wenig über die erlebte Wetterqualität und ist keine Regenmessung. |
| `rre150d0` | Niederschlagssumme 06:00 UTC bis 06:00 UTC des Folgetags; seit 11.06.1993 | Amtlich korrekt, aber für denselben Kalendertag noch ungünstiger abgegrenzt als das bereits gewählte `rka150d0`. |
| `fu3010d0` | mittlerer Wind in km/h; seit 01.01.1996 | Verständliche Einheit, aber inhaltlich Duplikat von `fkl010d0` und drei Jahre kürzere Reihe. |
| `fkl010d3`, `fu3010d3` | maximale 3-Sekundenböe in m/s beziehungsweise km/h; seit 02.07.2014 | Ähnliche Aussage wie die Sekundenböe, jedoch wesentlich kürzere Abdeckung. |
| `erefaod0` | Referenzverdunstung nach FAO; Tagessumme; seit 01.07.2014 | Für Landwirtschaft/Wasserhaushalt nützlich, für Festbesucher sehr indirekt. |
| `rreetsd0` | Wassereintrag aus Wasserbilanz; Tagessumme; seit 04.10.2022 | Abgeleitete Wasserbilanzgrösse und sehr kurze Reihe; kein Ersatz für tatsächlich gemessenen Regen während des Fests. |
| `xcd000d0` | Kühlgradzahl; seit 01.07.2014 | Kennzahl für Kühlbedarf, nicht für Aufenthaltsqualität im Freien. |
| `xno000d0`, `xno012d0` | zwei Heizgradkennzahlen; seit 2014 beziehungsweise 1993 | Für Gebäudeenergie statt Sommerveranstaltungen gedacht. |
| `htoautd0` | automatische Schneehöhe um 06:00 UTC; seit 07.05.2024 | Für ein Schwimmfest im August praktisch ohne Nutzen. |

Mehrere weitere Spalten stehen zwar im allgemeinen Schema der CHZ-Tagesdatei,
sind dort aber komplett leer: Temperatur 5 cm über Gras, geopotentielle Höhen,
Föhnindex, vier einzelne Strahlungskomponenten und Bodentemperaturen. Solche
Schema-Spalten dürfen nicht als für Cham verfügbare Messreihen angeboten werden.

## Zeitbezug: Tageswert ist nicht gleich Festzeit

MeteoSchweiz bildet Tageswerte aus feiner aufgelösten Messungen. Die allgemeine
Aufbereitungsdokumentation nennt bis Ende 2017 als Tagesfenster 23:50 Uhr des
Vortags bis 23:40 Uhr des betreffenden Tages und ab 2018 00:10 Uhr bis 00:00 Uhr
des Folgetags; Niederschlagsparameter können ausdrücklich abweichende
Intervalle besitzen
([MeteoSchweiz: Datenaufbereitung](https://www.meteoschweiz.admin.ch/wetter/messsysteme/datenmanagement/datenaufbereitung.html)).
Die Referenzzeitstempel der OGD-Dateien sind UTC
([MeteoSchweiz: Zeitstempel und Intervalle](https://opendatadocs.meteoswiss.ch/de/general/download#how-datetime-time-intervals-and-missing-values-are-represented)).

Damit beantworten Tageswerte die Frage „Wie war dieser Tag insgesamt?“, aber
nicht zuverlässig „Regnete es zwischen 10 und 18 Uhr?“. Für Cham stehen jedoch
bereits seit Juni 1993 stündliche Werte für Niederschlag (`rre150h0`),
Temperatur (`tre200h0`, `tre200hx`), relative Luftfeuchtigkeit (`ure200h0`),
mittleren Wind (`fu3010h0`) und maximale Sekundenböen (`fu3010h1`) zur
Verfügung. Eine spätere Auswertung der eigentlichen Feststunden könnte damit
voraussichtlich denselben Zeitraum wie der Tagesvergleich abdecken.

Zusätzlich gibt es die zentralen 10-Minuten-Reihen ab Februar 2004. Sie wären
für kurze Schauer und Böen noch genauer, würden den historischen Zeitraum aber
auf rund 22 Jahre verkürzen. Sowohl Stunden- als auch 10-Minuten-Werte erhöhen
Datenmenge und Komplexität. Ausserdem müsste ein lokales Festzeitfenster wegen
der amtlichen UTC-Zeitstempel korrekt in UTC übersetzt werden.

## Wichtige Aspekte ausserhalb der CHZ-Tagesdatei

Einige für ein Schwimmfest wichtige Fragen sind keine weiteren einfachen
Tagesindikatoren dieser Station:

- **Gewitter, Blitz und Hagel:** Sie sind sicherheitsrelevant und können lokal
  auftreten, ohne dass eine Tagessumme allein das Ereignis angemessen
  beschreibt. MeteoSchweiz verwendet dafür Warnungen und Nowcasting aus Radar,
  Blitzmessungen und weiteren Quellen
  ([Gewitter-Gefahrenstufen](https://www.meteoswiss.admin.ch/weather/hazards/explanation-of-the-danger-levels/thunderstorms.html),
  [Nowcasting](https://www.meteoswiss.admin.ch/weather/warning-and-forecasting-systems/nowcasting.html)).
- **UV-Index:** Er ist für Sonnenschutz wichtig, aber Globalstrahlung ist kein
  UV-Index. MeteoSchweiz berechnet den UV-Index als tägliche Vorhersage aus
  einem Strahlungsmodell; direkte UV-Messungen gibt es nur an vier spezialisierten
  Stationen
  ([UV-Index](https://www.meteoswiss.admin.ch/weather/weather-and-climate-from-a-to-z/uv-index.html)).
- **Wassertemperatur:** Sie ist für ein Schwimmfest unmittelbar relevant, wird
  aber nicht von der Wetterstation Cham geliefert. Seen werden über eigene
  hydrologische Messungen und Modelle beobachtet
  ([MeteoSchweiz zur Wassertemperatur](https://www.meteoswiss.admin.ch/weather/weather-and-climate-from-a-to-z/water-temperature-the-example-of-lake-geneva.html)).

## Messwerte und Bewertung strikt trennen

MeteoSchweiz liefert für CHZ einzelne Mess- und abgeleitete Fachparameter,
aber keinen Indikator „gutes Schwimmfestwetter“. Auch ein von der Anwendung
berechneter Gesamtwert wäre von menschlichen Präferenzen abhängig, zum Beispiel:

- Ist leichter Regen bereits schlecht oder nur starker Regen?
- Welche Temperatur ist für Schwimmende, Helfende und Zuschauer angenehm?
- Wie viel Wind ist wegen Zelten oder Sonnenschirmen noch akzeptabel?
- Zählt Regen in der Nacht überhaupt, wenn das Fest tagsüber stattfindet?

Deshalb sollte die nächste Darstellung zunächst einzelne amtliche Grössen
vergleichbar machen. Falls später ein Gesamturteil gewünscht ist, sollten seine
Regeln und Schwellen gemeinsam festgelegt, transparent angezeigt und als
**Bewertung der Anwendung** bezeichnet werden. Es darf nicht wie ein weiterer
amtlicher MeteoSchweiz-Messwert erscheinen.

## Fazit für die Weiterentwicklung

Die robuste Reihenfolge für das Dashboard ist:

1. bestehende Niederschlagssumme und Höchsttemperatur beibehalten;
2. Tagesmitteltemperatur, maximale Sekundenböe und mittleren Wind ergänzen;
3. relative Luftfeuchtigkeit als Kontext anbieten;
4. Sonnenschein/Globalstrahlung nur mit klar sichtbarer kürzerer Abdeckung
   ergänzen;
5. später eine Auswertung der eigentlichen Feststunden mit den seit 1993
   verfügbaren Stundenwerten prüfen; 10-Minuten-Werte nur bei echtem Bedarf an
   höherer zeitlicher Genauigkeit ergänzen;
6. einen kombinierten „Festwetter-Score“ erst nach Festlegung verständlicher
   Nutzerregeln entwickeln.
