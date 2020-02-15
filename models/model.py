## Import libraries
from abc import ABCMeta, abstractmethod
from common.database import Database
from typing import List

## Model Class
## Allows us abstract our model and enforce method definitions across child classes
class Model(metaclass=ABCMeta):
    ##### This doesn't do anything except get rid of warnings #####
    collection = 'models'

    def __init__(self, *args, **kwargs):
        pass
    ##### This doesn't do anything except get rid of warnings #####

    @abstractmethod
    def json(self): ## Must define json() in all models calling Model class
        raise NotImplementedError

    @classmethod
    def all(cls) -> List:
        """ Load all <collection> from mongo"""
        elements_from_db = Database.find(cls.collection, {})
        ## cls.collection - Warning because collection is not defined in Model class
        ## This is ok because child classes will have cls.collection defined

        return [cls(**elem) for elem in elements_from_db]