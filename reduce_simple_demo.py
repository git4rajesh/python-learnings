from functools import reduce
def add(x,y):
    return x+y

a = reduce(add, [5])

print(a)