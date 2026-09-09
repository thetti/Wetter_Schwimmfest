from io import StringIO
from unittest.mock import patch

import pandas as pd

from wetter_schwimmfest.weather_data import (
    combine_weather_data,
    load_cham_weather_data,
    read_weather_csv,
)


def test_weather_csv_keeps_missing_measurement_as_missing() -> None:
    csv_data = StringIO(
        "station_abbr;reference_timestamp;tre200dx;rka150d0\n"
        "CHZ;11.06.1993 00:00;17.8;25.6\n"
        "CHZ;12.06.1993 00:00;18.1;\n"
    )

    weather_data = read_weather_csv(csv_data, "historical")

    assert list(weather_data.columns) == [
        "station_code",
        "reference_timestamp",
        "max_temperature_c",
        "precipitation_mm",
        "data_period",
    ]
    assert weather_data.loc[0, "reference_timestamp"] == pd.Timestamp(
        "1993-06-11", tz="UTC"
    )
    assert pd.isna(weather_data.loc[1, "precipitation_mm"])


def test_recent_data_replaces_duplicate_historical_day() -> None:
    historical_data = pd.DataFrame(
        {
            "reference_timestamp": pd.to_datetime(
                ("2025-12-31", "2026-01-01"), utc=True
            ),
            "max_temperature_c": (5.0, 6.0),
            "data_period": ("historical", "historical"),
        }
    )
    recent_data = pd.DataFrame(
        {
            "reference_timestamp": pd.to_datetime(
                ("2026-01-01", "2026-01-02"), utc=True
            ),
            "max_temperature_c": (7.0, 8.0),
            "data_period": ("recent", "recent"),
        }
    )

    combined_data = combine_weather_data(historical_data, recent_data)

    assert list(combined_data["max_temperature_c"]) == [5.0, 7.0, 8.0]
    assert list(combined_data["data_period"]) == [
        "historical",
        "recent",
        "recent",
    ]


def test_cham_data_is_not_loaded_again_while_cached() -> None:
    historical_data = pd.DataFrame(
        {
            "reference_timestamp": pd.to_datetime(("2025-12-31",), utc=True),
        }
    )
    recent_data = pd.DataFrame(
        {
            "reference_timestamp": pd.to_datetime(("2026-01-01",), utc=True),
        }
    )
    load_cham_weather_data.clear()

    with patch(
        "wetter_schwimmfest.weather_data.read_weather_csv",
        side_effect=(historical_data, recent_data),
    ) as read_csv:
        load_cham_weather_data()
        load_cham_weather_data()

    assert read_csv.call_count == 2
    load_cham_weather_data.clear()
