from dataclasses import dataclass
from datetime import date, timedelta

import pandas as pd

from wetter_schwimmfest.calendar_dates import calculate_candidate_dates
from wetter_schwimmfest.comparison import (
    CANDIDATES,
    EARLIER_CANDIDATE,
    LATER_CANDIDATE,
)


LOCAL_TIME_ZONE = "Europe/Zurich"


@dataclass(frozen=True)
class HourlyIndicator:
    column: str
    label: str
    unit: str
    source_parameter: str


HOURLY_INDICATORS = {
    "Niederschlag": HourlyIndicator(
        "hourly_precipitation_mm", "Niederschlag", "mm", "rre150h0"
    ),
    "Mittlere Temperatur": HourlyIndicator(
        "hourly_mean_temperature_c", "Mittlere Temperatur", "°C", "tre200h0"
    ),
    "Tiefsttemperatur": HourlyIndicator(
        "hourly_min_temperature_c", "Tiefsttemperatur", "°C", "tre200hn"
    ),
    "Höchsttemperatur": HourlyIndicator(
        "hourly_max_temperature_c", "Höchsttemperatur", "°C", "tre200hx"
    ),
    "Sonnenscheindauer": HourlyIndicator(
        "hourly_sunshine_minutes", "Sonnenscheindauer", "min", "sre000h0"
    ),
    "Globalstrahlung": HourlyIndicator(
        "hourly_global_radiation_wm2", "Globalstrahlung", "W/m²", "gre000h0"
    ),
    "Mittlerer Wind": HourlyIndicator(
        "hourly_mean_wind_kmh", "Mittlerer Wind", "km/h", "fu3010h0"
    ),
    "Stärkste Böe": HourlyIndicator(
        "hourly_max_gust_kmh", "Stärkste Böe", "km/h", "fu3010h1"
    ),
    "Relative Luftfeuchtigkeit": HourlyIndicator(
        "hourly_mean_humidity_percent",
        "Relative Luftfeuchtigkeit",
        "%",
        "ure200h0",
    ),
    "Taupunkt": HourlyIndicator(
        "hourly_dew_point_c", "Taupunkt", "°C", "tde200h0"
    ),
}


def _candidate_days(first_day: date, last_day: date) -> pd.DataFrame:
    candidates = []
    for year in range(first_day.year, last_day.year + 1):
        dates = calculate_candidate_dates(year)
        for candidate, candidate_day in (
            (EARLIER_CANDIDATE, dates.earlier_candidate_day),
            (LATER_CANDIDATE, dates.later_candidate_day),
        ):
            if first_day <= candidate_day <= last_day:
                candidates.append(
                    {
                        "comparison_year": year,
                        "candidate": candidate,
                        "candidate_day": candidate_day,
                    }
                )
    return pd.DataFrame(candidates)


def _candidate_hour_slots(candidates: pd.DataFrame) -> pd.DataFrame:
    """Erzeuge die 36 Stundenplätze ab Beginn jedes Kandidatentags."""
    slots = []
    for candidate in candidates.itertuples(index=False):
        for hour_position in range(1, 37):
            hours_after_start = hour_position - 1
            slots.append(
                {
                    "comparison_year": candidate.comparison_year,
                    "candidate": candidate.candidate,
                    "hour_position": hour_position,
                    "observation_day": candidate.candidate_day
                    + timedelta(days=hours_after_start // 24),
                    "local_start_hour": hours_after_start % 24,
                }
            )
    return pd.DataFrame(slots)


def build_hourly_candidate_profile(
    hourly_data: pd.DataFrame,
    indicator_name: str,
) -> pd.DataFrame:
    """Fasse 36 Stunden ab Kandidatentag über die Vergleichsjahre zusammen."""
    indicator = HOURLY_INDICATORS[indicator_name]
    observations = hourly_data.copy()

    # MeteoSchweiz bezeichnet mit dem Zeitstempel das Ende des Stundenintervalls.
    # Die Stunde 24 endet um 00:00 Uhr des Folgetags und gehört noch zum Vortag.
    interval_start = (
        observations["reference_timestamp"].dt.tz_convert(LOCAL_TIME_ZONE)
        - pd.Timedelta(hours=1)
    )
    observations["observation_day"] = interval_start.dt.date
    observations["local_start_hour"] = interval_start.dt.hour

    candidates = _candidate_days(
        observations["observation_day"].min(),
        observations["observation_day"].max(),
    )
    candidate_hours = _candidate_hour_slots(candidates)
    matched = candidate_hours.merge(
        observations,
        on=("observation_day", "local_start_hour"),
        how="inner",
    )
    available = matched.dropna(subset=[indicator.column])

    statistics = (
        available.groupby(["candidate", "hour_position"], observed=True)
        .agg(
            median_value=(indicator.column, "median"),
            lower_value=(indicator.column, lambda values: values.quantile(0.25)),
            upper_value=(indicator.column, lambda values: values.quantile(0.75)),
            year_count=("comparison_year", "nunique"),
            first_year=("comparison_year", "min"),
            last_year=("comparison_year", "max"),
        )
        .reindex(
            pd.MultiIndex.from_product(
                (CANDIDATES, range(1, 37)),
                names=("candidate", "hour_position"),
            )
        )
        .reset_index()
    )
    return statistics
