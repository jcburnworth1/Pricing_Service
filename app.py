## Import libraries
from models.item import Item

URL = 'https://www.johnlewis.com/john-lewis-partners-hemingway-3-door-sideboard/p230727606'
# < p class ="price price--large" > £260.00 < / p >
TAG_NAME = 'p'
QUERY = {"class": "price price--large"}

item = Item(URL, TAG_NAME, QUERY)
print(item.load_price())

# from flask import Flask
# from learning import learning_blueprint
#
# ## Application
# app = Flask(__name__)
#
# ## Register the blueprint
# app.register_blueprint(learning_blueprint, url_prefix='/greetings')
#
# ## Run the application
# if __name__ == '__main__':
#     app.run()
