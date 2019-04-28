### String Substitution with  a Dictionary using Format ###
dict1 = {
    'no_hats': 122,
    'no_mats': 42
}
print('Sam had {no_hats} hats and {no_mats} mats'.format(**dict1))

### String Substitution with  a List using Format ###
list1 = ['a', 'b', 'c']
my_str = 'The first element is {}'.format(list1)
print(my_str)

### List extraction
my_str = 'The first element is {0}, the second element is {1} and third element is {2}'.format(*list1)
print(my_str)

### String Substitution with  a Tuple using Format ###
tuple1 = ('one', 'second', 'third')
my_str = 'The first element is {0}, the second element is {1} and third element is {2}'.format(*tuple1)
print(my_str)

### String Substitution with  a String variable using Format ###
my_name = 'Rajesh'
my_str = 'Hi {0}'.format(my_name)
print(my_str)
