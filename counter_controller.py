import json
from counter_model import CounterModel

class CounterController:
    def increase(self):
        counter_model = CounterModel()
        return counter_model.increase()
