from functools import wraps

def newobj(wrapped_method):
    @wraps(wrapped_method)
    # Well, newobj can be decorated with function, but we will cover the case
    # where it decorated with method
    def inner(self, *args, **kwargs):
        obj = self.__class__.__new__(self.__class__)
        obj.__dict__ = self.__dict__.copy()
        wrapped_method(obj, *args, **kwargs)
        del self
        return obj
    return inner


class Fluent(object):
    def __init__(self, content):
        self.content = content

    @newobj
    def call1(self, spaces='@@@@@'):
        self.content = self.content + spaces

    @newobj
    def call2(self, content):
        self.content += " - {}".format(content)

    # def __str__(self):
    #     return self.content





# p = Fluent("foo")
# q = p.call1()
# r = p.call1()
# print(str(q) == str(r))
# print(id(q), id(r))

f = Fluent('In Init').call1().call2('End').call1().call2('Final end').call1()
print(f.content)

