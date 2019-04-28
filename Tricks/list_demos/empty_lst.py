# Create an empty list of size n
lst = [None] * 5

print(lst)

# Adding a single element to last index
lst[4] =1
print(lst)


# To remove None elements from a list

filter_obj = filter(None, lst)
lst_final = list(filter_obj)

print(lst_final)

