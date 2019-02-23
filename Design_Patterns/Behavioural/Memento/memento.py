class Memento:
    def __init__(self, led_tv):
        self.LED_TV = led_tv

    def get_LED_TV_from_memento(self):
        return self.LED_TV


    ## Dont want users to set it directly
    # def set_LED_TV(self, led_tv):
    #      self.LED_TV = led_tv



