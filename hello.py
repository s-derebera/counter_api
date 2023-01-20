from flask import Flask
from flask import json as json_flask
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/counter.json")
def counter():
    data =  {"counter": 1}

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    
    return response