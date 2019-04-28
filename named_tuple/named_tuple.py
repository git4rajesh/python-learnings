from collections import namedtuple

Animal = namedtuple('AnimalDetails', 'name age type')
animal = Animal(name="perry", age=31, type="cat")

print(animal, type(animal))
print(animal.name)

# they are backward compatible too
print(animal[0])


