import importlib

# from Design_Patterns.Creational.Factory_Pattern.animal import Animal
# from Design_Patterns.Creational.Factory_Pattern.animal import Dog
# from Design_Patterns.Creational.Factory_Pattern.animal import Duck

# MODULE_PREFIX = 'Design_Patterns.Creational.Factory_Pattern.animal'
MODULE_PREFIX = 'animal'


class AnimalFactory:
    def __init__(self):
        pass
        # self.animal = Animal()

    # def get_animal_v1(self, animal_type):
    #     if animal_type == 'Dog':
    #         self.animal = Dog()
    #     else:
    #         self.animal = Duck()
    #     return self.animal

    def get_animal(self, animal_type):
        # Creating the module from a String using importlib
        module_name = importlib.import_module(MODULE_PREFIX)

        # Creating a Class from a module and a class in String string_format
        animal_class = getattr(module_name, animal_type)

        # Creating an instance of the Class
        animal = animal_class()
        return animal

