from pathlib import Path

from streamlit.testing.v1 import AppTest


def test_dashboard_starts_without_error() -> None:
    app_file = Path(__file__).parents[1] / "app.py"
    app = AppTest.from_file(app_file).run()

    assert not app.exception
    assert app.title[0].value == "Wettervergleich Schwimmfest"
    assert app.selectbox[0].value == "Niederschlagssumme"
    assert len(app.get("plotly_chart")) == 1
