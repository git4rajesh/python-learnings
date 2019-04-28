import pytest

from core.fluent import Fluent
from core.src.custom_annotations import zid, tags


@tags('dataimport')
@zid('563')
def test_import_exact_same_title_standard_fieldmapping(request):
    """
    Validate data import for updation of 5 projects when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have content for all standard fields and mandatory udf fields
    """
    Fluent(request).project('Project-1')
    Fluent(request).project('Project-2')
    Fluent(request).project('Project-3')
    Fluent(request).project('Project-4')
    Fluent(request).project('Project-5')

    Fluent(request). \
        data_import().update_for_entity('PROJECT') \
        .consider_entities(['Project-1', 'Project-2', 'Project-3', 'Project-4', 'Project-5']) \
        .where_field_mapping_is('SAME') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('564')
def test_import_similar_title_standard_fieldmapping(request):
    """
    Validate data import for updation of 5 projects when:
    a) dataimport field mapping is set to similar title based mapping
    b) Default status and category is set
    c) file should have contents for all standard fields and mandatory udf fields
    """
    Fluent(request).project('Project-1')
    Fluent(request).project('Project-2')
    Fluent(request).project('Project-3')
    Fluent(request).project('Project-4')
    Fluent(request).project('Project-5')

    Fluent(request). \
        data_import().update_for_entity('PROJECT') \
        .consider_entities(['Project-1', 'Project-2', 'Project-3', 'Project-4', 'Project-5']) \
        .with_default_status('PROPOSED').with_default_category('CATEGORY1').where_field_mapping_is(
        'SIMILAR') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('565')
def test_import_manual_standard_fieldmapping(request):
    """
    Validate data import for updation of 5 projects when:
    a) dataimport field mapping is set to manual field mapping
    b) Default status and category is set
    c) file should have contents for all standard fields and mandatory udf fields
    """
    Fluent(request).project('Project-1')
    Fluent(request).project('Project-2')
    Fluent(request).project('Project-3')
    Fluent(request).project('Project-4')
    Fluent(request).project('Project-5')

    Fluent(request). \
        data_import().update_for_entity('PROJECT') \
        .consider_entities(['Project-1', 'Project-2', 'Project-3', 'Project-4', 'Project-5']) \
        .with_default_status('PROPOSED').with_default_category('CATEGORY1').where_field_mapping_is(
        'MANUAL') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('566')
def test_import_with_udf_fields(request):
    """
    Validate data import for updation of 5 projects when:
    a) dataimport field mapping is set to exact same title based mapping
    b) Default status and category is set
    c) file should have contents for all udf fields and mandatory standard fields
    """
    Fluent(request).project('Project-1')
    Fluent(request).project('Project-2')
    Fluent(request).project('Project-3')
    Fluent(request).project('Project-4')
    Fluent(request).project('Project-5')

    Fluent(request). \
        data_import().update_for_entity('PROJECT') \
        .consider_entities(['Project-1', 'Project-2', 'Project-3', 'Project-4', 'Project-5']) \
        .with_default_status('PROPOSED').with_default_category('CATEGORY1').where_field_mapping_is(
        'SAME') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('567')
def test_import_similar_title_udf_fieldmapping(request):
    """
    Validate data import for updation of 5 projects when:
    a) dataimport field mapping is set to similar title based mapping
    b) Default status and category is set
    c) file should have contents for all udf fields and mandatory standard fields
    """
    Fluent(request).project('Project-1')
    Fluent(request).project('Project-2')
    Fluent(request).project('Project-3')
    Fluent(request).project('Project-4')
    Fluent(request).project('Project-5')

    Fluent(request). \
        data_import().update_for_entity('PROJECT') \
        .consider_entities(['Project-1', 'Project-2', 'Project-3', 'Project-4', 'Project-5']) \
        .with_default_status('PROPOSED').with_default_category('CATEGORY1').where_field_mapping_is(
        'SIMILAR') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('568')
def test_import_manual_udf_fieldmapping(request):
    """
    Validate data import for updation of 5 projects when:
    a) dataimport field mapping is set to manual field mapping
    b) Default status and category is set
    c) file should have contents for all udf fields and mandatory standard fields
    """
    Fluent(request).project('Project-1')
    Fluent(request).project('Project-2')
    Fluent(request).project('Project-3')
    Fluent(request).project('Project-4')
    Fluent(request).project('Project-5')

    Fluent(request). \
        data_import().update_for_entity('PROJECT') \
        .consider_entities(['Project-1', 'Project-2', 'Project-3', 'Project-4', 'Project-5']) \
        .with_default_status('PROPOSED').with_default_category('CATEGORY1').where_field_mapping_is(
        'MANUAL') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('569')
def test_import_default_category_and_empty_excel_category(request):
    """
    Validate data import for updation of 5 projects when:
    a) dataimport field mapping is set to exact same title based mapping
    b) Default category is set
    c) file should have contents for all fields except for 'Category'
    """
    Fluent(request).project('Project-1')
    Fluent(request).project('Project-2')
    Fluent(request).project('Project-3')
    Fluent(request).project('Project-4')
    Fluent(request).project('Project-5')

    Fluent(request). \
        data_import().update_for_entity('PROJECT') \
        .consider_entities(['Project-1', 'Project-2', 'Project-3', 'Project-4', 'Project-5']) \
        .with_default_category('CATEGORY1').where_field_mapping_is('SAME') \
        .remove_column('PROJECT CATEGORY') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('571')
