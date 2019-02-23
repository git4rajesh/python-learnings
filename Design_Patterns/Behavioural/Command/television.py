# This is the Device class or the receiver class

class Television:
    def __init__(self):
        self.volume = 1

    def tv_on(self):
        print('The TV is switched on')

    def tv_off(self):
        print('The TV is switched off')

    def increase_volume(self):
        print('The volume increased  to {}'.format(self.volume + 1))

    def decrease_volume(self):
        print('The volume decreased  to {}'.format(self.volume - 1))
