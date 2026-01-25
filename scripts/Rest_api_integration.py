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
        self.provider_c_api_key = os.getenv(env_token_key)
        self.provider_d_api_key = os.getenv(env_token_key)

        



    def weather_api_request(self,city_name,forecats):
        #class used to call weather forecats endoping#Free forecast for max 3 days
        if forecats:
            base_url = os.getenv("weather_api_base_url")
            sufix=os.getenv("weather_api_sufix")
            api_key = self.weather_api_key
            url = f"{base_url}{api_key}&q={city_name}{sufix}"
            requests.get(url)
        else:
            base_url = os.getenv("weather_api_base_current")
            sufix=os.getenv("weather_api_current_suffix")
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

    def weather_api_request_provider_c(self,lat,lon):
        prov_c_base_url=os.getenv("PROVIDER_C_BASE_URL")
        prov_c_sufix=os.getenv("PROVIDER_C_SUFIX")
        prov_c_api_key=self.provider_c_api_key
        url=f'{prov_c_base_url}{prov_c_api_key}&lat={lat}&lon={lon}{prov_c_sufix}'
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching weather data for lat:{lat} lon:{lon} : {e}")
            return None
        
    def weather_api_request_provider_d(self,city_name):
        prov_d_base_url=os.getenv("PROVIDER_D_BASE_URL")
        prov_d_sufix=os.getenv("PROVIDER_D_SUFIX")
        prov_d_api_key=self.provider_d_api_key
        url=f'{prov_d_base_url}{city_name}{prov_d_sufix}{prov_d_api_key}'
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching weather data for city:{city_name}: {e}")
            return None


        
def main():
    # function used to test how the integration works
    zabrze_test=WeatherRestProvider("meteoblue","Web_api_provider_c_key")
    resp=zabrze_test.weather_api_request_provider_c(52.2297,21.0122)
    print(resp['data_day']['temperature_max'][1:],resp['data_day']['temperature_min'][1:])
    #print(type(resp['forecast']['forecastday']))
    
    
    
    #print

if __name__ == "__main__":
    main()

        
       