from string import Template

from automation.core.src.assert_comparisons import AssertCompare
from automation.core.src.environment import Environment
from automation.core.logger import handler as logger
from automation.integration.pve.src import constants
from automation.integration.pve.src.xml_parse_wrapper import XmlParseWrapper
from automation.integration.pve.src.payload_generator import PayloadGen
from automation.integration.src.test_case_helper import TestCaseHelper
from automation.integration.src.artifact import Artifact
from automation.integration.src.request import Request


class Task(Artifact):
    def __init__(self):
        super(Task, self).__init__()
        env = Environment()
        template = Template(constants.TASK_WSDL)
        self.soap_wsdl = template.substitute(protocol=env.pve.protocol, pve_env=env.pve.name)

        self.request = Request()
        self.parse_wrapper = XmlParseWrapper()
        self.payload_gen = PayloadGen()
        self.verify_created_key, self.verify_description, self.verify_father_key = '', '', ''
        self.verify_update_key, self.verify_deleted_key, self.verify_schedule_start, self.verify_enter_progress, self.remarks = '', '', '', '', ''
        # self.lst_date_keys = ['ns1:ActualFinishDate', 'ns1:ActualStartDate', 'ns1:ScheduleStartDate', 'ns1:ScheduleFinishDate' ]
        self.lst_date_keys = ['ActualFinishDate', 'ActualStartDate', 'ScheduleStartDate','ScheduleFinishDate']
        self.verify_dct = {}

    def create_old(self, list_of_dict, encoding='utf-8'):
        soap_create_action, soap_payload = self.payload_gen.get_soap_details('task', 'create', list_of_dict)
        soap = self.request.initialize_soap_request(self.cert, soap_payload, soap_create_action)
        response = self.request.post(self.soap_wsdl, soap.body, soap.header, encoding)

        self.verify_created_key = self.parse_wrapper.get_values(response.text)[0]
        self.verify_description = list_of_dict[0]['ns1:Description']
        self.verify_father_key = list_of_dict[0]['ns1:FatherKey']

        logger.logs('Created Task with Name as: %(description)s and Key as %(key)s'
                    % {'description': self.verify_description, 'key': self.verify_created_key}, 'info')
        return response

    def create(self, list_of_dict, encoding='utf-8'):
        soap_create_action, soap_payload = self.payload_gen.get_soap_details_v1('task', 'create', list_of_dict)
        soap = self.request.initialize_soap_request(self.cert, soap_payload, soap_create_action)
        response = self.request.post(self.soap_wsdl, soap.body, soap.header, encoding)
        self.verify_created_key = self.parse_wrapper.get_values(response.text)[0]
        self.verify_description = list_of_dict['Description']
        self.verify_father_key = list_of_dict['FatherKey']

        logger.logs('Created Task with Name as: %(description)s and Key as %(key)s'
                    % {'description': self.verify_description, 'key': self.verify_created_key}, 'info')
        return response

    def read(self, task_key, encoding='utf-8'):
        list_dict_node_values = {'string': task_key}
        soap_read_action, soap_payload = self.payload_gen.get_soap_details_v1('task', 'read', list_dict_node_values)
        soap = self.request.initialize_soap_request(self.cert, soap_payload, soap_read_action)
        response = self.request.post(self.soap_wsdl, soap.body, soap.header, encoding)
        return response

    def update_old(self, list_of_dict, operation='update' , encoding='utf-8'):
        soap_update_action, soap_payload = self.payload_gen.get_soap_details('task', operation, list_of_dict)
        soap = self.request.initialize_soap_request(self.cert, soap_payload, soap_update_action)
        response = self.request.post(self.soap_wsdl, soap.body, soap.header, encoding)
        self.verify_update_key = list_of_dict[0]['ns1:Key']
        self.snap_shot_dct = list_of_dict[0]
        return response

    def update(self, list_of_dict, operation='update' , encoding='utf-8'):
        soap_update_action, soap_payload = self.payload_gen.get_soap_details_v1('task', operation, list_of_dict)
        soap = self.request.initialize_soap_request(self.cert, soap_payload, soap_update_action)
        response = self.request.post(self.soap_wsdl, soap.body, soap.header, encoding)
        self.verify_update_key = list_of_dict['Key']
        self.snap_shot_dct = list_of_dict
        return response

    def delete(self, list_of_dict, encoding='utf-8'):
        soap_delete_action, soap_payload = self.payload_gen.get_soap_details('task', 'delete',
                                                                             list_of_dict)
        soap = self.request.initialize_soap_request(self.cert, soap_payload, soap_delete_action)
        response = self.request.post(self.soap_wsdl, soap.body, soap.header, encoding)

        self.verify_deleted_key = list_of_dict[0]['arr:string']

        logger.logs('Deleted Task with Name as: %(description)s and Key as %(key)s' % {
            'description': self.verify_description,
            'key': self.verify_deleted_key}, 'info')

        return response

    def verify_create(self, encoding='utf-8'):
        status = True
        self.remarks = 'Verification:\n'
        try:
            if self.verify_created_key:
                resp = self.read(self.verify_created_key, encoding)
                description = self.parse_wrapper.get_values(resp.text, node='d:Description')[0]
                father_key = self.parse_wrapper.get_values(resp.text, node='d:FatherKey')[0]
                verify_dct = {'verify_description': description, 'verify_father_key': father_key}
                snap_shot_dct = self.__dict__

                for key in verify_dct:
                    if type(snap_shot_dct[key]) is int:
                        snap_shot_dct[key] = (str(snap_shot_dct[key])).replace(" ", "")

                    if AssertCompare.is_string_equal(verify_dct[key], snap_shot_dct[key]):
                        self.remarks += '%s assertion passed\n' % key
                    else:
                        self.remarks += '%s assertion failed Expected: %s Actual: %s\n' % (key, snap_shot_dct[key], verify_dct[key])
                        status = False


        except:
            logger.logs('Execution failed in Class: Task inside Method: verify_create()', 'error')
            self.remarks += 'Task not created due to exception in Class: Task inside Method: verify_create() \n'
            status = False
        finally:
            return status, self.remarks

    def verify_update(self, encoding='utf-8'):
        status = True
        lst_status = []
        self.remarks = 'Verification:\n'
        try:
            self.construct_verify_dict(encoding)
            for key in self.snap_shot_dct:
               if key in self.lst_date_keys:
                    status = self.compare_date_keys(key)
               else:
                    status = self.compare_string_keys(key)
               lst_status.append(status)
            status = all(lst_status)
        except:
            logger.logs('Execution failed in Class: Task inside Method: verify_update()', 'error')
            self.remarks += 'Task not updated due to exception in Class: Task inside Method: verify_update() \n'
            status = False
        finally:
            return status, self.remarks

    def verify_delete(self, encoding='utf-8'):
        status = False
        try:
            if self.verify_deleted_key:
                delete_response = self.read(self.verify_deleted_key, encoding)
                error_msg = self.parse_wrapper.get_values(delete_response.text, node='b:ErrorMessage')[0]
                expected_msg = 'Unable to find task:'

                if AssertCompare.is_substring_present(expected_msg, error_msg):
                    status = True
                    self.remarks += '%s task deleted successfully\n' % self.verify_deleted_key
                else:
                    self.remarks += '%s task not deleted successfully\n' % self.verify_deleted_key
        except:
            logger.logs('Execution failed in Class: Task inside Method: verify_delete()', 'error')
            self.remarks += 'Task not deleted due to exception in Class: Task inside Method: verify_delete() \n'
            status = False
        finally:
            return status, self.remarks

    def construct_verify_dict(self, encoding):
        if self.verify_update_key:
            resp = self.read(self.verify_update_key, encoding)
            for key in self.snap_shot_dct:
                node_value = 'd:' + key
                value = self.parse_wrapper.get_values(resp.text, node=node_value)[0]
                self.verify_dct[key] = value

    def compare_string_keys(self, key):
        lst_status = []
        if AssertCompare.is_string_equal(str(self.verify_dct[key]), str(self.snap_shot_dct[key])):
            self.remarks += '%s assertion passed\n' % key
            lst_status.append(True)
        else:
            self.remarks += '%s assertion failed Expected: %s Actual: %s\n' % (key, self.snap_shot_dct[key], self.verify_dct[key])
            lst_status.append(False)
        return all(lst_status)

    def compare_date_keys(self, key):
        actual_date = TestCaseHelper.string_to_date(self.verify_dct[key])
        expected_date = TestCaseHelper.string_to_date(self.snap_shot_dct[key])
        lst_status = []
        if AssertCompare.is_date_compare_pp(actual_date, expected_date):
            self.remarks += '%s assertion passed\n' % key
            lst_status.append(True)
        else:
            lst_status.append(False)
            self.remarks += '%s assertion failed Expected: %s Actual: %s\n' % (key, self.snap_shot_dct[key], self.verify_dct[key])
        return all(lst_status)