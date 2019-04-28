import inspect

from inspect_demo import MyClass

for name, data in inspect.getmembers(MyClass):
    if name == '__builtins__':
        continue
    print ('%s :' % name, repr(data))