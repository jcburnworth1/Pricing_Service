## Import libraries
import os
from flask import Flask, render_template
from views.alerts import alert_blueprint
from views.stores import store_blueprint
from views.users import user_blueprint
from common.database import Database

## Create the flask application
app = Flask(__name__) #'__main__'
app.secret_key = os.urandom(64) ## This needs to be random for secure key / cookie generation
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)

## This works fine
# @app.before_first_request
# def inti_db():
#     Database.initialize()

## Register blueprints
app.register_blueprint(alert_blueprint, url_prefix='/alerts')
app.register_blueprint(store_blueprint, url_prefix='/stores')
app.register_blueprint(user_blueprint, url_prefix='/users')

@app.route('/')
def home():
    return render_template('home.html')

## Execute the program
if __name__ == '__main__':
    app.run(debug=True)