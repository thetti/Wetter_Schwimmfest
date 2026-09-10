from pathlib import Path
from unittest.mock import patch

import pandas as pd
from streamlit.testing.v1 import AppTest

from wetter_schwimmfest.weather_data import WeatherDataError


def test_dashboard_starts_without_error() -> None:
    app_file = Path(__file__).parents[1] / "app.py"
    test_data = pd.DataFrame(
        {
            "station_code": ("CHZ", "CHZ"),
            "reference_timestamp": pd.to_datetime(
                ("2025-08-09", "2025-08-16"), utc=True
            ),
            "max_temperature_c": (32.6, 29.9),
            "mean_temperature_c": (24.0, 23.0),
            "min_temperature_c": (16.0, 15.0),
            "mean_wind_kmh": (8.0, 10.0),
            "max_gust_kmh": (25.0, 30.0),
            "mean_humidity_percent": (55.0, 60.0),
            "precipitation_mm": (0.0, 0.4),
            "sunshine_minutes": (600.0, 500.0),
            "relative_sunshine_percent": (90.0, 80.0),
            "global_radiation_wm2": (260.0, 240.0),
            "data_period": ("historical", "historical"),
        }
    )
    hourly_test_data = pd.DataFrame(
        {
            "reference_timestamp": pd.to_datetime(
                ("2025-08-08 23:00", "2025-08-15 23:00"), utc=True
            ),
            "hourly_precipitation_mm": (0.0, 0.2),
        }
    )

    with (
        patch(
            "wetter_schwimmfest.weather_data.load_cham_weather_data",
            return_value=test_data,
        ),
        patch(
            "wetter_schwimmfest.weather_data.load_cham_hourly_weather_data",
            return_value=hourly_test_data,
        ),
    ):
        app = AppTest.from_file(app_file).run()

    assert not app.exception
    assert app.title[0].value == "Wettervergleich Schwimmfest"
    assert [selectbox.value for selectbox in app.selectbox] == [
        "Niederschlagssumme",
        "Niederschlag",
    ]
    assert len(app.get("plotly_chart")) == 2
    assert app.subheader[0].value == "Tageswerte im Jahresvergleich"
    assert app.subheader[1].value == "Typischer Stundenverlauf"
    assert app.subheader[2].value == "Kalenderregel prüfen"
    assert app.number_input[0].label == "Vergleichsjahr"
    assert [metric.label for metric in app.metric] == [
        "Schulstart (Montag)",
        "Früher Kandidatentag (Samstag)",
        "Später Kandidatentag (Samstag)",
    ]
    assert app.subheader[3].value == "Geladene amtliche Tageswerte"
    assert len(app.dataframe) == 1


def test_dashboard_shows_a_clear_message_when_download_fails() -> None:
    app_file = Path(__file__).parents[1] / "app.py"
    daily_message = "Die Tageswerte von MeteoSchweiz sind momentan nicht verfügbar."
    hourly_message = "Die Stundenwerte von MeteoSchweiz sind momentan nicht verfügbar."

    with (
        patch(
            "wetter_schwimmfest.weather_data.load_cham_weather_data",
            side_effect=WeatherDataError(daily_message),
        ),
        patch(
            "wetter_schwimmfest.weather_data.load_cham_hourly_weather_data",
            side_effect=WeatherDataError(hourly_message),
        ),
    ):
        app = AppTest.from_file(app_file).run()

    assert not app.exception
    assert [error.value for error in app.error] == [daily_message, hourly_message]
