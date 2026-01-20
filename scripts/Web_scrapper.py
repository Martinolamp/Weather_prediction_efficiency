from dotenv import load_dotenv
from bs4 import BeautifulSoup
import os
import requests
import re


class WebScrapperA:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv("WEB_SCRAPPER_BASE_URL_A")
        #self.api_key = os.getenv("WEB_SCRAPPER_API_KEY")

    def fetch_data(self, city, params=None):
        """
        Fetch data from a web endpoint.
        endpoint: str - the specific API endpoint to hit
        params: dict - optional parameters for the request
        """
        url = f"{self.base_url}{city}"
        
        
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes
            pattern = re.compile(r'\d{2}\.\d{2}')
            response=response.text
            soup = BeautifulSoup(response, 'html.parser')
            print(soup)
            divs = soup.find_all('span', class_='weather-box__item-label')
            print(divs)
            extracted_values = []
            for div in divs:
                # Pobieramy tekst z diva
                print(div)

            return extracted_values
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching data from {url}: {e}")
            return None



def main():
    scrapper = WebScrapperA()
    city = "SampleCity"
    city_att = "SampleAttribute"
    data = scrapper.fetch_data('slaskie-zabrze/')
    if data:
        soup = BeautifulSoup(data, 'html.parser')
        print(soup.prettify()) 

if __name__ == "__main__":
    main()