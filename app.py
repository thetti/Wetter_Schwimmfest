import streamlit as st

from wetter_schwimmfest.demo import create_demo_chart


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


if __name__ == "__main__":
    main()
