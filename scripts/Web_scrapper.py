from dotenv import load_dotenv
from bs4 import BeautifulSoup
import os
import requests


class WebScrapperA:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv("WEB_SCRAPPER_BASE_URL_A")
        #self.api_key = os.getenv("WEB_SCRAPPER_API_KEY")

    def fetch_data(self, city,city_att, params=None):
        """
        Fetch data from a web endpoint.
        endpoint: str - the specific API endpoint to hit
        params: dict - optional parameters for the request
        """
        url = f"{self.base_url,city,city_att}"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise an error for bad status codes
            return response.text()
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching data from {url}: {e}")
            return None