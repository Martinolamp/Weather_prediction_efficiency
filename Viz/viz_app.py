import streamlit as st
import pandas as pd
from Data_apps import fetch_cities_from_db
from First_viz import fetch_todays_data
from datetime import datetime

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="Weather Dashboard", page_icon="⛅", layout="wide")

city_names=fetch_cities_from_db('Cities')



st.title("⛅ Monitor Skuteczności Prognoz Pogody")
st.markdown("---")

# --- BOCZNY PANEL (SIDEBAR) ---
st.sidebar.header("Ustawienia")
city = st.sidebar.selectbox("Wybierz miasto:", city_names)
show_raw_data = st.sidebar.checkbox("Pokaż surowe dane")

todays_data=fetch_todays_data('todays_weather')
todays_df=pd.DataFrame(todays_data.data)
todays_df = todays_df.sort_values(by='Daily_max', ascending=True)
st.subheader("Aktualne odczyty (ostatnia godzina)")
st.dataframe(todays_df, use_container_width=True)

    # 4. Prosty wykres słupkowy dla szybkiego podglądu mrozu
st.subheader("Last hour temps")
st.bar_chart(data=todays_df, x='City_name', y='Last_measure')
st.subheader("Daily extremes")
st.bar_chart(data=todays_df, x='City_name', y=['Daily_max','Daily_min'],color=["#FF4B4B", "#0000FF"],stack=False)

