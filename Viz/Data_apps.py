import sys
import os

# Dodaje folder główny projektu (poziom wyżej niż Viz) do ścieżek wyszukiwania Pythona
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.Supabase_operatoins import SupbaseConnection
#from scripts.Main import fetch_cities_from_db





db = SupbaseConnection()
client = db.get_client()
cities_dict={}

def fetch_cities_from_db(table_name):
    #db = SupbaseConnection()
    #client = db.get_client()
    try:
        response = client.table(table_name).select("*").execute()
        cities = response.data
        
        
        cities_dict={city['City_name']:city['City_id'] for city in cities}
        city_names=list(cities_dict.keys())
        city_id=list(cities_dict.values())
        
        return list(city_names,city_id)
    except Exception as e:
        print(f" Błąd podczas pobierania miast z {table_name}: {e}")
        return []
    

city_names=fetch_cities_from_db('Cities')

if __name__ == "__main__":
    #lista_miast=list(fetch_cities_from_db('Cities'))
    main()
    
