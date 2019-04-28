import random


def is_innotas():
    prod = get_product()
    if prod == 'Innotas':
        return True
    else:
        return False


def get_product():
    prod = random.choice(['PVE', 'PP', 'Innotas'])
    return prod

print(is_innotas())