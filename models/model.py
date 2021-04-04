## Import libraries
from abc import ABCMeta, abstractmethod
from common.database import Database
from typing import List, TypeVar, Type, Dict, Union

## Custom Type for get_by_id() method because subclasses return different object types
T = TypeVar('T', bound='Model') ## This will match return value to caller class

## Model Class - This is a superclass
## Allows us to abstract our model and enforce method definitions across child classes
class Model(metaclass=ABCMeta):
    ##### This doesn't do anything except get rid of warnings #####
    collection: str
    _id: str

    def __init__(self, *args, **kwargs):
        pass
    ##### This doesn't do anything except get rid of warnings #####

    def save_to_mongo(self):
        """
        This method upserts the model object to the database - If _id exists, update, if not insert data
        """
        Database.update(self.collection, {'_id': self._id}, self.json()) ## Leave this warning since assigned later

    def remove_from_mongo(self):
        """
        This method finds the given _id and removes from the database
        """
        Database.remove(self.collection, {'_id': self._id})

    @classmethod
    def get_by_id(cls: Type[T], _id: str) -> 'T': ## Item.get_by_id -> Item, Alert.get_by_id() -> Alert
        """
        This method finds the record by a given _id
        :param collection: Uses collection specified in the child class
        :return: The found record if exists
        """
        return cls.find_one_by('_id', _id)

    @abstractmethod
    def json(self) -> Dict: ## Must define json() in all models calling Model class
        """
        This is an abstracted method for child classes to make use of, Must be implemented by each child class
        """
        raise NotImplementedError

    @classmethod
    def all(cls: Type[T]) -> List[T]:
        """
        This method loads all objects found in a given database collection
        :return: List of all elements in a given database collection
        """
        elements_from_db = Database.find(cls.collection, {})
        ## cls.collection - Warning because collection is not defined in Model class
        ## This is ok because child classes will have cls.collection defined
        ## Above definition collection: str resolves warnings

        return [cls(**elem) for elem in elements_from_db]

    @classmethod
    def find_one_by(cls: Type[T], attribute: str, value: Union[str, Dict]) -> T: ## Item.find_one_by('url', 'https://bla.com')
        """
        This method finds a single record in the database matching a supplied attribute / value
        :param collection: Uses collection specified in the child class
        :param attribute: The key we want to search on
        :param value: The value we want to find
        :return: The record found
        """
        return cls(**Database.find_one(cls.collection, {attribute: value}))

    @classmethod
    def find_many_by(cls: Type[T], attribute: str, value: str) -> List[T]:
        """
        This method finds all records in the database matching a supplied attribute / value
        :param collection: Uses collection specified in the child class
        :param attribute: The key we want to search on
        :param value: The value we want to find
        :return: The records found
        """
        return [cls(**elem) for elem in Database.find(cls.collection, {attribute: value})]
