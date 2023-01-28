from flask import json as json_flask
from counter_model import CounterModel
from counter_response import CounterResponse

class CounterController:
    def increase(self):
        counter_model = CounterModel()
        response = counter_model.increase()

        return CounterResponse(
            response=json_flask.dumps(response),
            status=200,
            mimetype='application/json'
        )

    def decrease(self):
        counter_model = CounterModel()
        response = counter_model.decrease()

        return CounterResponse(
            response=json_flask.dumps(response),
            status=200,
            mimetype='application/json'
        )