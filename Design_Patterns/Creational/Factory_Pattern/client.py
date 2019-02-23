from Design_Patterns.Creational.Factory_Pattern.animal_factory import AnimalFactory


class Client:
    @staticmethod
    def demo(animal_type):
        animal_factory = AnimalFactory()
        return animal_factory.get_animal(animal_type)

if __name__ == '__main__':
    animal_dog = Client.demo('Dog')
    animal_dog.who_am_i()
    animal_dog.get_quality()
    animal_duck = Client.demo('Duck')
    animal_duck.who_am_i()
    animal_duck.get_behaviour()

