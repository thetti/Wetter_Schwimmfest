import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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


def create_candidate_chart(
    comparison: pd.DataFrame,
    indicator_name: str,
) -> go.Figure:
    """Erzeuge das Liniendiagramm für einen amtlichen Tagesindikator."""
    indicator = WEATHER_INDICATORS[indicator_name]
    figure = make_subplots(
        rows=1,
        cols=2,
        shared_yaxes=True,
        column_widths=(0.84, 0.16),
        horizontal_spacing=0.04,
        subplot_titles=("Jahresverlauf", "Verteilung"),
    )

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

        color = CANDIDATE_COLORS[candidate]
        figure.add_scatter(
            x=series["comparison_year"],
            y=series[indicator.column],
            name=candidate,
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
            row=1,
            col=1,
        )

        figure.add_box(
            y=series[indicator.column].dropna(),
            name="Früher" if candidate == CANDIDATES[0] else "Später",
            legendgroup=candidate,
            showlegend=False,
            boxpoints="outliers",
            marker={"color": color},
            line={"color": color},
            fillcolor=CANDIDATE_FILL_COLORS[candidate],
            hovertemplate=(
                f"{candidate}<br>{indicator.label}: %{{y}} {indicator.unit}"
                "<extra></extra>"
            ),
            row=1,
            col=2,
        )

    figure.update_layout(
        title=f"{indicator.label} an den Kandidatentagen",
        xaxis={"title": "Vergleichsjahr", "tickformat": "d"},
        xaxis2={"title": "Kandidatentag"},
        yaxis={
            "title": f"{indicator.label} ({indicator.unit})",
            "range": [0, 100] if indicator.column == "fest_score" else None,
        },
        legend_title="Vergleichstag",
        hovermode="closest",
    )
    return figure


def create_hourly_profile_chart(
    profile: pd.DataFrame,
    indicator_name: str,
) -> go.Figure:
    """Zeige Median und mittlere 50-Prozent-Bandbreite für 36 Stunden."""
    indicator = HOURLY_INDICATORS[indicator_name]
    figure = go.Figure()

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
        custom_data = list(
            zip(
                [
                    f"Kandidatentag, Stunde {hour}"
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

    tick_values = (1, 4, 8, 12, 16, 20, 24, 25, 28, 32, 36)
    tick_labels = (
        "1",
        "4",
        "8",
        "12",
        "16",
        "20",
        "24",
        "1<br>Folgetag",
        "4<br>Folgetag",
        "8<br>Folgetag",
        "12<br>Folgetag",
    )
    figure.update_layout(
        title=f"Typischer Stundenverlauf: {indicator.label}",
        xaxis={
            "title": "Lokale Stunde ab Kandidatentag",
            "tickmode": "array",
            "tickvals": tick_values,
            "ticktext": tick_labels,
            "range": [1, 36],
        },
        yaxis_title=f"{indicator.label} ({indicator.unit})",
        legend_title="Vergleichstag",
        hovermode="x unified",
    )
    figure.add_vline(
        x=24.5,
        line={"color": "#8A94A3", "dash": "dot", "width": 1},
    )
    return figure
