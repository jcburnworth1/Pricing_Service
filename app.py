## Import libraries
from flask import Flask
# from views.items_deprecated import item_blueprint
from views.alerts import alert_blueprint
from views.stores import store_blueprint

## Create the flask application
app = Flask(__name__) #'__main__'

## Register blueprints
app.register_blueprint(alert_blueprint, url_prefix='/alerts')
app.register_blueprint(store_blueprint, url_prefix='/stores')

## Execute the program
if __name__ == '__main__':
    app.run(debug=True)