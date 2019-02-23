class GOT:
    def __init__(self):
        self.animal = ''


class Targaryens(GOT):
    def __init__(self, animal):
        self.favorite = 'Daenerys'
        self.animal = animal

    def get_details(self):
        print('This is {0} who has {1}'.format(self.favorite, self.animal.name))


class Starks(GOT):
    def __init__(self, animal):
        self.favorite = 'Arya'
        self.animal = animal

    def get_details(self):
        print('This is {0} who has {1}'.format(self.favorite, self.animal.name))
