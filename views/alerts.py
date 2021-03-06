## Import libraries
from flask import Blueprint, render_template, request, redirect, url_for, session
from models.alert import Alert
from models.store import Store
from models.item import Item
from models.user import requires_login

## Create item Blueprint
alert_blueprint = Blueprint('alerts', __name__)

## Alert Endpoint
@alert_blueprint.route('/')
@requires_login
def index():
    """
    This endpoint shows all of a user's alerts from database
    :return: Alert index for the application
    """
    alerts = Alert.find_many_by('user_email', session['email'])

    return render_template('alerts/alert_index.html', alerts=alerts)

## New Alerts Endpoint
@alert_blueprint.route('/new', methods=['GET', 'POST'])
@requires_login
def new_alert(): ## Must be logged in to save an alert
    """
    This endpoint allows a user to enter a new alert and save to the database
    :return: Alert index for the application once alert is successfully added
    """

    if request.method == 'POST':
        alert_name = request.form['name']
        item_url = request.form['item_url']
        price_limit = float(request.form['price_limit'])

        store = Store.find_by_url(item_url)
        item = Item(item_url, store.tag_name, store.query)
        item.load_price()
        item.save_to_mongo()

        ## Using protected here is fine since we are not changing item._id
        Alert(alert_name, item._id, price_limit, session['email']).save_to_mongo()

        return redirect(url_for('.index'))

    return render_template('alerts/new_alert.html')

## Edit Alerts Endpoint
@alert_blueprint.route('/edit/<string:alert_id>', methods=['GET', 'POST']) ## http://mysite/alerts/edit/<alert_id>
@requires_login
def edit_alert(alert_id):
    """
    This endpoint allows a user to edit an existing alert and save to the database
    :return: Alert index for the application once alert is successfully edited
    """
    alert = Alert.get_by_id(alert_id)

    if request.method == 'POST':
        price_limit = float(request.form['price_limit'])

        alert.price_limit = price_limit
        alert.save_to_mongo()

        return redirect(url_for('.index'))

    return render_template('alerts/edit_alert.html', alert=alert)

## Delete Alerts Endpoint
@alert_blueprint.route('/delete/<string:alert_id>')
@requires_login
def delete_alert(alert_id):
    """
    This endpoint allows a user to delete an existing alert and remove from the database
    :return: Alert index for the application once alert is successfully removed
    """
    alert = Alert.get_by_id(alert_id)

    if alert.user_email == session['email']:
        alert.remove_from_mongo()

    return redirect(url_for('.index'))