# Demo Example for Decorators #


# Functions and methods are called CALLABLE as they can be called.
# In fact, any object which implements the special method __call__() is termed callable.
# So, in the most basic sense, a decorator is a callable that returns a callable.
# Basically, a decorator takes in a function, adds some functionality and returns it.
# So a return statement is important for a Decorator



def wrapper_func(my_func):
    print('Inside Wrapper Func')
    def inner_func():
        print('Inside Inner Func')
        my_func()
    return inner_func

def my_func():
    print('My Test Func')


if __name__ == '__main__':
   obj_for_wrapper = wrapper_func(my_func)
   input()
   obj_for_wrapper()

