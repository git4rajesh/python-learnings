import random


class Features3:
    def get_innotas(self):
        prod = self.get_product()
        while prod in ['PVE', 'Rally']:
            prod = self.get_product()
        return prod

    def get_product(self):
        prod = random.choice(['PVE', 'PP', 'Innotas'])
        return prod


# f = Features3()
# response = f.get_innotas()
# print(response)
