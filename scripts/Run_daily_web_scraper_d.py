from Main import current_weather_data,fetch_cities_from_db,run_web_srapperD
from Supabase_operatoins import SupbaseConnection
from Rest_api_integration import WeatherRestProvider
import datetime
import pandas as pd


def main():
   
    cities = fetch_cities_from_db("Cities")
      # Collectiing weather data from provider B - free forecast just for 2 days
    #print(cities)
    for city_id, (city_name, lon, lat) in cities.items():
        try:
            scrapped_array = run_web_srapperD(city_name,city_id)
            

    
            forecast_df = pd.DataFrame(scrapped_array)
            
            
            data_dict = forecast_df.astype({'Date': str}).to_dict(orient='records')
            db_connection = SupbaseConnection()
            db_connection.insert_weather_forecast('Weather_forecast', data_dict)
            
        except Exception as e:
            print(f"Błąd dla miasta {city_id}: {e}")
    



   

if __name__ == "__main__":
    
    main()