from Rest_api_integration import WeatherRestProvider
from Supabase_operatoins import SupbaseConnection
import datetime

#integracja z Rest api weatherapi.com

#Zanim sie to stanie podczytaj dane z tabeli cities to dict

cities_dict=[]

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
cities_list=[city for city in cities]      

###Weather api data fetch, petla zadziała tylko dwa razy, pownieważ weather api nie pozwala na większy dostęp do danych

def fetch_and_store_weather_data(cities):
    weather=WeatherRestProvider("weatherapi_key","weatherapi_key")
    try:
        response=weather.weather_api_request(cities)
        for i in [1,2]:
            date=response['forecast']['forecastday'][i]['date']
            min_temp=response['forecast']['forecastday'][i]['day']['mintemp_c']
            max_temp=response['forecast']['forecastday'][i]['day']['maxtemp_c']
            date_diff=datetime.datetime.strptime(date, '%Y-%m-%d').date() - datetime.date.today()
            print(date_diff.days)
             # Print the difference in days
            print(f"Data: {date}, Min Temp: {min_temp}°C")

    except Exception as e:
        print(f" Błąd podczas pobierania danych pogodowych z weatherapi: {e}")

        

for i in cities_list:
    city_name=i['City_name']
    print(city_name)


fetch_and_store_weather_data("Warszawa")

#weather_data_api={}
#weather_data=[city['City_name'] for city in cities_list]
