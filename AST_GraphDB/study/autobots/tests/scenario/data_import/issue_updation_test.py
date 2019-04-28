import pytest
from core.fluent import Fluent
from core.src.custom_annotations import zid, tags


@tags('dataimport')
@zid('1111')
def test_import_same(request):
    """
    Validate data import for updation of 5 issue when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have content for all standard fields and mandatory udf fields
    """
    Fluent(request).issue('Issue-1')
    Fluent(request).issue('Issue-2')
    Fluent(request).issue('Issue-3')
    Fluent(request).issue('Issue-4')
    Fluent(request).issue('Issue-5')

    Fluent(request). \
        data_import().update_for_entity('ISSUE') \
        .consider_entities(['Issue-1', 'Issue-2', 'Issue-3', 'Issue-4', 'Issue-5']) \
        .where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('1112')
def test_import_same_for_udfs(request):
    """
    Validate data import for updation of 5 issues when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have content for all udf fields and mandatory standard fields
    """
    Fluent(request).issue('Issue-1')
    Fluent(request).issue('Issue-2')
    Fluent(request).issue('Issue-3')
    Fluent(request).issue('Issue-4')
    Fluent(request).issue('Issue-5')

    Fluent(request). \
        data_import().update_for_entity('ISSUE') \
        .consider_entities(['Issue-1', 'Issue-2', 'Issue-3', 'Issue-4', 'Issue-5']) \
        .where_field_mapping_is('SAME') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('1113')
def test_import_same_for_standard(request):
    """
    Validate data import for updation of 5 issues when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have content for all standard fields and mandatory udf fields
    """
    Fluent(request).issue('Issue-1')
    Fluent(request).issue('Issue-2')
    Fluent(request).issue('Issue-3')
    Fluent(request).issue('Issue-4')
    Fluent(request).issue('Issue-5')

    Fluent(request). \
        data_import().update_for_entity('ISSUE') \
        .consider_entities(['Issue-1', 'Issue-2', 'Issue-3', 'Issue-4', 'Issue-5']) \
        .where_field_mapping_is('SAME') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('1114')
def test_import_similar_all(request):
    """
    Validate data import for updation of 5 issues when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for all standard fields and all udf fields
    """
    Fluent(request).issue('Issue-1')
    Fluent(request).issue('Issue-2')
    Fluent(request).issue('Issue-3')
    Fluent(request).issue('Issue-4')
    Fluent(request).issue('Issue-5')

    Fluent(request). \
        data_import().update_for_entity('ISSUE') \
        .consider_entities(['Issue-1', 'Issue-2', 'Issue-3', 'Issue-4', 'Issue-5']) \
        .where_field_mapping_is('SIMILAR') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('1115')
def test_import_similar_for_udfs(request):
    """
    Validate data import for updation of 5 issues when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for all udf fields and mandatory standard fields
    """
    Fluent(request).issue('Issue-1')
    Fluent(request).issue('Issue-2')
    Fluent(request).issue('Issue-3')
    Fluent(request).issue('Issue-4')
    Fluent(request).issue('Issue-5')

    Fluent(request). \
        data_import().update_for_entity('ISSUE') \
        .consider_entities(['Issue-1', 'Issue-2', 'Issue-3', 'Issue-4', 'Issue-5']) \
        .where_field_mapping_is('SIMILAR') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('1116')
def test_import_similar_for_standard(request):
    """
    Validate data import for updation of 5 issues when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for all standard fields and mandatory udf fields
    """
    Fluent(request).issue('Issue-1')
    Fluent(request).issue('Issue-2')
    Fluent(request).issue('Issue-3')
    Fluent(request).issue('Issue-4')
    Fluent(request).issue('Issue-5')

    Fluent(request). \
        data_import().update_for_entity('ISSUE') \
        .consider_entities(['Issue-1', 'Issue-2', 'Issue-3', 'Issue-4', 'Issue-5']) \
        .where_field_mapping_is('SIMILAR') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('1117')
