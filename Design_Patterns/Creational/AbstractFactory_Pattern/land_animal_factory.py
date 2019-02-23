from Design_Patterns.Creational.AbstractFactory_Pattern.animal import Animal
from Design_Patterns.Creational.AbstractFactory_Pattern.animal import Cat
from Design_Patterns.Creational.AbstractFactory_Pattern.animal import Dog


class LandAnimalFactory:
    def __init__(self):
        self.animal = Animal()

    def get_animal(self, animal_type):
        if animal_type == 'Dog':
            self.animal = Dog()
        else:
            self.animal = Cat()
        return self.animal









