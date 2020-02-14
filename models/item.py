## Import libraries
import re
import requests
from bs4 import BeautifulSoup
from typing import Dict

## Item Class
class Item:

    def __init__(self, url: str, tag_name: str, query: Dict): ## Type hinting
        self.url = url
        self.tag_name = tag_name
        self.query = query
        self.price = None

    def load_price(self) -> float: ## Type hinting on what will be returned
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