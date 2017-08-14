
class Books():
    def __init__(self, keys, values):
        self.data = values
        self.dict_data = dict(zip(keys, values))

    def getValue(self, key):
        return self.dict_data.get(key, '')

    def get_data(self):
        return self.data