import itertools

names = [ 'Raj', 'Amritha', 'Lakshmi']
colors = ['red', 'green', 'blue']

for name, color in itertools.izip(names, colors):
    print(name, '---', color)
