class Human:

    def __init__(self):
        self.name = 'Guido'
        self.mouth = self.Mouth()
        self.brain = self.Brain()

    class Mouth:
        def talk(self):
            print('talking...')
            return Human()

    class Brain:
        def think(self):
            print('thinking...')
            return Human()


if __name__ == '__main__':
    guido = Human()
    guido.brain.think().mouth.talk()