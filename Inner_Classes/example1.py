class Human:

    def __init__(self):
        self.name = 'Guido'
        self.head = self.Head()

    class Head:
        @classmethod
        def talk(cls, name):
            print('Name is: {}'.format(name))
            return 'talking...'

    def print_human(self):
        name = 'raj'
        self.Head.talk(name)



if __name__ == '__main__':
    guido = Human()
    guido.print_human()
    print(guido.name)
    print(guido.head.talk('Hello'))