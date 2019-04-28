from string import Template

from automation.core.src import helper as core_helper
from automation.core.datastore.tinydb_datastore import DataStore
from automation.pve.src import constants
from automation.fluent_ml.src import helper
from automation.fluent_ml.prm.features.artifact import Artifact


class Project(Artifact):
    tbl_name = 'PRM_Project'

    def __init__(self):
        super().__init__()
        template = Template(constants.PROJECT_WSDL)
        self.soap_wsdl = template.substitute(protocol=self.env.pve.protocol, pve_env=self.env.pve.name)

    def create(self, payload):
        soap_create_action, soap_payload = self.payload_gen.get_soap_details('project', 'create', payload)
        soap = self.initialize_soap_request(self.cert, soap_payload, soap_create_action)
        response = self.request.post(self.soap_wsdl, soap.body, soap.header, encoding='utf-8')

        project_key = self.verify_create_update(response, dct_expected=payload)
        name = payload.get('Description')

        DataStore.insert(Project.tbl_name, id=project_key, name=name, scope=self.scope, test_id=self.id,
                         dct_expected=payload)
        print("*****PRM_PROJECT TABLE*****\n", DataStore.read_all('PRM_Project'))
        return project_key

    def update(self, payload):
        soap_update_action, soap_payload = self.payload_gen.get_soap_details('project', 'update',
                                                                             payload)
        soap = self.initialize_soap_request(self.cert, soap_payload, soap_update_action)
        response = self.request.post(self.soap_wsdl, soap.body, soap.header, encoding='utf-8')

        project_key = self.verify_create_update(response, dct_expected=payload)
        DataStore.update(Project.tbl_name, payload, id=project_key)

        print("*****PRM_PROJECT TABLE*****\n", DataStore.read_all('PRM_Project'))
        return response

    def delete(self, project_key):
        dct_del_prj_values = {'string': project_key}

        soap_del_action, soap_payload = self.payload_gen.get_soap_details('project', 'delete', dct_del_prj_values)
        soap = self.initialize_soap_request(self.cert, soap_payload, soap_del_action)

        self.request.post(self.soap_wsdl, soap.body, soap.header, encoding='utf-8')
        self.verify_delete(project_key)

        DataStore.delete(Project.tbl_name, id=project_key)
        print("*****PRM_PROJECT TABLE*****\n", DataStore.read_all('PRM_Project'))

    def read(self, project_key):
        dict_read_prj_values = {'string': project_key}

        soap_read_action, soap_payload = self.payload_gen.get_soap_details('project', 'read', dict_read_prj_values)
        soap = self.initialize_soap_request(self.cert, soap_payload, soap_read_action)

        response = self.request.post(self.soap_wsdl, soap.body, soap.header, encoding='utf-8')
        return response

    def verify_create_update(self, response, dct_expected):
        self.step_desc = 'Verify Project Create/Update'
        self.step_input = 'Expected values: %s' % dct_expected
        self.remarks = '\n Inside feature class: %s method: %s \n' % (core_helper.get_invoking_method_name())

        project_key = None
        err_msg = self.parse_wrapper.get_values(response.text, node='b:ErrorMessage')[0]
        general_err_msg = self.parse_wrapper.get_values(response.text, node='a:GeneralErrorMessage')[0]

        if err_msg or general_err_msg or response.status_code != 200:
            error_message = str(err_msg) + str(general_err_msg)
            self.remarks += 'Project creation/updation failed with error: %s' % {'error_message': error_message,
                                                                        'response': response.text}
            self.status = False
        else:
            project_key = self.parse_wrapper.get_values(response.text)[0]
            read_resp = self.read(project_key)

            dct_actual = self.construct_pve_dct_actual(read_resp, dct_expected)

            self.status, verify_remarks = self.asserter.verify(dct_actual, expected=dct_expected)
            self.remarks += verify_remarks

        self.db_logger.log_into_steps(self)
        assert self.status, self.remarks

        return project_key

    def verify_delete(self, project_key):
        self.status = False
        self.step_desc = 'Verify Project Delete'
        self.step_input = 'Input value: %s' % project_key
        self.remarks = '\n Inside feature class: %s method: %s \n' % (core_helper.get_invoking_method_name())

        read_resp = self.read(project_key)
        status_code = read_resp.status_code
        if status_code == 200:
            project_scode = helper.get_scode(project_key)
            expected_msg = 'Unable to find project: {}'.format(project_scode)

            actual_msg = self.parse_wrapper.get_values(read_resp.text, node='b:ErrorMessage')[0]

            self.status, remarks = self.asserter.verify(actual_msg, expected=expected_msg,
                                                        condition='is_equal_to_ignoring_case')
            self.remarks += remarks
        else:
            self.remarks += 'Project Read API failed with status code: {0} and response: {1}'.format(status_code,
                                                                                                     read_resp.text)

        self.db_logger.log_into_steps(self)
        assert self.status, self.remarks
