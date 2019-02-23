class MessageSender:
    def send_message(self, message):
        pass


class SMSMessageSender(MessageSender):
    def send_message(self, message):
        print('SMS is being sent for: {}'.format(message))


class EmailMessageSender(MessageSender):
    def send_message(self, message):
        print('Email is being sent for: {}'.format(message))
