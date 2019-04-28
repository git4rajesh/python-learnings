def method1(dct_data2, **data1):

    print(type(dct_data2), type(data1))

    # dct_complete1 = {**data1, **dct_data2}
    # print('Expanding kwargs>>>', dct_complete1)

    dct_data2.update(data1)
    print('Updating the dict', dct_data2)



dct_data2 = {'a':1, 'b':2}

method1(dct_data2, name='Test', id =123)