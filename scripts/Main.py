from Rest_api_integration import WeatherRestProvider
from Supabase_operatoins import SupbaseConnection
from Web_scrapper import WebScrapperA
import datetime
import pandas as pd

#integracja z Rest api weatherapi.com

#Zanim sie to stanie podczytaj dane z tabeli cities to dict
db = SupbaseConnection()
client = db.get_client()
cities_dict={}

def fetch_cities_from_db(table_name):
    #db = SupbaseConnection()
    #client = db.get_client()
    try:
        response = client.table(table_name).select("*").execute()
        cities = response.data
        
        
        cities_dict={city['City_id']:[city['City_name'],city['Lon'],city['Lat']] for city in cities}
        return cities_dict
    except Exception as e:
        print(f" Błąd podczas pobierania miast z {table_name}: {e}")
        return []
    

def fetch_and_store_weather_data(cities,city_ref_id):
    weather=WeatherRestProvider("weatherapi","weatherapi_key")
    #db = SupbaseConnection()
    response=weather.weather_api_request(cities,False)
    
    try:
        
        
        for i in [1,2]:
            #1-2 counter is used becaouse of weatherapi.com free plan limitiation
            date=response['forecast']['forecastday'][i]['date']
            min_temp=response['forecast']['forecastday'][i]['day']['mintemp_c']
            max_temp=response['forecast']['forecastday'][i]['day']['maxtemp_c']
            date_diff=datetime.datetime.strptime(date, '%Y-%m-%d').date() - datetime.date.today()
            #print(date)
            dict_to_insert={
                "Date":date,
                "Date_difference":date_diff.days,
                "Actual":"false",
                "Max_temp":max_temp,
                "Min_temp":min_temp,
                "Provider_type":"Rest",
                "City_ref_id":city_ref_id
            }
             
            print(dict_to_insert)
            
            payload = db.insert_weather_data("Weather_forecast", dict_to_insert)
            print("✅ Wstawiono dane pogodowe:", dict_to_insert)  
                
    except Exception as e:
        print(f" Błąd podczas pobierania danych pogodowych z weatherapi: {e}")

        
def current_weather_data(cities,city_ref_id):
    weather=WeatherRestProvider("weatherapi","weatherapi_key")
    #db = SupbaseConnection()
    response=weather.weather_api_request(cities,True)
    try:
        current_temp=response['current']['temp_c']
        dict_to_insert={
            "Temp":current_temp,
            "City_ref_id":city_ref_id
        }
        
        
        payload = db.insert_weather_data("Weather_data", dict_to_insert)
        print("✅ Wstawiono dane pogodowe:", dict_to_insert)  
            
    except Exception as e:
        print(f" Błąd podczas pobierania aktualnych danych pogodowych z weatherapi: {e}")


    
    
def run_webscrapperA(lat,lon,city_id):
    scrapper = WebScrapperA()
    try:
        forcast_a=scrapper.fetch_data(lat,lon,city_id)
        #print(forcast_a)
        return forcast_a
    
    except Exception as e:
        print(f" Błąd podczas pobierania danych pogodowych z OpenMeteo: {e}")
    

def insert_weather_forecast_db(table_name,city_id,daily_temp_min,daily_temp_max):
    pass
    
    


def main():
    cities = fetch_cities_from_db("Cities")
    all_data = []  # Tutaj będziemy zbierać dane
    
    measure_date = pd.Timestamp.now().date()

    for city_id, (city_name, lon, lat) in cities.items():
        try:
            scrapped_array = run_webscrapperA(lat, lon, city_id)
            
            t_min = scrapped_array[1][1:]
            t_max = scrapped_array[2][1:]
            
            # Zamiast tworzyć DF tutaj, tworzymy listę słowników dla każdego dnia
            for i in range(len(t_min)):
                all_data.append({
                    'city_id': city_id,
                    'date': measure_date,
                    't_max': t_max[i],
                    't_min': t_min[i],
                    'Date_difference': i + 1
                })
                
        except Exception as e:
            print(f"Błąd dla miasta {city_id}: {e}")
                        
    forecast_df = pd.DataFrame(all_data)

    return forecast_df

            
if __name__ == "__main__":
    print(main())
   






  