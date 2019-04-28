from lxml import etree

class XML_Valid:

    def is_valid_xml(self, xml_string):
        is_valid = False
        try:
            if xml_string:
                root = self._parse(xml_string)
                is_valid = True
        except etree.XMLSyntaxError:
            pass

        return is_valid

    def initialize_nodes(self, base_file):
        base_file_content = self.file_read(base_file)
        run_file_content = self.file_read(run_file)
        parse_base_xml = XMLParser()



    def file_read(file_name):
        # fa = open(file_name, 'rb')
        with open(file_name, 'rb') as f:
            file_content = f.read()
        return file_content



if __name__ =='__main__':
    xml_obj = XML_Valid()
    xml_obj.initialize_nodes('test.xml')
    xml_obj.is_valid_xml()