from DynamicClassLoader.classloader_util import DynamicClassLoader


class Client:
    def __init__(self, module_name, class_name):
        self.module_name = module_name
        self.class_name = class_name

    def demo_method(self):
        instance = DynamicClassLoader.get_module_instance(module_name=self.module_name,
                                                         class_name=self.class_name)
        instance.run()


if __name__ == '__main__':
    obj = Client(module_name='black_jack', class_name='DummyClass')
    obj.demo_method()
