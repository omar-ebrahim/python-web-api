import flask
import json
import requests

from bson import json_util
from database_access import databaseaccess
from database_access import manufacturer
from flask import request, Response, abort, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello world!</h1>"


@app.route('/api/manufacturers/', methods=['GET', 'POST'])
def all_manufacturers():

    if request.method == 'GET':
        all_manufacturers = databaseaccess.DatabaseAccess.manufacturers_coll.find()
        manufacturer_list = []
        for doc in all_manufacturers:
            row = manufacturer.Manufacturer(
                doc['_id'], doc['name'], doc['abbreviation'])
            manufacturer_list.append(row.toObject())
        return jsonify(manufacturer_list)
    elif request.method == 'POST':
        data_to_insert = request.form
        row_to_insert = manufacturer.Manufacturer(
            int(data_to_insert['_id']
                ), data_to_insert['name'], data_to_insert['abbreviation']
        )
        inserted_row = databaseaccess.DatabaseAccess.manufacturers_coll.insert_one(
            row_to_insert.toObject())
        return_data = {'_id': inserted_row.inserted_id}
        resp = Response(json.dumps(return_data), status=200,
                        mimetype='application/json')
        return resp
    else:
        return abort(405)


@app.route('/api/manufacturers/<int:id>', methods=['GET', 'DELETE'])
def manufacturer_by_id(id):

    if request.method == 'GET':
        mf = databaseaccess.DatabaseAccess.manufacturers_coll.find_one({
                                                                       "_id": id})
        if mf is None:
            return abort(404, description="The manufacturer with id " + str(id) + " does not exist")
        else:
            row = manufacturer.Manufacturer(
                mf['_id'], mf['name'], mf['abbreviation'])
            return jsonify(row.toObject())
    elif request.method == 'DELETE':
        deleted_row = databaseaccess.DatabaseAccess.manufacturers_coll.delete_one({
                                                                                  "_id": id})
        return_data = {'deleted': deleted_row.deleted_count}
        resp = Response(json.dumps(return_data), status=200,
                        mimetype='application/json')
        return resp
    else:
        return abort(405)


app.run()  # this wil run on 127.0.0.1 - not accessible over network
# app.run(host="192.168.1.112") # run it on an IP that I can access over my local network
