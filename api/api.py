import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Test data
books = [
    {
        "id:" 1,
    }
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello world!</h1>"

app.run()