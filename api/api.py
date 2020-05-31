import flask
from flask import request, abort, jsonify
from database_access import databaseaccess
import json
from bson import json_util
import requests
from database_access import manufacturer

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello world!</h1>"

@app.route('/api/manufacturers/')
def get_all_manufacturers():
    all_manufacturers = databaseaccess.DatabaseAccess.manufacturers_coll.find()
    manufacturer_list = []
    for doc in all_manufacturers:
        row = manufacturer.Manufacturer(doc['_id'], doc['name'], doc['abbreviation'])
        manufacturer_list.append(row.toObject())
    return jsonify(manufacturer_list)

app.run() # this wil run on 127.0.0.1 - not accessible over network
#app.run(host="192.168.1.112") # run it on an IP that I can access over my local network