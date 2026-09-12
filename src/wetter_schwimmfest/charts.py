import pandas as pd
import plotly.graph_objects as go

from wetter_schwimmfest.comparison import (
    CANDIDATES,
    WEATHER_INDICATORS,
)
from wetter_schwimmfest.hourly_comparison import HOURLY_INDICATORS


CANDIDATE_COLORS = {
    CANDIDATES[0]: "#123B63",
    CANDIDATES[1]: "#67B7E1",
}
CANDIDATE_FILL_COLORS = {
    CANDIDATES[0]: "rgba(18, 59, 99, 0.18)",
    CANDIDATES[1]: "rgba(103, 183, 225, 0.22)",
}


def _candidate_value_range(
    comparison: pd.DataFrame,
    indicator_name: str,
) -> tuple[float, float] | None:
    indicator = WEATHER_INDICATORS[indicator_name]
    if indicator.column == "fest_score":
        return (0, 100)

    values = comparison[indicator.column].dropna()
    if values.empty:
        return None

    minimum = float(values.min())
    maximum = float(values.max())
    padding = max((maximum - minimum) * 0.08, abs(maximum) * 0.03, 0.5)
    return (minimum - padding, maximum + padding)


def create_candidate_trend_chart(
    comparison: pd.DataFrame,
    indicator_name: str,
) -> go.Figure:
    """Erzeuge den Jahresverlauf für einen amtlichen Tagesindikator."""
    indicator = WEATHER_INDICATORS[indicator_name]
    figure = go.Figure()

    for candidate_number, candidate in enumerate(CANDIDATES, start=1):
        series = comparison.loc[comparison["candidate"] == candidate]
        quality_labels = series["data_period"].map(
            {"historical": "historisch", "recent": "laufendes Jahr (vorläufig)"}
        ).fillna("Wert fehlt")
        custom_data = list(
            zip(
                series["candidate_date"].dt.strftime("%d.%m.%Y"),
                quality_labels,
                strict=True,
            )
        )

        color = CANDIDATE_COLORS[candidate]
        figure.add_scatter(
            x=series["comparison_year"],
            y=series[indicator.column],
            name=candidate,
            legendrank=candidate_number,
            mode="lines+markers",
            connectgaps=False,
            customdata=custom_data,
            marker={
                "size": 8,
                "color": color,
                "symbol": [
                    "circle-open" if period == "recent" else "circle"
                    for period in series["data_period"]
                ],
            },
            line={"color": color},
            hovertemplate=(
                "%{customdata[0]}<br>"
                f"{indicator.label}: %{{y}} {indicator.unit}<br>"
                "%{customdata[1]}<extra>%{fullData.name}</extra>"
            ),
        )

    figure.update_layout(
        title="Jahresverlauf",
        xaxis={"title": "Jahr", "tickformat": "d", "automargin": True},
        yaxis={
            "title": f"{indicator.label} ({indicator.unit})",
            "range": _candidate_value_range(comparison, indicator_name),
            "automargin": True,
        },
        legend={
            "orientation": "h",
            "x": 0,
            "y": 1.02,
            "yanchor": "bottom",
            "title": None,
        },
        hovermode="closest",
        height=430,
        margin={"l": 10, "r": 10, "t": 85, "b": 55},
    )
    return figure


