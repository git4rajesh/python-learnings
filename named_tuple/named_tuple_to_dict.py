from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
animal = Animal(name="perry", age=31, type="cat")

# Named tuple to Ordered Dict
animal_dct = animal._asdict()
print(animal_dct['age'], type(animal_dct))




