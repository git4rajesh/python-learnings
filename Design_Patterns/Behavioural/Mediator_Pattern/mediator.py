class Mediator:

    def __init__(self):
        self.person_list = []

    def add_person(self, person_object):
        self.person_list.append(person_object)

    def get_person_list(self):
        return self.person_list

    def send_message(self, message, person_object):
        print('-' * 100)
        for person in self.person_list:
            if person != person_object:
                person.receive(message)
