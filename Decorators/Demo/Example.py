### Decorators also called Meta Programming ###

### Functions that take other functions as arguments and return function objects are called as Higher Order functions ###

### Examples : map, filter and reduce ###

def incr (x):
        return x + 1

def decr(x):
        return x - 1

def higher_order_wrapper(func, n):
    result = func(n)
    return result

if __name__ == '__main__':
    print(higher_order_wrapper(incr, 5))
    print(higher_order_wrapper(decr, 3))

    from functools import partial
    # print(incr,)



