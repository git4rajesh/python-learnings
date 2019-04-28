from itertools import cycle

polys = ['triangle', 'square', 'pentagon', 'rectangle']
print('The master list of shapes:  {0}'.format(polys))
itr = cycle(polys)

shape1 = next(itr)
print(shape1)


shape2 =next(itr)
print(shape2)

shape3=next(itr)
print(shape3)

shape4=next(itr)
print(shape4)

shape5=next(itr)
print(shape5)

next(itr)
