from Design_Patterns.Structural.Adapter.example2.DictAdapter import DictAdapter
from Design_Patterns.Structural.Adapter.example2.SourceArrayClass import SourceArray

class Client:
    def __init__(self):
        pass

    def run(self):
        source_obj = SourceArray()
        adapter_obj = DictAdapter()
        adapter_obj.show_dict_wrapper(source_obj)

if __name__ == '__main__':
    obj = Client()
    obj.run()