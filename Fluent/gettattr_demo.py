class Dummy(object):
    def __getattr__(self, *attr, **kwargs):
        #
        print(attr)

d = Dummy()
# d.value = "Python"
# print(d.value)
print(d.not_a_value('hi'))

# But using the __getattr__ magic method, we can intercept that inexistent attribute lookup and do something so it doesn’t fail.
# But if the attribute does exist, __getattr__ won’t be invoked.