class Animal:
    def __init__(self):
        pass

    def who_am_i(self):
        print('I am an Animal')


class Dog(Animal):
    def who_am_i(self):
        print('I am a Dog')


class Cat(Animal):
    def who_am_i(self):
        print('I am a Cat')

class Fish(Animal):
    def who_am_i(self):
        print('I am a Fish')

class Shark(Animal):
    def who_am_i(self):
        print('I am a Shark')