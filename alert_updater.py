## Import libraries
from models.alert import Alert

## Add an alert to mongo for testing purposes
# alert = Alert("607059942c484c72830b2fb3d93ef5c2", 1000)
# alert.save_to_mongo()

## Check mongo and the website - Alert the user if price is under the threshold
alerts = Alert.all()

for alert in alerts:
    alert.load_item_price()
    alert.notify_if_price_reached()

if not alerts:
    print("No alerts have been created. Add an item and an alert to begin!")