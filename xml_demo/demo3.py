from lxml.builder import ElementMaker
from lxml import etree

E1 = ElementMaker(namespace="http://schemas.xmlsoap.org/soap/envelope/",
                nsmap={'soapenv': "http://schemas.xmlsoap.org/soap/envelope/"})

E2 = ElementMaker(namespace="http://schemas.planview.com/PlanviewEnterprise/Services/TaskService3/2012/08",
                nsmap={'ns': "http://schemas.planview.com/PlanviewEnterprise/Services/TaskService3/2012/08"})

E3 = ElementMaker(namespace="http://schemas.planview.com/PlanviewEnterprise/OpenSuite/Dtos/TaskDto2/2012/08",
                 nsmap={'ns1': "http://schemas.planview.com/PlanviewEnterprise/OpenSuite/Dtos/TaskDto2/2012/08"})

ENVELOPE = E1.Envelope
HEADER = E1.Header
BODY = E1.Body
UPDATE = E2.Update
DTOS = E2.dtos
TASK = E3.TaskDto2
DESCRIPTION = E3.Description
DURATION = E3.Duration

root = ENVELOPE(
    HEADER,
    BODY(
        UPDATE(
                DTOS(
                     TASK(
                         DESCRIPTION('My Description'),
                         DURATION('10')
                     )
                    )
        )
     )
)

etree_out = (etree.tostring(root, pretty_print=True))

file_handle = open("etree_out.xml",'wb')
file_handle.write(etree_out)
file_handle.close()