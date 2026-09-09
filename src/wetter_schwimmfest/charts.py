import pandas as pd
import plotly.graph_objects as go

from wetter_schwimmfest.comparison import (
    CANDIDATES,
    WEATHER_INDICATORS,
)


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
        yaxis_title=f"{indicator.label} ({indicator.unit})",
        legend_title="Vergleichstag",
        hovermode="x unified",
    )
    return figure
