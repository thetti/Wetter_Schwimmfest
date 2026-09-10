import pandas as pd
import plotly.graph_objects as go

from wetter_schwimmfest.comparison import (
    CANDIDATES,
    WEATHER_INDICATORS,
)
from wetter_schwimmfest.hourly_comparison import HOURLY_INDICATORS


CANDIDATE_COLORS = {
    CANDIDATES[0]: "#1f77b4",
    CANDIDATES[1]: "#e76f51",
}


def create_candidate_chart(
    comparison: pd.DataFrame,
    indicator_name: str,
) -> go.Figure:
    """Erzeuge das Liniendiagramm für einen amtlichen Tagesindikator."""
    indicator = WEATHER_INDICATORS[indicator_name]
    figure = go.Figure()

    for candidate in CANDIDATES:
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

        figure.add_scatter(
            x=series["comparison_year"],
            y=series[indicator.column],
            name=candidate,
            mode="lines+markers",
            connectgaps=False,
            customdata=custom_data,
            marker={
                "size": 8,
                "symbol": [
                    "circle-open" if period == "recent" else "circle"
                    for period in series["data_period"]
                ],
            },
            hovertemplate=(
                "%{customdata[0]}<br>"
                f"{indicator.label}: %{{y}} {indicator.unit}<br>"
                "%{customdata[1]}<extra>%{fullData.name}</extra>"
            ),
        )

    figure.update_layout(
        title=f"{indicator.label} an den Kandidatentagen",
        xaxis={"title": "Vergleichsjahr", "tickformat": "d"},
        yaxis={
            "title": f"{indicator.label} ({indicator.unit})",
            "range": [0, 100] if indicator.column == "fest_score" else None,
        },
        legend_title="Vergleichstag",
        hovermode="x unified",
    )
    return figure


def create_hourly_profile_chart(
    profile: pd.DataFrame,
    indicator_name: str,
) -> go.Figure:
    """Zeige Mittelwert und mittlere 50-Prozent-Bandbreite je Stunde."""
    indicator = HOURLY_INDICATORS[indicator_name]
    figure = go.Figure()

    for candidate in CANDIDATES:
        series = profile.loc[profile["candidate"] == candidate]
        color = CANDIDATE_COLORS[candidate]
        fill_color = (
            "rgba(31, 119, 180, 0.18)"
            if candidate == CANDIDATES[0]
            else "rgba(231, 111, 81, 0.18)"
        )
        figure.add_scatter(
            x=series["hour_of_day"],
            y=series["lower_value"],
            mode="lines",
            line={"width": 0, "color": color},
            hoverinfo="skip",
            showlegend=False,
        )
        figure.add_scatter(
            x=series["hour_of_day"],
            y=series["upper_value"],
            mode="lines",
            line={"width": 0, "color": color},
            fill="tonexty",
            fillcolor=fill_color,
            hoverinfo="skip",
            showlegend=False,
        )
        custom_data = list(
            zip(
                series["lower_value"],
                series["upper_value"],
                series["year_count"],
                strict=True,
            )
        )
        figure.add_scatter(
            x=series["hour_of_day"],
            y=series["mean_value"],
            name=candidate,
            mode="lines+markers",
            line={"color": color},
            customdata=custom_data,
            hovertemplate=(
                "Stunde %{x}<br>"
                f"Mittelwert: %{{y:.1f}} {indicator.unit}<br>"
                f"Typische Bandbreite: %{{customdata[0]:.1f}}–%{{customdata[1]:.1f}} {indicator.unit}<br>"
                "Jahre: %{customdata[2]:.0f}<extra>%{fullData.name}</extra>"
            ),
        )

    figure.update_layout(
        title=f"Typischer Stundenverlauf: {indicator.label}",
        xaxis={
            "title": "Lokale Stunde am Tag",
            "tickmode": "linear",
            "tick0": 1,
            "dtick": 1,
            "range": [1, 24],
        },
        yaxis_title=f"{indicator.label} ({indicator.unit})",
        legend_title="Vergleichstag",
        hovermode="x unified",
    )
    return figure
