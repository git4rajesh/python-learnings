def outer_print_msg():
    status = True

    def inner_print_msg():
        nonlocal status
        # status = False
        if status:
            print('Status value: {}'.format(status))
    return inner_print_msg

output = outer_print_msg()
output()
