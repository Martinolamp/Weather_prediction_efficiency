import streamlit as st
import pandas as pd
from Data_apps import fetch_cities_from_db
from First_viz import fetch_todays_data
from Simple_error_fetch import get_simple_error_data
from datetime import datetime

#wykresy bledow
# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="Weather Dashboard", page_icon="⛅", layout="wide")

st.sidebar.title("Nawigacja")
view = st.sidebar.radio("Wybierz widok:", ["Todays weather", "Error analysis"])

city_names=fetch_cities_from_db('Cities')



st.title("⛅ Monitor Skuteczności Prognoz Pogody")
st.markdown("---")

# --- BOCZNY PANEL (SIDEBAR) ---
#st.sidebar.header("Ustawienia")
#city = st.sidebar.selectbox("Wybierz miasto:", city_names)
#show_raw_data = st.sidebar.checkbox("Pokaż surowe dane")
if view =="Todays weather":
    todays_data=fetch_todays_data('todays_weather')
    todays_df=pd.DataFrame(todays_data.data)
    todays_df = todays_df.sort_values(by='Daily_max', ascending=True)
    st.subheader("Aktualne odczyty (ostatnia godzina)")
    st.dataframe(todays_df, use_container_width=True)

        # 4. Prosty wykres słupkowy dla szybkiego podglądu mrozu
    st.subheader("Last hour temps")
    st.bar_chart(data=todays_df, x='City_name', y='Last_measure')
    st.subheader("Daily extremes")
    st.bar_chart(data=todays_df.sort_values(by='Daily_max', ascending=True), x='City_name', y=['Daily_max','Daily_min'],color=["#FF4B4B", "#0000FF"],stack=False)
elif view == "Error analysis":
    simple_error_analysis=get_simple_error_data('simple error')
    mean_error_analysis=get_simple_error_data('mean absolute error')
    pivot_max_simple = simple_error_analysis.pivot(index='Date_difference', columns='Provider_type', values='avg_error_max')
    pivot_min_simple = simple_error_analysis.pivot(index='Date_difference', columns='Provider_type', values='avg_error_min')
    pivot_max_mean= mean_error_analysis.pivot(index='Date_difference', columns='Provider_type', values='avg_error_max')
    pivot_min_mean= mean_error_analysis.pivot(index='Date_difference', columns='Provider_type', values='avg_error_min')

    # --- WIDOK 1: Temperatura Maksymalna ---
    st.subheader("Mean simple error in max temperature weather data prediction")
   
    st.line_chart(
    pivot_max_simple, 
    x_label="Days of forecast", 
    y_label="Mean Error (°C)"
    )   

    # --- WIDOK 2: Temperatura Minimalna ---
    st.subheader("Mean simple error in min temperature weather data prediction")
    
    st.line_chart(
    pivot_min_simple, 
    x_label="Days of forecast", 
    y_label="Mean Error (°C)"
    ) 


# --- WIDOK 1: Temperatura Maksymalna ---
    st.subheader("Mean absolute error in max temperature weather data prediction")
   
    
    st.line_chart(
    pivot_max_mean, 
    x_label="Days of forecast", 
    y_label="Mean Error (°C)"
    )   

    # --- WIDOK 2: Temperatura Minimalna ---
    st.subheader("Mean absolute error in min temperature weather data prediction")
    

    st.line_chart(
    pivot_min_mean, 
    x_label="Days of forecast", 
    y_label="Mean Error (°C)"
    ) 
    



