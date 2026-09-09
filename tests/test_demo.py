import math

from wetter_schwimmfest.demo import create_demo_chart


def test_demo_chart_shows_two_lines_and_keeps_missing_value_as_gap() -> None:
    chart = create_demo_chart("Niederschlagssumme")

    assert len(chart.data) == 2
    assert all(line.connectgaps is False for line in chart.data)
    assert any(
        value is None or (isinstance(value, float) and math.isnan(value))
        for value in chart.data[0].y
    )
