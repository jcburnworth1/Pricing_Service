## Import libraries
from abc import ABCMeta, abstractmethod

## Model Class
## Allows us abstract our model and enforce method definitions across child classes
class Model(metaclass=ABCMeta):

    @abstractmethod
    def json(self): ## Must define json() in all models calling Model class
        raise NotImplementedError

class MyModel(Model):
    def json(self):
        return {
            "name": "My Model"
        }

model = MyModel()
print(model.json())