def test_import_default_category_and_excel_category(request):
    """
    Validate data import for updation of 5 projects when:
    a) dataimport field mapping is set to exact same title based mapping
    b) Default category is set
    c) file should have contents for all fields
    """
    Fluent(request).project('Project-1')
    Fluent(request).project('Project-2')
    Fluent(request).project('Project-3')
    Fluent(request).project('Project-4')
    Fluent(request).project('Project-5')

    Fluent(request). \
        data_import().update_for_entity('PROJECT') \
        .consider_entities(['Project-1', 'Project-2', 'Project-3', 'Project-4', 'Project-5']) \
        .with_default_category('CATEGORY1').where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('572')
def test_import_default_status_and_empty_excel_status(request):
    """
    Validate data import for updation of 5 projects when:
    a) dataimport field mapping is set to exact same title based mapping
    b) Default status is set
    c) file should have contents for all fields except for 'Category'
    """
    Fluent(request).project('Project-1')
    Fluent(request).project('Project-2')
    Fluent(request).project('Project-3')
    Fluent(request).project('Project-4')
    Fluent(request).project('Project-5')

    Fluent(request). \
        data_import().update_for_entity('PROJECT') \
        .consider_entities(['Project-1', 'Project-2', 'Project-3', 'Project-4', 'Project-5']) \
        .with_default_status('PROPOSED').where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields().remove_column('PROJECT STATUS') \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('573')
def test_import_default_status_and_excel_status(request):
    """
    Validate data import for updation of 5 projects when:
    a) dataimport field mapping is set to exact same title based mapping
    b) Default status is set
    c) file should have contents for all fields
    """
    Fluent(request).project('Project-1')
    Fluent(request).project('Project-2')
    Fluent(request).project('Project-3')
    Fluent(request).project('Project-4')
    Fluent(request).project('Project-5')

    Fluent(request). \
        data_import().update_for_entity('PROJECT') \
        .with_default_status('PROPOSED') \
        .consider_entities(['Project-1', 'Project-2', 'Project-3', 'Project-4', 'Project-5']) \
        .where_field_mapping_is('SAME').include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@pytest.mark.parametrize('string_comb',
                         ['abcd&s', 'a<b==&"s{>ss!s}d{', 'a&b', '^&', '5&', 'a>b', 'a<b', '5>b',
                          '6<3', '%$&*', 'a\'b',
                          'a"b', 'a+b', 'a@b'])
@zid('576')
def test_import_special_character_in_string(request, string_comb):
    """
    Validate data import for updation of two projects where special character is  in all string fields
    """
    Fluent(request).project('Project-1')
    Fluent(request).project('Project-2')

    Fluent(request). \
        data_import().update_for_entity('PROJECT') \
        .consider_entities(['Project-1', 'Project-2']) \
        .where_field_mapping_is('SAME').include_both_standard_and_udf_fields() \
        .set_fields({'string': string_comb}) \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('577')
def test_import_select_list(request):
    """
    Validate data import for updation of two projects having &(ampersand) in values of the list field types
    """
    Fluent(request).project('Project-1')
    Fluent(request).project('Project-2')

    Fluent(request). \
        data_import().update_for_entity('PROJECT') \
        .consider_entities(['Project-1', 'Project-2']) \
        .where_field_mapping_is('SAME').include_both_standard_and_udf_fields() \
        .set_fields({'UDF PEXS Multiselect List': 'Time & Materials',
                     'UDF Multi Select Lookup/Status List (CheckBox) 51': 'Scope & Strategy'}) \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@pytest.mark.parametrize('text_comb',
                         ['abcd&s', 'a&b', '^&', '5&', 'a>b', 'a<b', '5>b', '6<3', '%$&*'])
def test_textbox(request, text_comb):
    """
    Validate data import for updation of two projects where special character is  in all string fields
    """
    Fluent(request).project('Project-1')
    Fluent(request).project('Project-2')

    Fluent(request). \
        data_import().update_for_entity('PROJECT') \
        .consider_entities(['Project-1', 'Project-2']) \
        .where_field_mapping_is('SAME').include_both_standard_and_udf_fields() \
        .set_fields({'description': text_comb}) \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
def test_udf_picklist_user_automation(request):
    """
    Validate data import for updation of two projects where special character is  in all string fields
    """
    Fluent(request).project('Project-1')
    Fluent(request).project('Project-2')

    Fluent(request). \
        data_import().update_for_entity('PROJECT') \
        .consider_entities(['Project-1', 'Project-2']) \
        .where_field_mapping_is('SAME').include_both_standard_and_udf_fields() \
        .set_fields({'UDF PEXS Picklist': 'TeamUser, Automation'}) \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@pytest.mark.skip
@tags('dataimport')
def test_dynamic_special_character_textbox_and_string(request):
    """
    Validate data import for updation of two projects where special character is  in all string fields
    """
    Fluent(request).project('Project-1')
    Fluent(request).project('Project-2')

    Fluent(request). \
        data_import().update_for_entity('PROJECT') \
        .consider_entities(['Project-1', 'Project-2']) \
        .where_field_mapping_is('SAME').include_both_standard_and_udf_fields() \
        .turn_on_special_characters() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()
