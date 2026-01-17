import os
from dotenv import load_dotenv
import requests
import logging


logger = logging.getLogger(__name__)


class WeatherRestProvider:
    def __init__(self, name, env_token_key):
        load_dotenv()
        self.name = name
        self.weather_api_key = os.getenv(env_token_key)

        



    def weather_api_request(self,city_name):
        base_url = os.getenv("weather_api_base_url")
        sufix=os.getenv("weather_api_sufix")
        api_key = self.weather_api_key
        url = f"{base_url}{api_key}&q={city_name}{sufix}"
        requests.get(url)
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching weather data for {city_name}: {e}")
            return None
    


def main():
    # function used to test how the integration works
    zabrze_test=WeatherRestProvider("weatherapi_key","weatherapi_key")
    resp=zabrze_test.weather_api_request("Warszawa")
    
    
    print(resp['forecast']['forecastday'][1]['date'],resp['forecast']['forecastday'][1]['day']['mintemp_c'])
    print(resp['forecast']['forecastday'][2]['date'],resp['forecast']['forecastday'][2]['day']['mintemp_c'])
    #print

if __name__ == "__main__":
    main()

        
       