## Import libraries
from flask import Flask, render_template, request
from models.item import Item
import json

## Create the flask application
app = Flask(__name__) #'__main__'

## Home Endpoint
@app.route('/', methods=['GET', 'POST'])
def new_item():

    ## Process the data on submit
    if request.method == 'POST':
        ## Capture the input values
        url = request.form['url']
        tag_name = request.form['tag_name']
        query =  json.loads(request.form['query']) ## Use json.loads to transform string to dict

        ## Create item object and save to mongo
        Item(url, tag_name, query).save_to_mongo()


    return render_template('new_item.html')

## Execute the program
if __name__ == '__main__':
    app.run(debug=True)