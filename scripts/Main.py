from Rest_api_integration import WeatherRestProvider
from Supabase_operatoins import SupbaseConnection

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
        print(f"❌ Błąd podczas pobierania miast z {table_name}: {e}")
        return []
    
cities=fetch_cities_from_db("Cities")
cities_dict=[city for city in cities]      

##Weather api data fetch

def fetch_and_store_weather_data(cities):
    weather=WeatherRestProvider("weatherapi_key","weatherapi_key")
    response=weather.weather_api_request(cities)
    print(response['forecast']['forecastday'][1]['date'],response['forecast']['forecastday'][1]['day']['mintemp_c'],response['forecast']['forecastday'][2]['day']['maxtemp_c'])
        




fetch_and_store_weather_data("Warszawa")