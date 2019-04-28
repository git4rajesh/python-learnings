from lxml import etree


root = etree.Element("{xmlns:soapenv=http://schemas.xmlsoap.org/soap/envelope/}Envelope")

# <soapenv:Header/>
header1 = etree.SubElement(root, "{xmlns:soapenv=http://schemas.xmlsoap.org/soap/envelope/}Header")
body = etree.SubElement(root, "{xmlns:soapenv=http://schemas.xmlsoap.org/soap/envelope/}Body")
child1 = etree.SubElement(body, "Update")
child2 = etree.SubElement(child1, "dtos")
child3 = etree.SubElement(child2, "TaskDto2")
child4 = etree.SubElement(child3, "Description")
child4.text = 'My Desc'

print(etree.tostring(root, pretty_print=True))

# root.insert(0, etree.Element("child0"))
#
# children = list(root)
#
# for child in children:
#     print(child.tag)

