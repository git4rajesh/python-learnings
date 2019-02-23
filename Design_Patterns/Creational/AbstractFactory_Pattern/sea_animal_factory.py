from Design_Patterns.Creational.AbstractFactory_Pattern.animal import Animal
from Design_Patterns.Creational.AbstractFactory_Pattern.animal import Fish
from Design_Patterns.Creational.AbstractFactory_Pattern.animal import Shark


class SeaAnimalFactory:
    def __init__(self):
        self.animal = Animal()

    def get_animal(self, animal_type):
        if animal_type == 'Fish':
            animal = Fish()
        else:
            animal = Shark()
        return animal