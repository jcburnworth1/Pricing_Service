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

    def load_item_price(self) -> float:
        """
        This method reaches out to the item's url and gets an updated price
        :return: Price of the item
        """
        self.item.load_price()

        return self.item.price

    def notify_if_price_reached(self) -> None:
        """
        This method will notify the user if the specified price limit was reached
        :return: Print notification that item is below specified price
        """
        if self.item.price < self.price_limit:
            print(f'Item {self.item} has reached a price under {self.price_limit}. Latest Price: {self.item.price}')

    def json(self) -> Dict:
        """
        This method returns the JSON structure of an alert object for insertion into database
        :return: Dict version of the alert parameters
        """
        return {
            "_id": self._id,
            "name": self.name,
            "item_id": self.item_id,
            "price_limit": self.price_limit,
            "user_email": self.user_email
        }