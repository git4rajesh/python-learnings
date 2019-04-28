import time

class Parent:
    class_var = None

    def __init__(self):
        self.ticks = time.time()
        print('Inside parent')

    def my_impl(self, var):
        print('Parents impl', var)


class Child1(Parent):
    def __init__(self):
        super().__init__()
        print('>>>Inside Child1', Child1.class_var)
        print('Getting name', self.ticks)

    def my_impl(self):
        print('Childs impl')

        super().my_impl('a')



class Child2(Parent):
    def __init__(self):
        super().__init__()
        print('>>>Inside Child2', Child2.class_var)
        print('Getting name', self.ticks)


    def change_child3(self, c3_obj):
        c3_obj.a = 'Changed'






