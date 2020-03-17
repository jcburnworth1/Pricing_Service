## Import libraries
import os
import pymongo
from typing import Dict

## Database Class
## Will create connection to Mongo for interactions
class Database(object):
    URI = os.environ.get('MONGO_URI')
    DATABASE = pymongo.MongoClient(URI).get_database()

    @staticmethod
    def insert(collection: str, data: Dict) -> None:
        """
        This method inserts a record into the specified collection in the database
        :param collection: The collection in the database
        :param data: The data we want inserted
        """
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor: ## cursor is an iterable
        """
        This method finds all records in the specified database collection matching the query
        :param collection: The collection in the database
        :param query: The JSON query we want to search on
        :return: Iterable cursor of records
        """
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        """
        This method finds first record in the specified database collection matching the query
        :param collection: The collection in the database
        :param query: The JSON query we want to search on
        :return: First record in the database as a Dict
        """
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        """
        This method upserts data into the specified database collection - If record exists, update else insert
        :param collection: The collection in the database
        :param query: The query to search on
        :param data: The data we want updated / inserted
        """
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict) -> Dict:
        """
        This method removes data that was queried from the specified database collection
        :param collection: The collection in the database
        :param query: The query to search on and remove
        :return: True is successful
        """
        return Database.DATABASE[collection].remove(query)