import json
import traceback
import pandas

from collections import OrderedDict
from core import utils
from core.asserter import Asserter
from core.db import db_wrapper
from entities.asset.asset import Asset
from entities.dataimport import helper
from autobots.entities.dataimport.base import Base
from entities.dataimport.field_data_gen_helper import DataGen
from entities.portfolio.portfolio import Portfolio
from entities.project.project import Project
from entities.issue.issue import Issue

ENTITY = 'dataimport'


class Dataimport(Base):

    def __init__(self, request):
        super().__init__(request)
        self.filename = None
        self.entity = None
        self.asserter = Asserter()
        self.lst_expected_dct = []
        self.set_values_dct = OrderedDict()
        self.ignore_fields = []
        self.category = None
        self.status = None
        self.field_mapping = None
        self.mandatory_fields = False
        self.standard_fields_flag = True
        self.udf_fields_flag = True
        self.is_update = False
        self.update_entities_lst = []
        self.data_gen = DataGen()

    def generate_import_file(self, entity):

        self.filename = super().export_file(entity, self.is_update)
        self.template_columns_dataframe, self.fields_lst = self._get_available_fields(entity)
        data = {'file_name': self.filename, 'excel_columns': self.template_columns_dataframe,
                'fields_lst': self.fields_lst}
        self.db_store.insert(self.scope, self.test_id, ENTITY, data)
        return self

    def create_for_entity(self, entity):
        self.is_update = False
        self.entity = entity.lower()
        return self

    def update_for_entity(self, entity):
        self.is_update = True
        self.entity = entity.lower()
        return self

    def consider_entities(self, entities_lst):
        if not self.entity:
            raise NameError('Entity value is required')
        entity = self.entity
        for entity_title in entities_lst:
            entity_dict = self.db_store.search_by_key(entity, 'title', entity_title)[0]
            self.update_entities_lst.append(entity_dict['id'])
        return self

    def include_only_mandatory_fields(self):
        self.standard_fields_flag, self.udf_fields_flag, self.mandatory_fields = False, False, True
        return self

    def include_only_standard_fields(self):
        self.standard_fields_flag, self.udf_fields_flag = True, False
        return self

    def include_only_udf_fields(self):
        self.standard_fields_flag, self.udf_fields_flag = False, True
        return self

    def include_both_standard_and_udf_fields(self):
        self.standard_fields_flag, self.udf_fields_flag = True, True
        return self

    def with_default_category(self, category):
        entity = self.entity.upper()
        self.category = self.constants[entity]['CATEGORIES'][category]
        return self

    def with_default_status(self, status):
        entity = self.entity.upper()
        self.status = self.constants[entity]['STATUS'][status]
        return self

    def where_field_mapping_is(self, mapping):
        field_mapping = ['same', 'similar', 'manual']
        self.field_mapping = field_mapping.index(mapping.lower()) + 1
        return self

    def set_fields(self, specified_values_dct):
        self.set_values_dct.update(specified_values_dct)
        return self

    def turn_on_special_characters(self):
        self.data_gen.turn_on_special_character = True
        return self

    def import_file(self):
        entity = self.entity.upper()
        standard_fields = {'category': self.category['ID'] if self.category else None,
                           'status': self.status['ID'] if self.status else None,
                           'ptid': self.constants[ENTITY.upper()][entity.upper()],
                           'fieldMapping': self.field_mapping if self.field_mapping else '1'}
        super().import_file_in_system(self.entity, standard_fields, self.is_update)

        return self

    def delete(self, entity_details):
        super().delete(entity_id=entity_details['file_name'])

    def _get_available_fields(self, entity):
        template_columns_dataframe = pandas.read_excel(self.filename)
        fields_lst = super().read_all_available_fields(entity)
        return template_columns_dataframe, fields_lst

    def _get_entity_fields_and_columns(self):
        self.filename = '{}.xlsx'.format(self.entity)
        entity_data_dct = self.db_store.search_by_key(ENTITY, 'file_name',
                                                      self.filename)
        if not entity_data_dct:
            if self.entity:
                self.generate_import_file(self.entity)
                entity_data_dct = self.db_store.search_by_key(ENTITY, 'file_name', self.filename)
            else:
                raise Exception(
                    'Entity parameter has to be provided to identify the file name')

        fields_lst = entity_data_dct[0]['fields_lst']
        template_columns_dataframe = entity_data_dct[0]['excel_columns']
        lst_template_columns = list(template_columns_dataframe)
        return fields_lst, lst_template_columns

    def populate_dynamic_data_to_excel_file(self, no_of_rows=1):
        fields_lst, lst_template_columns = self._get_entity_fields_and_columns()

        fields_with_types = super().filter_available_fields(self.entity,
                                                            fields_lst,
                                                            lst_template_columns,
                                                            self.standard_fields_flag,
                                                            self.udf_fields_flag,
                                                            self.mandatory_fields,
                                                            self.ignore_fields)

        default_values_dct = OrderedDict()
        default_values_dct.update({'CATEGORY': self.category['DISPLAYTEXT'] if self.category else None,
                                   'STATUS': self.status['DISPLAYTEXT'] if self.status else None})
        if self.is_update:
            self.generate_data_for_update_entity(fields_with_types, default_values_dct)
        else:
            self.generate_data_for_create_entity(fields_with_types, default_values_dct, no_of_rows)
        return self

    def generate_data_for_update_entity(self, fields_with_types, default_values_dct):
        lst_row_dct = []
        for entity_id in self.update_entities_lst:
            row_dct, expected_dct = self.data_gen.generate(self.entity, fields_with_types, self.set_values_dct,
                                                           default_values_dct)
            if 'PROJECT % COMPLETE METHOD' in row_dct.keys():
                del row_dct['PROJECT % COMPLETE METHOD']
            if '% complete method' in expected_dct.keys():
                del expected_dct['% complete method']
            if 'PROJECT PROJECTPLACE SYNC NOW' in row_dct.keys():
                del row_dct['PROJECT PROJECTPLACE SYNC NOW']
            if 'projectplace sync now' in expected_dct.keys():
                del expected_dct['projectplace sync now']
            if 'PROJECT DEFAULT TASK CATEGORY TITLE' in row_dct.keys():
                del row_dct['PROJECT DEFAULT TASK CATEGORY TITLE']
            if 'default task category' in expected_dct.keys():
                del expected_dct['default task category']

            row_dct.update({'ID': entity_id})
            lst_row_dct.append(row_dct)
            self.lst_expected_dct.append(expected_dct)
        super().update(lst_row_dct)
        return self

    def generate_data_for_create_entity(self, fields_with_types, default_values_dct, no_of_rows=1):
        lst_row_dct = []
        for row_no in range(0, no_of_rows):
            row_dct, expected_dct = self.data_gen.generate(self.entity, fields_with_types, self.set_values_dct,
                                                           default_values_dct)
            default_values_dct.update({'CATEGORY': self.category[
                'DISPLAYTEXT'] if self.category else None,
                                       'STATUS': self.status[
                                           'DISPLAYTEXT'] if self.status else None})
            lst_row_dct.append(row_dct)
            self.lst_expected_dct.append(expected_dct)
        super().update(lst_row_dct)
        return self

    def remove_column(self, column_name):
        self.ignore_fields.append(column_name.upper())
        return self

    def _verify_project(self, expected_dct):
        """
        Verification of single project creation via data-import using new-project-template.
        1) Read details, additional-details and settings of projects and combine them to form actual_dct
        2) Verify the expected_dct with actual_dct
        """
        self.status = True
        self.step_desc = 'Data Import of Project verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        self.step_input = '\n Expected Dictionary\n{}'.format(json.dumps(expected_dct))
        project = Project(self.request)

        # Read details of project based on title. In UI, these details can be seen under 'Details' of project
        read_response = project.read_title(expected_dct['title'])
        act_project_details = helper.get_formatted_dct(read_response.json())
        project.project_id = read_response.json()['id']

        # Read additional details of project. In UI, these additional details can be seen under 'Executive Summary' of project
        read_response = project.read_more(project.project_id)
        act_project_details_more = helper.get_formatted_dct(
            read_response.json())

        # Read settings of project. In UI, these additional details can be seen under 'Settings' of project
        read_response = project.read_settings(project.project_id)
        act_project_details_settings = helper.get_formatted_dct(read_response.json())

        # Combine all the details to form the actual_dct
        actual_dct = OrderedDict()
        actual_dct.update({act_project_details, act_project_details_more,
                           act_project_details_settings})
        self.step_input += '\n Actual Dictionary\n{}'.format(json.dumps(actual_dct))

        expected_dct = helper.lower_keys(expected_dct)
        actual_dct = helper.lower_keys(actual_dct)
        # ignore_keys = helper.get_ignore_keys(expected_dct, actual_dct)

        try:
            self.status, remark = self.asserter.verify(actual_dct, expected_dct)
            self.remarks += remark
        except KeyError:
            self.status = False
            self.remarks += 'KeyError Exception occurred, please see stack trace below: \n %s' \
                            % traceback.format_exc()
        finally:
            db_wrapper.log_into_steps(self.request, self)
        return

    def _verify_portfolio(self, expected_dct):
        """
        Verification of portfolio creation via data-import using new-portfolio-template.
        1) Read details, finance of portfolio and combine them to form actual_dct
        2) Verify the expected_dct with actual_dct
        """
        self.status = True
        self.step_desc = 'Data Import of Portfolio verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        self.step_input = '\n Expected Dictionary\n{}'.format(json.dumps(expected_dct))
        portfolio = Portfolio(self.request)

        read_category_resp = portfolio.read_category()
        category = expected_dct['category'].replace('Portfolio - ', '')
        category = category.replace('Port - ', '')
        class_id = utils.filter_dct_for_key('title',
                                            category, 'classId.value', read_category_resp.json())[0]

        read_title_resp = portfolio.read_title(expected_dct['title'], class_id)
        act_portfolio_details = helper.get_formatted_dct(read_title_resp.json())
        portfolio.portfolio_id = read_title_resp.json()['id']

        read_finance_resp = portfolio.read_finance(
            {'entity_id': portfolio.portfolio_id})
        act_portfolio_details_finance = helper.get_formatted_dct(
            read_finance_resp.json())

        # Combine all the details to form the actual_dct
        actual_dct = OrderedDict()
        actual_dct.update(
            {act_portfolio_details, act_portfolio_details_finance})
        self.step_input += '\n Actual Dictionary\n{}'.format(json.dumps(actual_dct))

        expected_dct = helper.lower_keys(expected_dct)
        actual_dct = helper.lower_keys(actual_dct)
        ignore_keys = ['parent portfolio']

        try:
            self.status, remark = self.asserter.verify(actual_dct, expected_dct, ignore_keys)
            self.remarks += remark
        except KeyError:
            self.status = False
            self.remarks += 'KeyError Exception occurred, please see stack trace below: \n %s' \
                            % traceback.format_exc()
        finally:
            db_wrapper.log_into_steps(self.request, self)
        return

    def _verify_issue(self, expected_dct):
        """
        Verification of single issue creation via data-import using new-issue-template.
        1) Read details, additional-details and settings of projects and combine them to form actual_dct
        2) Verify the expected_dct with actual_dct
        """
        self.status = True
        self.step_desc = 'Data Import of Issue verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        self.step_input = '\n Expected Dictionary\n{}'.format(json.dumps(expected_dct))
        issue = Issue(self.request)

        read_response = issue.read_title(expected_dct['title'])
        actual_dct = helper.get_formatted_dct(read_response.json())
        self.step_input += '\n Actual Dictionary\n{}'.format(json.dumps(actual_dct))
        issue.issue_id = read_response.json()['id']

        expected_dct = helper.lower_keys(expected_dct)
        actual_dct = helper.lower_keys(actual_dct)
        # TODO: Removal of this ignore_keys
        ignore_keys = ['udf issu multi-select list']

        try:
            self.status, remark = self.asserter.verify(actual_dct, expected_dct, ignore_keys)
            self.remarks += remark
        except KeyError:
            self.status = False
            self.remarks += 'KeyError Exception occurred, please see stack trace below: \n %s' \
                            % traceback.format_exc()
        finally:
            db_wrapper.log_into_steps(self.request, self)
        return

    def _verify_asset(self, expected_dct):
        """
        Verification of single issue creation via data-import using new-asset-template.
        1) Read details, additional-details and settings of projects and combine them to form actual_dct
        2) Verify the expected_dct with actual_dct
        """
        self.status = True
        self.step_desc = 'Data Import of Asset verification'
        self.remarks = '\n Inside class: %s method: %s \n' % utils.get_method_class_names()
        self.step_input = '\n Expected Dictionary\n{}'.format(json.dumps(expected_dct))
        asset = Asset(self.request)

        read_category_resp = asset.read_category()
        class_id = utils.filter_dct_for_key('title',
                                            expected_dct['asset category'], 'classId.value',
                                            read_category_resp.json())[0]

        read_response = asset.read_title(expected_dct['title'], class_id)
        actual_dct = helper.get_formatted_dct(read_response.json())
        self.step_input += '\n Actual Dictionary\n{}'.format(json.dumps(actual_dct))
        asset.asset_id = read_response.json()['id']

        expected_dct = helper.lower_keys(expected_dct)
        actual_dct = helper.lower_keys(actual_dct)

        try:
            self.status, remark = self.asserter.verify(actual_dct, expected_dct)
            self.remarks += remark
        except KeyError:
            self.status = False
            self.remarks += 'KeyError Exception occurred, please see stack trace below: \n %s' \
                            % traceback.format_exc()
        finally:
            db_wrapper.log_into_steps(self.request, self)
        return

    def verify(self):
        """
        Calls verification of single project by passing each project's expected_dct
        """
        status_lst = []
        remarks_lst = []
        expected_dct_lst = self.lst_expected_dct
        if not expected_dct_lst:
            assert False
        for expected_dct in expected_dct_lst:
            method = '_verify_{}'.format(self.entity)
            func = getattr(self, method)
            func(expected_dct)
            status_lst.append(self.status)
            remarks_lst.append(self.remarks)
        assert all(status_lst), remarks_lst
        return self
