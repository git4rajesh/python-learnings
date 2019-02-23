class CareTaker:
    def __init__(self):
        self.lst_memento = []

    def add_to_memento_list(self, memento):
        self.lst_memento.append(memento)

    def fetch_from_memento_list(self, index):
        print('The LED TV state is fetched from caretaker for index : %s' % str(index))
        return self.lst_memento[index]

    def print_care_taker(self):
        for item in self.lst_memento:
            item.LED_TV.describe_led_tv()