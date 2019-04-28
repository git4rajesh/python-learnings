lst_complete = [1, 2, 3, None, 4, 5, None, 6, None]
print(lst_complete)

# def remove_none(item):
#     if item:
#         return item

#
# lst_using_map = map(lambda x: x if x else None, lst_complete)
# print(tuple(lst_using_map))


lst_filtered = filter(None, lst_complete)
print('after filtering')
print(tuple(lst_filtered))


# lst_filtered = list(filter(remove_none, lst_complete))




