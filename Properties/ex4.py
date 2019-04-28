class Distance(object):
    def __init__(self):
        # This private attribute will store the distance in metres
        # All units provided using setters will be converted before
        # being stored
        self._distance = 0.0

    @property
    def in_metres(self):
        return self._distance

    @in_metres.setter
    def in_metres(self, val):
        try:
            self._distance = float(val)
        except:
            raise ValueError("The input you have provided is not recognised "
                             "as a valid number")

    @property
    def in_feet(self):
        return self._distance * 3.2808399

    @in_feet.setter
    def in_feet(self, val):
        try:
            self._distance = float(val) / 3.2808399
        except:
            raise ValueError("The input you have provided is not recognised "
                             "as a valid number")


if __name__ == '__main__':
    distance = Distance()
    # distance.in_metres = 1000.0
    # print(distance.in_feet)

    distance.in_feet = 1000.0
    print(distance.in_metres)



