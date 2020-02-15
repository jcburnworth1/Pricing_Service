## Import libraries
import re
import uuid
import requests
from bs4 import BeautifulSoup
from typing import Dict, List
from common.database import Database

## Item Class
class Item:

    def __init__(self, url: str, tag_name: str, query: Dict, _id: str = None): ## Type hinting
        self.url = url
        self.tag_name = tag_name
        self.query = query
        self.price = None
        self.collection = 'items'
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
        """JSON model for our application to mongo"""
        return {
            '_id': self._id,
            'url': self.url,
            'tag_name': self.tag_name,
            'query': self.query
        }

    def save_to_mongo(self):
        """Save blog details to mongo items collection"""
        Database.insert(self.collection, self.json())

    @classmethod
    def get_by_id(cls, _id):
        """Retrieve our data from mongo based on item id"""

        item_json = Database.find_one("items", {"_id": _id})

        return cls(**item_json)

    @classmethod
    def all(cls) -> List:
        """Return all items from items collection"""
        items_from_db = Database.find('items', {})  ## cursor

        return [cls(**item) for item in items_from_db]
