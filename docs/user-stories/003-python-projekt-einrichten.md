# User-Story 003: Python-Projekt einrichten

## Status

Umgesetzt und geprüft.

## Story

Als wenig erfahrener Python-Entwickler möchte ich ein kleines, mit Poetry
verwaltetes Projekt und ein minimales lokales Dashboard starten können, damit
die technische Grundlage auf meinem Mac nachweislich funktioniert und für die
erste fachliche Funktion bereit ist.

## Sichtbares Ergebnis

Ein lokales Streamlit-Dashboard öffnet sich im Browser. Es zeigt einen Titel,
ein einfaches Auswahlfeld und ein kleines Plotly-Liniendiagramm mit einer
absichtlichen Datenlücke. Das Diagramm verwendet noch keine echten
Wetterdaten.

## Umfang

- Poetry-Projekt für Python 3.13 mit lokalem `.venv` anlegen
- Streamlit, Plotly und pandas als direkte Laufzeitabhängigkeiten eintragen
- pytest als Entwicklungsabhängigkeit eintragen
- eine kleine, verständliche Projektstruktur anlegen
- einen einfachen Startbefehl über Poetry bereitstellen
- einen normalen Test und einen Streamlit-AppTest ergänzen
- Installations-, Start- und Testbefehle in der README dokumentieren
- virtuelle Umgebung, Caches und erzeugte Dateien von Git ausschließen

## Nicht enthalten

- MeteoSchweiz-Daten herunterladen
- Kandidatentage oder Schulstart berechnen
- echte Wetterwerte aufbereiten oder darstellen
- mehrere Seiten, Benutzerkonten oder eine Cloud-Bereitstellung einrichten
- zusätzliche Entwicklungswerkzeuge ohne unmittelbaren Bedarf einführen

## Vorgesehene Struktur

```text
app.py                         Streamlit-Einstieg
src/wetter_schwimmfest/        später wiederverwendbare Fachlogik
tests/                         automatische Tests
pyproject.toml                 Projekt und direkte Abhängigkeiten
poetry.lock                    aufgelöste Paketversionen
```

## Akzeptanzkriterien

- `poetry install` installiert das Projekt reproduzierbar aus dem Lockfile.
- `poetry run streamlit run app.py` startet das lokale Dashboard ohne Fehler.
- Auswahlfeld und Plotly-Diagramm werden angezeigt.
- Die absichtliche Lücke wird im Diagramm nicht durch eine Linie verbunden.
- `poetry run pytest` führt alle Tests erfolgreich aus.
- Ein Streamlit-AppTest prüft, dass die Seite ohne Ausnahme aufgebaut wird.
- Die README erklärt Einrichtung, Start und Tests in einfachen Schritten.
- Es werden keine echten Wetterdaten und kein Anwendungscode außerhalb des
  beschriebenen technischen Nachweises eingeführt.

## Umsetzungsergebnis

- Python 3.13, Poetry 2.1.2 und Git wurden auf dem Entwicklungsrechner geprüft.
- Poetry verwaltet die virtuelle Umgebung lokal in `.venv`.
- Das Dashboard zeigt die beiden vereinbarten Demo-Reihen und lässt den
  Wetterindikator auswählen.
- Eine absichtliche Datenlücke bleibt als Unterbrechung der Linie sichtbar.
- Zwei automatische Tests prüfen Diagramm und Start der Streamlit-App.
- `poetry install`, `poetry run pytest` und der lokale Dashboard-Start wurden
  erfolgreich ausgeführt.
- Die Darstellung wurde zusätzlich im lokalen Browser kontrolliert.
