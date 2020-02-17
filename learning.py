########## Set the blueprint for our application ##########
## Import libraries
from flask import Blueprint

## Setup blueprint
learning_blueprint = Blueprint('learning', __name__)

## Define Base Endpoint
@learning_blueprint.route('/<string:name>')

## Function for base endpoint
def home(name):
    return f"Hello, {name}!"