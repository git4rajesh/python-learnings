from abc import abstractmethod


class Persons:
    @abstractmethod
    def send(self, message, mediator_object):
        pass

    @abstractmethod
    def receive(message):
        pass


class Person1(Persons):
    def send(self, message, mediator_object):
        print('\n\n')
        print('Person1 : %s' % message)
        mediator_object.send_message(message, self)

    @staticmethod
    def receive(message):
        print('Person1 received : %s' % message)


class Person2(Persons):
    def send(self, message, mediator_object):
        print('\n\n')
        print('Person2 : %s' % message)
        mediator_object.send_message(message, self)

    @staticmethod
    def receive(message):
        print('Person2 received : %s' % message)


class Person3(Persons):
    def send(self, message, mediator_object):
        print('\n\n')
        print('Person3 : %s' % message)
        mediator_object.send_message(message, self)

    @staticmethod
    def receive(message):
        print('Person3 received : %s' % message)
