## Import libraries
import json
from flask import Blueprint, render_template, request, redirect, url_for
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

        return redirect(url_for('.index'))


    return render_template('stores/new_store.html')

## Edit Stores Endpoint
@store_blueprint.route('/edit/<string:store_id>', methods=['GET', 'POST']) ## http://mysite/alerts/edit/<store_id>
def edit_alert(store_id):
    """Retrieve store from mongo for modification"""
    store = Store.get_by_id(store_id)

    if request.method == 'POST':
        name = request.form['name']
        url_prefix = request.form['url_prefix']
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query']) # String to Dict (JSON)

        store.name = name
        store.url_prefix = url_prefix
        store.tag_name = tag_name
        store.query = query

        store.save_to_mongo()

        return redirect(url_for('.index'))

    return render_template('stores/edit_store.html', store=store)

## Delete Stores Endpoint
@store_blueprint.route('/delete/<string:store_id>')
def delete_store(store_id):
    Store.get_by_id(store_id).remove_from_mongo()