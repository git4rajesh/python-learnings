from functools import partial


def multiply(x, y):
    return x * y


def multiples_of_two():
    return 2


def multiples_of_three():
    return 3


dbl = partial(multiply, multiples_of_three())
print(dbl(4))
