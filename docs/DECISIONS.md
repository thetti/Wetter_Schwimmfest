# Entscheidungen und offene Fragen

Dieses Dokument hält Produktentscheidungen fest, die für die nächste Arbeit
relevant sind. Architekturentscheidungen erhalten erst bei Bedarf eigene ADRs.

## Bestätigt

### D-001: Schulstart als Kalenderanker

Der Schulstart ist der erste Montag nach dem 15. August. Die Formulierung „nach“
ist strikt; der 15. August selbst zählt auch dann nicht, wenn er ein Montag ist.

### D-002: Zwei Kandidatentage als erster Use-Case

Verglichen werden der Samstag direkt vor dem Schulstart und der Samstag genau
eine Woche davor. Diese Auswahl definiert die erste Darstellung, aber nicht den
gesamten Funktionsumfang des Dashboards.

### D-003: Historisches Wetter-Dashboard

Die Anwendung stellt historische Wetterdaten über mehrere Jahre dar. Der erste
Vergleich zeigt je eine Linie pro Kandidatentag, mit dem Vergleichsjahr auf der
x-Achse und einem Tagesindikator auf der y-Achse.

### D-004: Entwicklungsunterstützung statt Laufzeit-Agent

Codex wird über `AGENTS.md` und Projektdokumente beim Entwickeln unterstützt.
Die Anwendung selbst enthält keinen KI-Agenten.

### D-005: Flexible Kalenderauswahl

Spätere Darstellungen können mehr als zwei einzelne Kalendertage oder einen
zusammenhängenden Zeitraum wie einen ganzen Monat auswerten. Das fachliche
Modell soll diese Erweiterung offenhalten.

### D-006: Stationsmessung für den ersten Meilenstein

Der erste Meilenstein verwendet Messwerte einer repräsentativen offiziellen
Wetterstation für den Auswertungsort. Für Zug ist dies die MeteoSchweiz-Station
Cham (CHZ). Diese Zuordnung gilt nur für die erste Konfiguration und begrenzt
das Produkt nicht auf Zug oder Cham. Bei jedem anderen Auswertungsort wird die
Stationszuordnung neu bestimmt. Stationsname, Höhe und räumlicher Bezug zum
Auswertungsort bleiben in der Darstellung sichtbar. Exakte Koordinatenwerte
oder räumlich interpolierte Rasterdaten können später ergänzt werden.

Grundlage: [Recherche zur historischen Wetterdatenquelle](research/weather-data-source.md)

### D-007: Niederschlagssumme mit UTC-Tagesgrenze

Als erster täglicher Niederschlagsindikator wird der amtliche
MeteoSchweiz-Parameter `rka150d0` in Millimetern verwendet. Sein Intervall
reicht von 00:00 UTC bis 00:00 UTC des Folgetags und entspricht im August
ungefähr 02:00 Uhr bis 02:00 Uhr lokaler Zeit. Diese Verschiebung bleibt in der
Darstellung nachvollziehbar. Für andere Zeitauflösungen wird der jeweils
passende amtliche Parameter verwendet.

### D-008: Maximal verfügbarer Vergleichszeitraum

Die Auswertung verwendet für die gewählte Station und die ausgewählten
Indikatoren so viele Daten wie verfügbar. Der Zeitraum beginnt beim frühesten
gemeinsamen Datenbeginn und reicht bis zu den neuesten verfügbaren Werten. Für
Cham (CHZ) und die ersten beiden Indikatoren beginnt er 1993. Einzelne fehlende
Werte werden als Lücken dargestellt, statt den gesamten Zeitraum zu verkürzen.
Daten des laufenden Jahres dürfen mit erkennbarem vorläufigem Qualitätsstand
einbezogen werden. Bei einer anderen Station oder Indikatorauswahl passt sich
der Zeitraum entsprechend an. Eine kurze oder fehlende Reihe an einer Station
entfernt einen fachlich sinnvollen Indikator nicht aus dem allgemeinen Katalog;
sie begrenzt nur die dort mögliche Darstellung.

### D-009: Lokales Dashboard mit Streamlit und Plotly

Das erste Dashboard wird mit Streamlit erstellt und lokal im Browser
ausgeführt. Plotly übernimmt die interaktiven Diagramme; pandas wird direkt zum
Einlesen und Aufbereiten der Wetterdaten verwendet. Tests verwenden pytest und
Streamlits AppTest. Eine Veröffentlichung wird erst später entschieden.

Grundlage: [Recherche zur Dashboard-Technologie](research/dashboard-technology.md)

### D-010: Amtliches Tagesmaximum unverändert übernehmen

Die Höchsttemperatur der ersten Tagesansicht wird direkt aus dem amtlichen
MeteoSchweiz-Parameter `tre200dx` in Grad Celsius übernommen und nicht selbst
neu berechnet. Der in der Quellendokumentation beschriebene Wechsel des
Aggregationsfensters um 2018 wird als Einschränkung der Datenquelle
dokumentiert.

### D-011: Wetterdaten bei Bedarf laden und lokal zwischenspeichern

Die Anwendung lädt die amtlichen Wetterdaten bei Bedarf direkt von
MeteoSchweiz. Die Daten werden nicht in Git eingecheckt. Ein lokaler Cache
vermeidet unnötige wiederholte Downloads und erhält eine begrenzte
Gültigkeitsdauer, damit neue Daten später automatisch berücksichtigt werden.
Beim ersten Laden und nach Ablauf des Caches ist eine Internetverbindung nötig.
Die genaue Umsetzung gehört zur User-Story für den Datenabruf.

Streamlit stellt dafür mit
[`st.cache_data`](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data)
einen eingebauten Datencache mit einstellbarer Gültigkeitsdauer bereit.

### D-012: Fachlichen Indikatorenkatalog von Stationsverfügbarkeit trennen

Wetterindikatoren werden zuerst nach ihrem Nutzen für die Fragestellung
beurteilt. Erst danach wird anhand des amtlichen Dateninventars geprüft, an
welchen Stationen, in welcher Zeitauflösung und für welchen Zeitraum sie
verfügbar sind. Die erste Station Cham definiert deshalb weder den allgemeinen
Indikatorenkatalog noch dessen zeitliche Abdeckung.

Grundlage: [Allgemeiner Wetterindikatorenkatalog](research/weather-indicator-catalog.md)

### D-013: Tages- und Stundenperspektive getrennt anbieten

Tageswerte bleiben für lange Vergleiche ganzer Kalendertage vorgesehen.
Stundenwerte sollen später den Verlauf und das Wetter innerhalb eines örtlichen
Festzeitfensters zeigen. Beide Perspektiven verwenden die amtlichen Werte ihrer
jeweiligen Zeitauflösung. UTC-Zeitstempel werden für die Stundenansicht korrekt
in lokale Zeit einschliesslich Sommerzeit umgerechnet.
