from lxml.builder import ElementMaker
from lxml import etree

E1 = ElementMaker(namespace="http://schemas.xmlsoap.org/soap/envelope/",
                nsmap={'soapenv': "http://schemas.xmlsoap.org/soap/envelope/"})

E2 = ElementMaker(namespace="http://schemas.planview.com/PlanviewEnterprise/Services/TaskService3/2012/08",
                nsmap={'ns': "http://schemas.planview.com/PlanviewEnterprise/Services/TaskService3/2012/08"})

E3 = ElementMaker(namespace="http://schemas.planview.com/PlanviewEnterprise/OpenSuite/Dtos/TaskDto2/2012/08",
                 nsmap={'ns1': "http://schemas.planview.com/PlanviewEnterprise/OpenSuite/Dtos/TaskDto2/2012/08"})


class XML_Generator:
    def __init__(self):
        self.ENVELOPE = E1.Envelope
        self.HEADER = E1.Header
        self.BODY = E1.Body
        self.UPDATE = E2.Update
        self.DTOS = E2.dtos
        self.TASK = E3.TaskDto2

    def construct_struct(self, tup_funcs):
            self.root = self.ENVELOPE(
                self.HEADER,
                self.BODY(
                    self.UPDATE(
                        self.DTOS(
                            self.TASK(
                                    *tup_funcs
                            )
                        )
                    )
                )
            )

    def generate_xml_file(self, file_name):
        etree_out = (etree.tostring(self.root, pretty_print=True))
        with open(file_name, 'ab') as fileHandle:
            fileHandle.write(etree_out)

    def construct_tuple_funcs(self, dict_func):
        lst_func = []
        for key in dict_func:
            func = dict_func[key][0]
            val = dict_func[key][1]
            lst_func.append(func(val))
        return tuple(lst_func)

if __name__ == '__main__':
    xml_gen = XML_Generator()
    dict_func={}
    dict_func['E3.Description'] = (E3.Description, 'My Desc')
    dict_func['E3.Duration'] = (E3.Duration,'10')

    tup_funcs = xml_gen.construct_tuple_funcs(dict_func)
    xml_gen.construct_struct(tup_funcs)

    xml_gen.generate_xml_file('Out_demo5.xml')
