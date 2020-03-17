## Import libraries
import json
from flask import Blueprint, render_template, request, redirect, url_for
from models.store import Store
from models.user import requires_admin, requires_login

## Create item Blueprint
store_blueprint = Blueprint('stores', __name__)

## Store Endpoint
@store_blueprint.route('/')
@requires_login
def index():
    """
    This endpoint shows all available stores from the database
    :return: Store index for the application
    """
    stores = Store.all()

    return render_template('stores/store_index.html', stores=stores)

## New Store Endpoint
@store_blueprint.route('/new', methods=['GET', 'POST'])
@requires_admin
def create_store():
    """
    This endpoint allows a user to enter a new store and save to the database
    :return: Store index for the application once store is successfully added
    """
    if request.method == 'POST':
        name = request.form['name']
        url_prefix = request.form['url_prefix']
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])

        Store(name, url_prefix, tag_name,query).save_to_mongo()

        return redirect(url_for('.index'))


    return render_template('stores/new_store.html')

## Edit Stores Endpoint
@store_blueprint.route('/edit/<string:store_id>', methods=['GET', 'POST']) ## http://mysite/stores/edit/<store_id>
@requires_admin
def edit_store(store_id):
    """
    This endpoint allows a user to edit an existing store and save to the database
    :return: Store index for the application once store is successfully edited
    """
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
@requires_admin
def delete_store(store_id):
    """
    This endpoint allows a user to delete an existing store and remove from the database
    :return: Store index for the application once store is successfully removed
    """
    Store.get_by_id(store_id).remove_from_mongo()

    return redirect(url_for('.index'))