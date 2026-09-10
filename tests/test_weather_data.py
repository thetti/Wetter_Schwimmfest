from io import StringIO
from unittest.mock import patch

import pandas as pd

from wetter_schwimmfest.weather_data import (
    HOURLY_SOURCE_COLUMNS,
    combine_weather_data,
    load_cham_weather_data,
    read_weather_csv,
)


def test_weather_csv_keeps_missing_measurement_as_missing() -> None:
    csv_data = StringIO(
        "station_abbr;reference_timestamp;tre200d0;tre200dx;tre200dn;"
        "ure200d0;fkl010d0;fu3010d1;rka150d0;gre000d0;sre000d0;sremaxdv\n"
        "CHZ;11.06.1993 00:00;15.0;17.8;12.1;70;2;24;25.6;180;240;50\n"
        "CHZ;12.06.1993 00:00;16.0;18.1;13.2;68;3;20;;190;300;60\n"
    )

    weather_data = read_weather_csv(csv_data, "historical")

    assert list(weather_data.columns) == [
        "station_code",
        "reference_timestamp",
        "mean_temperature_c",
        "max_temperature_c",
        "min_temperature_c",
        "mean_humidity_percent",
        "max_gust_kmh",
        "precipitation_mm",
        "global_radiation_wm2",
        "sunshine_minutes",
        "relative_sunshine_percent",
        "mean_wind_kmh",
        "data_period",
    ]
    assert weather_data.loc[0, "reference_timestamp"] == pd.Timestamp(
        "1993-06-11", tz="UTC"
    )
    assert pd.isna(weather_data.loc[1, "precipitation_mm"])
    assert weather_data.loc[0, "mean_wind_kmh"] == 7.2


def test_hourly_weather_csv_uses_hourly_parameter_mapping() -> None:
    csv_data = StringIO(
        "station_abbr;reference_timestamp;tre200h0;tre200hn;tre200hx;ure200h0;"
        "tde200h0;fu3010h0;fu3010h1;rre150h0;gre000h0;sre000h0\n"
        "CHZ;09.08.2025 12:00;24;23;25;55;14;8;20;0.2;500;60\n"
    )

    weather_data = read_weather_csv(
        csv_data,
        "historical",
        HOURLY_SOURCE_COLUMNS,
    )

    assert weather_data.loc[0, "hourly_mean_temperature_c"] == 24
    assert weather_data.loc[0, "hourly_precipitation_mm"] == 0.2
    assert weather_data.loc[0, "hourly_sunshine_minutes"] == 60


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
