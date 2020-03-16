## Import libraries
import uuid
import re
from dataclasses import dataclass, field
from typing import Dict
from models.model import Model

## Store Class - Instantiation of Model class
@dataclass(eq=False)
class Store(Model):
    collection: str = field(init=False, default='stores')
    name: str
    url_prefix: str
    tag_name: str
    query: Dict
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    @classmethod
    def get_by_name(cls, store_name: str) -> "Store": #Store.get_by_name('John Lewis')
        """
        This method finds the store record for the supplied store name
        :param collection: Uses collection specified in the class
        :param store_name: The name of the store we are trying to search for
        :return: The store record found
        """
        return cls.find_one_by("name", store_name)

    @classmethod
    def get_by_url_prefix(cls, url_prefix: str) -> "Store": #Store.get_by_url_prefix('https://www.johnlewis.com')
        """
        This method finds the store record for the supplied store name
        :param collection: Uses collection specified in the class
        :param url_prefix: The url prefix, 'https://www.johnlewis.com'
        :return: The store record found
        """
        ## https://johnlewis.com/items - Regex will handle this and find proper records
        url_regex = {"$regex": "^{}".format(url_prefix)}
        return cls.find_one_by("url_prefix", url_regex)

    @classmethod
    def find_by_url(cls, url: str) -> "Store":
        """
        This method finds a store from a url like http//www.johnlewis.com/item/asdfasdfas.html
        :param collection: Uses collection specified in the class
        :param url: The item's url
        :return: The store record found
        Test URL - https://www.johnlewis.com/john-lewis-partners-murray-ergonomic-office-chair-black/p1919328
        """
        pattern = re.compile(r"(https?://.*?/)")
        match = pattern.search(url)
        url_prefix = match.group(1)
        return cls.get_by_url_prefix(url_prefix)

    def json(self) -> Dict:
        """
        This method returns the JSON structure of a store object for insertion into database
        :return: Dict version of the alert parameters
        """
        return {
            "_id": self._id,
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query
        }

