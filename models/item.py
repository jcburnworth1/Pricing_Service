## Import libraries
import re, uuid, requests
from bs4 import BeautifulSoup
from typing import Dict
from models.model import Model

## Item Class - Instantiation of Model Class
class Item(Model):
    collection = 'items_deprecated'

    def __init__(self, url: str, tag_name: str, query: Dict, _id: str = None): ## Type hinting
        super().__init__()
        self.url = url
        self.tag_name = tag_name
        self.query = query
        self.price = None

        self._id = _id or uuid.uuid4().hex ## Will overwrite the mongo db default id

    def __repr__(self): ## Return an string representation of the item object
        """Return a custom representation of Item"""
        return f'<Item {self.url}>' ## f in front of quotes denotes an f string to add variable inside {}

    def load_price(self) -> float: ## Type hinting on what will be returned
        """Reach out to the specified URL and capture the price"""
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

    def json(self) -> Dict:
        """JSON model for item class to mongo"""
        return {
            '_id': self._id,
            'url': self.url,
            'tag_name': self.tag_name,
            'query': self.query
        }