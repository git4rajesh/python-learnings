from Inheritance_Demo.ex1 import Parent
from Inheritance_Demo.ex1 import *
from Inheritance_Demo.ex2 import *


if __name__ == '__main__':
    # objP = Parent()

    Parent.class_var = 'overridden'

    objc1 = Child1()
    # objc1.my_impl()

    time.sleep(30)
    objc2 = Child2()
    # objc3 = Child3()
    # print(objc3.a)

    # objc2.change_child3(objc3)
    # print(objc3.a)
    #
    # print('>>>>>>>>>>>', Child2.class_var)