from datetime import date

import pandas as pd

from wetter_schwimmfest.charts import create_hourly_profile_chart
from wetter_schwimmfest.hourly_comparison import build_hourly_candidate_profile


def interval_end_utc(candidate_day: date, hour_of_day: int) -> pd.Timestamp:
    local_start = pd.Timestamp(candidate_day, tz="Europe/Zurich") + pd.Timedelta(
        hours=hour_of_day - 1
    )
    return (local_start + pd.Timedelta(hours=1)).tz_convert("UTC")


def make_hourly_data() -> pd.DataFrame:
    rows = []
    values = {
        date(2024, 8, 10): (10.0, 20.0),
        date(2024, 8, 17): (20.0, 30.0),
        date(2025, 8, 9): (30.0, 40.0),
        date(2025, 8, 16): (40.0, 50.0),
    }
    for candidate_day, (first_hour, last_hour) in values.items():
        rows.extend(
            (
                {
                    "reference_timestamp": interval_end_utc(candidate_day, 1),
                    "hourly_mean_temperature_c": first_hour,
                },
                {
                    "reference_timestamp": interval_end_utc(candidate_day, 24),
                    "hourly_mean_temperature_c": last_hour,
                },
            )
        )
    return pd.DataFrame(rows)


def test_hourly_profile_uses_local_hours_and_historical_distribution() -> None:
    profile = build_hourly_candidate_profile(make_hourly_data(), "Mittlere Temperatur")
    earlier_first_hour = profile.loc[
        (profile["candidate"] == "Früher Kandidatentag")
        & (profile["hour_of_day"] == 1)
    ].iloc[0]
    earlier_last_hour = profile.loc[
        (profile["candidate"] == "Früher Kandidatentag")
        & (profile["hour_of_day"] == 24)
    ].iloc[0]

    assert earlier_first_hour["mean_value"] == 20.0
    assert earlier_first_hour["lower_value"] == 15.0
    assert earlier_first_hour["upper_value"] == 25.0
    assert earlier_first_hour["year_count"] == 2
    assert earlier_last_hour["mean_value"] == 30.0


def test_hourly_chart_has_two_mean_lines_and_two_bands() -> None:
    profile = build_hourly_candidate_profile(make_hourly_data(), "Mittlere Temperatur")

    chart = create_hourly_profile_chart(profile, "Mittlere Temperatur")

    assert len(chart.data) == 6
    assert [trace.name for trace in chart.data if trace.showlegend is not False] == [
        "Früher Kandidatentag",
        "Später Kandidatentag",
    ]
    assert sum(trace.fill == "tonexty" for trace in chart.data) == 2
    assert chart.layout.xaxis.title.text == "Lokale Stunde am Tag"
    assert chart.layout.yaxis.title.text == "Mittlere Temperatur (°C)"
