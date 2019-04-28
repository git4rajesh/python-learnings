import pytest

from core.fluent import Fluent
from core.src.custom_annotations import zid, tags


@zid('atom-1')
@pytest.mark.parametrize('field_mapping', ['same', 'similar', 'manual'])
def test_import_without_default_fields(request, field_mapping):
    """
    Validation of data import for project creation from excel sheet having all fields a specific value
    :param request: request object of pytest
    :param field_mapping: field_mapping from the paramterization which specifies the setting of field mapping required for this test
    :return:
    """
    Fluent(request) \
        .data_import().create_for_entity('project') \
        .where_field_mapping_is(field_mapping) \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=3) \
        .import_file().verify()


@zid('atom-2')
@pytest.mark.parametrize('field_mapping', ['same', 'similar', 'manual'])
def test_import_with_default_fields(request, field_mapping):
    """
    Validation of dataimport for project creation from excel sheet having all fields a specific value except Status and Category fields.
    Status and Category should be taken from the default value which has been set prior to the import
    :param request: request object of pytest
    :param field_mapping: field_mapping from the paramterization which specifies the setting of field mapping required for this test
    :return:
    """
    Fluent(request) \
        .data_import().create_for_entity('project') \
        .with_default_status('PROPOSED').with_default_category('CATEGORY1').where_field_mapping_is(field_mapping) \
        .remove_column('PROJECT STATUS').remove_column('PROJECT CATEGORY') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=6) \
        .import_file().verify()


@zid('atom-3')
@pytest.mark.parametrize('field_mapping', ['same', 'similar', 'manual'])
def test_import_update_without_default_fields(request, field_mapping):
    """
    Validation of data import for project updation from excel sheet having all fields a specific value
    :param request: request object of pytest
    :param field_mapping: field_mapping from the paramterization which specifies the setting of field mapping required for this test
    :return:
    """
    Fluent(request).project('Project-1')
    Fluent(request).project('Project-2')
    Fluent(request).project('Project-3')

    Fluent(request) \
        .data_import().update_for_entity('project') \
        .consider_entities(['Project-1', 'Project-2', 'Project-3']) \
        .where_field_mapping_is(field_mapping) \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@zid('atom-4')
@pytest.mark.parametrize('field_mapping', ['same', 'similar', 'manual'])
def test_import_update_with_default_fields(request, field_mapping):
    """
    Validation of dataimport for project updation from excel sheet having all fields a specific value except Status and Category fields.
    Status and Category should be taken from the default value which has been set prior to the import
    :param request: request object of pytest
    :param field_mapping: field_mapping from the paramterization which specifies the setting of field mapping required for this test
    :return:
    """
    Fluent(request).project('Project-1')
    Fluent(request).project('Project-2')
    Fluent(request).project('Project-3')

    Fluent(request) \
        .data_import().update_for_entity('project') \
        .consider_entities(['Project-1', 'Project-2', 'Project-3']) \
        .with_default_status('PROPOSED').with_default_category('CATEGORY1').where_field_mapping_is(field_mapping) \
        .remove_column('PROJECT STATUS').remove_column('PROJECT CATEGORY') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()
