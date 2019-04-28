res = ((1, 'pass', '12-10'), (2, 'fail', '12-11'), (3, 'pass', '12-12'))

lookup = ((1, 'desc1', 'url1'), (2, 'desc2', 'url2'), (3, 'desc3', 'url3'))

def print_dict():
    import sys
    this_function_name = sys._getframe().f_code.co_name
    print(this_function_name)
    my_dict = {}
    for rindex, rvalue in enumerate(res):
        for lindex, lvalue in enumerate(lookup):
            if rvalue[0] == lvalue[0]:
                my_dict[lvalue[0]] = [rvalue[1], rvalue[0], lvalue[2]]


print_dict()


# z = zip(lookup, res)
#
# my_list = list(z)
#
# for index, value in enumerate(my_list):
#     print(index, value)