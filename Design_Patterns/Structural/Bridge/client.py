from Design_Patterns.Structural.Bridge.abstraction_layer.message import LongMessage
from Design_Patterns.Structural.Bridge.abstraction_layer.message import ShortMessage

from Design_Patterns.Structural.Bridge.implementation_layer.message_sender import EmailMessageSender
from Design_Patterns.Structural.Bridge.implementation_layer.message_sender import SMSMessageSender


class Client:
    def __init__(self):
        self.message_sender = None
        self.message = None

    def run(self):
        print('Enter if the client wants to send Long or Short message')
        message_type = input()

        if message_type == 'Long':
            self.message_sender = EmailMessageSender()
            self.message = LongMessage(self.message_sender)
            self.message.send_message('Long Message')
        else:
            self.message_sender = SMSMessageSender()
            self.message = ShortMessage(self.message_sender)
            self.message.send_message('Short Message')


if __name__ == '__main__':
    client = Client()
    client.run()
