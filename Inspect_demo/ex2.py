import pkgutil
import sys


def explore_package(module_name):
    loader = pkgutil.get_loader(module_name)
    for sub_module in pkgutil.walk_packages([loader.filename]):
        _, sub_module_name, _ = sub_module
        qname = module_name + "." + sub_module_name
        print(qname)
        explore_package(qname)


explore_package(sys.argv[1])