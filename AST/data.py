def wrapper_func(my_func):
    print('Inside Wrapper Func')
    def inner_func():
        print('Inside Inner Func')
        my_func()
    return inner_func

@wrapper_func
def test_func():
    print('My Test Func')


