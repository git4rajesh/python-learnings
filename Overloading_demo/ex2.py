class Vector:
    """
    Demo of a class with multiple signatures for the constructor
    """
    def __init__(self, constructor=()):
        self.values = list(constructor)

    @classmethod
    def from_values(cls, *args):
        return cls(args)

    @classmethod
    def from_vector(cls, vector):
        return cls(vector.values)

if __name__ == '__main__':
    v = Vector.from_values(1,2,3)
    # print('>>>', v.__dict__)
    # v = Vector([4,5,6])
    #
    # q = Vector.from_vector(v);
    print('>>>', v.values)