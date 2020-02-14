## Import libraries
import requests
from bs4 import BeautifulSoup
import re

## Item Class
class Item():

    def __init__(self):
        self.url = 'https://www.johnlewis.com/john-lewis-partners-hemingway-3-door-sideboard/p230727606'
        self.tag_name = 'p'
        self.query = {"class": "price price--large"}
        self.price = None

    def load_price(self):
        response = requests.get(self.url)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()

        pattern = re.compile(r'(\d+,?\d*\.\d\d)')
        match = pattern.search(string_price)
        found_price = match.group(1)
        without_commas = found_price.replace(',', '')
        self.price = float(without_commas)

        return self.price