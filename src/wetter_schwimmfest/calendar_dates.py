from dataclasses import dataclass
from datetime import date, timedelta


@dataclass(frozen=True)
class CandidateDates:
    comparison_year: int
    school_start: date
    later_candidate_day: date
    earlier_candidate_day: date


def calculate_candidate_dates(comparison_year: int) -> CandidateDates:
    """Berechne Schulstart und Kandidatentage für ein Vergleichsjahr."""
    first_possible_day = date(comparison_year, 8, 16)
    days_until_monday = (7 - first_possible_day.weekday()) % 7
    school_start = first_possible_day + timedelta(days=days_until_monday)
    later_candidate_day = school_start - timedelta(days=2)
    earlier_candidate_day = later_candidate_day - timedelta(days=7)

    return CandidateDates(
        comparison_year=comparison_year,
        school_start=school_start,
        later_candidate_day=later_candidate_day,
        earlier_candidate_day=earlier_candidate_day,
    )
