from Design_Patterns.Behavioural.Memento.led_tv import LED_TV
from Design_Patterns.Behavioural.Memento.originator import Originator
from Design_Patterns.Behavioural.Memento.care_taker import CareTaker


class Client:
    def memento_demo(self):
        tv_42 = LED_TV(42, 60000, False)

        originator = Originator()
        originator.set_LED_TV(tv_42)

        memento_42 = originator.create_memento()

        care_taker = CareTaker()
        care_taker.add_to_memento_list(memento_42)
        print('*'* 100)
        tv_46 = LED_TV(46, 80000, True)
        originator.set_LED_TV(tv_46)
        memento_46 = originator.create_memento()
        care_taker.add_to_memento_list(memento_46)
        print('*' * 100)

        tv_50 = LED_TV(50, 100000, True)
        originator.set_LED_TV(tv_50)
        memento_50 = originator.create_memento()
        care_taker.add_to_memento_list(memento_50)
        print('*' * 100)
        tv_42.price = 75000

        memento = care_taker.fetch_from_memento_list(0)
        led_tv = originator.set_from_memento(memento)
        led_tv.describe_led_tv()


if __name__ == '__main__':
    client = Client()
    client.memento_demo()
