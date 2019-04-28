def print_hello():
    print('Hello')


def print_hi():
    print('Hi')


def print_bye():
    print('Bye')


def make_template():
    [func() for func in (print_hello, print_hi, print_bye)]


make_template()
