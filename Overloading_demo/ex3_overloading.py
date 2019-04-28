from overloading import overload

@overload
def biggest(name, age):
    print(name, age)

@overload
def biggest(name):
    print(name)

biggest('Ram', 3)
biggest('Raj')