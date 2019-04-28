import os
import re

my_dir = 'C:\\Sprint\\longhorn\\automation\\integration\\tests\\time'

lst_files = [file.name for file in os.scandir(my_dir) if re.match('tc_', file.name)]


def my_func(file_name):
    my_file = my_dir + '\\' + file_name

    file_contents = read_file(my_file)

    # pattern = 'SetupWork'
    pattern = 'setup_config'
    search_result = pattern_match(pattern, file_contents)

    if search_result:
        return file_name


def read_file(my_file):
    with open(my_file, encoding='utf-8') as file_handle:
        file_contents = file_handle.read()
        return file_contents


def pattern_match(patten, string):
    return re.search(patten, string)


output_iter = filter(my_func, lst_files)

print(list(output_iter))

# [print(item) for item in list(output_iter) if item]
