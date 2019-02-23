from abc import ABC, abstractmethod


class Message(ABC):
    def __init__(self):
        self.message_sender = ''

    @abstractmethod
    def send_message(self, message):
        pass


class LongMessage(Message):
    def __init__(self, message_sender_type):
        self.message_sender = message_sender_type

    def send_message(self, message):
        self.message_sender.send_message(message)


class ShortMessage(Message):
    def __init__(self, message_sender_type):
        self.message_sender = message_sender_type

    def send_message(self, message):
        if len(message) <= 50:
            self.message_sender.send_message(message)
        else:
            raise NameError('Cannot send message of size greater than 5')
