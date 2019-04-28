import random


class Features:
    def is_innotas(self):
        prod = self.get_product()
        if prod == 'Innotas':
            return True
        else:
            return False

    def get_product(self):
        prod = random.choice(['PVE', 'PP', 'Innotas'])
        return prod


f = Features()
bool_response = f.is_innotas()
print(bool_response)
