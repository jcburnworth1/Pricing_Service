## Import libraries
from flask import Blueprint, render_template, request
from models.item import Item
import json

## Create item Blueprint
item_blueprint = Blueprint('items', __name__)

## Item Index Endpoint
@item_blueprint.route('/')
def index(): ## By default will show a list of all items stored in mongo
    items = Item.all()

    return render_template('items/index.html', items=items)

## Items Endpoint
@item_blueprint.route('/new', methods=['GET', 'POST'])
def new_item():

    ## Process the data on submit
    if request.method == 'POST':
        ## Capture the input values
        url = request.form['url']
        tag_name = request.form['tag_name']
        query =  json.loads(request.form['query']) ## Use json.loads to transform string to dict

        ## Create item object and save to mongo
        Item(url, tag_name, query).save_to_mongo()


    return render_template('items/new_item.html')