"""Sample file to serve as the basis for inspect examples.
"""


def module_level_function(arg1, arg2='default', *args, **kwargs):
    """This function is declared in the module."""
    local_variable = arg1
    print(local_variable)
    return


class A(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


obj_a = A('I am A')
objA_name= obj_a.get_name()
print(objA_name)


class B(A):
    def do_something(self):
        print('This is do-something of B class')


    def get_name(self):
        return 'B(' + self.name + ')'

obj_b = B('I am B')
objB_name = obj_b.get_name()
print(objB_name)


module_level_function('Call me Anywhere')