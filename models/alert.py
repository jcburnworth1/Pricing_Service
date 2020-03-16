## Import libraries
import uuid
from typing import Dict
from dataclasses import dataclass, field
from models.item import Item
from models.model import Model
from models.user import User

## Alert Class - Instantiation of Model class
@dataclass(eq=False) # Remove all equality generation for now
class Alert(Model):
    collection: str = field(init=False, default='alerts')
    name: str
    item_id: str
    price_limit: float
    user_email: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def __post_init__(self):
        self.item = Item.get_by_id(self.item_id)
        self.user = User.find_by_email(self.user_email)

    def json(self) -> Dict:
        """JSON model for alert class to mongo"""
        return {
            "_id": self._id,
            "name": self.name,
            "item_id": self.item_id,
            "price_limit": self.price_limit,
            "user_email": self.user_email
        }

    def load_item_price(self) -> float:
        """Reach out to specific url and get new price"""
        self.item.load_price()

        return self.item.price

    def notify_if_price_reached(self) -> None:
        """Determine if price is less than our limit and notify user"""
        if self.item.price < self.price_limit:
            print(f'Item {self.item} has reached a price under {self.price_limit}. Latest Price: {self.item.price}')