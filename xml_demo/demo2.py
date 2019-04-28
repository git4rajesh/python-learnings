from lxml import etree

SOAP_NAMESPACE = "http://schemas.xmlsoap.org/soap/envelope/"
SOAP = "{%s}" % SOAP_NAMESPACE

TASK_NAMESPACE = "http://schemas.planview.com/PlanviewEnterprise/Services/TaskService3/2012/08"
TASK = "{%s}" % TASK_NAMESPACE

PAYLOAD_NAMESPACE = "http://schemas.planview.com/PlanviewEnterprise/OpenSuite/Dtos/TaskDto2/2012/08"
PAYLOAD = "{%s}" % PAYLOAD_NAMESPACE

NSMAP_SOAP = {"soapenv": SOAP_NAMESPACE}
NSMAP_TASK = {"ns": TASK_NAMESPACE}
NSMAP_PAYLOAD = {"ns1": PAYLOAD_NAMESPACE}

envelope = etree.Element(SOAP + "Envelope", nsmap=NSMAP_SOAP)
header = etree.SubElement(envelope, SOAP + "Header", nsmap=NSMAP_SOAP)
body = etree.SubElement(envelope, SOAP + "Body", nsmap=NSMAP_SOAP)

payload_node1 = etree.SubElement(body, TASK + "Update", nsmap=NSMAP_TASK)
payload_node2 = etree.SubElement(payload_node1, TASK + "dtos", nsmap=NSMAP_TASK)
payload_node3 = etree.SubElement(payload_node2, PAYLOAD + "TaskDto2", nsmap=NSMAP_PAYLOAD)



payload_node = etree.SubElement(payload_node3, PAYLOAD + "Description", nsmap=NSMAP_PAYLOAD)
payload_node.text = " This is my Description"

payload_node = etree.SubElement(payload_node3, PAYLOAD + "Duration", nsmap=NSMAP_PAYLOAD)
payload_node.text = "10"


print(etree.tostring(envelope, pretty_print=True))

my_output = etree.tostring(envelope, pretty_print=True)

file_handle = open("output.xml",'wb')
file_handle.write(my_output)
file_handle.close()
