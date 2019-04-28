import traceback
from jinja2 import Template, Environment, FileSystemLoader
from automation.integration.pve.src import constants
from automation.integration.pve.src.xml_parse_wrapper import XmlParseWrapper
from automation.core.logger import handler as logger


class PayloadGen:

    def __init__(self):
        self.operation = None
        self.artifact = None
        self.parse_wrapper = XmlParseWrapper()

    def get_action(self, artifact, operation):
        self.artifact = artifact
        self.operation = operation
        return constants.ARTIFACT_MAP[artifact][operation]['url']

    def get_template(self):
        payload_path = constants.ARTIFACT_MAP[self.artifact][self.operation]['payload']
        return self.parse_wrapper.read_template(payload_path)

    def get_payload(self, list_dict_values):
        template = self.get_template()
        return self.parse_wrapper.set_values(template, list_dict_values)

    def get_soap_details(self, artifact, operation, list_dict_values):
        soap_action = self.get_action(artifact, operation)
        soap_payload = self.get_payload(list_dict_values)
        return soap_action, soap_payload


    def get_soap_details_v1(self, artifact, operation, list_dict_values):
        soap_action = self.get_action(artifact, operation)
        soap_payload = self.get_jinja_payload(list_dict_values)
        return soap_action, soap_payload

    def get_jinja_payload(self, dict_nodes):
        payload_path = constants.ARTIFACT_MAP[self.artifact][self.operation]['payload']
        try:
            self.template_env = Environment(
                                        autoescape=False,
                                        loader=FileSystemLoader(payload_path),
                                        trim_blocks=False)
            template = self.template_env.get_template('').render(dict_nodes=dict_nodes)
            return template
        except:
            logger.logs('Exception occurred in preparing SOAP payload in get_payload() method', 'error')
            logger.logs('Exception Trace: \n %s', traceback.print_exc())