def create_candidate_distribution_chart(
    comparison: pd.DataFrame,
    indicator_name: str,
) -> go.Figure:
    """Erzeuge die Verteilung der Tageswerte für Datum 1 und Datum 2."""
    indicator = WEATHER_INDICATORS[indicator_name]
    figure = go.Figure()

    for candidate_number, candidate in enumerate(CANDIDATES, start=1):
        color = CANDIDATE_COLORS[candidate]
        values = comparison.loc[
            comparison["candidate"] == candidate,
            indicator.column,
        ].dropna()
        figure.add_box(
            y=values,
            name=candidate,
            legendrank=candidate_number,
            showlegend=False,
            boxpoints="outliers",
            marker={"color": color},
            line={"color": color},
            fillcolor=CANDIDATE_FILL_COLORS[candidate],
            hovertemplate=(
                f"{candidate}<br>{indicator.label}: %{{y}} {indicator.unit}"
                "<extra></extra>"
            ),
        )

    figure.update_layout(
        title="Verteilung",
        xaxis={"title": None, "automargin": True},
        yaxis={
            "range": _candidate_value_range(comparison, indicator_name),
            "automargin": True,
        },
        height=430,
        margin={"l": 10, "r": 10, "t": 85, "b": 55},
    )
    return figure


def create_hourly_profile_chart(
    profile: pd.DataFrame,
    indicator_name: str,
) -> go.Figure:
    """Zeige Median und mittlere 50-Prozent-Bandbreite für 36 Stunden."""
    indicator = HOURLY_INDICATORS[indicator_name]
    figure = go.Figure()

    # Schatten zuerst zeichnen, damit beide Medianlinien gut sichtbar darüber liegen.
    for candidate in CANDIDATES:
        series = profile.loc[profile["candidate"] == candidate]
        color = CANDIDATE_COLORS[candidate]
        fill_color = CANDIDATE_FILL_COLORS[candidate]
        figure.add_scatter(
            x=series["hour_position"],
            y=series["lower_value"],
            mode="lines",
            line={"width": 0, "color": color},
            hoverinfo="skip",
            showlegend=False,
        )
        figure.add_scatter(
            x=series["hour_position"],
            y=series["upper_value"],
            mode="lines",
            line={"width": 0, "color": color},
            fill="tonexty",
            fillcolor=fill_color,
            hoverinfo="skip",
            showlegend=False,
        )

    for candidate_number, candidate in enumerate(CANDIDATES, start=1):
        series = profile.loc[profile["candidate"] == candidate]
        color = CANDIDATE_COLORS[candidate]
        custom_data = list(
            zip(
                [
                    f"Datum, Stunde {hour}"
                    if hour <= 24
                    else f"Folgetag, Stunde {hour - 24}"
                    for hour in series["hour_position"]
                ],
                series["lower_value"],
                series["upper_value"],
                series["year_count"],
                strict=True,
            )
        )
        figure.add_scatter(
            x=series["hour_position"],
            y=series["median_value"],
            name=candidate,
            legendrank=candidate_number,
            mode="lines+markers",
            line={"color": color},
            customdata=custom_data,
            hovertemplate=(
                "%{customdata[0]}<br>"
                f"Median: %{{y:.1f}} {indicator.unit}<br>"
                f"Typische Bandbreite: %{{customdata[1]:.1f}}–%{{customdata[2]:.1f}} {indicator.unit}<br>"
                "Jahre: %{customdata[3]:.0f}<extra>%{fullData.name}</extra>"
            ),
        )

    tick_values = (1, 6, 12, 18, 24, 30, 36)
    tick_labels = (
        "1",
        "6",
        "12",
        "18",
        "24",
        "6<br>Folgetag",
        "12<br>Folgetag",
    )
    figure.update_layout(
        title=f"Typischer Stundenverlauf: {indicator.label}",
        xaxis={
            "title": "Lokale Stunde ab Datum",
            "tickmode": "array",
            "tickvals": tick_values,
            "ticktext": tick_labels,
            "range": [1, 36],
        },
        yaxis_title=f"{indicator.label} ({indicator.unit})",
        legend={
            "orientation": "h",
            "x": 0,
            "y": 1.02,
            "yanchor": "bottom",
            "title": None,
        },
        hovermode="x unified",
        height=460,
        margin={"l": 10, "r": 10, "t": 85, "b": 65},
    )
    figure.add_vline(
        x=24.5,
        line={"color": "#8A94A3", "dash": "dot", "width": 1},
    )
    return figure
