import os
import sys
import importlib
import re

path = os.path.join(os.path.dirname(__file__))
sys.path.extend([path])


class A:
    '''
        This is for class A
    '''

    def __init__(self):
        self.curr_path = os.getcwd() + '\\'
        self.list_of_tup = []

    def get_testcase_files(self, my_dir):
        for dirpath, dirs, files in os.walk(my_dir):
            for filename in files:
                if re.match('tc_\d+.py',filename):
                    filename = os.path.join(dirpath, filename)
                    print(filename)
                    module_name = filename.split(self.curr_path)[-1]
                    print(module_name)
                    module = module_name.split('.')[0]
                    self.dynamic_import(module)


    def dynamic_import(self,fname):
        module = importlib.import_module(fname)
        my_class = getattr(module, 'TestCase')
        instance = my_class()
        (zid, doc, url) = (instance.a, instance.__doc__, instance.b)
        doc = doc.strip()
        self.list_of_tup.append((zid, doc, url))


if __name__ == '__main__':
    obj = A()
    my_dir = os.getcwd()
    print(my_dir)
    obj.get_testcase_files(my_dir)

    print(obj.list_of_tup)