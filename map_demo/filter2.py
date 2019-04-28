names = ['Ram', 'Raj', 'Amir', 'Shyam']

def filter_names_using_map(name):
    if (name.startswith('R')):
        return name


def filter_names_using_filter(name):
    if(name.startswith('R')):
        return True
    # else:
    #     return False
#
filteredNames= list(filter(filter_names_using_filter, names))

# filteredNames= list(map(filter_names_using_map, names))

print('The filtered Names are:')
print(filteredNames)