def test_import_manual_all(request):
    """
    Validate data import for updation of 5 issues when:
    a) dataimport field mapping is set to exact manual title based mapping
    b) file should have content for all standard fields and all udf fields
    """
    Fluent(request).issue('Issue-1')
    Fluent(request).issue('Issue-2')
    Fluent(request).issue('Issue-3')
    Fluent(request).issue('Issue-4')
    Fluent(request).issue('Issue-5')

    Fluent(request). \
        data_import().update_for_entity('ISSUE') \
        .consider_entities(['Issue-1', 'Issue-2', 'Issue-3', 'Issue-4', 'Issue-5']) \
        .where_field_mapping_is('MANUAL') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('1118')
def test_import_manual_for_udfs(request):
    """
    Validate data import for updation of 5 issues when:
    a) dataimport field mapping is set to exact manual title based mapping
    b) file should have content for all udf fields and mandatory standard fields
    """
    Fluent(request).issue('Issue-1')
    Fluent(request).issue('Issue-2')
    Fluent(request).issue('Issue-3')
    Fluent(request).issue('Issue-4')
    Fluent(request).issue('Issue-5')

    Fluent(request). \
        data_import().update_for_entity('ISSUE') \
        .consider_entities(['Issue-1', 'Issue-2', 'Issue-3', 'Issue-4', 'Issue-5']) \
        .where_field_mapping_is('MANUAL') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('1119')
def test_import_manual_for_standard(request):
    """
    Validate data import for updation of 5 issues when:
    a) dataimport field mapping is set to exact manual title based mapping
    b) file should have content for all standard fields and mandatory udf fields
    """
    Fluent(request).issue('Issue-1')
    Fluent(request).issue('Issue-2')
    Fluent(request).issue('Issue-3')
    Fluent(request).issue('Issue-4')
    Fluent(request).issue('Issue-5')

    Fluent(request). \
        data_import().update_for_entity('ISSUE') \
        .consider_entities(['Issue-1', 'Issue-2', 'Issue-3', 'Issue-4', 'Issue-5']) \
        .where_field_mapping_is('MANUAL') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('11110')
@pytest.mark.parametrize('text_comb', ['abcd&s', 'a&b', '^&', '5&', 'a>b', 'a<b', '5>b', '6<3', '%$&*'])
def test_dynamic_special_character_textbox(request, text_comb):
    """
    Validate data import for updation of two issues where special character is in all text box fields
    """
    Fluent(request).issue('Issue-1')
    Fluent(request).issue('Issue-2')

    Fluent(request). \
        data_import().update_for_entity('ISSUE') \
        .consider_entities(['Issue-1', 'Issue-2']) \
        .where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields() \
        .set_fields({'problem description': text_comb}) \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('11111')
@pytest.mark.parametrize('text_comb', ['a&b', '^&', '5&', 'a>b', 'a<b', '5>b', '6<3', '%$&*'])
def test_dynamic_special_character_string(request, text_comb):
    """
    Validate data import for updation of two issues where special character is in all string fields
    """
    Fluent(request).issue('Issue-1')
    Fluent(request).issue('Issue-2')

    Fluent(request). \
        data_import().update_for_entity('ISSUE') \
        .consider_entities(['Issue-1', 'Issue-2']) \
        .where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields() \
        .set_fields({'string': text_comb}) \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@pytest.mark.skip
@tags('dataimport')
@zid('11112')
def test_dynamic_special_character_textbox_and_string(request):
    """
    Validate data import for updation of two issues where special character is in all string fields
    """
    Fluent(request).issue('Issue-1')
    Fluent(request).issue('Issue-2')

    Fluent(request). \
        data_import().update_for_entity('ISSUE') \
        .consider_entities(['Issue-1', 'Issue-2']) \
        .where_field_mapping_is('SAME').include_both_standard_and_udf_fields() \
        .turn_on_special_characters() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('11113')
def test_resource_with_same_lastname_and_similar_firstname(request):
    """
    Validate data import for updation of issues where resource with same last name and similar first name starting
    There was a reported issue on this
    """
    Fluent(request).issue('Issue-1')
    Fluent(request).issue('Issue-2')

    Fluent(request). \
        data_import().update_for_entity('ISSUE') \
        .consider_entities(['Issue-1', 'Issue-2']) \
        .where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields() \
        .set_fields({'udf issu autocomplete list': 'QA_01, Full_Autoabc'}) \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()
