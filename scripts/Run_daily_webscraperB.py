from Main import current_weather_data,fetch_cities_from_db,fetch_and_store_weather_data
from Supabase_operatoins import SupbaseConnection
from Rest_api_integration import WeatherRestProvider
import pandas as pd


def main():
    

    cities = fetch_cities_from_db("Cities")
    all_data = []  # Collectiing weather data from provider B - free forecast just for 2 days
    for city_id, city_name in cities.items():
        try:
            scrapped_array =fetch_and_store_weather_data(city_name[0],city_id)
            
        except Exception as e:
            print(f"Błąd dla miasta {city_id}: {e}")


if __name__ == "__main__":
    main()
    