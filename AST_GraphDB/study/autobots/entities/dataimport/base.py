import gzip
import json
from collections import OrderedDict

import requests
import pandas

from core import utils
from core.db import db_wrapper
from core.src import userpool
from entities.dataimport import helper

ENTITY = 'dataimport'


class Base:
    def __init__(self, request):
        self.request = request
        self.scope = request.scope
        self.test_id = request.config.option.test_id
        self.jsessionid = userpool.get_usertoken_of_current_user(request)
        self.session = requests.session()
        self.urls = request.getfixturevalue('read_urls')
        self.constants = request.config.option.constants
        self.cmd_options = request.getfixturevalue('set_cmdline_opts')
        self.db_store = request.getfixturevalue('tiny_db_store')

    def _create_excel_field_mapping(self, entity, file_name, standard_fields,
                                    is_update):
        """
        This method will hit the excel field mapping url and gives the response
        :param file_name: file_name which needs to be imported
        :return:
        """
        data = open(file_name, 'rb')
        file = {'importFile': data}
        payload = {'functionType': 'create' if not is_update else 'update',
                   'hasHeader': True,
                   'fieldMapping': standard_fields['fieldMapping'],
                   'department': None,
                   'status': standard_fields['status'],
                   'category': standard_fields['category']}
        api = self.urls[ENTITY]['excel_field_mapping']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'],
            ptid=self.constants[ENTITY.upper()][entity.upper()])

        response = self.session.post(url=url,
                                     cookies={'JSESSIONID': self.jsessionid},
                                     files=file, data=payload)
        return response.json()

    def _get_map_and_field_id(self, combodata, val):
        for cdata in combodata:
            if val.lower() in cdata['displayText'].lower():
                return cdata['displayText'], cdata['value']

    def _read_default_values_for_list(self, field_type_id, field_sub_type_id):
        """
        This method is used to get the default values for available fields which has list as its field type
        :param field_type_id: field type id of the available field <int>
        :param field_sub_type_id: field sub type id of the available field <int>
        :return:
        """
        api = self.urls[ENTITY]['default_values']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'],
            field_type_id=field_type_id,
            field_sub_type_id=field_sub_type_id)

        response = self.session.get(url=url,
                                    cookies={'JSESSIONID': self.jsessionid})
        display_values = response.json()['data']
        return display_values

    def _datatype_mapping_for_available_fields(self, entity, fields_lst,
                                               lst_template_columns,
                                               standard_fields_flag,
                                               udf_fields_flag,
                                               mandatory_flag,
                                               ignore_fields=None):
        """
        This method to generate available fields dictionary in below format
        { <field_name>: 'fieldtype' <mandatory>: <string/list/multiselectlist/integer>
                        'default_values' <optional>: will be populated only if the field is of "list" fieldtype <list of values>
        }

        :param entity: for which entity you have to update the xls
        :param fields_lst: list of available fields
        :param lst_template_columns: headers of the xls
        :return: return available fields in below format
                { <field_name>: 'fieldtype' <mandatory>: <string/list/multiselectlist/integer>
                                'default_values' <optional>: will be populated only if the field is of "list" fieldtype <list of values>,
                                'field_title': title of the field
        }
        """
        # There are few field names which are different from xls to available field names,
        # so we have considered only mandatory above mentioned special fields
        different_names_lst = ['PORTFOLIO CATEGORY', 'ISSUE CATEGORY']
        available_fields = OrderedDict()
        ignore_fields = [name.upper() for name in ignore_fields]
        for field_dct in fields_lst:
            for header in lst_template_columns:
                field_name = '{} {}'.format(entity, field_dct['title']['value'])
                field_name = field_name.upper()
                header_tmp = header.rstrip('*').rstrip()
                if field_name == 'PORTFOLIO PARENT PORTFOLIO':
                    field_name = 'PORTFOLIO PARENT PORTFOLIO TITLE'
                if field_name not in ignore_fields and (field_name == header_tmp
                                                        or ((
                                                                    field_name in different_names_lst)
                                                            and (
                                                                    field_name in header))):

                    if standard_fields_flag and udf_fields_flag:
                        self._append_all_fields(available_fields, field_dct,
                                                header)
                    elif standard_fields_flag:
                        self._append_standard_fields(available_fields,
                                                     field_dct, header)
                    elif udf_fields_flag:
                        self._append_udf_fields(available_fields, field_dct,
                                                header)
                    elif mandatory_flag:
                        self._append_mandatory_fields(available_fields,
                                                      field_dct, header)
                    break
        return available_fields

    def _append_standard_fields(self, available_fields, field_dct, header):
        if field_dct['fieldOrigin']['value'] == 'STANDARD':
            self._prepare_available_fields_dct(available_fields, field_dct,
                                               header)
        return available_fields

    def _append_udf_fields(self, available_fields, field_dct, header):
        if field_dct['fieldOrigin']['value'] == 'USER_DEFINED' or \
                field_dct['isRequired']['value']:
            self._prepare_available_fields_dct(available_fields, field_dct,
                                               header)
        return available_fields

    def _append_mandatory_fields(self, available_fields, field_dct, header):
        if field_dct['isRequired']['value']:
            self._prepare_available_fields_dct(available_fields, field_dct,
                                               header)
        return available_fields

    def _append_all_fields(self, available_fields, field_dct, header):
        self._prepare_available_fields_dct(available_fields, field_dct, header)
        return available_fields

    def _prepare_available_fields_dct(self, available_fields, field_dct,
                                      header):
        available_fields[header] = {
            'fieldType': field_dct['fieldTypeId']['displayText']}
        # If 'fieldSubTypeId' in response then the field will have some default values
        # which we need to append to the dictionary
        if 'fieldSubTypeId' in field_dct.keys():
            field_type_id = field_dct['fieldTypeId']['value']
            field_sub_type_id = field_dct['fieldSubTypeId']['value']
            default_values = self._read_default_values_for_list(field_type_id,
                                                                field_sub_type_id)
            available_fields[header].update({'default_values': default_values})
        if 'displayTypeId' in field_dct.keys():
            available_fields[header].update(
                {'display_option': field_dct['displayTypeId']['displayText']})
        # this key value is needed for generating expected dictionary
        field_title = field_dct['title']['value']
        available_fields[header].update({'field_title': field_title})

    def export_file(self, entity, is_update):
        """
        API call to export the template for the new entity into an xls
        :param filename: file name
        """
        filename = '{}.xlsx'.format(entity)
        api = self.urls[ENTITY]['read']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'],
            ptid=self.constants[ENTITY.upper()][entity.upper()],
            operation='update' if is_update else 'new'
        )

        response = self.session.get(url=url,
                                    cookies={'JSESSIONID': self.jsessionid})
        with open(filename, 'wb') as file:
            file.write(response.content)
        return filename

    def update(self, lst_row_dct):
        """
        update the xlsx with the values generated for all the columns
        :param filename: filename
        :param row_data: row date for all the columns
        :param template_columns_dataframe: pandas data frame object which have template column details
        :return:
        """
        file_name = self.request.config.option.test_id + '.xlsx'
        dataframe = pandas.DataFrame.from_dict(lst_row_dct)
        dataframe.to_excel(file_name, index=False)
        data = {'file_name': file_name, 'excel_columns': dataframe}
        self.db_store.insert(self.scope, self.test_id, ENTITY, data)

    def import_file_in_system(self, entity, standard_fields, is_update):
        """
        This method :
         a) calls the function which calls the api to get the excel field mapping
         b) formulates the payload by 3 step process (inorder to align with the application way of business logic handling)
                i) creates data with necessary details
                ii) converts the data into string
                iii) encodes the string to bytes and then compress it via gzip
            - PPM Pro Application uses 'pako' javascript library to do the above process at the front end
        c) Payload formulated via above step will be posted to the api with necessary headers
        :param filename: file name of the excel file to be imported
        :param standard_fields: dictionary which contains standard fields as keys and its values
        :return: response of the api which consists of import results with success/failure details
        """
        # TODO: Filename has to be intialiazed at one place and inherit in other places rather than initializing the same at different places
        file_name = self.request.config.option.test_id + '.xlsx'
        create_excel_field_mapping_resp = self._create_excel_field_mapping(
            entity, file_name, standard_fields,
            is_update)
        # If the fieldmapping is set to 'Manually map fields' then get the manually mapped dictionary
        if standard_fields['fieldMapping'] == 3:
            create_excel_field_mapping_resp = helper.perform_manualmapping(
                entity,
                create_excel_field_mapping_resp, is_update)
        if standard_fields['fieldMapping'] == 2:
            for mapping in create_excel_field_mapping_resp['data']:
                if mapping['id'] == '11402':
                    if is_update:
                        excel_field, value = self._get_map_and_field_id(
                            create_excel_field_mapping_resp['combodata'],
                            '] PORTFOLIO TITLE')
                    else:
                        excel_field, value = self._get_map_and_field_id(
                            create_excel_field_mapping_resp['combodata'],
                            'PORTFOLIO TITLE *')
                    # excel_field = utils.filter_dct_for_key1('displayText', 'PORTFOLIO TITLE *', 'displayText', create_excel_field_mapping_resp['combodata'])
                    mapping['excelField'] = excel_field
                    mapping['mappedId'] = value
                if mapping['id'] == '435':
                    excel_field, value = self._get_map_and_field_id(
                        create_excel_field_mapping_resp['combodata'],
                        '] ID')
                    mapping['excelField'] = excel_field
                    mapping['mappedId'] = value
                if mapping['id'] in ['114130', '114136']:
                    mapping['mappedId'] = '-1'
                if is_update and mapping['id'] == '11401':
                    excel_field, value = self._get_map_and_field_id(create_excel_field_mapping_resp['combodata'],
                                                                    '] ID')
                    mapping['excelField'] = excel_field
                    mapping['mappedId'] = value

        payload = {'data': create_excel_field_mapping_resp['data'],
                   'importFileId': create_excel_field_mapping_resp[
                       'importFileId'],
                   'functionType': 'create' if not is_update else 'update',
                   'hasHeader': True}
        payload.update(standard_fields)
        payload_str = json.dumps(payload)
        payload_compressed = gzip.compress(payload_str.encode())
        api = self.urls[ENTITY]['import_file']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'])

        response = self.session.post(url=url,
                                     cookies={'JSESSIONID': self.jsessionid},
                                     headers={'Content-Encoding': 'gzip',
                                              'Content-Type': 'application/json',
                                              'Content-Length': str(
                                                  len(payload_compressed))},
                                     data=payload_compressed)
        self.verify_import(response)
        return response

    def read_all_available_fields(self, entity):
        """
        calls the api to get details of available fields for project
        :return: list of field dictionaries which will have details of field type, title, values etc.
        """
        api = self.urls[ENTITY]['available_fields']
        url = api.format(
            protocol=self.constants['SERVER']['PROTOCOL'],
            env=self.cmd_options['env'],
            entity=entity)
        response = self.session.get(url=url,
                                    cookies={'JSESSIONID': self.jsessionid})
        fields_lst = response.json()['data']
        return fields_lst

    def filter_available_fields(self, entity, fields_lst, lst_template_columns,
                                standard_fields_flag, udf_fields_flag, mandatory_flag,
                                ignore_fields=None):
        """
        This method will
        1. call an api to read all the available fields for the given entity
        2. will compare the response with the lst_template_columns input parameter
        3. wil generate the dictionary of available fields with its field type and display values if it is a list field
        :param entity: entity
        :param lst_template_columns: list of columns which exists in the template generated in export_file method
        :return: available fields dictionary in below format
            { <field_name>: 'fieldtype' <mandatory>: <string/list/multi select list/integer>
                            'default_values' <optional>: will be populated only if the field is of "list" fieldtype <list of values>
                            'field_title': title of the field
        }
        """
        # TODO : Optimization has to be checked
        available_fields = self._datatype_mapping_for_available_fields(entity,
                                                                       fields_lst,
                                                                       lst_template_columns,
                                                                       standard_fields_flag,
                                                                       udf_fields_flag,
                                                                       mandatory_flag,
                                                                       ignore_fields)
        return available_fields

    def delete(self, entity_id):
        """
        Deletes the excel file created for the dataimport
        :param entity_id: excel filename
        """
        import os
        os.remove(entity_id)
        self.db_store.delete(ENTITY, 'file_name', entity_id)

        # TODO : Confirm if response success and err msgs have to be parsed and verified

    def verify_import(self, response):
        """
        Verification is done only for the response status code
        :param response: Create response which needs to be verified
        """
        self.status = True
        self.step_desc = 'Innotas  Data Import verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        self.step_input = '\n Response \n{}\n'.format(response.text)

        if response.status_code == 200:
            json_resp = response.json()
            err_count = json_resp.get('errCount')
            if err_count == 'Sheet1 unable to be created  : 0' or err_count == 'Sheet1 unable to be updated  : 0':
                self.remarks += '\nDataImport is executed'
            else:
                self.status = False
                err_msg = json_resp.get('err_msg')
                self.remarks += '\n Import error \n{}'.format(err_msg)

        else:
            self.status = False
            self.remarks += 'Data Import failed \n Response status is not 200 \n Failure response : {}'.format(
                response.text)

        db_wrapper.log_into_steps(self.request, self)

        assert self.status
