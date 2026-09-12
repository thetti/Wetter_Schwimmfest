from dataclasses import dataclass

import pandas as pd

from wetter_schwimmfest.calendar_dates import calculate_candidate_dates
from wetter_schwimmfest.fest_indicator import add_fest_score


EARLIER_CANDIDATE = "Datum 1"
LATER_CANDIDATE = "Datum 2"
CANDIDATES = (EARLIER_CANDIDATE, LATER_CANDIDATE)


@dataclass(frozen=True)
class WeatherIndicator:
    column: str
    label: str
    unit: str
    source_parameter: str
    time_note: str


WEATHER_INDICATORS = {
    "Niederschlagssumme": WeatherIndicator(
        column="precipitation_mm",
        label="Niederschlagssumme",
        unit="mm",
        source_parameter="rka150d0",
        time_note="00:00–00:00 UTC (im August ungefähr 02:00–02:00 Uhr lokal)",
    ),
    "Höchsttemperatur": WeatherIndicator(
        column="max_temperature_c",
        label="Höchsttemperatur",
        unit="°C",
        source_parameter="tre200dx",
        time_note="amtliches Tagesmaximum; Aggregationsfenster änderte sich um 2018",
    ),
    "Tagesmitteltemperatur": WeatherIndicator(
        "mean_temperature_c",
        "Tagesmitteltemperatur",
        "°C",
        "tre200d0",
        "amtliches Tagesmittel",
    ),
    "Tagestiefsttemperatur": WeatherIndicator(
        "min_temperature_c",
        "Tagestiefsttemperatur",
        "°C",
        "tre200dn",
        "amtliches Tagesminimum",
    ),
    "Mittlerer Wind": WeatherIndicator(
        "mean_wind_kmh",
        "Mittlerer Wind",
        "km/h",
        "fkl010d0",
        "amtliches Tagesmittel, von m/s mit × 3,6 in km/h umgerechnet",
    ),
    "Stärkste Böe": WeatherIndicator(
        "max_gust_kmh",
        "Stärkste Böe",
        "km/h",
        "fu3010d1",
        "amtliches Tagesmaximum der Sekundenböe",
    ),
    "Relative Luftfeuchtigkeit": WeatherIndicator(
        "mean_humidity_percent",
        "Relative Luftfeuchtigkeit",
        "%",
        "ure200d0",
        "amtliches Tagesmittel",
    ),
    "Sonnenscheindauer": WeatherIndicator(
        "sunshine_minutes",
        "Sonnenscheindauer",
        "min",
        "sre000d0",
        "amtliche Tagessumme",
    ),
    "Relative Sonnenscheindauer": WeatherIndicator(
        "relative_sunshine_percent",
        "Relative Sonnenscheindauer",
        "%",
        "sremaxdv",
        "Anteil an der maximal möglichen Tagessumme",
    ),
    "Globalstrahlung": WeatherIndicator(
        "global_radiation_wm2",
        "Globalstrahlung",
        "W/m²",
        "gre000d0",
        "amtliches Tagesmittel; kein UV-Index",
    ),
    "Fest-Indikator": WeatherIndicator(
        "fest_score",
        "Fest-Indikator",
        "Punkte",
        "Berechnung der Anwendung",
        "feste Regeln von 0 bis 100; kein amtlicher Messwert",
    ),
}


def build_candidate_comparison(weather_data: pd.DataFrame) -> pd.DataFrame:
    """Verbinde Datum 1 und Datum 2 vollständiger Jahre mit den Tageswerten."""
    first_weather_day = weather_data["reference_timestamp"].min().date()
    last_weather_day = weather_data["reference_timestamp"].max().date()

    candidates = []
    for year in range(first_weather_day.year, last_weather_day.year + 1):
        dates = calculate_candidate_dates(year)
        if (
            dates.earlier_candidate_day < first_weather_day
            or dates.later_candidate_day > last_weather_day
        ):
            continue

        candidates.extend(
            (
                {
                    "comparison_year": year,
                    "candidate": EARLIER_CANDIDATE,
                    "candidate_date": pd.Timestamp(
                        dates.earlier_candidate_day, tz="UTC"
                    ),
                },
                {
                    "comparison_year": year,
                    "candidate": LATER_CANDIDATE,
                    "candidate_date": pd.Timestamp(
                        dates.later_candidate_day, tz="UTC"
                    ),
                },
            )
        )

    candidate_data = pd.DataFrame(candidates)
    weather_columns = [
        "reference_timestamp",
        *(
            indicator.column
            for indicator in WEATHER_INDICATORS.values()
            if indicator.column != "fest_score"
        ),
        "data_period",
    ]
    comparison = candidate_data.merge(
        weather_data.loc[:, weather_columns],
        how="left",
        left_on="candidate_date",
        right_on="reference_timestamp",
    ).drop(columns="reference_timestamp")
    return add_fest_score(comparison)
