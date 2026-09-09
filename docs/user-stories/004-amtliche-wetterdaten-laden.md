# User-Story 004: Amtliche Wetterdaten laden

## Status

Umgesetzt und geprüft.

## Story

Als Nutzer möchte ich die amtlichen Tageswerte der Station Cham direkt im
Dashboard laden können, damit die Anwendung mit echten Wetterdaten arbeitet,
ohne Datendateien im Git-Repository abzulegen.

## Sichtbares Ergebnis

Das Dashboard zeigt unterhalb des technischen Demo-Diagramms einen Abschnitt
mit echten MeteoSchweiz-Daten. Er nennt Quelle, Station und verfügbaren
Zeitraum und zeigt einige der zuletzt geladenen Tageswerte. Beim normalen
Bedienen der App werden dieselben Dateien nicht ständig erneut heruntergeladen.

## Umfang

- historische und aktuelle Tagesdatei der Station Cham (CHZ) direkt von
  MeteoSchweiz laden
- die amtlichen Spalten `tre200dx` und `rka150d0` einlesen
- Datumsangaben als UTC-Zeitstempel verstehen
- historische und aktuelle Werte ohne doppelte Tage zusammenführen
- leere Messwerte als fehlend erhalten
- Downloads mit Streamlits eingebautem Datencache zwölf Stunden lang
  zwischenspeichern
- Datenquelle, Station, Zeitraum und eine kleine Vorschau im Dashboard zeigen
- verständliche Meldung anzeigen, falls MeteoSchweiz nicht erreichbar ist
- Einlesen und Zusammenführen mit lokalen Testdaten prüfen

## Nicht enthalten

- heruntergeladene CSV-Dateien im Repository speichern
- ETag-Dateien oder einen dauerhaften Cache über App-Neustarts hinweg verwalten
- Schulstart und Kandidatentage berechnen
- das Demo-Diagramm bereits durch den historischen Vergleich ersetzen
- andere Stationen oder Orte auswählbar machen

## Akzeptanzkriterien

- Beim ersten Aufruf lädt die App die beiden amtlichen CHZ-Tagesdateien.
- Weitere Streamlit-Durchläufe verwenden für zwölf Stunden den Cache.
- Die zusammengeführten Daten enthalten höchstens eine Zeile pro Zeitstempel.
- Bei Überschneidungen hat die aktuelle Datei Vorrang.
- Fehlende Werte bleiben fehlend und werden nicht zu null.
- Das Dashboard nennt MeteoSchweiz als Quelle und zeigt den Datenzeitraum.
- Automatische Tests benötigen keine Internetverbindung.
- Eine manuelle Stichprobe mit den amtlichen Dateien bestätigt Datenbeginn,
  neuestes Datum und einzelne Messwerte.

## Umsetzungsergebnis

- Das Dashboard lädt die historischen und aktuellen CHZ-Tageswerte direkt von
  MeteoSchweiz und hält sie zwölf Stunden im Streamlit-Cache.
- Im Repository werden keine heruntergeladenen Wetterdateien abgelegt.
- Die Datenvorschau nennt Quelle, Station und verfügbaren Zeitraum und zeigt
  die letzten fünf Tage.
- Sechs automatische Tests prüfen unter anderem App-Start, Fehlermeldung,
  CSV-Format, fehlende Werte, Zusammenführen und Cache-Nutzung ohne Internet.
- Der echte Download und die Darstellung wurden am 9. September 2026 geprüft.

## Amtliche Stichprobe vom 9. September 2026

| Prüfung | Ergebnis |
| --- | --- |
| Historische Datei | 11'748 Zeilen |
| Datei des laufenden Jahres | 251 Zeilen |
| Zusammengeführt | 11'999 eindeutige Tageszeilen |
| Erster Tag | 11.06.1993: 17,8 °C; 25,6 mm |
| Neuester Tag | 08.09.2026: 31,2 °C; 0,0 mm |
| Früher Kandidatentag 2025 | 09.08.2025: 32,6 °C; 0,0 mm |
| Später Kandidatentag 2025 | 16.08.2025: 29,9 °C; 0,4 mm |

Die Werte wurden sowohl mit dem neuen Einlesecode als auch direkt in den
amtlichen CSV-Zeilen kontrolliert.
