import time

SLEEP = 0.1


# Complex Parts
class Decoration:
    def do_decoration(self):
        print(u'Decorations are done with flowers')


class Food:
    def arrange_food(self):
        print(u'Food arrangements done')


class Invitations:
    def send_invitations(self):
        print(u'Invitations are being send')


class MusicTroops:
    def conduct_music(self):
        print(u"Music troop rehearsal managed")


# Facade
class EventManager:
    def __init__(self):
        self.dec_obj = Decoration()
        self.food_obj = Food()
        self.invite_obj = Invitations()
        self.music_obj = MusicTroops()


    def arrange_event(self):
        self.dec_obj.do_decoration()
        self.food_obj.arrange_food()
        self.invite_obj.send_invitations()
        self.music_obj.conduct_music()


# Client
if __name__ == '__main__':
    mgr_obj = EventManager()
    mgr_obj.arrange_event()
