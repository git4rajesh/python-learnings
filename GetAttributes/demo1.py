from importlib import import_module

module_path = 'GetAttributes.my_module'

template_module = import_module(module_path)

print(getattr(template_module, 'var1'))