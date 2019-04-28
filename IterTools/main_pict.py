from itertools import chain, combinations, product


# Method to extract a value from nested tuple recursively
def extract_elem_from_tuple(my_var):
    for val in my_var:
        if type(val) == tuple:
            for val in extract_elem_from_tuple(val):
                yield val
        else:
            yield val


# Read from yaml file and create a list for each fields
lst_brand = ['Brand-X', 'Brand-Y', 'Brand-A']
lst_platform = ['98', 'NT', '2000', 'XP']
lst_version = [1, 2]


# Getting the Combinations from two lists
lst_complete = list(chain(lst_brand, lst_platform))
print(lst_complete)
combination_lst = list(combinations(lst_complete, 2))
print(len(combination_lst), combination_lst)



# Removing unwanted combinations
temp_combination_lst = combination_lst.copy()
for item in combination_lst:
    if item[0] in lst_brand and item[1] in lst_brand:
        temp_combination_lst.remove(item)
    elif item[0] in lst_platform and item[1] in lst_platform:
        temp_combination_lst.remove(item)
    else:
        continue
print(len(temp_combination_lst), temp_combination_lst)


# Expanding a nested tuple
lst_out = []
for every_item in temp_combination_lst:
    out = list(extract_elem_from_tuple(every_item))
    lst_out.append(out)
print('>>>>>>>>>>>>>>>>', lst_out)



# Get number of occurence of value1 in the combination list
flatten_lst = list(chain(*lst_out))
occurence_count = flatten_lst.count(lst_brand[0])
print('Count of item in field-1:  {0}'.format(occurence_count))
print(lst_out)








# Cartesian Product
# out_lst = list(product(temp_combination_lst, lst_version))
# print(len(out_lst), out_lst)


# Expanding a nested tuple
# lst_out = []
# for every_item in out_lst:
#     out = list(extract_elem_from_tuple(every_item))
#     lst_out.append(out)
# print('>>>>>>>>>>>>>>>>', lst_out)








