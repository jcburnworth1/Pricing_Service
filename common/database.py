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