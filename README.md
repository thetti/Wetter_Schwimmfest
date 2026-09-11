# Wetter Schwimmfest

Dieses Projekt macht historische Wetterdaten für frei wählbare Orte und
Kalenderzeiträume vergleichbar. Der erste Use-Case untersucht, welcher von zwei
Samstagen im August für das Schwimmfest erfahrungsgemäss günstiger ist.

In der ersten implementierten Konfiguration lädt das Dashboard amtliche Tages-
und Stundenwerte der MeteoSchweiz-Station Cham als Repräsentation für Zug.

Das Tagesdiagramm vergleicht Niederschlag, Temperatur, Wind, Böen,
Luftfeuchtigkeit, Sonnenschein und Globalstrahlung über die Jahre. Zusätzlich
steht ein transparenter Fest-Indikator von 0 bis 100 zur Verfügung. Ein
schmaler Boxplot je Kandidatentag ergänzt den Jahresverlauf um die Verteilung
der Tageswerte. Ein separates Stundendiagramm zeigt je Kandidatentag den
historischen Median vom Beginn des Kandidatentags bis 12:00 Uhr des Folgetags
sowie die typische Bandbreite vom 25. bis zum 75. Perzentil.

Das Produktziel ist nicht auf Zug, Cham, diese beiden Indikatoren oder
Tageswerte beschränkt. Später sollen Auswertungsort, Wetterstation,
Kalenderauswahl und Zeitauflösung variabel sein. Die jeweils verfügbare
Zeitreihe richtet sich nach der gewählten Kombination aus Station, Indikator
und Zeitauflösung.

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

Beim ersten Aufruf lädt das Dashboard die historischen Tages- und Stundenwerte
sowie die Werte des laufenden Jahres direkt von MeteoSchweiz. Die Dateien
werden nicht im Repository gespeichert. Solange die App läuft, hält Streamlit
die eingelesenen Daten zwölf Stunden im Cache. Der erste Aufruf nach einem
Neustart benötigt daher wieder eine Internetverbindung und kann wegen der
grösseren Stundenhistorie einen Moment dauern.

## Tests ausführen

```bash
poetry run pytest
```

## Projektdokumentation

- [Fachbegriffe](CONTEXT.md)
- [Ziel und erster Use-Case](docs/PROJECT.md)
- [Entwicklungsablauf](docs/WORKFLOW.md)
- [Entscheidungen und offene Fragen](docs/DECISIONS.md)
- [Allgemeiner Wetterindikatorenkatalog](docs/research/weather-indicator-catalog.md)
- [Zug/Cham-Fallstudie zur Wetterdatenquelle](docs/research/weather-data-source.md)
