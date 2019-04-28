from collections import defaultdict

class AttributeDict(defaultdict):
    def __init__(self):
        super(AttributeDict, self).__init__(AttributeDict)
        self.my_dict = {'a': 1}

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        self[key] = value


obj = AttributeDict()

print(obj.my_dict['a'])