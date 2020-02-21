## Import libraries
import uuid
from typing import Dict
from models.item import Item
from models.model import Model

## Alert Class - Instantiation of Model class
class Alert(Model):
    collection = 'alerts'

    def __init__(self, item_id: str, price_limit: float, _id: str = None):
        super().__init__()
        self.item_id = item_id
        self.item = Item.get_by_id(item_id)
        self.price_limit = price_limit
        self._id = _id or uuid.uuid4().hex

    def json(self) -> Dict:
        """JSON model for alert class to mongo"""
        return {
            "_id": self._id,
            "price_limit": self.price_limit,
            "item_id": self.item_id
        }

    def load_item_price(self) -> float:
        """Reach out to specific url and get new price"""
        self.item.load_price()

        return self.item.price

    def notify_if_price_reached(self) -> None:
        """Determine if price is less than our limit and notify user"""
        if self.item.price < self.price_limit:
            print(f'Item {self.item} has reached a price under {self.price_limit}. Latest Price: {self.item.price}')