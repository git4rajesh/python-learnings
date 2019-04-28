class Child():
    def __init__(self):
        self.age = 32


c = Child()
if not hasattr(c, 'weight'):
    print(c.age)