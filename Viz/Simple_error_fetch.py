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

def get_data_from_views(table_name):
    try:

        response = client.table(table_name).select("*").execute()

        return response
    except:
        print(f" Błąd podczas pobierania danych z {table_name}: {e}")

        return []
    

resp=simple_error_view=get_data_from_views('simple error')

df = pd.DataFrame(resp.data)
print(df)


