from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, availability):
        pass


class Person(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, is_available):
        if is_available:
            print('The Book is available for person: %s' % (self.name) )
        else:
            print('The Book is not available for person: %s' % (self.name))

