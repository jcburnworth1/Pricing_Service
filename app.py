## Import libraries
from flask import Flask
from learning import learning_blueprint

## Application
app = Flask(__name__)

## Register the blueprint
app.register_blueprint(learning_blueprint, url_prefix='/greetings')

## Run the application
if __name__ == '__main__':
    app.run()