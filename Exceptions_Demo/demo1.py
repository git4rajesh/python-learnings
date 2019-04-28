def func1():
    print('Inside func1')
    try:
        func2()
    except:
        print('Caught in main func1')
    print('After func call')

def func2():
    print('Inside func2')
    a = 3/0
    print('Inside except block')

    # finally:
    #     print('Inside finally')


func1()