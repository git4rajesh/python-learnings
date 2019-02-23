from Design_Patterns.Behavioural.Template.parent import BrahminsCoffee
from Design_Patterns.Behavioural.Template.parent import KumbakonamCoffee


class Client():
    def __init__(self):
        pass

    def run(self, coffee_type):
        coffee_type.prepare_coffee()


if __name__ == '__main__':
    client_obj = Client()
    b_coffee = BrahminsCoffee()
    k_coffee = KumbakonamCoffee()

    client_obj.run(b_coffee)

    print('==========================')
    client_obj.run(k_coffee)
