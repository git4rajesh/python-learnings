from abc import ABC, abstractmethod


class CoffeeTemplate(ABC):
    @abstractmethod
    def boil_water(self):
        pass

    @abstractmethod
    def add_milk(self):
        pass

    @abstractmethod
    def add_sugar(self):
        pass

    @abstractmethod
    def add_coffee_powder(self):
        pass

    def prepare_coffee(self):
        self.boil_water()
        self.add_milk()
        self.add_sugar()
        self.add_coffee_powder()
        print('{} Coffee is prepared'.format(self.__class__.__name__))

    # def make_template(self):
    #     func_seq = [self.boil_water, self.add_milk, self.add_sugar, self.add_coffee_powder]
    #     return func_seq
    #
    # def prepare_coffee(self):
    #     [func() for func in self.make_template()]
    #     print('{} Coffee is prepared'.format(self.__class__.__name__))


class BrahminsCoffee(CoffeeTemplate):
    def boil_water(self):
        print('Boiled 20 ml of water')

    def add_milk(self):
        print('Added and boiled 250 ml of milk')

    def add_sugar(self):
        print('Added  2 spoons of sugar')

    def add_coffee_powder(self):
        print('Added 10ml of b-patented dicoction')


class KumbakonamCoffee(CoffeeTemplate):
    def boil_water(self):
        print('Boiled 10 ml of water')

    def add_milk(self):
        print('Boiled and added 250 ml of milk')

    def add_sugar(self):
        print('Added  4 spoons of jaggery')

    def add_coffee_powder(self):
        print('Added 15ml of k-patented dicoction')
