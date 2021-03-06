## Import libraries
import re, uuid, requests
from bs4 import BeautifulSoup
from typing import Dict
from models.model import Model
from dataclasses import dataclass, field

## Item Class - Instantiation of Model Class
@dataclass(eq=False)
class Item(Model):
    collection: str = field(init=False, default='items')
    url: str
    tag_name: str
    query: Dict
    price: float = field(default=None)
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def load_price(self) -> float: ## Type hinting on what will be returned
        """
        This method reaches out to the website to get the current price
        :return: Price of the object
        """
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
        """
        This method returns the JSON structure of an item object for insertion into database
        :return: Dict version of the item parameters
        """
        return {
            '_id': self._id,
            'url': self.url,
            'tag_name': self.tag_name,
            'price': self.price,
            'query': self.query
        }