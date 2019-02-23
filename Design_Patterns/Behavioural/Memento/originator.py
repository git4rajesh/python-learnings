import copy
from Design_Patterns.Behavioural.Memento.memento import Memento

class Originator:
    def get_LED_TV(self):
        return self.LED_TV

    def set_LED_TV(self, led_tv):
        self.LED_TV = led_tv
        self.LED_TV.describe_led_tv()

    def create_memento(self):
        memento = Memento(copy.deepcopy(self.LED_TV))
        return memento

    def set_from_memento(self, memento):
        self.LED_TV = memento.get_LED_TV_from_memento()
        return self.LED_TV

