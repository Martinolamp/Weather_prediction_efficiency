from Rest_api_integration import WeatherRestProvider
from Supabase_operatoins import SupbaseConnection
import datetime

#integracja z Rest api weatherapi.com

#Zanim sie to stanie podczytaj dane z tabeli cities to dict

cities_dict={}

def fetch_cities_from_db(table_name):
    db = SupbaseConnection()
    client = db.get_client()
    try:
        response = client.table(table_name).select("*").execute()
        cities = response.data
        return cities
    except Exception as e:
        print(f" Błąd podczas pobierania miast z {table_name}: {e}")
        return []
    
cities=fetch_cities_from_db("Cities")

#cities_dict={city for city in cities}     

cities_dict={city['City_id']:city['City_name'] for city in cities}



###Weather api data fetch, petla zadziała tylko dwa razy, pownieważ weather api nie pozwala na większy dostęp do danych

def fetch_and_store_weather_data(cities,city_ref_id):
    weather=WeatherRestProvider("weatherapi_key","weatherapi_key")
    try:
        response=weather.weather_api_request(cities)
        for i in [1,2]:
            date=response['forecast']['forecastday'][i]['date']
            min_temp=response['forecast']['forecastday'][i]['day']['mintemp_c']
            max_temp=response['forecast']['forecastday'][i]['day']['maxtemp_c']
            date_diff=datetime.datetime.strptime(date, '%Y-%m-%d').date() - datetime.date.today()
            print(date_diff.days)
            dict_to_insert={
                "Date":date,
                "Date_difference":date_diff.days,
                "Actual":"false",
                "Max_temp":max_temp,
                "Min_temp":min_temp,
                "Provider_type":"REST_API",
                "City_ref_id":city_ref_id
            }
             # Print the difference in days
            #print(dict_to_insert)

    except Exception as e:
        print(f" Błąd podczas pobierania danych pogodowych z weatherapi: {e}")

        
    #insert_data_to_database
    try:
        db = SupbaseConnection()
        response=db.insert_weather_data("Weather_data",dict_to_insert)
        print("✅ Wstawiono dane pogodowe:", response)
    except Exception as e:
        print(f"❌ Błąd podczas wstawiania danych pogodowych: {e}")



for city_id, city_name in cities_dict.items():
    try:
        fetch_and_store_weather_data(city_name,city_id)
    except Exception as e:
        print(f" Błąd podczas przetwarzania miasta {city_name}: {e}")


