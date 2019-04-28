import pickle

class A:
    def __init__(self):
        self.name = 'Anonymous'
        self.age = None
        self.gender = 'M'

    def __getstate__(self):
        self.name = 'Raj'
        self.age = 24
        return (self.name,self.age)

    def __setstate__(self):
        self.name = 'Test'
        self.age = 42

if __name__ == '__main__':
    obj = A()
    print(obj.name, obj.age, obj.gender)
    a_pickled = pickle.dumps(obj)
    a_unpickled = pickle.loads(a_pickled)
    print(a_unpickled.name, a_unpickled.age)