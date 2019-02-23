# ChangeInterface/Facade.py
class A:
    def __init__(self, x):
        print('Created object A with value {}'.format(x))


class B:
    def __init__(self, x):
        print('Created object B with value {}'.format(x))


class C:
    def __init__(self, x):
        print('Created object C with value {}'.format(x))


# Other classes that aren't exposed by the
# facade go here ...


class Facade:
    @staticmethod
    def makeA(x):
        return A(x)

    @staticmethod
    def makeB(x):
        return B(x)

    @staticmethod
    def makeC(x):
        return C(x)


# The client programmer gets the objects
# by calling the static methods:
a = Facade.makeA('A');
b = Facade.makeB('B');
c = Facade.makeC('C');

# Façade is often implemented as singleton abstract factory.
# Of course, you can easily get this effect by creating a class containing static factory methods