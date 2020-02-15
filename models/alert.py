## Import libraries
import uuid
from typing import Dict, List
from models.item import Item
from common.database import Database

## Alert Class
class Alert:

    def __init__(self, item_id: str, price_limit: float, _id: str = None):
        self.item_id = item_id
        self.item = Item.get_by_id(item_id)
        self.price_limit = price_limit
        self.collection = 'alerts'
        self._id = _id or uuid.uuid4().hex

    def json(self) -> Dict:
        """JSON model for our application to mongo"""
        return {
            "_id": self._id,
            "price_limit": self.price_limit,
            "item_id": self.item_id
        }

    def save_to_mongo(self):
        """Save new user to mongo alerts collection"""
        Database.insert(self.collection, self.json())

    def load_item_price(self) -> float:
        """Reach out to specific url and get new price"""
        self.item.load_price()

        return self.item.price

    def notify_if_price_reached(self) -> None:
        """Determine if price is less than our limit and notify user"""
        if self.item.price < self.price_limit:
            print(f'Item {self.item} has reached a price under {self.price_limit}. Latest Price: {self.item.price}')


    @classmethod
    def all(cls) -> List:
        """ Load all alerts from mongo"""
        alerts_from_db = Database.find('alerts', {})  ## cursor

        return [cls(**alert) for alert in alerts_from_db]