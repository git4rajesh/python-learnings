from collections import namedtuple
d = {"name": "joe", "age": 20}

Emp = namedtuple("Employee", d.keys())(*d.values())
print(Emp)

print(Emp.name)
print(Emp.age)
