## Import libraries
from flask import Blueprint, render_template, request, url_for
import json
from models.store import Store

## Create item Blueprint
store_blueprint = Blueprint('stores', __name__)

## Store Endpoint
@store_blueprint.route('/')
def index():
    """Return all stores from mongo when landing here"""
    stores = Store.all()

    return render_template('stores/store_index.html', stores=stores)

## New Store Endpoint
@store_blueprint.route('/new', methods=['GET', 'POST'])
def create_store():

    if request.method == 'POST':
        name = request.form['name']
        url_prefix = request.form['url_prefix']
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])

        Store(name, url_prefix, tag_name,query).save_to_mongo()


    return render_template('stores/new_store.html')