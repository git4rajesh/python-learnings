class Fluent:
    def __init__(self, cache=None):
        self.lst_cache = cache or []

    # Build the cache, and handle special cases
    def terminate_call(self, name):
        # Enables method chaining
        # lst_new = []
        # lst_new = self.lst_cache.append(name)

        return Fluent(self.lst_cache + [name])

    # Final method call
    def method(self):
        return self.lst_cache

    # Reflection
    def __getattr__(self, name):
        return self.terminate_call(name)

    # Reflection
    # def __getattribute__(self, name):
    #       return self.terminate_call(name)


fluent = Fluent()
chain = fluent.hello.world
print(chain.method())
# 'for' is a Python reserved word
new_chain = chain.thanks.terminate_call('for').all.the.fish
print(new_chain.method())




