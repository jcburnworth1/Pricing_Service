########## Alert Update Code ##########
## Import libraries
from models.alert import Alert
from dotenv import load_dotenv

## load Environmental Variables
load_dotenv()

## Check mongo and the website - Alert the user if price is under the threshold
alerts = Alert.all()

for alert in alerts:
    alert.load_item_price()
    alert.notify_if_price_reached()

if not alerts:
    print("No alerts have been created. Add an item and an alert to begin!")