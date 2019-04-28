def demo_method_for_kwargs(**kwargs):
    dct_var = kwargs
    print(type(dct_var))
    if 'name' in dct_var:
        print(dct_var['name'])
        print(dct_var['id'])

    # second_method(**dct_var)
#
#
# def second_method(**data):
#     d2 = {'a':1, 'b':2}
#     print('data', type(data))
#     print('d2', type(d2))
#     print({**d2, **data})
#     print('>>>>>', data.update(d2))
#
#
# data = {}
# data['name'] = 'Test'
# data['id'] = 1234

# Invoking the method using **dct
# demo_method_for_kwargs(**data)

# Invoking the method using key-word arguement
demo_method_for_kwargs(name='testing', id=123)

# def demo_method_for_args(*args):
#     lst_var = args
#     print(lst_var, type(lst_var))
# #
# #
# lst_data = [1, 2, 3, 4]
# # Invoking the method using *list
# demo_method_for_args(*lst_data)
# #
# # # Invoking the method using a series of values as below
# # demo_method_for_args(1, 2, 3, 4)


#####To Note #####
# 1. We cant pass a dictionery as such to a  **kwargs.
# 2. We can pass a key-word arguement list to a **kwargs.
# 3. We can pass a dictionary as **dct for a **kwargs.
