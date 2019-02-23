from abc import ABC, abstractmethod

from Design_Patterns.Creational.AbstractFactory_Pattern.sea_animal_factory import SeaAnimalFactory

from Design_Patterns.Creational.AbstractFactory_Pattern.land_animal_factory import LandAnimalFactory


class AnimalFactory(ABC):

    @abstractmethod
    def getAnimal(self, animal_type):
        pass

    @staticmethod
    def get_animal_factory(factory_type):
        if factory_type == 'Land':
            animal_factory = LandAnimalFactory()
        else:
            animal_factory = SeaAnimalFactory()
        return animal_factory

