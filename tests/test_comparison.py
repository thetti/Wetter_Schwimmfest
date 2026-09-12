import math

import pandas as pd

from wetter_schwimmfest.charts import (
    CANDIDATE_COLORS,
    create_candidate_distribution_chart,
    create_candidate_trend_chart,
)
from wetter_schwimmfest.comparison import (
    EARLIER_CANDIDATE,
    LATER_CANDIDATE,
    build_candidate_comparison,
)


def make_weather_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "reference_timestamp": pd.to_datetime(
                (
                    "2025-08-09",
                    "2025-08-16",
                    "2026-08-08",
                ),
                utc=True,
            ),
            "max_temperature_c": (32.6, 29.9, 28.0),
            "mean_temperature_c": (24.0, 23.0, 22.0),
            "min_temperature_c": (16.0, 15.0, 14.0),
            "mean_wind_kmh": (8.0, 10.0, 12.0),
            "max_gust_kmh": (25.0, 30.0, 35.0),
            "mean_humidity_percent": (55.0, 60.0, 65.0),
            "precipitation_mm": (0.0, 0.4, None),
            "sunshine_minutes": (600.0, 500.0, 400.0),
            "relative_sunshine_percent": (90.0, 80.0, 70.0),
            "global_radiation_wm2": (260.0, 240.0, 220.0),
            "data_period": ("historical", "historical", "recent"),
        }
    )


def test_comparison_uses_candidate_dates_of_complete_years() -> None:
    comparison = build_candidate_comparison(make_weather_data())

    assert list(comparison["comparison_year"]) == [2025, 2025]
    assert list(comparison["candidate"]) == [EARLIER_CANDIDATE, LATER_CANDIDATE]
    assert list(comparison["candidate_date"].dt.strftime("%d.%m.%Y")) == [
        "09.08.2025",
        "16.08.2025",
    ]
    assert list(comparison["max_temperature_c"]) == [32.6, 29.9]
    assert list(comparison["precipitation_mm"]) == [0.0, 0.4]


def test_daily_charts_have_two_lines_and_two_matching_boxplots() -> None:
    weather_data = make_weather_data().iloc[:2].copy()
    weather_data.loc[0, "precipitation_mm"] = None
    comparison = build_candidate_comparison(weather_data)

    trend_chart = create_candidate_trend_chart(comparison, "Niederschlagssumme")
    distribution_chart = create_candidate_distribution_chart(
        comparison,
        "Niederschlagssumme",
    )
    lines = list(trend_chart.data)
    boxes = list(distribution_chart.data)

    assert [line.name for line in lines] == [
        EARLIER_CANDIDATE,
        LATER_CANDIDATE,
    ]
    assert [box.name for box in boxes] == [EARLIER_CANDIDATE, LATER_CANDIDATE]
    assert [line.line.color for line in lines] == [
        CANDIDATE_COLORS[EARLIER_CANDIDATE],
        CANDIDATE_COLORS[LATER_CANDIDATE],
    ]
    assert [box.line.color for box in boxes] == [
        CANDIDATE_COLORS[EARLIER_CANDIDATE],
        CANDIDATE_COLORS[LATER_CANDIDATE],
    ]
    assert all(line.connectgaps is False for line in lines)
    assert math.isnan(lines[0].y[0])
    assert len(boxes[0].y) == 0
    assert list(boxes[1].y) == [0.4]
    assert trend_chart.layout.yaxis.title.text == "Niederschlagssumme (mm)"
    assert trend_chart.layout.yaxis.range == distribution_chart.layout.yaxis.range
    assert lines[0].customdata[0][0] == "09.08.2025"


def test_recent_values_use_open_markers_and_temperature_unit() -> None:
    weather_data = make_weather_data().iloc[[0, 2]].reset_index(drop=True)
    weather_data.loc[1, "reference_timestamp"] = pd.Timestamp(
        "2025-08-16", tz="UTC"
    )
    comparison = build_candidate_comparison(weather_data)

    chart = create_candidate_trend_chart(comparison, "Höchsttemperatur")
    lines = list(chart.data)

    assert chart.layout.yaxis.title.text == "Höchsttemperatur (°C)"
    assert lines[1].marker.symbol[0] == "circle-open"
    assert lines[1].customdata[0][1] == "laufendes Jahr (vorläufig)"


def test_fest_indicator_chart_uses_fixed_scale() -> None:
    comparison = build_candidate_comparison(make_weather_data().iloc[:2])

    trend_chart = create_candidate_trend_chart(comparison, "Fest-Indikator")
    distribution_chart = create_candidate_distribution_chart(
        comparison,
        "Fest-Indikator",
    )

    assert tuple(trend_chart.layout.yaxis.range) == (0, 100)
    assert tuple(distribution_chart.layout.yaxis.range) == (0, 100)
