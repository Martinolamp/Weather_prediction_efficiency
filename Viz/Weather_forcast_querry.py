import sys
import os

# Dodaje folder główny projektu (poziom wyżej niż Viz) do ścieżek wyszukiwania Pythona
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.Supabase_operatoins import SupbaseConnection
#from scripts.Main import fetch_cities_from_db





db = SupbaseConnection()
client = db.get_client()
cities_dict={}

def fetch_forcast_for_city(city_id):
    #db = SupbaseConnection()
    #client = db.get_client()
    try:
        response = client.table("Forcast_for_city").select("*").eq("City_ref_id", city_id).execute()
        weather = response.data
        return weather
        
        
    except Exception as e:
        print(f" Błąd podczas pobierania miast z {"Forcast_for_city"}: {e}")
        return []
    



if __name__ == "__main__":
    print(fetch_forcast_for_city(24))