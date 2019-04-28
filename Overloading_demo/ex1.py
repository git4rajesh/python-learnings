class Book(object):
    def __init__(self, name=''):
        "defaults to a Book name"
        self.name = name

    @classmethod
    def name_and_cost(cls, name, cost):
        Book.cost = cost
        return cls(name)

    @classmethod
    def name_cost_category(cls, name, cost, category):
        Book.category = category
        return cls(name)

    @classmethod
    def book_wrapper(cls, name, cost, category):
        return Book.name_cost_category(name, cost, category)

if __name__ == '__main__':
    # obj1 = Book('Python')
    obj1 = Book()
    obj2 = Book.name_and_cost('Python', 45)
    print(obj2.__dict__)