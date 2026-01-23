from Main import current_weather_data,fetch_cities_from_db,run_webscrapperA
from Supabase_operatoins import SupbaseConnection
import pandas as pd

def main():
    cities = fetch_cities_from_db("Cities")
    all_data = []  # Tutaj będziemy zbierać dane
    print(cities)
    measure_date = pd.Timestamp.now().date()

    for city_id, (city_name, lon, lat) in cities.items():
        try:
            scrapped_array = run_webscrapperA(lat, lon, city_id)
            
            t_min = scrapped_array[2][1:]
            t_max = scrapped_array[1][1:]
            
            # Zamiast tworzyć DF tutaj, tworzymy listę słowników dla każdego dnia
            for i in range(len(t_min)):
                all_data.append({
                    'City_ref_id': city_id,
                    'Date': measure_date,
                    'Max_temp': t_max[i],
                    'Min_temp': t_min[i],
                    'Provider_type':'A',
                    'Date_difference': i + 1
                })
                
        except Exception as e:
            print(f"Błąd dla miasta {city_id}: {e}")
    return all_data


    

if __name__ == "__main__":
    all_data=main()
    forecast_df = pd.DataFrame(all_data)
    db_connection = SupbaseConnection()
    data_dict = forecast_df.astype({'Date': str}).to_dict(orient='records')
    db_connection.insert_weather_forecast('Weather_forecast', data_dict)
    #db_connection.insert_weather_forecast('Weather_forecast', all_data)
   
  