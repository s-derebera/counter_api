from flask import Flask
from flask import json as json_flask
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/counter.json")
def counter():
    f = open('counter.json')
    data = json.load(f)

    with open('counter.json', "w") as f:
        data['counter'] += 1
        json.dump(data, f)

    response = app.response_class(
        response=json_flask.dumps(data),
        status=200,
        mimetype='application/json'
    )
    
    return response