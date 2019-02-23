import copy


class LED_TV:
    def __init__(self, size, price, usb_support):
        self.size = size
        self.price = price
        self.usb_support = usb_support

    def describe_led_tv(self):
        print('The LED TV @ Hall is ==> size: %s , price: %s, usb_support: %s' % (self.size, self.price, self.usb_support))


if __name__ == '__main__':
    tv_42 = LED_TV(42, 60000, False)
    tv_42.describe_led_tv()

    tv_46 = LED_TV(46, 80000, True)
    tv_46.describe_led_tv()

    tv_50 = LED_TV(50, 100000, True)
    tv_50.describe_led_tv()

    tv_42_deepcopy = copy.deepcopy(tv_42)
    tv_42_deepcopy.price = 20000
    tv_42.describe_led_tv()
    tv_42_deepcopy.describe_led_tv()