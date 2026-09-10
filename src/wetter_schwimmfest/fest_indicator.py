from dataclasses import dataclass
from math import isnan

import pandas as pd


@dataclass(frozen=True)
class FestScoreRule:
    column: str
    label: str
    unit: str
    weight: float
    points: tuple[tuple[float, float], ...]


# Jeder Messwert wird zuerst über gut lesbare Stützpunkte auf 0 bis 100
# abgebildet. Zwischen zwei Punkten wird geradlinig gerechnet. Die Gewichte
# ergeben zusammen 100 Prozent und ändern sich weder zwischen Jahren noch
# zwischen Stationen.
FEST_SCORE_RULES = (
    FestScoreRule(
        column="precipitation_mm",
        label="Niederschlag",
        unit="mm/Tag",
        weight=0.30,
        points=((0, 100), (0.5, 90), (2, 70), (5, 40), (10, 10), (20, 0)),
    ),
    FestScoreRule(
        column="mean_temperature_c",
        label="Tagesmitteltemperatur",
        unit="°C",
        weight=0.25,
        points=(
            (5, 0),
            (12, 20),
            (16, 60),
            (20, 100),
            (26, 100),
            (30, 60),
            (35, 0),
        ),
    ),
    FestScoreRule(
        column="max_temperature_c",
        label="Höchsttemperatur",
        unit="°C",
        weight=0.10,
        points=((10, 0), (18, 50), (22, 100), (30, 100), (35, 50), (40, 0)),
    ),
    FestScoreRule(
        column="mean_wind_kmh",
        label="Mittlerer Wind",
        unit="km/h",
        weight=0.10,
        points=((0, 100), (10, 100), (20, 70), (30, 30), (40, 0)),
    ),
    FestScoreRule(
        column="max_gust_kmh",
        label="Stärkste Böe",
        unit="km/h",
        weight=0.15,
        points=((0, 100), (30, 100), (50, 60), (70, 20), (90, 0)),
    ),
    FestScoreRule(
        column="mean_humidity_percent",
        label="Relative Luftfeuchtigkeit",
        unit="%",
        weight=0.10,
        points=(
            (0, 50),
            (20, 70),
            (35, 100),
            (65, 100),
            (75, 80),
            (85, 40),
            (95, 0),
            (100, 0),
        ),
    ),
)


def score_between_points(
    value: float,
    points: tuple[tuple[float, float], ...],
) -> float:
    """Bewerte einen Messwert anhand linear verbundener Stützpunkte."""
    if pd.isna(value):
        return float("nan")
    if value <= points[0][0]:
        return points[0][1]
    if value >= points[-1][0]:
        return points[-1][1]

    for (left_value, left_score), (right_value, right_score) in zip(
        points,
        points[1:],
    ):
        if left_value <= value <= right_value:
            share = (value - left_value) / (right_value - left_value)
            return left_score + share * (right_score - left_score)

    raise ValueError("Der Messwert liegt ausserhalb der Bewertungsstützpunkte.")


def calculate_fest_score(row: pd.Series) -> float:
    """Berechne den Fest-Indikator; bei fehlenden Kernwerten bleibt er leer."""
    weighted_scores = []
    for rule in FEST_SCORE_RULES:
        score = score_between_points(row[rule.column], rule.points)
        if isnan(score):
            return float("nan")
        weighted_scores.append(score * rule.weight)

    return round(sum(weighted_scores), 1)


def add_fest_score(data: pd.DataFrame) -> pd.DataFrame:
    """Ergänze den Fest-Indikator, ohne die amtlichen Messwerte zu verändern."""
    result = data.copy()
    result["fest_score"] = result.apply(calculate_fest_score, axis="columns")
    return result


def fest_score_explanation() -> pd.DataFrame:
    """Liefere die vollständigen Regeln in menschenlesbarer Tabellenform."""
    return pd.DataFrame(
        {
            "Teilwert": [rule.label for rule in FEST_SCORE_RULES],
            "Gewicht": [f"{rule.weight:.0%}" for rule in FEST_SCORE_RULES],
            "Stützpunkte Messwert → Punkte": [
                ", ".join(
                    f"{value:g} {rule.unit} → {score:g}"
                    for value, score in rule.points
                )
                for rule in FEST_SCORE_RULES
            ],
        }
    )
