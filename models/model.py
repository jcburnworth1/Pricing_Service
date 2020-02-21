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
        """Upserting record into db - If _id exists, update, if not insert data"""
        Database.update(self.collection, {'_id': self._id}, self.json()) ## Leave this warning since assigned later

    def remove_from_mongo(self):
        """Find record for given _id and remove"""
        Database.remove(self.collection, {'_id': self._id})

    @classmethod
    def get_by_id(cls: Type[T], _id: str) -> 'T': ## Item.get_by_id -> Item, Alert.get_by_id() -> Alert
        """Return record for given _id"""
        return cls.find_one_by('_id', _id)

    @abstractmethod
    def json(self) -> Dict: ## Must define json() in all models calling Model class
        """Generic JSON model for child classes"""
        raise NotImplementedError

    @classmethod
    def all(cls: Type[T]) -> List[T]:
        """ Load all <collection> from mongo"""
        elements_from_db = Database.find(cls.collection, {})
        ## cls.collection - Warning because collection is not defined in Model class
        ## This is ok because child classes will have cls.collection defined
        ## Above definition collection: str resolves warnings

        return [cls(**elem) for elem in elements_from_db]

    @classmethod
    def find_one_by(cls: Type[T], attribute: str, value: Union[str, Dict]) -> T: ## Item.find_one_by('url', 'https://bla.com')
        """Find single record in mongo matching supplied attribute / value"""
        return cls(**Database.find_one(cls.collection, {attribute: value}))

    @classmethod
    def find_many_by(cls: Type[T], attribute: str, value: Union[str, Dict]) -> List[T]:
        """Find all records in mongo matching supplied attribute / value"""
        return [cls(**elem) for elem in Database.DATABASE.find(cls.collection, {attribute: value})]