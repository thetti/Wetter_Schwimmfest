# Recherche: lokale Dashboard-Technik

Stand: 9. September 2026

## Empfehlung

Für den ersten Meilenstein sollte **Streamlit mit Plotly** verwendet werden.

Diese Kombination erfüllt die Anforderungen mit dem kleinsten technischen
Einstieg:

- Die Oberfläche wird vollständig in Python beschrieben; eine separate
  JavaScript-Anwendung ist nicht nötig.
- Auswahlfelder sind direkt vorhanden (st.selectbox, st.multiselect).
- Plotly liefert interaktive Linien, Legende, Zoom und Tooltips. Fehlende Werte
  können ausdrücklich als Lücken dargestellt werden.
- Streamlit bringt mit AppTest ein eigenes, leichtgewichtiges Testwerkzeug mit,
  das Eingaben und dargestellte Elemente ohne echten Browser simuliert.
- Die Anwendung läuft lokal im Browser und kann später unter anderem über
  Streamlit Community Cloud bereitgestellt werden. Community Cloud erkennt
  pyproject.toml ausdrücklich als Poetry-Abhängigkeitsdatei.

Dash ist ebenfalls fachlich geeignet, verlangt aber schon für einfache
Interaktionen explizite Komponenten-IDs und Callback-Verkabelung. Seine
End-to-End-Tests benötigen zudem Selenium und einen passenden WebDriver. Diese
zusätzlichen Konzepte bringen dem kleinen ersten Dashboard noch keinen
entscheidenden Vorteil.

## Geprüfte Systemvoraussetzungen

Das vorhandene System meldet:

| Bestandteil | Vorhanden | Bewertung |
| --- | --- | --- |
| Python | 3.13.3 | geeignet |
| Prozessor | Apple Silicon (arm64) | geeignet |
| macOS | 26.6.2 | geeignet |
| Poetry | 2.1.2 | geeignet |

