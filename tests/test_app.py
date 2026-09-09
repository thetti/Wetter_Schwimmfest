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
            "precipitation_mm": (0.0, 0.4),
            "data_period": ("historical", "historical"),
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
    assert app.subheader[0].value == "Kalenderregel prüfen"
    assert app.number_input[0].label == "Vergleichsjahr"
    assert [metric.label for metric in app.metric] == [
        "Schulstart (Montag)",
        "Früher Kandidatentag (Samstag)",
        "Später Kandidatentag (Samstag)",
    ]
    assert app.subheader[1].value == "Geladene amtliche Wetterdaten"
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
