class CounterResponse:
    def __init__(self, response, status, mimetype):
        self.response = response
        self.status = status
        self.mimetype = mimetype
        