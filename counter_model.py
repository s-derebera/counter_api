import json

class CounterModel:
    def increase(self):
        f = open('counter.json')
        data = json.load(f)

        with open('counter.json', "w") as f:
            data['counter'] += 1
            json.dump(data, f)
        
        return data

    def decrease(self):
        f = open('counter.json')
        data = json.load(f)

        with open('counter.json', "w") as f:
            if data['counter'] > 0:
                data['counter'] -= 1
            else:
                data['counter'] = 0
            json.dump(data, f)

        return data 

if __name__ == "__main__":
    c = CounterModel()
