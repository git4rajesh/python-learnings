from lxml.builder import ElementMaker
from lxml import etree
from collections import OrderedDict

E1 = ElementMaker(namespace="http://schemas.xmlsoap.org/soap/envelope/",
                nsmap={'soapenv': "http://schemas.xmlsoap.org/soap/envelope/"})

E2 = ElementMaker(namespace="http://schemas.planview.com/PlanviewEnterprise/Services/TaskService3/2012/08",
                nsmap={'ns': "http://schemas.planview.com/PlanviewEnterprise/Services/TaskService3/2012/08"})

E3 = ElementMaker(namespace="http://schemas.planview.com/PlanviewEnterprise/OpenSuite/Dtos/TaskDto2/2012/08",
                 nsmap={'ns1': "http://schemas.planview.com/PlanviewEnterprise/OpenSuite/Dtos/TaskDto2/2012/08"})

E4 = ElementMaker(namespace="http://schemas.microsoft.com/2003/10/Serialization/Arrays",
                  nsmap={'arr': "http://schemas.microsoft.com/2003/10/Serialization/Arrays"})


class Task_XML_Generator:
    def __init__(self):
        self.ENVELOPE = E1.Envelope
        self.HEADER = E1.Header
        self.BODY = E1.Body
        self.CREATE = E2.Create
        self.UPDATE = E2.Update
        self.READ = E2.Read
        self.DELETE = E2.Delete
        self.DTOS = E2.dtos
        self.TASK = E3.TaskDto2
        self.KEYS = E2.keys
        self.ARR = E4.arr

        self.dict_crud = {'create': self.CREATE, 'update': self.UPDATE, 'read': self.READ, 'delete': self.DELETE}

    def create_update(self, tup_funcs, operation):
            self.OPERATION = self.dict_crud[operation]

            root = self.ENVELOPE(
                self.HEADER,
                self.BODY(
                    self.OPERATION(
                        self.DTOS(
                            self.TASK(
                                    *tup_funcs
                            )
                        )
                    )
                )
            )
            return etree.tostring(root, pretty_print=True)

    def read_delete(self, tup_funcs, operation):
        self.OPERATION = self.dict_crud[operation]

        root = self.ENVELOPE(
            self.HEADER,
            self.BODY(
                self.OPERATION(
                    self.KEYS(
                            self.ARR(
                                *tup_funcs
                            )

                    )
                )
            )
        )
        return etree.tostring(root, pretty_print=True)

    @staticmethod
    def generate_xml_file(payload, file_name):
        with open(file_name, 'wb') as fileHandle:
            fileHandle.write(payload)

    @staticmethod
    def construct_tuple_funcs(dict_func):
        lst_func = []
        for key in dict_func:
            func = dict_func[key][0]
            val = dict_func[key][1]
            lst_func.append(func(val))
        return tuple(lst_func)


if __name__ == '__main__':
    xml_gen = Task_XML_Generator()
    dict_func = OrderedDict()
    dict_func['E3.Description'] = (E3.Description, 'My Desc')
    dict_func['E3.Duration'] = (E3.Duration,'10')

    tup_funcs = xml_gen.construct_tuple_funcs(dict_func)
    payload = xml_gen.create_update(tup_funcs, 'create')

    xml_gen.generate_xml_file(payload, 'Out_demo5.xml')
