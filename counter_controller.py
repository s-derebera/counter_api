import json

class CounterController:
    def increase(self):
        f = open('counter.json')
        data = json.load(f)

        with open('counter.json', "w") as f:
            data['counter'] += 1
            json.dump(data, f)
        
        return data
