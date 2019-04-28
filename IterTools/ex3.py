import itertools

A = [1, 2, 3]
B = [4]
C = [5, 6]

print("product example:")
s = [A, B, C]
print(s)
print(list(itertools.product(*s)))
