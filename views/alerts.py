## Import libraries
from flask import Blueprint, render_template, request
from models.alert import Alert
from models.store import Store
from models.item import Item

## Create item Blueprint
alert_blueprint = Blueprint('alerts', __name__)

## Alert Endpoint
@alert_blueprint.route('/')
def index():
    """Return all alerts from mongo when landing here"""
    alerts = Alert.all()

    return render_template('alerts/index.html', alerts=alerts)

## New Alerts Endpoint
@alert_blueprint.route('/new', methods=['GET', 'POST'])
def new_alert():
    """Capture inputs from new alert page and save to mongo"""
    #
    if request.method == 'POST':
        item_url = request.form['item_url']
        price_limit = float(request.form['price_limit'])

        store = Store.find_by_url(item_url)
        item = Item(item_url, store.tag_name, store.query)
        item.save_to_mongo()

        Alert(item._id, price_limit).save_to_mongo() ## Using protected here is fine since we are not changing item._id

    return render_template('alerts/new_alert.html')