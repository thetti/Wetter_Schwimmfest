from typing import IO
from urllib.error import HTTPError, URLError

import pandas as pd
import streamlit as st


HISTORICAL_DATA_URL = (
    "https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/chz/"
    "ogd-smn_chz_d_historical.csv"
)
RECENT_DATA_URL = (
    "https://data.geo.admin.ch/ch.meteoschweiz.ogd-smn/chz/"
    "ogd-smn_chz_d_recent.csv"
)

SOURCE_COLUMNS = {
    "station_abbr": "station_code",
    "reference_timestamp": "reference_timestamp",
    "tre200dx": "max_temperature_c",
    "rka150d0": "precipitation_mm",
}


class WeatherDataError(RuntimeError):
    """Die amtlichen Wetterdaten konnten nicht geladen werden."""


def read_weather_csv(source: str | IO[str], data_period: str) -> pd.DataFrame:
    """Lese die benötigten Spalten einer MeteoSchweiz-Tagesdatei ein."""
    data = pd.read_csv(
        source,
        sep=";",
        encoding="windows-1252",
        usecols=list(SOURCE_COLUMNS),
    ).rename(columns=SOURCE_COLUMNS)

    data["reference_timestamp"] = pd.to_datetime(
        data["reference_timestamp"],
        format="%d.%m.%Y %H:%M",
        utc=True,
    )
    for column in ("max_temperature_c", "precipitation_mm"):
        data[column] = pd.to_numeric(data[column], errors="raise")

    data["data_period"] = data_period
    return data


def combine_weather_data(
    historical_data: pd.DataFrame,
    recent_data: pd.DataFrame,
) -> pd.DataFrame:
    """Führe beide Zeiträume zusammen; die aktuelle Datei hat Vorrang."""
    return (
        pd.concat((historical_data, recent_data), ignore_index=True)
        .drop_duplicates(subset="reference_timestamp", keep="last")
        .sort_values("reference_timestamp")
        .reset_index(drop=True)
    )


@st.cache_data(ttl=12 * 60 * 60, show_spinner=False)
def load_cham_weather_data() -> pd.DataFrame:
    """Lade die Tageswerte für Cham direkt von MeteoSchweiz."""
    try:
        historical_data = read_weather_csv(HISTORICAL_DATA_URL, "historical")
        recent_data = read_weather_csv(RECENT_DATA_URL, "recent")
    except (HTTPError, URLError, OSError, ValueError, pd.errors.ParserError) as error:
        raise WeatherDataError(
            "Die Wetterdaten von MeteoSchweiz sind momentan nicht verfügbar."
        ) from error

    return combine_weather_data(historical_data, recent_data)
