# Write a function rotate(ar[], d) that rotates arr[] of size n by d elements.

# in_arr = [1,2,3,4,5]
# out_arr = [3,4,5,1,2]


def rotate_array_v1(l, d):
    if d == len(l):
        return l
    l2 = l.copy()
    for index, value in enumerate(l):
        if index < d:
            l2.append(value)
            del l2[0]
        else:
            return l2

def rotate_array_v2(l, d):
    index = 0
    while(index < d):
        l.append(l[0])
        del l[0]
        index +=1
    return l



l = [1,2,3,4,5]
print(l)
l = rotate_array_v2(l, 5)
print(l)

