from jsonpath_ng.ext import parse
from random import choice
from string import digits, ascii_letters

from automation.core.datastore.tinydb_datastore import DataStore
from automation.core.src.helper import calculate_start_end_dates
from automation.fluent_ml.src.constants import TINYDB_TABLE_MAP

expected_actual_key_map = {'boardId': 'board.id', 'typeId': 'type.id', 'createdBy': 'createdBy.emailAddress',
                           'laneId': 'lane.id', 'isBlocked': 'blockedStatus.isBlocked',
                           'blockReason': 'blockedStatus.reason'
                           }


def get_scode(key):
    return key.split('/')[-1]


def get_start_end_dates(start_delta=0, end_delta=7):
    """
    returns: week days
    """
    date_format = '%Y-%m-%d'
    start_date, end_date = calculate_start_end_dates(start_delta, end_delta)
    str_start_date = start_date.strftime(date_format)
    str_end_date = end_date.strftime(date_format)
    return str_start_date, str_end_date


def get_description_with_numbers(length):
    return ''.join(choice(digits) for i in range(length))


def get_description_with_characters(length):
    return ''.join(choice(ascii_letters) for i in range(length))


def get_description_with_special_characters(length):
    special_characters = ['!', '$', '%', '‘', '(', ')', '*', '.', '+', ',', '-', '/', ':', ';', '=',
                          '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', 'Ç', 'ü', 'é', 'â', 'ä',
                          'ç', 'ê', 'ë', 'è', 'ï', 'î', 'ì', 'Ä', 'É', 'Ô', 'ö', 'ò', 'û', 'ù', 'Ö', 'Ü', '£', 'á', 'í',
                          'ó', 'ú', 'ñ', 'Ñ', '¿', '¬', 'Á', 'Â', 'ã', 'Ã', '¤', 'Ê', 'Ë', 'È', 'Í', 'Î', 'Ï', '¦', 'Ì',
                          'Ó', 'ß', 'Ô', 'Ò', 'õ', 'Õ', 'µ', 'Ú', 'Û', 'Ù', '§', '°','€']
    return ''.join(choice(special_characters) for i in range(length))


def get_prm_start_end_dates(start_delta=0, end_delta=7):
    """
    returns: week days
    """
    startdate_format = '%Y-%m-%dT08:00:00'
    enddate_format = '%Y-%m-%dT17:00:00'
    start_date, end_date = calculate_start_end_dates(start_delta, end_delta)
    str_start_date = start_date.strftime(startdate_format)
    str_end_date = end_date.strftime(enddate_format)
    return str_start_date, str_end_date


def construct_actual(response, dct_expected):
    dct_actual = {}
    for key in dct_expected:
        if key in expected_actual_key_map:
            mapped_key = expected_actual_key_map[key]
        else:
            mapped_key = key

        dct_actual[key] = extract_value(mapped_key, response)

    return dct_actual


def extract_value(json_path, json_resp):
    appended_path = '$..{}'.format(json_path)
    jsonpath_expr = parse(appended_path)
    lst_finds = jsonpath_expr.find(json_resp)
    if lst_finds:
        return lst_finds[0].value


def teardown(scope):
    lst_tables = DataStore.table_names

    for table in reversed(lst_tables):
        artifact = TINYDB_TABLE_MAP[table]
        artifact().teardown(scope)
