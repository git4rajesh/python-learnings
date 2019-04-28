import itertools

my_lst = [4, 1, 2, 3, 5]

print('Source list :   {0}'.format(my_lst))

combination_lst = list(itertools.combinations(my_lst, 2))

print('After combination:   {0}'.format(combination_lst))

# permutation_lst = list(itertools.permutations(my_lst, 2))
#
# print('After permutation:   {0}'.format(permutation_lst))
