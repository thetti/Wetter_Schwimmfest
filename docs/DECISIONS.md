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
Cham (CHZ). Stationsname und Entfernung zum Auswertungsort bleiben in der
Darstellung sichtbar. Exakte Koordinatenwerte oder räumlich interpolierte
Rasterdaten können später ergänzt werden.

Grundlage: [Recherche zur historischen Wetterdatenquelle](research/weather-data-source.md)

### D-007: Niederschlagssumme mit UTC-Tagesgrenze

Als täglicher Niederschlagsindikator wird der amtliche MeteoSchweiz-Parameter
`rka150d0` in Millimetern verwendet. Sein Intervall reicht von 00:00 UTC bis
00:00 UTC des Folgetags und entspricht im August ungefähr 02:00 Uhr bis 02:00
Uhr lokaler Zeit. Diese Verschiebung bleibt in der Darstellung nachvollziehbar.

### D-008: Maximal verfügbarer Vergleichszeitraum

Die Auswertung verwendet für die gewählte Station und die ausgewählten
Indikatoren so viele Daten wie verfügbar. Der Zeitraum beginnt beim frühesten
gemeinsamen Datenbeginn und reicht bis zu den neuesten verfügbaren Werten. Für
Cham (CHZ) und die ersten beiden Indikatoren beginnt er 1993. Einzelne fehlende
Werte werden als Lücken dargestellt, statt den gesamten Zeitraum zu verkürzen.
Daten des laufenden Jahres dürfen mit erkennbarem vorläufigem Qualitätsstand
einbezogen werden. Bei einer anderen Station oder Indikatorauswahl passt sich
der Zeitraum entsprechend an.

## Offen vor der ersten Implementierung

### O-004: Definition der Tagesindikatoren

Für die Niederschlagssumme sind Parameter, Einheit und Tagesgrenze festgelegt.
Zu klären bleibt die genaue historische Intervallbeschreibung der
Höchsttemperatur sowie die Definition späterer Indikatoren.

### O-005: Erste Bedienoberfläche

Zu entscheiden ist, welche einfache Dashboard-Technik wir verwenden und wie
der Nutzer Ort, Zeitraum und Tagesindikator auswählt.
