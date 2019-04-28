import os

COUNT_OCCURENCE = 0
EXCLUDE_DIRS = ['D:\JavaExamples\DIP']
SEARCH_STRINGS = ['Rectangle', 'Square']


def find_recursively(path, search_str):
    for items in os.listdir(path):
        abs_path = os.path.join(path, items)
        if os.path.isdir(abs_path):
            if abs_path not in EXCLUDE_DIRS:
                find_recursively(abs_path, search_str)
        elif os.path.isfile(abs_path):
            status = search_in_file(abs_path, search_str)
            if status:
                print('{0} file has the pattern: {1}'.format(abs_path, search_str))


def search_in_file(newpath, text):
    status = False
    with open(newpath, "r") as file_handle:
        for line in file_handle.readlines():
            if text in line:
                status = True
                global COUNT_OCCURENCE
                COUNT_OCCURENCE += 1
    return status


path = input("Please enter the directory to recursively search in: ")

for search_str in SEARCH_STRINGS:
    find_recursively(path, search_str)
    print('Total Occurences', COUNT_OCCURENCE)
    print('')
