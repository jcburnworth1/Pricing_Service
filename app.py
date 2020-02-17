## Import libraries
from flask import Flask
from views.items import item_blueprint
from views.alerts import alert_blueprint

## Create the flask application
app = Flask(__name__) #'__main__'

## Register blueprints
app.register_blueprint(item_blueprint, url_prefix='/items')
app.register_blueprint(alert_blueprint, url_prefix='/alerts')

## Execute the program
if __name__ == '__main__':
    app.run(debug=True)