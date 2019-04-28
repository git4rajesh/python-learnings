class Props(object):
    def __init__(self, val):
        self._x = val

    @property
    def x(self):
        return self._x


if __name__ == '__main__':
    obj = Props(6)
    print(obj.x)

    obj.x = 5  #We cant set a value as this
    print(obj.x)

