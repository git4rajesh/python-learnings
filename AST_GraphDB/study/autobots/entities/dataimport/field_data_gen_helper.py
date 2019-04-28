from datetime import datetime
from random import randint, uniform, choice

from core import utils
from collections import OrderedDict
from entities.dataimport import helper


class DataGen:

    def __init__(self):
        self.turn_on_special_character = False

    @staticmethod
    def _dynamic_generation_of_val(method, field, default_values, user_specified_value):
        # TODO : Once all methods are implemented, have to decide the presence of 'field' parameter
        if user_specified_value:
            field_value = method(field, user_specified_value)
        # TODO: __date has to be removed once api specific issue is resolved where subtypeid is 1
        elif default_values and method.__name__ != '_date':
            field_value = DataGen._dynamic_generate_list(method, field, default_values[:])
        else:
            field_value = method(field)
        return field_value

    @staticmethod
    def _dynamic_generate_list(method, field, default_values):
        field_value, index = method(field, default_values)
        if (field_value == 'TeamUser, Automation') or (field_value == 'TEUser, QA') or (field_value!= None and 'QA_01' in field_value):
            default_values.pop(index)
            if default_values:
                field_value = DataGen._dynamic_generate_list(method, field, default_values)
            else:
                field_value = None
        return field_value

    @staticmethod
    def _construct_expected_dct(field, field_data_type, field_value, default_values, display_option):
        lst_fields_accepts_integer = ['PROJECT % COMPLETE METHOD *', 'PROJECT ALLOCATION UNITS',
                                      'PROJECT CONFIDENTIAL PROJECT', 'PROJECT NEW TASKS']
        if field == 'PORTFOLIO CATEGORY ID *' or field == 'PORTFOLIO CATEGORY ID':
            if field_value == 'Port':
                field_value = 'Port - ' + field_value
            else:
                field_value = 'Portfolio - ' + field_value
        elif field_value is None:
            field_value = ''
        elif field_data_type == 'date':
            date_time = datetime.strptime(field_value, '%m/%d/%Y')
            field_value = date_time.strftime('%Y-%m-%dT00:00:00.000')
        elif field_data_type == 'float':
            # PPMPRO has float rounding to 3 decimal places
            field_value = round(field_value, 3)
        elif field_data_type == 'number' and display_option == 'Percent':
            field_value = field_value / 100
        elif field_data_type == 'boolean' and display_option == 'Yes/No':
            dct_bool_yes_no = {True: 'Yes', False: 'No'}
            field_value = dct_bool_yes_no[field_value]
        elif field in lst_fields_accepts_integer:
            for default_value in default_values:
                if default_value['value'] == field_value:
                    field_value = default_value['displayText']
                    break
        if isinstance(field_value, str):
            field_value = utils.html_encode(field_value)
        return field_value

    def _get_method(self, field_data_type):
        lst_char = [' ', '/', '-', '(', ')']
        for char in lst_char:
            if char in field_data_type:
                field_data_type = field_data_type.replace(char, '_')
        method_name = '_' + field_data_type
        method = getattr(self, method_name)
        return method

    def _integer(self, field):
        """
        Generating a random integer in between 0 to 100 (both inclusive)
        """
        integer_value = randint(0, 1000)
        return integer_value

    def _float(self, field):
        """
        Generating a random float in between 0.0 to 100.0 (both inclusive)
        """
        float_value = uniform(0.0, 100.0)
        return float_value

    def _string(self, field, user_specified_value=None):
        """
        Generating a random string with a prefix 'Auto_DataImport'.
        Random string will be framed from the pool of ascii letters, digits, punctuations and white space
        """

        if field == '{} TITLE *'.format(self.entity.upper()) or field == '{} TITLE'.format(self.entity.upper()):
            str_value = utils.get_title_randomint('DataImport')
        elif user_specified_value:
            str_value = user_specified_value
        else:
            str_value = helper.get_random_string(self.turn_on_special_character)

        return str_value

    def _number(self, field):
        """
        Generating a random number in between 0 to 100 (both inclusive)
        """
        num_val = randint(0, 100)
        return num_val

    def _boolean(self, field):
        """
        Generating a random boolean value
        """
        bool_value = choice([True, False])
        return bool_value

    def _list(self, field, default_values):
        """
        Generating dynamic list values for autocomplete fields for example "ALTERNATE PM TIMESHEET APPROVER: LAST,FIRST"
        :param field: field name
        :param default_values: list of default values for the corresponding field
        :return: dynamic value from the default values
        """
        if isinstance(default_values, str):
            return default_values
        index = randint(0, len(default_values) - 1)
        lst_val = default_values[index]['displayText']
        return lst_val, index

    def _date(self, *args):
        """
        Generating today's date with the format MM/DD/YYYY
        """
        date_value = datetime.today().strftime('%m/%d/%Y')
        return date_value

    def _money(self, field):
        """
        Generating random money value in a range of 0.0 to 100.0 (both inclusive) with a decimal precision of one
        """
        money_value = round(uniform(0.0, 100.0), 2)
        return money_value

    def _percent(self, field):
        """
        Generating random percent value in a range of 0.0 to 100.0 (both inclusive) with a decimal precision of one
        """
        percent_value = round(uniform(0.0, 100.0), 2)
        return percent_value

    def _radio(self, field):
        """
        Generating the toggling values of radio randomly between 1 and 10 (inclusive). PPM PRO allows radio buttons in this range.
        """
        radio_value = randint(1, 10)
        radio_value = "".join(['Radio ', str(radio_value)])
        return radio_value

    def _checkbox(self, field):
        """
        Generating the toggling values of checkbox randomly - either 0 or 1
        """
        checkbox_value = randint(0, 1)
        return checkbox_value

    def _text(self, field, user_specified_value=None):
        """
        Generating random 3 separate lines from the pool of ascii letters, digits, punctuations and white space
        3 lines generated separately will be joined with a new-line break '\n'
        """
        if user_specified_value:
            str_value = user_specified_value
        else:
            random_first_line_str = helper.get_random_string(self.turn_on_special_character)
            random_second_line_str = helper.get_random_string(self.turn_on_special_character)
            random_third_line_str = helper.get_random_string(self.turn_on_special_character)
            str_value = '\n'.join([random_first_line_str, random_second_line_str, random_third_line_str])
        return str_value

    def _text_box(self, field, user_specified_value=None):
        """
        Generating random 3 separate lines from the pool of ascii letters, digits, punctuations and white space
        3 lines generated separately will be joined with a new-line break '\n'
        """
        if user_specified_value:
            str_value = user_specified_value
        else:
            random_first_line_str = helper.get_random_string(self.turn_on_special_character)
            random_second_line_str = helper.get_random_string(self.turn_on_special_character)
            random_third_line_str = helper.get_random_string(self.turn_on_special_character)
            str_value = '\n'.join([random_first_line_str, random_second_line_str, random_third_line_str])
        return str_value

    def _udf_pulldown_field(self, field):
        return 'Pulldown1'

    def _autocomplete(self, field, default_values):
        """
        Generating dynamic list values for autocomplete fields for example "ALTERNATE PM TIMESHEET APPROVER: LAST,FIRST"
        :param field: field name
        :param default_values: list of default values for the corresponding field
        :return: dynamic value from the default values
        """
        if isinstance(default_values, str):
            return default_values
        index = randint(0, len(default_values) - 1)
        autocomplete_value = default_values[index]['displayText']
        return autocomplete_value, index

    def _ll_status_list(self, field, default_values):
        """
        Generating dynamic list values for ll status list fields for example "PROJECT STATUS *"
        :param field: field name
        :param default_values: list of default values for the corresponding field
        :return: dynamic value from the default values
        """
        if isinstance(default_values, str):
            return default_values
        index = randint(0, len(default_values) - 1)
        status_value = default_values[index]['displayText']
        return status_value, index

    def _ll_lookup_list(self, field, default_values):
        """
        Generating dynamic list values for ll lookup list fields for example "PROJECT PHASE"
        :param field: field name
        :param default_values: list of default values for the corresponding field
        :return: dynamic value from the default values
        """
        if isinstance(default_values, str):
            return default_values
        index = randint(0, len(default_values) - 1)
        status_value = default_values[index]['displayText']
        return status_value, index

    def _picklist(self, field, default_values):
        """
        Generating dynamic list values for pick list fields for example "PROJECT OWNER: LAST, FIRST *"
        :param field: field name
        :param default_values: list of default values for the corresponding field
        :return: dynamic value from the default values
        """
        if isinstance(default_values, str):
            return default_values
        index = randint(0, len(default_values) - 1)
        pick_value = default_values[index]['displayText']
        return pick_value, index

    def _select_list(self, field, default_values):
        """
        Generating dynamic list values for select list fields for example "PROJECT CATEGORY *"
        :param field: field name
        :param default_values: list of default values for the corresponding field
        :return: dynamic value from the default values
        """

        if isinstance(default_values, str):
            return default_values
        index = randint(0, len(default_values) - 1)
        select_value = default_values[index]['displayText']

        if 'PROJECT CATEGORY' in field:
            select_value = 'Project'
        elif field == 'PORTFOLIO PARENT PORTFOLIO TITLE':
            select_value = None
        return select_value, index

    def _multi_select(self, field, default_values):
        """
        Generating dynamic list values for multi select fields
        :param field: field name
        :param default_values: list of default values for the corresponding field
        :return: dynamic value from the default values
        """
        if isinstance(default_values, str):
            return default_values
        index = randint(0, len(default_values) - 1)
        multi_select_value = default_values[index]['displayText']
        return multi_select_value, index

    def _multiselect_list(self, field, default_values):
        """
        Generating dynamic list values for multi select list fields
        :param field: field name
        :param default_values: list of default values for the corresponding field
        :return: dynamic value from the default values
        """
        if isinstance(default_values, str):
            return default_values
        index = randint(0, len(default_values) - 1)
        multi_select_value = default_values[index]['displayText']
        return multi_select_value, index

    def _multi_select__checkbox_value_field_(self, field, default_values):
        """
        Generating dynamic list values for multi select checkbox value fields
        :param field: field name
        :param default_values: list of default values for the corresponding field
        :return: dynamic value from the default values
        """
        if isinstance(default_values, str):
            return default_values
        index = randint(0, len(default_values) - 1)
        multi_select_value = default_values[index]['displayText']
        return multi_select_value, index

    def _multi_select__checkbox_default_field_(self, field, default_values):
        """
        Generating dynamic list values for multi select checkbox default fields
        :param field: field name
        :param default_values: list of default values for the corresponding field
        :return: dynamic value from the default values
        """
        if isinstance(default_values, str):
            return default_values
        index = randint(0, len(default_values) - 1)
        multi_select_value = default_values[index]['displayText']
        return multi_select_value, index

    def _multi_select_lookup_status_list(self, field, default_values):
        """
        Generating dynamic list values for multi select lookup status list fields
        :param field: field name
        :param default_values: list of default values for the corresponding field
        :return: dynamic value from the default values
        """
        if isinstance(default_values, str):
            return default_values
        index = randint(0, len(default_values) - 1)
        multi_select_value = default_values[index]['displayText']
        return multi_select_value, index

    def _multi_select_lookup_status_list__checkbox_(self, field, default_values):
        """
        Generating dynamic list values for multi select lookup status list checkboc fields
        :param field: field name
        :param default_values: list of default values for the corresponding field
        :return: dynamic value from the default values
        """
        if isinstance(default_values, str):
            return default_values
        index = randint(0, len(default_values) - 1)
        multi_select_value = default_values[index]['displayText']
        return multi_select_value, index

    def _java_defined_pic_list(self, field, default_values):
        """
        Generating dynamic list values for java defined pic list fields
        :param field: field name
        :param default_values: list of default values for the corresponding field
        :return: dynamic value from the default values
        """
        if isinstance(default_values, str):
            return default_values
        index = randint(0, len(default_values) - 1)
        java_value = default_values[index]['displayText']
        return java_value, index

    def _java_defined_select_list(self, field, default_values):
        """
        Generating dynamic list values for java defined select list fields
        :param field: field name
        :param default_values: list of default values for the corresponding field
        :return: dynamic value from the default values
        """
        if isinstance(default_values, str):
            return default_values
        lst_fields_accepts_integer = ['PROJECT % COMPLETE METHOD *', 'PROJECT ALLOCATION UNITS',
                                      'PROJECT CONFIDENTIAL PROJECT', 'PROJECT NEW TASKS',
                                      'PROJECT PROJECTPLACE INTEGRATION']
        index = randint(0, len(default_values) - 1)
        if field in lst_fields_accepts_integer:
            # TODO: Once confidential project issue with 'Yes' for update solves, this can be uncommented
            # java_value = default_values[index]['value']
            java_value = default_values[0]['value']
        else:
            java_value = default_values[index]['displayText']
        return java_value, index

    def _multi_select__checkbox_display_field_(self, field, default_values):
        """
        Generating dynamic list values for multi select checkbox display fields
        :param field: field name
        :param default_values: list of default values for the corresponding field
        :return: dynamic value from the default values
        """
        if isinstance(default_values, str):
            return default_values
        index = randint(0, len(default_values) - 1)
        multi_select_value = default_values[index]['displayText']
        return multi_select_value, index

    def generate(self, entity, fields_with_types, set_values_dct, default_values_dct=None):
        """
        Constructs the rows and expected dictionary as per the given field type and its list of default values if exists
        :param fields_with_types: the dictionary will be in below format
            {"PROJECT CATEGORY *": { "field_title": "Category",
                                    "default_values":[{"displayText": "category_api", "value": "1614107066"},
                                                      {"displayText": "Project", "value": "1320597422"}
                                                    ],
                                    "fieldType": "Select List"
                                    }
            }
        """
        self.entity = entity
        row_dct = OrderedDict()
        expected_dct = OrderedDict()

        if set_values_dct:
            set_values_dct = helper.lower_keys(set_values_dct)

        elif default_values_dct:
            default_values_dct = helper.lower_keys(default_values_dct)
            expected_dct.update(default_values_dct)

        for field in fields_with_types:
            is_set_values_dct_used = False
            user_specified_value = None
            field_details = fields_with_types[field]
            field_data_type = (field_details.get('fieldType')).lower()
            default_values = field_details.get('default_values', [])
            field_title = field_details.get('field_title')
            display_option = field_details.get('display_option', None)
            method = self._get_method(field_data_type)
            if field_data_type in set_values_dct.keys():
                user_specified_value = set_values_dct[field_data_type]
                is_set_values_dct_used = True
            if field_title.lower() in set_values_dct.keys():
                user_specified_value = set_values_dct[field_title.lower()]
                is_set_values_dct_used = True

            row_field_value = self._dynamic_generation_of_val(method, field, default_values, user_specified_value)
            row_dct.update({field: row_field_value})
            if (not set_values_dct) or (set_values_dct and is_set_values_dct_used) or field == '{} TITLE *'.format(
                    self.entity.upper()) or field == '{} TITLE'.format(self.entity.upper()) or (
                    self.entity.upper() == 'PORTFOLIO' and 'portfolio category id' in field.lower()) or (
                    self.entity.upper() == 'ASSET' and 'asset asset category' in field.lower()):
                expected_field_value = self._construct_expected_dct(field, field_data_type, row_field_value,
                                                                    default_values,
                                                                    display_option)
                expected_dct.update({field_title.lower(): expected_field_value})

        return row_dct, expected_dct
