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

## Offen vor der ersten Implementierung

### O-001: Historische Wetterdaten

Welche offene und langfristig verfügbare Datenquelle verwenden wir? Zu prüfen
sind insbesondere Angebote von MeteoSchweiz oder anderen Schweizer
Open-Government-Data-Portalen.

### O-002: Bezug zwischen Ort und Messung

Soll ein Auswertungsort einer Wetterstation, dem nächstgelegenen Messpunkt oder
einem räumlichen Rasterwert zugeordnet werden? Diese Wahl beeinflusst, was ein
Wert „für Zug“ genau bedeutet.

### O-003: Historischer Zeitraum

Ab welchem Vergleichsjahr soll die Auswertung beginnen, und wie gehen wir mit
Jahren ohne vollständige Messwerte um?

### O-004: Definition der Tagesindikatoren

Zu klären sind Einheit, Tagesgrenzen und genaue Berechnung von
Niederschlagssumme, Höchsttemperatur und späteren Indikatoren.

### O-005: Erste Bedienoberfläche

Zu entscheiden ist, welche einfache Dashboard-Technik wir verwenden und wie
der Nutzer Ort, Zeitraum und Tagesindikator auswählt.
