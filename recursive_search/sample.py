import os


def find_recursively(p, text, level):
    for item in os.listdir(p):
        if os.path.isdir(os.path.join(p, item)):
            newlevel = level + "--"
            print(newlevel + item + "(d)")
            newpath = os.path.join(p, item)
            find_recursively(newpath, text, newlevel)
        elif os.path.isfile(os.path.join(p, item)):
            flag = 0
            newlevel = level + "--"
            newpath = os.path.join(p, item)
            file = open(newpath, "r")
            for line in file.readlines():
                if text in line:
                    flag = 1
                    break
            if (flag == 1):
                print(newpath + ": String found!")
                file.seek(0)
                for line in file.readlines():
                    if text in line:
                        print(newpath)

            file.close()


path = input("Please enter the directory to recursively search in: ")
search_str = input("Please enter the string to look for in the file contents: ")

find_recursively(path, search_str, "")