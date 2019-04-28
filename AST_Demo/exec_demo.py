code = """
def f(x):
    x = x + 1
    return x

print('This is my output.')
"""

Brand = 'Brand-X'
version = ''
code1 = """
if Brand == 'Brand-X':
    version = 2
"""

exec(code1)
print(version)

