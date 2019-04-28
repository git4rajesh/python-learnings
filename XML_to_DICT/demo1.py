import xmltodict
import pprint
import json

my_xml = """
    <audience>
      <id what="attribute">123</id>
      <name>Shubham</name>
    </audience>
"""

my_dct = xmltodict.parse(my_xml)

print(my_dct)

print(my_dct['audience']['id']['#text'])