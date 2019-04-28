from Decorators.Demo.advanced.foo import Foo


class Bar:
    foo = Foo()
    param = 'test'

    @foo.decorate1(param)
    @foo.decorate2(param)
    def func(self, number):
        print('Inside func')
        print(Bar.foo.new_param)


if __name__ == '__main__':
    bar_obj = Bar()
    bar_obj.func(3)
