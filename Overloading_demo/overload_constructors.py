from overloading import overload


class Book(object):
    @overload
    def __init__(self, name: str):
        self.name = name

    @overload
    def __init__(self, name: str, cost: int):
        self.__init__(name)
        self.cost = cost

    @overload
    def __init__(self, name: str, cost: int, category: str):
        self.__init__(name, cost)
        self.category = category


if __name__ == '__main__':
    obj1 = Book('Python')
    print(obj1.__dict__)

    obj1 = Book('Ruby', 500)
    print(obj1.__dict__)

    obj1 = Book('Django', 1000, 'Technical')
    print(obj1.__dict__)
