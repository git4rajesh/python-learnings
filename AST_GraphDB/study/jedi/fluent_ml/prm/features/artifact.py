from automation.core.utils.asserter import Asserter
from automation.core.src.environment import Environment
from automation.core.src.test_details import TestDetails
from automation.core.db.db_logging.db_factory import DBLoggerFactory
from automation.integration.src.cert import Cert
from automation.integration.src.request import Request
from automation.pve.src.payload_generator import PayloadGen
from automation.pve.src.xml_parse_wrapper import XmlParseWrapper
from automation.pve.soap import Soap_Request


class Artifact:
    def __init__(self):
        self.env = Environment()
        self.cert = Cert().pve_cert

        self.request = Request()
        self.asserter = Asserter()
        self.payload_gen = PayloadGen()
        self.parse_wrapper = XmlParseWrapper()
        self.db_logger = DBLoggerFactory().logger

        self.id = TestDetails.test_id
        self.uuid = TestDetails.test_uuid
        self.scope = TestDetails.scope

    def construct_pve_dct_actual(self, response, dct_expected):
        dct_actual = {}
        for key, expected_value in dct_expected.items():
            node = 'd:{}'.format(key)
            lst_value = self.parse_wrapper.get_values(response.text, node=node)
            actual_value = lst_value[0]
            dct_actual[key] = actual_value
        return dct_actual

    @staticmethod
    def initialize_soap_request(cert, payload, soap_action):
        soap = Soap_Request(soap_action, cert)
        soap.construct_soap_request(payload)
        return soap
