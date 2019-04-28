import json


class MyClass:
    def __init__(self, name):
        self.name = name

    def who_am_i(self):
        print(self.__dict__)

if __name__ == '__main__':
    obj1 = MyClass('Awesome')
    # Converting an Object dictionery to a Json ###
    json_obj1 = json.dumps(obj1.__dict__)
    print('obj1:\n', json_obj1, type(json_obj1))

    # Getting back the Object's dictionery ###
    obj2 = json.loads(json_obj1)

    print('obj2:\n', obj2, type(obj2))
    print(obj2['name'])

    # Assigning the dictionery to a new Object
    obj3 = MyClass('Hello')
    obj3.__dict__ = obj2
    print('obj3:\n', obj3.name)



