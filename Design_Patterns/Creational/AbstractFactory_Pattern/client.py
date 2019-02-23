from Design_Patterns.Creational.AbstractFactory_Pattern.animal_factory import AnimalFactory


class Client:

    @staticmethod
    def demo(animal_factory_type, animal_type):
        animal_factory = AnimalFactory.get_animal_factory(animal_factory_type)
        animal_factory.get_animal(animal_type).who_am_i()

if __name__ == '__main__':
    client = Client()
    client.demo('Land', 'Cat')
    client.demo('Sea', 'Fish')
