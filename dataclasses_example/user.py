## Import libraries
import uuid
from typing import Dict
from dataclasses import dataclass, field

## Function to generate unique id
# def generate_hex():
#     return uuid.uui4().hex

@dataclass
class User:
    username: str
    password: str = field(repr=False, compare=False)
    country: str = field(default="United Kingdom")
    _id: str = field(default_factory=lambda: uuid.uuid4().hex, compare=False)  # field(default_factory=generate_hex also works

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "username": self.username
        }