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
    response=weather.weather_api_request(cities,True)
    #print(response)
    try:
        
        
        for i in [1,2]:
            #1-2 counter is used becaouse of weatherapi.com free plan limitiation
            date=response['forecast']['forecastday'][i]['date']
            min_temp=response['forecast']['forecastday'][i]['day']['mintemp_c']
            max_temp=response['forecast']['forecastday'][i]['day']['maxtemp_c']
            date_diff=datetime.datetime.strptime(date, '%Y-%m-%d').date() - datetime.date.today()
            current_date=datetime.date.today()
            #print(date)
            dict_to_insert={
                "Date":date,
                "Date_difference":date_diff.days,
                "Max_temp":max_temp,
                "Min_temp":min_temp,
                "Provider_type":"Rest",
                "City_ref_id":city_ref_id,
                "Provider_type":"B"
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
    

def run_web_srapperC(lat,lon,city_id):
    
    all_data = []  # Tutaj będziemy zbierać dane

    try:
        rest_scrapping=WeatherRestProvider("meteoblue","WEB_API_PROVIDER_C_KEY")

        scrapped_dict = rest_scrapping.weather_api_request_provider_c(lat, lon)
        today=datetime.datetime.now().date()
        t_min = scrapped_dict['data_day']['temperature_min'][1:]
        t_max = scrapped_dict['data_day']['temperature_max'][1:]
        print(t_min,t_max)
        # Zamiast tworzyć DF tutaj, tworzymy listę słowników dla każdego dnia
        for i in range(1,len(scrapped_dict['data_day']['temperature_min'][1:])):
            
            all_data.append({

                'City_ref_id': city_id,
                'Date': today,
                'Max_temp': t_max[i],
                'Min_temp': t_min[i],
                'Provider_type':'C',
                'Date_difference': i
            })
            
        

    
    except Exception as e:
        print(f"Błąd dla miasta {city_id}: {e}")
    
    return all_data



def run_web_srapperD(city_name,city_id):


    all_data = []  # Tutaj będziemy zbierać dane
    rest_scrapping=WeatherRestProvider("Visualcrossing","PROVIDER_D_API_KEY")
    scrapped_dict = rest_scrapping.weather_api_request_provider_d(city_name)
    today=datetime.datetime.now().date()
    for i in range(1,len(scrapped_dict['days'][:7])):
        all_data.append({
                'City_ref_id': city_id,
                'Date': today,
                'Max_temp': scrapped_dict['days'][i]['tempmax'],
                'Min_temp': scrapped_dict['days'][i]['tempmin'],
                'Provider_type':'D',
                'Date_difference': i + 1
            })

       

    return all_data




def main():
    cities = fetch_cities_from_db("Cities")
    all_data = []  # Tutaj będziemy zbierać dane
    for city_id, (city_name, lon, lat) in cities.items():
        dict_test=run_web_srapperD(city_name,city_id)
        print(dict_test)
   

   

            
if __name__ == "__main__":
    main()
   






  