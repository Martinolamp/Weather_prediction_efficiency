import streamlit as st
import pandas as pd
from Data_apps import fetch_cities_from_db
from First_viz import fetch_todays_data
from datetime import datetime

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="Weather Dashboard", page_icon="⛅", layout="wide")

city_names=fetch_cities_from_db('Cities')

print(city_names)

st.title("⛅ Monitor Skuteczności Prognoz Pogody")
st.markdown("---")

# --- BOCZNY PANEL (SIDEBAR) ---
st.sidebar.header("Ustawienia")
city = st.sidebar.selectbox("Wybierz miasto:", city_names)
show_raw_data = st.sidebar.checkbox("Pokaż surowe dane")

todays_data=fetch_todays_data('todays_weather')
todays_df=pd.DataFrame(todays_data.data)
print(todays_df)

