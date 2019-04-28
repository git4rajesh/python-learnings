# Note:
# Our task is to search if some number is present in the array or not in O(1) time.
# Since range is limited, we can use index mapping (or trivial hashing).
# We use values as index in a big array. Therefore we can search and
# insert elements in O(1) time.

l = [1,4,3,-3,-2, 0, 2, 5, -5]

dct_numbers = {}
lst_pos =[None] * 6
lst_neg = [None] * 6

f_neg =  f_pos = None

for item in l:
    if item >= 0:
        index = item
        lst_pos[index] = item
    else:
        index = item * -1
        lst_neg[index] = item

dct_numbers['pos'] = lst_pos
dct_numbers['neg'] = lst_neg

print(dct_numbers)

def find_num(dct_numbers, num):
    status = False
    if num >= 0:
        lst_pos = dct_numbers['pos']
        if num in lst_pos:
            status =  True
    else:
        lst_neg = dct_numbers.get('neg')
        if num in lst_neg:
            status = True
    return status

status_found = find_num(dct_numbers, 3)
print(status_found)








