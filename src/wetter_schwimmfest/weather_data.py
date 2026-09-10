from typing import IO
from urllib.error import HTTPError, URLError

import pandas as pd
import streamlit as st


DAILY_HISTORICAL_DATA_URL = (
    "https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/chz/"
    "ogd-smn_chz_d_historical.csv"
)
DAILY_RECENT_DATA_URL = (
    "https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/chz/"
    "ogd-smn_chz_d_recent.csv"
)
HOURLY_HISTORICAL_DATA_URLS = tuple(
    "https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/chz/"
    f"ogd-smn_chz_h_historical_{decade}-{decade + 9}.csv"
    for decade in (1990, 2000, 2010, 2020)
)
HOURLY_RECENT_DATA_URL = (
    "https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/chz/"
    "ogd-smn_chz_h_recent.csv"
)

DAILY_SOURCE_COLUMNS = {
    "station_abbr": "station_code",
    "reference_timestamp": "reference_timestamp",
    "tre200d0": "mean_temperature_c",
    "tre200dx": "max_temperature_c",
    "tre200dn": "min_temperature_c",
    "ure200d0": "mean_humidity_percent",
    "fkl010d0": "mean_wind_ms",
    "fu3010d1": "max_gust_kmh",
    "rka150d0": "precipitation_mm",
    "gre000d0": "global_radiation_wm2",
    "sre000d0": "sunshine_minutes",
    "sremaxdv": "relative_sunshine_percent",
}

HOURLY_SOURCE_COLUMNS = {
    "station_abbr": "station_code",
    "reference_timestamp": "reference_timestamp",
    "tre200h0": "hourly_mean_temperature_c",
    "tre200hn": "hourly_min_temperature_c",
    "tre200hx": "hourly_max_temperature_c",
    "ure200h0": "hourly_mean_humidity_percent",
    "tde200h0": "hourly_dew_point_c",
    "fu3010h0": "hourly_mean_wind_kmh",
    "fu3010h1": "hourly_max_gust_kmh",
    "rre150h0": "hourly_precipitation_mm",
    "gre000h0": "hourly_global_radiation_wm2",
    "sre000h0": "hourly_sunshine_minutes",
}


class WeatherDataError(RuntimeError):
    """Die amtlichen Wetterdaten konnten nicht geladen werden."""


def read_weather_csv(
    source: str | IO[str],
    data_period: str,
    source_columns: dict[str, str] | None = None,
) -> pd.DataFrame:
    """Lese ausgewählte Spalten einer MeteoSchweiz-Stationsdatei ein."""
    selected_columns = source_columns or DAILY_SOURCE_COLUMNS
    data = pd.read_csv(
        source,
        sep=";",
        encoding="windows-1252",
        usecols=list(selected_columns),
    ).rename(columns=selected_columns)

    data["reference_timestamp"] = pd.to_datetime(
        data["reference_timestamp"],
        format="%d.%m.%Y %H:%M",
        utc=True,
    )
    for column in selected_columns.values():
        if column in ("station_code", "reference_timestamp"):
            continue
        data[column] = pd.to_numeric(data[column], errors="raise")

    if "mean_wind_ms" in data:
        data["mean_wind_kmh"] = data["mean_wind_ms"] * 3.6
        data = data.drop(columns="mean_wind_ms")

    data["data_period"] = data_period
    return data


def combine_weather_data(
    *data_frames: pd.DataFrame,
) -> pd.DataFrame:
    """Führe Zeiträume zusammen; die jeweils spätere Datei hat Vorrang."""
    return (
        pd.concat(data_frames, ignore_index=True)
        .drop_duplicates(subset="reference_timestamp", keep="last")
        .sort_values("reference_timestamp")
        .reset_index(drop=True)
    )


@st.cache_data(ttl=12 * 60 * 60, show_spinner=False)
def load_cham_weather_data() -> pd.DataFrame:
    """Lade die Tageswerte für Cham direkt von MeteoSchweiz."""
    try:
        historical_data = read_weather_csv(
            DAILY_HISTORICAL_DATA_URL,
            "historical",
            DAILY_SOURCE_COLUMNS,
        )
        recent_data = read_weather_csv(
            DAILY_RECENT_DATA_URL,
            "recent",
            DAILY_SOURCE_COLUMNS,
        )
    except (HTTPError, URLError, OSError, ValueError, pd.errors.ParserError) as error:
        raise WeatherDataError(
            "Die Tageswerte von MeteoSchweiz sind momentan nicht verfügbar."
        ) from error

    return combine_weather_data(historical_data, recent_data)


@st.cache_data(ttl=12 * 60 * 60, show_spinner=False)
def load_cham_hourly_weather_data() -> pd.DataFrame:
    """Lade die Stundenwerte für Cham direkt von MeteoSchweiz."""
    try:
        historical_data = combine_weather_data(
            *(
                read_weather_csv(url, "historical", HOURLY_SOURCE_COLUMNS)
                for url in HOURLY_HISTORICAL_DATA_URLS
            )
        )
        recent_data = read_weather_csv(
            HOURLY_RECENT_DATA_URL,
            "recent",
            HOURLY_SOURCE_COLUMNS,
        )
    except (HTTPError, URLError, OSError, ValueError, pd.errors.ParserError) as error:
        raise WeatherDataError(
            "Die Stundenwerte von MeteoSchweiz sind momentan nicht verfügbar."
        ) from error

    return combine_weather_data(historical_data, recent_data)
