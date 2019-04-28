import copy

l1 = [{'a': 1}, {'b': 2, 'cat': 'animal', 'crow': 'bird'}, {'d': 4}]

l2 = copy.deepcopy(l1)

print(l1)
print(l2)

# Mutating l1
l1.append({'Planet':'Earth'})
l1[1].pop('b')
print(l1)
print(l2)