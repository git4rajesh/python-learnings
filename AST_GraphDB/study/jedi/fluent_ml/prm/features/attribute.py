from string import Template

from automation.core.src import helper as core_helper
from automation.pve.src import constants
from automation.fluent_ml.prm.features.artifact import Artifact


class Attribute(Artifact):
    def __init__(self):
        super().__init__()
        template = Template(constants.ATTRIBUTES_WSDL)
        self.soap_wsdl = template.substitute(protocol=self.env.pve.protocol, pve_env=self.env.pve.name)

    def set(self, lst_payload):
        soap_attr_action, soap_payload = self.payload_gen.get_soap_details('attributes', 'set_attributes', lst_payload)
        self.soap = self.initialize_soap_request(self.cert, soap_payload, soap_attr_action)
        response = self.request.post(self.soap_wsdl, self.soap.body, self.soap.header, encoding='utf-8')

        self.verify_set(response, lst_payload)

    def read(self, entity_key, attribute_id):
        dict_attr_values = {'string': attribute_id, 'EntityKey': entity_key}
        soap_attr_action, soap_payload = self.payload_gen.get_soap_details('attributes', 'read', dict_attr_values)
        self.soap = self.initialize_soap_request(self.cert, soap_payload, soap_attr_action)
        response = self.request.post(self.soap_wsdl, self.soap.body, self.soap.header, encoding='utf-8')

        attrib_value = self.parse_wrapper.get_values(response.text, node='d:Value')[0]
        return attrib_value

    def verify_set(self, response, lst_expected):
        self.step_desc = 'Verify Set Attribute'
        self.step_input = 'Expected values: %s' % lst_expected
        self.remarks = '\n Inside feature class: %s method: %s \n' % (core_helper.get_method_class_names())

        err_msg = self.parse_wrapper.get_values(response.text, node='b:ErrorMessage')[0]
        general_err_msg = self.parse_wrapper.get_values(response.text, node='a:GeneralErrorMessage')[0]

        lst_status = [True]

        if err_msg or general_err_msg or response.status_code != 200:
            error_message = str(err_msg) + str(general_err_msg)
            self.remarks += 'Set Attribute failed with error: %s' % {'error_message': error_message,
                                                                     'response': response.text}
            lst_status.append(False)
        else:
            for dct_payload in lst_expected:
                project_key = dct_payload['EntityKey']
                attr_id = dct_payload['Id']
                exp_attr_value = str(dct_payload['Value'])
                actual_attr_value = str(self.read(project_key, attr_id))

                status, verify_remarks = self.asserter.verify(actual_attr_value, expected=exp_attr_value,
                                                              condition='is_equal_to')

                self.remarks += verify_remarks
                lst_status.append(status)
        self.status = all(lst_status)

        self.db_logger.log_into_steps(self)
        assert self.status
