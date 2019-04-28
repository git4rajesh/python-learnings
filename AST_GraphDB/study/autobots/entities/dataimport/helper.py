import string
from collections import OrderedDict
from random import choice


def get_formatted_dct(json_resp):
    """
    Create a new dictionary with keys from 'fields' part of json response and values from 'data' part of json response.
    Keys in the 'data' part of json will be field internal names which has to be replaced with corresponding header/displaytext.
    We are using 'fields' dict part of json to get the header/displaytext of the same field
    :param json_resp: json response consisting of 'fields' dict  and 'data' dict
    :return: new dictionary with displayed field names as keys and values
    """
    formatted_dct = OrderedDict()
    fields_lst_dict = json_resp['fields']
    data_dict = json_resp['data'][0]
    for key, value in data_dict.items():
        for field_dict in fields_lst_dict:
            if field_dict.get('name') == key:
                actual_key = field_dict.get('header')
                # To align with expected dict, if value of data_dict is a dict then populate the value of actual_dct with the displayText(i.e, field-value)
                if isinstance(value, dict):
                    formatted_dct[actual_key] = value['displayText']
                else:
                    formatted_dct[actual_key] = value
                break
    return formatted_dct


def lower_keys(dictionary):
    """
    This function serves the purpose of lowering the keys of passed dictionary, values will be untouched
    :param dictionary: dictionary on which keys have to be lowered
    :return: new dictionary with lowered keys
    """
    new_dictionary = OrderedDict()
    new_dictionary.update({key.lower(): value for key, value in dictionary.items()})
    return new_dictionary


def perform_manualmapping(entity, create_excel_field_mapping_resp, is_update):
    """
    This function holds the business logic for data import, when field mapping of excel to application fields are set as 'Manually map fields'.
    Logic follows like this :
    1) 'combodata' part of json response will be having the parsed excel columns(displayText) and mapped_id(value).
    2) 'data' part of json response will be having the entity-fields and excel-column mapping details.
        While, values of excel-column mapping details will be absent as mapping has yet to be done.
    3) Outer Loop will
        a) loop through the excel columns extracted from Step-1('combodata'). This will be a list of excel-column-dict
        b) column_name will have a prefix with sheet name. So formatting is done to extract only column name
    4) Inner Loop will
        a) loop through the entity-field & excel-column mappings from Step-2('data'). This will be a list of dicts
        b) formatted column-name and excel-field name will be matched to identify the eligible column for mapping.
            Once matching excel-column is found out, then assign  column name and mappedId into the entity-field mapping dict
        b) After assigning, break that inner loop and resume the outer loop with next item
    :param create_excel_field_mapping_resp: json response containing 'combodata' and 'data' dictionary
    :return: updated json response which has entity-field & excel-column mappings in the 'data' dict part.
    """
    excel_columns = create_excel_field_mapping_resp['combodata']
    entity_field_mappings = create_excel_field_mapping_resp['data']
    for excel_column in excel_columns:
        column_name = excel_column['displayText']
        mapped_id = excel_column['value']

        index = column_name.index(']')
        index = index + 1
        column_name_formatted = column_name[++index:]
        column_name_formatted = column_name_formatted.strip().rstrip('*').rstrip()

        for entity_field_mapping in entity_field_mappings:
            entity_field_name = entity_field_mapping['fieldName']
            import re
            reg_to_remove = re.compile(r'<.*?/>')
            entity_field_name = reg_to_remove.sub('', entity_field_name).rstrip()
            # This condition is for dataimport updation.Excel column will have 'ID' and mapping field name will be '<entityname> ID'
            if is_update and column_name_formatted.lower() == 'id':
                column_name_formatted = '{} id'.format(entity)
            if entity_field_mapping.get('excelField') and column_name_formatted.lower() == entity_field_name.lower():
                entity_field_mapping['mappedId'] = mapped_id
                entity_field_mapping['excelField'] = column_name
                break

    return create_excel_field_mapping_resp


def get_random_string(include_special_character=False):
    string_choices = string.ascii_letters + string.digits + ' '
    if include_special_character:
        string_choices = string_choices + string.punctuation
    random_str = ''.join([choice(string_choices) for n in range(10)])

    # TODO: Once issue is resolved, remove replacement
    # random_str = random_str.replace('<', '')
    # random_str = random_str.replace('{', '')
    # Removing white space and '=' sign. = sign at the starting misguides excel as a formula, so removing.
    random_str = random_str.strip().lstrip('=')
    return random_str


# def get_ignore_keys(expected_dct, actual_dct):
#     """
#     This is a temporary function, once invalid keys in the excel sheet and problematic keys are resolved, this function will be removed
#     """
#     expected_set = set(expected_dct.keys())
#     actual_set = set(actual_dct.keys())
#     # TODO: Has to remove this once UI and available field alignment is clarified
#     ignore_keys = list(expected_set - actual_set)
#     # ignore_keys = []
#     # TODO: Has to remove once these problematic fields are resolved
#     temp_ignore_keys = ['udf pexs multiselect list', 'udf multi select lookup/status list (checkbox) 51',
#                         'udf multi-lookup', 'udf pexs picklist', 'udf resource picklist', 'sponsor', 'can be template',
#                         'udf multi-lookup', 'conversion for tasks-hours per week', 'objective',
#                         'resource planning mode', 'conversion for tasks-hours per day', 'udf radio',
#                         'udf pexs radiobutton', 'udf pexs float', 'udf pexs multiselect list']
#     ignore_keys.extend(temp_ignore_keys)
#     return ignore_keys
