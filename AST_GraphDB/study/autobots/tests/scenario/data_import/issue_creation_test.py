import pytest
from core.fluent import Fluent
from core.src.custom_annotations import zid, tags


@tags('dataimport')
@zid('1111')
def test_import_same(request):
    """
    Validate data import for creation of 5 issue when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have content for all standard fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ISSUE') \
        .where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('1112')
def test_import_same_for_udfs(request):
    """
    Validate data import for creation of 5 issue when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have content for all udf fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ISSUE') \
        .where_field_mapping_is('SAME') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('1113')
def test_import_same_for_standard(request):
    """
    Validate data import for creation of 5 issue when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have content for all udf fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ISSUE') \
        .where_field_mapping_is('SAME') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('1114')
def test_import_similar_all(request):
    """
    Validate data import for creation of 5 issue when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for all standard fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ISSUE') \
        .where_field_mapping_is('SIMILAR') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('1115')
def test_import_similar_for_udfs(request):
    """
    Validate data import for creation of 5 issue when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for all udf fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ISSUE') \
        .where_field_mapping_is('SIMILAR') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('1116')
def test_import_similar_for_standard(request):
    """
    Validate data import for creation of 5 issue when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for all udf fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ISSUE') \
        .where_field_mapping_is('SIMILAR') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('1117')
def test_import_manual_all(request):
    """
    Validate data import for creation of 5 issue when:
    a) dataimport field mapping is set to exact manual title based mapping
    b) file should have content for all standard fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ISSUE') \
        .where_field_mapping_is('MANUAL') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('1118')
def test_import_manual_for_udfs(request):
    """
    Validate data import for creation of 5 issue when:
    a) dataimport field mapping is set to exact manual title based mapping
    b) file should have content for all udf fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ISSUE') \
        .where_field_mapping_is('MANUAL') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('1119')
def test_import_manual_for_standard(request):
    """
    Validate data import for creation of 5 issue when:
    a) dataimport field mapping is set to exact manual title based mapping
    b) file should have content for all udf fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ISSUE') \
        .where_field_mapping_is('MANUAL') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('11110')
@pytest.mark.parametrize('text_comb', ['abcd&s', 'a&b', '^&', '5&', 'a>b', 'a<b', '5>b', '6<3', '%$&*'])
def test_dynamic_special_character_textbox(request, text_comb):
    """
    Validate data import for creation of two issues where special character is  in all string fields
    """
    Fluent(request). \
        data_import().create_for_entity('ISSUE') \
        .where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields() \
        .set_fields({'text box': text_comb}) \
        .populate_dynamic_data_to_excel_file(no_of_rows=2) \
        .import_file().verify()


@tags('dataimport')
@zid('11110')
@pytest.mark.parametrize('text_comb', ['a&b', '^&', '5&', 'a>b', 'a<b', '5>b', '6<3', '%$&*'])
def test_dynamic_special_character_textbox(request, text_comb):
    """
    Validate data import for creation of two issues where special character is  in all string fields
    """
    Fluent(request). \
        data_import().create_for_entity('ISSUE') \
        .where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields() \
        .set_fields({'problem description': text_comb}) \
        .populate_dynamic_data_to_excel_file(no_of_rows=2) \
        .import_file().verify()


@tags('dataimport')
@zid('11111')
@pytest.mark.parametrize('text_comb', ['a&b', '^&', '5&', 'a>b', 'a<b', '5>b', '6<3', '%$&*'])
def test_dynamic_special_character_string(request, text_comb):
    """
    Validate data import for creation of two issues where special character is  in all string fields
    """
    Fluent(request). \
        data_import().create_for_entity('ISSUE') \
        .where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields() \
        .set_fields({'string': text_comb}) \
        .populate_dynamic_data_to_excel_file(no_of_rows=2) \
        .import_file().verify()


@tags('dataimport')
@zid('11112')
def test_import_mandatory_fields(request):
    """
    Validate data import for creation of a portfolio when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for standard fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ISSUE') \
        .where_field_mapping_is('SAME') \
        .include_only_mandatory_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=1) \
        .import_file().verify()
