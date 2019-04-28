import importlib
import traceback


class DynamicClassLoader:
    @staticmethod
    def get_module_instance(module_name, class_name):
        module = importlib.import_module(module_name)
        instance = None
        try:
            my_class = getattr(module, class_name)
            instance = my_class()
        except AttributeError:
            print(traceback.print_exc())

        return instance
