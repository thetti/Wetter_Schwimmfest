from dataclasses import dataclass

import pandas as pd

from wetter_schwimmfest.calendar_dates import calculate_candidate_dates


EARLIER_CANDIDATE = "Früher Kandidatentag"
LATER_CANDIDATE = "Später Kandidatentag"
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
}


def build_candidate_comparison(weather_data: pd.DataFrame) -> pd.DataFrame:
    """Verbinde die Kandidatentage vollständiger Jahre mit den Tageswerten."""
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
    weather_columns = (
        "reference_timestamp",
        "max_temperature_c",
        "precipitation_mm",
        "data_period",
    )
    return candidate_data.merge(
        weather_data.loc[:, weather_columns],
        how="left",
        left_on="candidate_date",
        right_on="reference_timestamp",
    ).drop(columns="reference_timestamp")
