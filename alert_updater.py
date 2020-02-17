########## Alert Example ##########
## Import libraries
from models.alert import Alert

## Add an alert to mongo for testing purposes
alert = Alert("25dee59f49f34cb4b70a96315e7a3890", 1700)
alert.save_to_mongo()

## Check mongo and the website - Alert the user if price is under the threshold
alerts = Alert.all()

for alert in alerts:
    alert.load_item_price()
    alert.notify_if_price_reached()

if not alerts:
    print("No alerts have been created. Add an item and an alert to begin!")