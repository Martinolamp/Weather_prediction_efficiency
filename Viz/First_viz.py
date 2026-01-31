import sys
import os

# Dodaje folder główny projektu (poziom wyżej niż Viz) do ścieżek wyszukiwania Pythona
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.Supabase_operatoins import SupbaseConnection

db = SupbaseConnection()
client = db.get_client()

def fetch_todays_data(table_name):
    #db = SupbaseConnection()
    #client = db.get_client()
    try:
        response = client.table(table_name).select("*").execute()
        todays_data=response
        return todays_data
    except Exception as e:
        print(f" Błąd podczas pobierania miast z {table_name}: {e}")
        
    

todays_data=fetch_todays_data('todays_weather')




