from dataclasses import dataclass

import pandas as pd
import plotly.graph_objects as go


@dataclass(frozen=True)
class DemoIndicator:
    unit: str
    earlier_values: tuple[float | None, ...]
    later_values: tuple[float | None, ...]


DEMO_INDICATORS = {
    "Niederschlagssumme": DemoIndicator(
        unit="mm",
        earlier_values=(2.0, None, 8.0, 1.0),
        later_values=(0.0, 5.0, 3.0, 7.0),
    ),
    "Höchsttemperatur": DemoIndicator(
        unit="°C",
        earlier_values=(25.0, None, 29.0, 24.0),
        later_values=(23.0, 27.0, 26.0, 28.0),
    ),
}


def create_demo_chart(indicator_name: str) -> go.Figure:
    """Erzeuge das vereinbarte Liniendiagramm mit künstlichen Daten."""
    indicator = DEMO_INDICATORS[indicator_name]
    data = pd.DataFrame(
        {
            "Jahr": (2022, 2023, 2024, 2025),
            "Früher Kandidatentag": indicator.earlier_values,
            "Später Kandidatentag": indicator.later_values,
        }
    )

    figure = go.Figure()
    for series_name in ("Früher Kandidatentag", "Später Kandidatentag"):
        figure.add_scatter(
            x=data["Jahr"],
            y=data[series_name],
            name=series_name,
            mode="lines+markers",
            connectgaps=False,
        )

    figure.update_layout(
        title=f"{indicator_name} – Demodaten",
        xaxis={"title": "Jahr", "tickmode": "linear", "dtick": 1},
        yaxis_title=f"{indicator_name} ({indicator.unit})",
        legend_title="Vergleichstag",
    )
    return figure
