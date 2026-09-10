from datetime import date

import streamlit as st

from wetter_schwimmfest.calendar_dates import calculate_candidate_dates
from wetter_schwimmfest.charts import (
    create_candidate_chart,
    create_hourly_profile_chart,
)
from wetter_schwimmfest.comparison import WEATHER_INDICATORS, build_candidate_comparison
from wetter_schwimmfest.fest_indicator import fest_score_explanation
from wetter_schwimmfest.hourly_comparison import (
    HOURLY_INDICATORS,
    build_hourly_candidate_profile,
)
from wetter_schwimmfest.weather_data import (
    WeatherDataError,
    load_cham_hourly_weather_data,
    load_cham_weather_data,
)


st.set_page_config(page_title="Wetter Schwimmfest", page_icon="🏊")

st.title("Wettervergleich Schwimmfest")
st.caption("Historischer Vergleich amtlicher Tages- und Stundenwerte")

st.markdown(
    "**Quelle:** [MeteoSchweiz Open Data]"
    "(https://opendatadocs.meteoswiss.ch/de/a-data-groundbased/"
    "a1-automatic-weather-stations)"
)
st.write(
    "**Auswertungsort:** Zug, repräsentiert durch die Station Cham (CHZ), "
    "443 m ü. M., ca. 5,9 km Luftlinie entfernt"
)

st.subheader("Tageswerte im Jahresvergleich")
daily_indicator_name = st.selectbox(
    "Tagesindikator",
    tuple(WEATHER_INDICATORS),
    key="daily_indicator",
)
daily_indicator = WEATHER_INDICATORS[daily_indicator_name]

with st.expander(
    "So wird der Fest-Indikator berechnet",
    expanded=daily_indicator_name == "Fest-Indikator",
):
    st.write(
        "Jeder amtliche Messwert wird anhand der gezeigten Stützpunkte auf "
        "0 bis 100 Punkte abgebildet. Zwischen zwei Stützpunkten wird linear "
        "gerechnet. Der Fest-Indikator ist die gewichtete Summe aller "
        "Teilwerte. Fehlt ein Kernwert, bleibt das Ergebnis leer."
    )
    st.table(fest_score_explanation())
    st.caption(
        "Der Fest-Indikator ist eine transparente Bewertung dieser Anwendung, "
        "kein amtlicher MeteoSchweiz-Wert und keine Wettervorhersage."
    )

daily_weather_data = None
try:
    with st.spinner("Tageswerte werden geladen …"):
        daily_weather_data = load_cham_weather_data()
except WeatherDataError as error:
    st.error(str(error))
else:
    daily_comparison = build_candidate_comparison(daily_weather_data)
    available_daily = daily_comparison.dropna(subset=[daily_indicator.column])
    if available_daily.empty:
        st.warning("Für diesen Tagesindikator sind an der Station keine Werte verfügbar.")
    else:
        st.plotly_chart(
            create_candidate_chart(daily_comparison, daily_indicator_name),
            width="stretch",
        )
        first_year = int(available_daily["comparison_year"].min())
        last_year = int(available_daily["comparison_year"].max())
        st.caption(
            f"Verfügbare Vergleichsjahre {first_year}–{last_year} · "
            f"Parameter {daily_indicator.source_parameter} · "
            f"{daily_indicator.time_note}"
        )
        if "recent" in available_daily["data_period"].values:
            st.caption(
                "○ Offene Markierungen kennzeichnen Werte des laufenden Jahres; "
                "diese können noch amtlich korrigiert werden."
            )

st.subheader("Typischer Stundenverlauf")
st.write(
    "Die Linien zeigen den Mittelwert über alle verfügbaren Jahre. Die "
    "Schatten zeigen die typische Bandbreite vom 25. bis 75. Perzentil."
)
hourly_indicator_name = st.selectbox(
    "Stundenindikator",
    tuple(HOURLY_INDICATORS),
    key="hourly_indicator",
)
hourly_indicator = HOURLY_INDICATORS[hourly_indicator_name]

try:
    with st.spinner("Stundenwerte werden geladen …"):
        hourly_weather_data = load_cham_hourly_weather_data()
except WeatherDataError as error:
    st.error(str(error))
else:
    hourly_profile = build_hourly_candidate_profile(
        hourly_weather_data,
        hourly_indicator_name,
    )
    available_hours = hourly_profile.dropna(subset=["mean_value"])
    if available_hours.empty:
        st.warning(
            "Für diesen Stundenindikator sind an der Station keine Werte verfügbar."
        )
    else:
        st.plotly_chart(
            create_hourly_profile_chart(hourly_profile, hourly_indicator_name),
            width="stretch",
        )
        first_year = int(available_hours["first_year"].min())
        last_year = int(available_hours["last_year"].max())
        minimum_years = int(available_hours["year_count"].min())
        maximum_years = int(available_hours["year_count"].max())
        year_count_text = (
            str(minimum_years)
            if minimum_years == maximum_years
            else f"{minimum_years}–{maximum_years}"
        )
        st.caption(
            f"Vergleichsjahre {first_year}–{last_year} · "
            f"{year_count_text} Werte je Stunde und Kandidatentag · "
            f"Parameter {hourly_indicator.source_parameter} · "
            "lokale Zeit Europe/Zurich"
        )

st.subheader("Kalenderregel prüfen")
comparison_year = st.number_input(
    "Vergleichsjahr",
    min_value=1900,
    max_value=2100,
    value=date.today().year,
    step=1,
)
candidate_dates = calculate_candidate_dates(comparison_year)

school_start_column, earlier_day_column, later_day_column = st.columns(3)
school_start_column.metric(
    "Schulstart (Montag)", candidate_dates.school_start.strftime("%d.%m.%Y")
)
earlier_day_column.metric(
    "Früher Kandidatentag (Samstag)",
    candidate_dates.earlier_candidate_day.strftime("%d.%m.%Y"),
)
later_day_column.metric(
    "Später Kandidatentag (Samstag)",
    candidate_dates.later_candidate_day.strftime("%d.%m.%Y"),
)

if daily_weather_data is not None:
    st.subheader("Geladene amtliche Tageswerte")
    first_day = daily_weather_data["reference_timestamp"].min().date()
    last_day = daily_weather_data["reference_timestamp"].max().date()
    st.write(f"**Verfügbarer Zeitraum:** {first_day:%d.%m.%Y}–{last_day:%d.%m.%Y}")

    preview = daily_weather_data.tail(5).loc[
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
