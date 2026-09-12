from datetime import date

import pandas as pd

from wetter_schwimmfest.calendar_dates import calculate_candidate_dates
from wetter_schwimmfest.charts import CANDIDATE_COLORS, create_hourly_profile_chart
from wetter_schwimmfest.comparison import EARLIER_CANDIDATE, LATER_CANDIDATE
from wetter_schwimmfest.hourly_comparison import build_hourly_candidate_profile


def interval_end_utc(candidate_day: date, hour_position: int) -> pd.Timestamp:
    local_start = pd.Timestamp(candidate_day, tz="Europe/Zurich") + pd.Timedelta(
        hours=hour_position - 1
    )
    return (local_start + pd.Timedelta(hours=1)).tz_convert("UTC")


def make_hourly_data() -> pd.DataFrame:
    rows = []
    first_hour_values = (10.0, 20.0, 100.0)
    for year, first_hour_value in zip(
        (2023, 2024, 2025), first_hour_values, strict=True
    ):
        candidate_dates = calculate_candidate_dates(year)
        for candidate_offset, candidate_day in enumerate(
            (
                candidate_dates.earlier_candidate_day,
                candidate_dates.later_candidate_day,
            )
        ):
            for hour_position in (1, 24, 25, 36):
                rows.append(
                    {
                        "reference_timestamp": interval_end_utc(
                            candidate_day, hour_position
                        ),
                        "hourly_mean_temperature_c": (
                            first_hour_value
                            + candidate_offset
                            + hour_position
                            - 1
                        ),
                    }
                )
    return pd.DataFrame(rows)


def test_hourly_profile_uses_median_and_continues_to_next_noon() -> None:
    profile = build_hourly_candidate_profile(make_hourly_data(), "Mittlere Temperatur")
    earlier = profile.loc[profile["candidate"] == EARLIER_CANDIDATE]
    first_hour = earlier.loc[earlier["hour_position"] == 1].iloc[0]

    assert list(earlier["hour_position"]) == list(range(1, 37))
    assert first_hour["median_value"] == 20.0
    assert first_hour["lower_value"] == 15.0
    assert first_hour["upper_value"] == 60.0
    assert first_hour["year_count"] == 3
    assert earlier.loc[earlier["hour_position"] == 24, "median_value"].iloc[0] == 43.0
    assert earlier.loc[earlier["hour_position"] == 25, "median_value"].iloc[0] == 44.0
    assert earlier.loc[earlier["hour_position"] == 36, "median_value"].iloc[0] == 55.0


def test_hourly_chart_has_two_median_lines_and_two_bands() -> None:
    profile = build_hourly_candidate_profile(make_hourly_data(), "Mittlere Temperatur")

    chart = create_hourly_profile_chart(profile, "Mittlere Temperatur")
    median_lines = [trace for trace in chart.data if trace.showlegend is not False]

    assert len(chart.data) == 6
    assert [trace.name for trace in median_lines] == [
        EARLIER_CANDIDATE,
        LATER_CANDIDATE,
    ]
    assert [trace.line.color for trace in median_lines] == [
        CANDIDATE_COLORS[EARLIER_CANDIDATE],
        CANDIDATE_COLORS[LATER_CANDIDATE],
    ]
    assert sum(trace.fill == "tonexty" for trace in chart.data) == 2
    assert tuple(chart.layout.xaxis.range) == (1, 36)
    assert chart.layout.xaxis.title.text == "Lokale Stunde ab Datum"
    assert chart.layout.yaxis.title.text == "Mittlere Temperatur (°C)"
    assert chart.layout.shapes[0].x0 == 24.5
