# Decorators with arguements #

# The parameters of the nested inner() function inside the decorator is same
      # as the parameters of functions it decorates


def decor_wrapper(func):
    print('Inside Decorator')

    def inner_func(num):
        if num < 0:
            print("Negative number")
            return
        return func(num)
    return inner_func



@decor_wrapper
def incr(x):
    return x + 1

@decor_wrapper
def decr(x):
    return x - 1


if __name__ == '__main__':
    print(incr(5))

    # print(decr(2))
    # print(incr(-1))

## Why we get 'Inside Decorator' twice in the output?