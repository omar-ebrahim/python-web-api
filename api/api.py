import flask
from flask import request, abort, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Test data
books = [
    {
        "id": 1,
        "name": "Harry Potter"
    },
    {
        "id": 2,
        "name": "Lord of the Rings"
    }
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello world!</h1>"

@app.route('/api/books/')
def get_all():
    return jsonify(books)

@app.route('/api/books/<int:id>')
def get_byid(id):
    for book in books:
        if book["id"] == id:
            return jsonify(book)
        else:
            abort(404, description = "Not found")

app.run() # this wil run on 127.0.0.1 - not accessible over network
#app.run(host="192.168.1.112") # run it on an IP that I can access over my local network