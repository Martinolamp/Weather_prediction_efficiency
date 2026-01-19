from Main import current_weather_data,fetch_cities_from_db
from Supabase_operatoins import SupbaseConnection

if __name__ == "__main__":
        cities=fetch_cities_from_db("Cities")
          
        for city_id, city_name in cities.items():
            try:
                #print(city_id,city_name)
                current_weather_data(city_name,city_id)
            except Exception as e:
                print(f" Błąd podczas przetwarzania miasta {city_name}: {e}")

 
