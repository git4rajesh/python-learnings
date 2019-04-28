class Foo:
    def decorate1(self, param):
        def wrapper(func):
            def wrapped(*args, **kwargs):
                self.new_param = param + 'new1'
                return func(*args, **kwargs)

            return wrapped

        return wrapper

    def decorate2(self, param):
        def wrapper(func):
            def wrapped(*args, **kwargs):
                self.new_param = str(args[1]) + self.new_param + 'new2'
                return func(*args, **kwargs)

            return wrapped

        return wrapper
