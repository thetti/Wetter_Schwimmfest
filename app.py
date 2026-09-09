import streamlit as st

from wetter_schwimmfest.demo import create_demo_chart
from wetter_schwimmfest.weather_data import (
    WeatherDataError,
    load_cham_weather_data,
)


def main() -> None:
    st.set_page_config(page_title="Wetter Schwimmfest", page_icon="🏊")

    st.title("Wettervergleich Schwimmfest")
    st.caption("Technischer Nachweis mit künstlichen Demodaten")

    indicator = st.selectbox(
        "Wetterindikator",
        ("Niederschlagssumme", "Höchsttemperatur"),
    )

    chart = create_demo_chart(indicator)
    st.plotly_chart(chart, width="stretch")

    st.subheader("Geladene amtliche Wetterdaten")
    st.markdown(
        "**Quelle:** [MeteoSchweiz Open Data]"
        "(https://opendatadocs.meteoswiss.ch/de/a-data-groundbased/"
        "a1-automatic-weather-stations)"
    )
    st.write("**Station:** Cham (CHZ), 443 m ü. M.")

    try:
        with st.spinner("Wetterdaten werden geladen …"):
            weather_data = load_cham_weather_data()
    except WeatherDataError as error:
        st.error(str(error))
    else:
        first_day = weather_data["reference_timestamp"].min().date()
        last_day = weather_data["reference_timestamp"].max().date()
        st.write(f"**Verfügbarer Zeitraum:** {first_day:%d.%m.%Y}–{last_day:%d.%m.%Y}")

        preview = weather_data.tail(5).loc[
            :,
            (
                "reference_timestamp",
                "max_temperature_c",
                "precipitation_mm",
                "data_period",
            ),
        ]
        preview = preview.rename(
            columns={
                "reference_timestamp": "Datum (UTC)",
                "max_temperature_c": "Höchsttemperatur (°C)",
                "precipitation_mm": "Niederschlagssumme (mm)",
                "data_period": "Datei",
            }
        )
        preview["Datum (UTC)"] = preview["Datum (UTC)"].dt.strftime("%d.%m.%Y")
        preview["Datei"] = preview["Datei"].replace(
            {"historical": "historisch", "recent": "laufendes Jahr"}
        )
        st.dataframe(preview, hide_index=True, width="stretch")


if __name__ == "__main__":
    main()
