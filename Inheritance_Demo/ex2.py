from Inheritance_Demo.ex1 import Parent

class Child3(Parent):
    def __init__(self):
        super().__init__()
        self.a = 'Raj'
        print('>>>Inside Child2', self.class_var)

    def change_member(self):
        self.a = 'esh'