Die aktuelle stabile Streamlit-Version ist laut PyPI **1.63.0**. Ihre
Paketmetadaten verlangen Python ab 3.10 und nennen Python 3.13 ausdrücklich als
unterstützte Version. Das Streamlit-Wheel ist plattformunabhängig
(py3-none-any). Auch wichtige binäre Abhängigkeiten bieten aktuelle Wheels für
CPython 3.13 auf macOS ARM64 an, beispielsweise
[PyArrow](https://pypi.org/project/pyarrow/) und
[NumPy](https://pypi.org/project/numpy/). Damit gibt es in den offiziellen
Paketmetadaten keinen erkennbaren Systemblocker
([Streamlit auf PyPI](https://pypi.org/project/streamlit/),
[offiziell unterstützte Python-Versionen](https://docs.streamlit.io/knowledge-base/using-streamlit/sanity-checks)).

Eine Installation im Projekt sollte trotzdem durch Poetry aufgelöst und danach
mit einem minimalen Start- und Darstellungstest bestätigt werden. Erst der
erzeugte Lockfile hält die konkrete, gemeinsam funktionierende Kombination
aller indirekten Abhängigkeiten fest.

## Streamlit mit Plotly

### Passung zu den Anforderungen

Streamlit macht aus einem normalen Python-Skript eine lokale Webanwendung. Der
offizielle Einstieg installiert ein Python-Paket und startet die Anwendung im
Browser mit dem Befehl „streamlit run“
([Installation](https://docs.streamlit.io/get-started/installation),
[Streamlit auf PyPI](https://pypi.org/project/streamlit/)).

Die benötigten Bedienelemente gehören zur Kern-API. Ein einzelner Indikator oder
Ort kann mit st.selectbox, eine spätere Auswahl mehrerer Tage oder Reihen mit
st.multiselect umgesetzt werden
([Widget-Übersicht](https://docs.streamlit.io/develop/api-reference/widgets),
[st.multiselect](https://docs.streamlit.io/develop/api-reference/widgets/st.multiselect)).

st.plotly_chart zeigt eine interaktive Plotly-Figur direkt in Streamlit an.
Plotly unterstützt mehrere Linien über eine Farbkategorie, Marker und
konfigurierbare Hover-Texte. Mit connectgaps=False bleiben None-/NaN-Werte als
sichtbare Lücke erhalten; dies entspricht dem fachlichen Anspruch des Projekts
([st.plotly_chart](https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart),
[Plotly-Liniendiagramme und Datenlücken](https://plotly.com/python/line-charts/),
[Plotly-Tooltips](https://plotly.com/python/hover-text-and-formatting/)).

Eine erste Umsetzung benötigt voraussichtlich nur diese direkten
Laufzeitabhängigkeiten:

- streamlit[charts] für Oberfläche und Diagrammintegration;
- die im Projekt verwendete Datenbibliothek, falls sie direkt importiert wird,
  zum Beispiel pandas.

Die Streamlit-Dokumentation nennt streamlit[charts] als Sammelinstallation für
Diagrammabhängigkeiten. Direkte Importe sollten trotzdem als direkte
Poetry-Abhängigkeiten festgehalten werden, damit das Projekt nicht versehentlich
von einer indirekten Abhängigkeit lebt.

### Einfaches Testen

streamlit.testing.v1.AppTest führt eine Seite ohne Browser aus, kann Widgets
setzen und sichtbare Elemente sowie Fehler prüfen. Es lässt sich direkt mit
pytest verwenden. Damit kann der erste Meilenstein beispielsweise prüfen, dass

- die Anwendung ohne Ausnahme startet,
- beide Kandidatentage auswählbar sind,
- der Indikatorwechsel funktioniert und
- eine Plotly-Figur ausgegeben wird.

Das ist weniger aufwendig als eine Browserautomatisierung
([Streamlit App Testing](https://docs.streamlit.io/develop/concepts/app-testing),
[AppTest-Referenz](https://docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest)).
Die eigentliche Kalenderlogik, Datenaufbereitung und Behandlung fehlender Werte
sollten unabhängig von Streamlit als normale Python-Funktionen mit pytest
getestet werden.

Eine Einschränkung: AppTest prüft die erzeugte Plotly-Figur, aber nicht jedes
Detail des tatsächlichen Browser-Renderings. Ein kurzer manueller Sichttest im
Browser bleibt deshalb für Diagramm, Tooltip und Lücken sinnvoll.

### Spätere Bereitstellung

Streamlit Community Cloud kann ein GitHub-Repository und dessen Einstiegsskript
direkt bereitstellen. In den erweiterten Einstellungen lässt sich die
Python-Version wählen. Die Plattform erkennt neben requirements.txt auch
pyproject.toml und ordnet es Poetry zu
([Bereitstellung](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy),
[Abhängigkeitsdateien](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies)).

Das ist eine **Möglichkeit, noch keine Entscheidung**. Die Cloud verlangt ein
GitHub-Repository und führt die App auf fremder Infrastruktur aus. Vor einer
Veröffentlichung müssen Zugriffsrechte, Kosten-/Nutzungsmodell und der Umgang
mit zwischengespeicherten Wetterdaten separat entschieden werden. Alternativ
kann Streamlit später containerisiert und bei einem anderen Anbieter betrieben
werden
([offizielle Docker-Anleitung](https://docs.streamlit.io/deploy/tutorials/docker)).

### Nachteile von Streamlit

- Bei einer Widget-Änderung wird das Python-Skript im normalen Modell erneut
  von oben ausgeführt. Teure Downloads müssen daher sauber getrennt und
  zwischengespeichert werden
  ([Streamlit-Grundkonzept](https://docs.streamlit.io/get-started/fundamentals/main-concepts)).
- Sehr individuelle Seitenlayouts und fein abgestimmte Interaktionsabläufe sind
  weniger flexibel als bei einem klassischen Webframework.
- Plotly wird für die hier geforderten kontrollierten Tooltips und Datenlücken
  benötigt; die einfachsten eingebauten Diagrammaufrufe reichen dafür nicht so
  eindeutig aus.
- AppTest ersetzt keinen vollständigen visuellen Browsertest.

Diese Nachteile sind für das kleine Analyse-Dashboard vertretbar. Die
fachlichen Funktionen sollten außerhalb der UI-Datei bleiben; dadurch wäre ein
späterer Wechsel der Oberfläche möglich.

## Alternative: Dash mit Plotly

Dash ist ein Python-Framework für reaktive Webanwendungen und benötigt keine
separat entwickelte JavaScript-Anwendung. Die aktuelle PyPI-Version ist
**4.4.1**, verlangt Python ab 3.9 und wird als plattformunabhängiges
py3-none-any-Wheel angeboten
([Dash auf PyPI](https://pypi.org/project/dash/),
[offizielle Installation](https://dash.plotly.com/installation)).

Python 3.13 wird durch die Paketanforderung „>=3.9“ nicht ausgeschlossen. Die
aktuellen PyPI-Klassifikatoren nennen allerdings nur Python 3.9 bis 3.12
explizit. Die Metadaten sind damit weniger eindeutig als bei Streamlit; eine
lokale Poetry-Installation und ein Starttest wären vor einer Entscheidung
zwingend.

Dash erfüllt die funktionalen Anforderungen:

- dcc.Dropdown kann einen oder mit multi=True mehrere Werte auswählen
  ([Dropdown-Dokumentation](https://dash.plotly.com/dash-core-components/dropdown));
- dcc.Graph zeigt interaktive Plotly-Figuren an
  ([Graph-Dokumentation](https://dash.plotly.com/dash-core-components/graph));
- Plotly liefert dieselben Linien-, Tooltip- und Lückenfunktionen wie in der
  empfohlenen Streamlit-Kombination.

Der wesentliche Unterschied liegt im Programmiermodell: Layout-Komponenten
erhalten IDs; Callback-Funktionen verbinden Eingabeeigenschaften explizit mit
Ausgabeeigenschaften. Das ist kontrollierbar und für größere, komplexe Apps
attraktiv, erzeugt im ersten Meilenstein aber mehr Begriffe und Verkabelung
([Dash-Callbacks](https://dash.plotly.com/basic-callbacks)).

Dash unterstützt Callback-Unit-Tests mit pytest. Realistische UI-Tests starten
jedoch einen Server und echten Browser über Selenium; dafür muss zusätzlich ein
zur Browser-Version passender ChromeDriver oder anderer WebDriver eingerichtet
werden
([Dash Testing](https://dash.plotly.com/testing)). Das widerspricht nicht den
Anforderungen, ist für einen wenig erfahrenen Entwickler aber unnötige
Einrichtung.

Für eine spätere Bereitstellung ist Dash offen genug für normale
Python-Hostingplattformen. Die besonders integrierte offizielle Variante Dash
Enterprise ist jedoch ein separates kommerzielles Produkt; die
Streamlit-Community-Cloud bietet für einen ersten geteilten Prototyp den
direkteren dokumentierten Weg.

## Direkter Vergleich

| Kriterium | Streamlit + Plotly | Dash + Plotly |
| --- | --- | --- |
| Python 3.13 | offiziell klassifiziert | durch >=3.9 erlaubt, aber 3.13 nicht explizit klassifiziert |
| macOS ARM | passende offizielle Paket-Wheels vorhanden | Hauptpaket plattformunabhängig; Installation lokal zu bestätigen |
| UI-Modell | lineares Python-Skript mit Widgets | Komponentenbaum plus explizite Callbacks |
| Auswahlfelder | direkt | direkt |
| mehrere Linien und Tooltips | Plotly | Plotly |
| sichtbare Lücken | Plotly connectgaps=False | Plotly connectgaps=False |
| einfacher UI-Test | eingebautes AppTest, kein Browser | Callback-Tests einfach; E2E mit Selenium/WebDriver |
| Poetry | normales PyPI-Paket; Community Cloud erkennt pyproject.toml | normales PyPI-Paket; Hosting separat zu konfigurieren |
| Eignung jetzt | **sehr gut** | gut, aber mehr Grundstruktur |

## Vorgeschlagener einfacher Installationsschritt

Nach Bestätigung der Entscheidung sollte Poetry die Abhängigkeiten im Projekt
auflösen:

    poetry add "streamlit[charts]" pandas
    poetry add --group dev pytest

poetry add ist der normale Poetry-Weg, Abhängigkeiten einzutragen und einen
Lockfile zu erzeugen
([Poetry: Dependency Management](https://python-poetry.org/)). Der Zusatz
pandas ist nur dann gerechtfertigt, wenn die Anwendung es direkt zum Einlesen
und Formen der Wetterdaten verwendet; andernfalls sollte es weggelassen werden.

Der erste technische Nachweis sollte bewusst klein bleiben:

1. leere lokale Streamlit-Seite starten;
2. ein Auswahlfeld und eine kleine Plotly-Linie mit einer absichtlichen Lücke
   anzeigen;
3. einen AppTest und einen normalen Fachlogik-Test mit pytest ausführen;
4. erst danach MeteoSchweiz-Download und Kalenderlogik anbinden.

## Bestätigtes Ergebnis

- Streamlit bildet die lokale Browseroberfläche.
- Plotly stellt die interaktiven Diagramme dar.
- pandas wird als direkte Abhängigkeit für CSV-Daten und Datenaufbereitung
  verwendet.
- pytest und Streamlits AppTest prüfen Fachlogik und Oberfläche.
- Die erste Version läuft lokal; eine Bereitstellung wird später entschieden.
