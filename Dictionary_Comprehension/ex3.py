from Dictionary_Comprehension.dotable import Dotable


class Myclass():
    def __init__(self):
        old_dct = {'a': [{'b': {'b1': 'BE ONE'}, 'c': 5}]}
        self.new_dct = Dotable.parse(old_dct)


if __name__ == '__main__':
    obj = Myclass()
    print(obj.new_dct.a[0].b.b1)
