# Wetter Schwimmfest

Dieses Projekt macht historische Wetterdaten für frei wählbare Orte und
Kalenderzeiträume vergleichbar. Der erste Use-Case untersucht, welcher von zwei
Samstagen im August für das Schwimmfest erfahrungsgemäss günstiger ist.

Der technische Grundaufbau ist vorhanden. Das kleine Dashboard lädt amtliche
Tageswerte der MeteoSchweiz-Station Cham, zeigt eine Datenvorschau und berechnet
für ein eingegebenes Vergleichsjahr den Schulstart sowie beide
Kandidatentage. Das Liniendiagramm verwendet noch künstliche Demodaten.

## Einrichten

Voraussetzung sind Python 3.13 und Poetry. Im Projektordner genügt:

```bash
poetry install
```

Poetry legt die virtuelle Python-Umgebung lokal im Ordner `.venv` an. Dieser
Ordner wird nicht in Git aufgenommen.

## Dashboard starten

```bash
poetry run streamlit run app.py
```

Streamlit öffnet das Dashboard normalerweise automatisch im Browser. Beenden
kannst du es im Terminal mit `Ctrl+C`.

Beim ersten Aufruf lädt das Dashboard die historischen Tageswerte und die
Werte des laufenden Jahres direkt von MeteoSchweiz. Die Dateien werden nicht im
Repository gespeichert. Solange die App läuft, hält Streamlit die eingelesenen
Daten zwölf Stunden im Cache. Der erste Aufruf nach einem Neustart benötigt
daher wieder eine Internetverbindung.

## Tests ausführen

```bash
poetry run pytest
```

## Projektdokumentation

- [Fachbegriffe](CONTEXT.md)
- [Ziel und erster Use-Case](docs/PROJECT.md)
- [Entwicklungsablauf](docs/WORKFLOW.md)
- [Entscheidungen und offene Fragen](docs/DECISIONS.md)
