import streamlit as st
import pandas as pd
from datetime import datetime

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="Weather Dashboard", page_icon="⛅", layout="wide")

st.title("⛅ Monitor Skuteczności Prognoz Pogody")
st.markdown("---")

# --- BOCZNY PANEL (SIDEBAR) ---
st.sidebar.header("Ustawienia")
city = st.sidebar.selectbox("Wybierz miasto:", ["Lublin", "Katowice"])
show_raw_data = st.sidebar.checkbox("Pokaż surowe dane")