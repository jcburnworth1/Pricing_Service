## Import libraries
import pymongo
from typing import Dict

## Database Class
## Will create connection to Mongo for interactions
class Database(object):
    URI = "mongodb://127.0.0.1:27017/pricing"
    DATABASE = pymongo.MongoClient(URI).get_database()

    @staticmethod
    def insert(collection: str, data: Dict) -> None:
        """Insert record into pricing database"""
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor: ## cursor is an iterable
        """Retrieve all results data from fullstack based on supplied query"""
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        """Retrieve first document in the query result"""
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        """Upsert mongo data - Update will happen if data already exists, insert happens if data does not exists"""
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict) -> Dict:
        """Remove selected ata from supplied mongo collection"""
        return Database.DATABASE[collection].remove(query)