class Parent:
    def __init__(self, name ):
        self.name = name


class Child(Parent):
    def __init__(self, name, age):
        super(name)
        self.age = age

    @classmethod
    def get_details(cls):
        name = input('Enter name')
        age = input('Enter age')
        cls(name, age)
        


