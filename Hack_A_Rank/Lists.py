if __name__ == '__main__':
    my_lst = []
    n = int(input())

    number_of_commands = 0
    while number_of_commands < n:

        command_params = input().split()
        command = command_params[0]
        if command == 'insert':
            index = int(command_params[1])
            item = int(command_params[2])
            my_lst.insert(index, item)

        if command == 'print':
            print(my_lst)

        if command == 'remove':
            del_elem = int(command_params[1])
            if my_lst.__contains__(del_elem):
                my_lst.remove(del_elem)

        if command == 'append':
            append_elem = int(command_params[1])
            my_lst.append(append_elem)

        if command == 'sort':
            my_lst.sort()

        if command == 'pop':
            my_lst.pop()

        if command == 'reverse':
            my_lst.reverse()

        number_of_commands += 1