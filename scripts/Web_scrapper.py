from dotenv import load_dotenv
from bs4 import BeautifulSoup
import os
import requests
import re
import pandas as pd
import openmeteo_requests
import requests_cache
from retry_requests import retry


class WebScrapperA:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv("WEB_SCRAPPER_BASE_URL_A")
        #self.api_key = os.getenv("WEB_SCRAPPER_API_KEY")
        cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        self.opopenmeteo = openmeteo_requests.Client()

    def fetch_data(self,lat,lon,city_id):
        url = f"{self.base_url}"
        params = {
        "latitude": lat,
        "longitude": lon,
        "daily":["temperature_2m_max","temperature_2m_min"],
        "timezone":"GMT"
        }
        try:
            responses = self.opopenmeteo.weather_api(url, params=params)
            response=responses[0]
            daily = response.Daily()
            daily_temp_min=daily.Variables(0).ValuesAsNumpy()
            daily_temp_max=daily.Variables(1).ValuesAsNumpy()

            return_dictionary={
                "daily_temp_min":daily_temp_min,
                "daily_temp_max":daily_temp_max,
                "city_id":city_id,

            }
            
            return return_dictionary

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")
            return None
      
    


def main():
    scrapper = WebScrapperA()
    temp={}
    result=scrapper.fetch_data(52.2297, 21.0122,2313)
    
    for key, value in result.items():
        temp['city_id']=result['city_id']
        temp['temp_min']=result['daily_temp_min']
        temp['temp_max']=result['daily_temp_max']
    
    print(temp)

if __name__ == "__main__":
    main()