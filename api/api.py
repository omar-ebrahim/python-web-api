import flask
import json
import requests

from bson import json_util
from database_access import databaseaccess
from database_access import manufacturer
from flask import request, abort, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello world!</h1>"


@app.route('/api/manufacturers/', methods=['GET'])
def get_all_manufacturers():
    all_manufacturers = databaseaccess.DatabaseAccess.manufacturers_coll.find()
    manufacturer_list = []
    for doc in all_manufacturers:
        row = manufacturer.Manufacturer(
            doc['_id'], doc['name'], doc['abbreviation'])
        manufacturer_list.append(row.toObject())
    return jsonify(manufacturer_list)


@app.route('/api/manufacturers/<int:id>/', methods=['GET'])
def get_manufacturer_by_id(id):
    mf = databaseaccess.DatabaseAccess.manufacturers_coll.find_one({"_id": id})
    if mf is None:
        return abort(404, description="The manufacturer with id " + str(id) + " does not exist")
    else:
        row = manufacturer.Manufacturer(
            mf['_id'], mf['name'], mf['abbreviation'])
        return jsonify(row.toObject())


app.run()  # this wil run on 127.0.0.1 - not accessible over network
# app.run(host="192.168.1.112") # run it on an IP that I can access over my local network
