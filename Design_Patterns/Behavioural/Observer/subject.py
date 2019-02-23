from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def unregister_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class LibraryBook(Subject):
    def __init__(self, name, available=False):
        self.name = name
        self.is_available = available
        self.list_observers = []

    def register_observer(self, observer):
        self.list_observers.append(observer)

    def unregister_observer(self, observer):
        self.list_observers.remove(observer)

    def notify_observers(self):
        # The state of the Subject, which is 'self.is_available' is being passed
        # to all registered Observers
        for observer in self.list_observers:
            observer.update(self.is_available)

    def get_availability(self):
        return self.is_available

    def set_availability(self):
        print('Book is available now')
        self.is_available = True
        self.notify_observers()
