from datetime import date

import pytest

from wetter_schwimmfest.calendar_dates import calculate_candidate_dates


@pytest.mark.parametrize(
    ("year", "school_start", "later_day", "earlier_day"),
    (
        (2026, date(2026, 8, 17), date(2026, 8, 15), date(2026, 8, 8)),
        (2027, date(2027, 8, 16), date(2027, 8, 14), date(2027, 8, 7)),
        (2028, date(2028, 8, 21), date(2028, 8, 19), date(2028, 8, 12)),
    ),
)
def test_candidate_dates_match_documented_examples(
    year: int,
    school_start: date,
    later_day: date,
    earlier_day: date,
) -> None:
    result = calculate_candidate_dates(year)

    assert result.school_start == school_start
    assert result.later_candidate_day == later_day
    assert result.earlier_candidate_day == earlier_day


def test_august_15_on_monday_is_not_the_school_start() -> None:
    result = calculate_candidate_dates(2022)

    assert result.school_start == date(2022, 8, 22)
    assert result.later_candidate_day == date(2022, 8, 20)
    assert result.earlier_candidate_day == date(2022, 8, 13)


def test_weekdays_and_distance_are_always_correct() -> None:
    for year in range(1990, 2051):
        result = calculate_candidate_dates(year)

        assert result.school_start.weekday() == 0
        assert result.later_candidate_day.weekday() == 5
        assert result.earlier_candidate_day.weekday() == 5
        assert (result.later_candidate_day - result.earlier_candidate_day).days == 7
