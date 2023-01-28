from flask import Flask
from flask import json as json_flask
from counter_controller import CounterController

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/increase.json")
def increase():
    controller = CounterController()

    response = app.response_class(
        response=json_flask.dumps(controller.increase()),
        status=200,
        mimetype='application/json'
    )
    
    return response