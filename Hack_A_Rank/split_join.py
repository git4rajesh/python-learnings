def split_and_join(line):
    lst_line = line.split()

    s = '-'
    s = s.join(lst_line)
    return s


new_s = split_and_join('This is a string')
print(new_s)