import pytest
from core.fluent import Fluent
from core.src.custom_annotations import zid, tags

@pytest.mark.debug
@tags('dataimport')
@zid('111')
def test_import_all_fields_mapping_is_same(request):
    """
    Validate data import for creation of 5 portfolios when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have content for all fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('PORTFOLIO') \
        .where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('601')
def test_import_standard_fields_mapping_is_same(request):
    """
    Validate data import for creation of 5 portfolios when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have content for standard fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('PORTFOLIO') \
        .where_field_mapping_is('SAME') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('113')
def test_import_udf_fields_mapping_is_same(request):
    """
    Validate data import for creation of 5 portfolios when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have content for udf fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('PORTFOLIO') \
        .where_field_mapping_is('SAME') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('114')
def test_import_standard_fields_mapping_is_similar(request):
    """
    Validate data import for creation of 5 portfolios when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for standard fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('PORTFOLIO') \
        .where_field_mapping_is('SIMILAR') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('115')
def test_import_udf_fields_mapping_is_similar(request):
    """
    Validate data import for creation of 5 portfolios when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for udf fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('PORTFOLIO') \
        .where_field_mapping_is('SIMILAR') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('116')
def test_import_all_fields_mapping_is_similar(request):
    """
    Validate data import for creation of 5 portfolios when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for all fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('PORTFOLIO') \
        .where_field_mapping_is('SIMILAR') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('117')
def test_import_standard_fields_mapping_is_manual(request):
    """
    Validate data import for creation of 5 portfolios when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for standard fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('PORTFOLIO') \
        .where_field_mapping_is('MANUAL') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('118')
def test_import_udf_fields_mapping_is_manual(request):
    """
    Validate data import for creation of 5 portfolios when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for udf fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('PORTFOLIO') \
        .where_field_mapping_is('MANUAL') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('119')
def test_import_all_fields_mapping_is_manual(request):
    """
    Validate data import for creation of 5 portfolios when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for all fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('PORTFOLIO') \
        .where_field_mapping_is('MANUAL') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('1110')
@pytest.mark.parametrize('text_comb', ['a&b', '^&', '5&', 'a>b', 'a<b', '5>b', '6<3', '%$&*'])
def test_dynamic_special_character_textbox(request, text_comb):
    """
    Validate data import for creation of two portfolio where special character is  in all string fields
    """
    Fluent(request). \
        data_import().create_for_entity('PORTFOLIO') \
        .where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields() \
        .set_fields({'description': text_comb}) \
        .populate_dynamic_data_to_excel_file(no_of_rows=2) \
        .import_file().verify()


@tags('dataimport')
@zid('1111')
@pytest.mark.parametrize('text_comb', ['a&b', '^&', '5&', 'a>b', 'a<b', '5>b', '6<3', '%$&*'])
def test_dynamic_special_character_string(request, text_comb):
    """
    Validate data import for creation of two portfolio where special character is  in all string fields
    """
    Fluent(request). \
        data_import().create_for_entity('PORTFOLIO') \
        .where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields() \
        .set_fields({'string': text_comb}) \
        .populate_dynamic_data_to_excel_file(no_of_rows=2) \
        .import_file().verify()


@tags('dataimport')
@zid('1112')
def test_import_mandatory_fields(request):
    """
    Validate data import for creation of a portfolio when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for standard fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('PORTFOLIO') \
        .where_field_mapping_is('SAME') \
        .include_only_mandatory_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=1) \
        .import_file().verify()
