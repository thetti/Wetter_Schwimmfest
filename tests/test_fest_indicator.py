import math

import pandas as pd

from wetter_schwimmfest.fest_indicator import (
    FEST_SCORE_RULES,
    calculate_fest_score,
)


def ideal_day() -> pd.Series:
    return pd.Series(
        {
            "precipitation_mm": 0.0,
            "mean_temperature_c": 23.0,
            "max_temperature_c": 27.0,
            "mean_wind_kmh": 5.0,
            "max_gust_kmh": 20.0,
            "mean_humidity_percent": 50.0,
        }
    )


def test_ideal_day_scores_100_points() -> None:
    assert calculate_fest_score(ideal_day()) == 100.0


def test_rain_score_is_linearly_weighted() -> None:
    day = ideal_day()
    day["precipitation_mm"] = 5.0

    assert calculate_fest_score(day) == 82.0


def test_missing_core_measurement_keeps_score_missing() -> None:
    day = ideal_day()
    day["max_gust_kmh"] = None

    assert math.isnan(calculate_fest_score(day))


def test_score_weights_add_up_to_one() -> None:
    assert sum(rule.weight for rule in FEST_SCORE_RULES) == 1.0
