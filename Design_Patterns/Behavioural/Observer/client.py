from Design_Patterns.Behavioural.Observer.observer import Person
from Design_Patterns.Behavioural.Observer.subject import LibraryBook


class Client:

    def __init__(self):
        self.person1 = Person('Ram')
        self.person2 = Person('Shyam')
        self.person3 = Person('Albert')

        self.libray_book = LibraryBook('Harry Potter')

        self.libray_book.register_observer(self.person1)
        self.libray_book.register_observer(self.person2)
        self.libray_book.register_observer(self.person3)

    def demo(self):
        print('Status of the Books availability: %s' % (self.libray_book.get_availability()))
        self.libray_book.set_availability()


if __name__ == '__main__':
    client = Client()
    client.demo()

