### A function can return another function ###

### Here, inner_func() is a nested function which is defined and returned, each time we call wrapper_func() ###

def wrapper_func():
    print('Inside wrapper_func')
    def inner_func():
        print('Inside inner func')
    return inner_func


if __name__ == '__main__':
   inner_func_obj = wrapper_func()
   input()
   inner_func_obj()


