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
                ("2025-12-31", "2026-01-01"), utc=True
            ),
            "max_temperature_c": (5.0, 6.0),
            "precipitation_mm": (1.0, 0.0),
            "data_period": ("historical", "recent"),
        }
    )

    with patch(
        "wetter_schwimmfest.weather_data.load_cham_weather_data",
        return_value=test_data,
    ):
        app = AppTest.from_file(app_file).run()

    assert not app.exception
    assert app.title[0].value == "Wettervergleich Schwimmfest"
    assert app.selectbox[0].value == "Niederschlagssumme"
    assert len(app.get("plotly_chart")) == 1
    assert app.subheader[0].value == "Geladene amtliche Wetterdaten"
    assert len(app.dataframe) == 1


def test_dashboard_shows_a_clear_message_when_download_fails() -> None:
    app_file = Path(__file__).parents[1] / "app.py"
    message = "Die Wetterdaten von MeteoSchweiz sind momentan nicht verfügbar."

    with patch(
        "wetter_schwimmfest.weather_data.load_cham_weather_data",
        side_effect=WeatherDataError(message),
    ):
        app = AppTest.from_file(app_file).run()

    assert not app.exception
    assert app.error[0].value == message
