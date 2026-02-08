import streamlit as st
import pandas as pd
from Data_apps import fetch_cities_from_db
from First_viz import fetch_todays_data
from Simple_error_fetch import get_simple_error_data
from Weather_forcast_querry import fetch_forcast_for_city
from datetime import datetime

#wykresy bledow
# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="Weather Dashboard", page_icon="⛅", layout="wide")

st.sidebar.title("Nawigacja")
view = st.sidebar.radio("Wybierz widok:", ["Todays weather", "Error analysis","City Forecast"])

#city_names=fetch_cities_from_db('Cities')

#print(city_names)



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
    mean_square_error_analysis=get_simple_error_data('root mean square error')
    pivot_max_simple = simple_error_analysis.pivot(index='Date_difference', columns='Provider_type', values='avg_error_max')
    pivot_min_simple = simple_error_analysis.pivot(index='Date_difference', columns='Provider_type', values='avg_error_min')
    pivot_max_mean= mean_error_analysis.pivot(index='Date_difference', columns='Provider_type', values='avg_error_max')
    pivot_min_mean= mean_error_analysis.pivot(index='Date_difference', columns='Provider_type', values='avg_error_min')
    pivot_max_root_error = mean_square_error_analysis.pivot(index='Date_difference', columns='Provider_type', values='avg_error_max')
    pivot_min_root_error = mean_square_error_analysis.pivot(index='Date_difference', columns='Provider_type', values='avg_error_max')
    # --- WIDOK 1: Temperatura Maksymalna ---
    st.subheader("Mean simple error in max temperature weather data prediction")
   
    st.line_chart(
    pivot_max_simple, 
    x_label="Days of forecast", 
    y_label="Mean Simple Error (°C)"
    )   


    st.subheader("Mean absolute error in max temperature weather data prediction")
   
    
    st.line_chart(
    pivot_max_mean, 
    x_label="Days of forecast", 
    y_label="Mean Absolute Error (°C)"
    )   


    st.subheader("Root mean square error in max temperature weather data prediction")
   
    
    st.line_chart(
    pivot_max_root_error, 
    x_label="Days of forecast", 
    y_label="Mean Swuare Error (°C)"
    )   



    # --- WIDOK 2: Temperatura Minimalna ---
    st.subheader("Mean simple error in min temperature weather data prediction")
    
    st.line_chart(
    pivot_min_simple, 
    x_label="Days of forecast", 
    y_label="Mean Simple Error (°C)"
    ) 



    # --- WIDOK 2: Temperatura Minimalna ---
    st.subheader("Mean absolute error in min temperature weather data prediction")
    

    st.line_chart(
    pivot_min_mean, 
    x_label="Days of forecast", 
    y_label="Mean Simple Error (°C)"
    ) 

    st.subheader("Root mean square error in min temperature weather data prediction")
   
    
    st.line_chart(
    pivot_min_root_error, 
    x_label="Days of forecast", 
    y_label="Mean Simple Error (°C)"
    )   

elif view == "City Forecast":
    city_names=fetch_cities_from_db('Cities')
    st.sidebar.header("Cities")
    city_list=list(city_names)
    selected_city = st.sidebar.selectbox("Choose city:",city_list[0])
    st.subheader(selected_city)
    st.subheader(city_list[1][city_list[0].index(selected_city)])
    #st.subheader("test")
    #city_id=city_list[1][city_list[0].index(selected_city)]
    #forcast_df=pd.DataFrame(fetch_forcast_for_city(city_id))
    #st.dataframe(forcast_df, use_container_width=True)tetstest


