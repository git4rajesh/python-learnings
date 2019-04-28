class Props(object):
    def __init__(self):
        self._x = 0

    @property
    def get_x(self):
        return self._x

    @get_x.setter
    def x(self, x):
        print('Inside setter')
        if (x > 4):
            self._x = x
        else:
            print('Cant set')


if __name__ == '__main__':
    obj = Props()
    obj.x = 4  # Validations inside setter method
    print(obj.x)

    # obj.x = 5
    # print(obj.x)
