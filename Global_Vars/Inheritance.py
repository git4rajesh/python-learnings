class Parent(object):
    def __init__(self):
        print(self.ATTRS)


class Child(Parent):
    #class variable
    ATTRS = ['attr1', 'attr2', 'attr3']

    def __init__(self):
        super().__init__()


c = Child()