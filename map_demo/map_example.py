def my_func(item, alst):
    d={}
    d[item] = alst
    return d


def call_func():

    m = map(my_func, ['a','b','c', 'd'], [1,2,3])
    print(list(m))

call_func()