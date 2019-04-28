class Props(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        print('Inside delete method')
        del self._x

if __name__ == '__main__':
    obj = Props()
    print(obj.__dict__)
    obj.x = 5
    print(obj.x)

    del obj.x

    print(obj.__dict__)

