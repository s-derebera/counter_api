from flask import Flask
from counter_controller import CounterController

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/increase.json")
def increase():
    controller = CounterController()
    counter_response = controller.increase()

    response = app.response_class(
        response=counter_response.response,
        status=counter_response.status,
        mimetype=counter_response.mimetype
    )
    
    return response