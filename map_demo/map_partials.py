a = [1, 2, 3]

import functools


def add(x, y):
    return x + y


output = map(functools.partial(add, y=2), a)

print(list(output))
