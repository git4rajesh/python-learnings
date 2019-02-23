from Design_Patterns.Behavioural.Mediator_Pattern.persons import *

from Design_Patterns.Behavioural.Mediator_Pattern.mediator import Mediator


class Client:
    def __init__(self):
        self.mediator_object = Mediator()
        self.person1 = Person1()
        self.person2 = Person2()
        self.person3 = Person3()

        self.mediator_object.add_person(self.person1)
        self.mediator_object.add_person(self.person2)
        self.mediator_object.add_person(self.person3)

    def demo(self):
        self.person1.send('Nice demo for Mediator Pattern', self.mediator_object)
        self.person2.send('I agree', self.mediator_object)
        self.person3.send('Thanks a lot', self.mediator_object)


if __name__ == '__main__':
    client = Client()
    client.demo()