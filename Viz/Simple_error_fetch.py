import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os
import json
# Dodaje folder główny projektu (poziom wyżej niż Viz) do ścieżek wyszukiwania Pythona
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.Supabase_operatoins import SupbaseConnection


db = SupbaseConnection()
client = db.get_client()

def get_simple_error_data(table_name):
    try:

        response = client.table(table_name).select("*").execute()
        response=pd.DataFrame(response.data)
        return response
    except:
        print(f" Błąd podczas pobierania danych z {table_name}: {e}")

        return []
    
def get_error_per_city_min(table_name,city_id):

    try:

        

        response = client.table(table_name).select("*").eq("City_ref_id", city_id).execute()
        response=pd.DataFrame(response.data)
        pivot_min_mean= response.pivot_table(index='Date_difference', columns='Provider_type', values='avg_error_min')
        response=pivot_min_mean.round(1).fillna('no forecast')
        return response
    except:
        print(f" Błąd podczas pobierania danych z {table_name}: {e}")

    return []
    
def get_error_per_city_max(table_name,city_id):

    try:

        response = client.table(table_name).select("*").eq("City_ref_id", city_id).execute()
        response=pd.DataFrame(response.data)
        pivot_min_mean= response.pivot_table(index='Date_difference', columns='Provider_type', values='avg_error_max')
        response=pivot_min_mean.round(1).fillna('no forecast')
        return response
    except:
        print(f" Błąd podczas pobierania danych z {table_name}: {e}")

    return []

#resp=simple_error_view=get_simple_error_data('simple error')

resp=get_error_per_city_min('Errors_for_city')
print(resp)
#pivot_min_mean= resp.pivot_table(index='Date_difference', columns='Provider_type', values='avg_error_min')

#print(pivot_min_mean.round(1).fillna('no forecast'))



if __name__ == "__main__":
    main()



