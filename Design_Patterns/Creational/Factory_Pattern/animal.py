class Animal:
    def __init__(self):
        pass

    def who_am_i(self):
        print('I am an Animal')


class Dog(Animal):
    def who_am_i(self):
        print('I am a Dog')

    def get_quality(self):
        print('I am an awesome pet')


class Duck(Animal):
    def who_am_i(self):
        print('I am a Duck')

    def get_behaviour(self):
        print('I can swim')
