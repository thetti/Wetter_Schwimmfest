# User-Story 002: Dashboard-Technologie entscheiden

## Status

Abgeschlossen. Streamlit, Plotly und pandas sind für das lokale Dashboard
bestätigt; Tests verwenden pytest und Streamlits AppTest.

Ergebnis: [Recherche zur Dashboard-Technologie](../research/dashboard-technology.md)

## Story

Als wenig erfahrener Python-Entwickler möchte ich eine einfache Technik für ein
lokales Wetter-Dashboard auswählen, damit ich Auswahlfelder und Diagramme im
Browser entwickeln kann, ohne zusätzlich eine JavaScript-Anwendung betreiben
zu müssen.

## Umfang

- wenige geeignete Python-Dashboard-Lösungen vergleichen
- Unterstützung für Python 3.13 und macOS auf Apple Silicon prüfen
- Installation und Start mit Poetry berücksichtigen
- Auswahlfelder, interaktive Liniendiagramme, Tooltips und sichtbare
  Messwertlücken berücksichtigen
- einfache automatische Tests und eine spätere Bereitstellung berücksichtigen
- eine begründete Empfehlung mit bekannten Nachteilen formulieren

Nicht Teil dieser User-Story sind die Installation der gewählten Pakete, das
Anlegen des Python-Projekts und die Implementierung des Dashboards.

## Akzeptanzkriterien

- Die Empfehlung ist durch direkte Links auf Primärquellen belegt.
- Die empfohlenen Komponenten erfüllen die Anforderungen des ersten Diagramms.
- Die Lösung benötigt keine separat entwickelte JavaScript-Anwendung.
- Komplexität und Nachteile sind für einen Einsteiger verständlich beschrieben.
- Der Nutzer kann die Technologie vor der Implementierung bestätigen oder
  anpassen.
