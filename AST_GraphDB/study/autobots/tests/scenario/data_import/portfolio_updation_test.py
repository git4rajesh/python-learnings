import pytest

from core.fluent import Fluent
from core.src.custom_annotations import zid, tags


@tags('dataimport')
@zid('111')
def test_import_all_fields_mapping_is_same(request):
    """
    Validate data import for updation of 5 portfolios when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have content for all standard fields and all udf fields
    """
    Fluent(request).portfolio('Portfolio-1')
    Fluent(request).portfolio('Portfolio-2')
    Fluent(request).portfolio('Portfolio-3')
    Fluent(request).portfolio('Portfolio-4')
    Fluent(request).portfolio('Portfolio-5')

    Fluent(request). \
        data_import().update_for_entity('PORTFOLIO') \
        .consider_entities(['Portfolio-1', 'Portfolio-2', 'Portfolio-3', 'Portfolio-4', 'Portfolio-5']) \
        .where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('112')
def test_import_standard_fields_mapping_is_same(request):
    """
    Validate data import for updation of 5 portfolios when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have content for all standard fields and mandatory udf fields
    """
    Fluent(request).portfolio('Portfolio-1')
    Fluent(request).portfolio('Portfolio-2')
    Fluent(request).portfolio('Portfolio-3')
    Fluent(request).portfolio('Portfolio-4')
    Fluent(request).portfolio('Portfolio-5')

    Fluent(request). \
        data_import().update_for_entity('PORTFOLIO') \
        .consider_entities(['Portfolio-1', 'Portfolio-2', 'Portfolio-3', 'Portfolio-4', 'Portfolio-5']) \
        .where_field_mapping_is('SAME') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('113')
def test_import_udf_fields_mapping_is_same(request):
    """
    Validate data import for updation of 5 portfolios when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have content for all udf fields and mandatory standard fields
    """
    Fluent(request).portfolio('Portfolio-1')
    Fluent(request).portfolio('Portfolio-2')
    Fluent(request).portfolio('Portfolio-3')
    Fluent(request).portfolio('Portfolio-4')
    Fluent(request).portfolio('Portfolio-5')

    Fluent(request). \
        data_import().update_for_entity('PORTFOLIO') \
        .consider_entities(['Portfolio-1', 'Portfolio-2', 'Portfolio-3', 'Portfolio-4', 'Portfolio-5']) \
        .where_field_mapping_is('SAME') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('114')
def test_import_standard_fields_mapping_is_similar(request):
    """
    Validate data import for updation of 5 portfolios when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for all standard fields and mandatory udf fields
    """
    Fluent(request).portfolio('Portfolio-1')
    Fluent(request).portfolio('Portfolio-2')
    Fluent(request).portfolio('Portfolio-3')
    Fluent(request).portfolio('Portfolio-4')
    Fluent(request).portfolio('Portfolio-5')

    Fluent(request). \
        data_import().update_for_entity('PORTFOLIO') \
        .consider_entities(['Portfolio-1', 'Portfolio-2', 'Portfolio-3', 'Portfolio-4', 'Portfolio-5']) \
        .where_field_mapping_is('SIMILAR') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('115')
def test_import_udf_fields_mapping_is_similar(request):
    """
    Validate data import for updation of 5 portfolios when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for all udf fields and mandatory standard fields
    """
    Fluent(request).portfolio('Portfolio-1')
    Fluent(request).portfolio('Portfolio-2')
    Fluent(request).portfolio('Portfolio-3')
    Fluent(request).portfolio('Portfolio-4')
    Fluent(request).portfolio('Portfolio-5')

    Fluent(request). \
        data_import().update_for_entity('PORTFOLIO') \
        .consider_entities(['Portfolio-1', 'Portfolio-2', 'Portfolio-3', 'Portfolio-4', 'Portfolio-5']) \
        .where_field_mapping_is('SIMILAR') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('116')
def test_import_all_fields_mapping_is_similar(request):
    """
    Validate data import for updation of 5 portfolios when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for all standard fields and all udf fields
    """
    Fluent(request).portfolio('Portfolio-1')
    Fluent(request).portfolio('Portfolio-2')
    Fluent(request).portfolio('Portfolio-3')
    Fluent(request).portfolio('Portfolio-4')
    Fluent(request).portfolio('Portfolio-5')

    Fluent(request). \
        data_import().update_for_entity('PORTFOLIO') \
        .consider_entities(['Portfolio-1', 'Portfolio-2', 'Portfolio-3', 'Portfolio-4', 'Portfolio-5']) \
        .where_field_mapping_is('SIMILAR') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('117')
def test_import_standard_fields_mapping_is_manual(request):
    """
    Validate data import for updation of 5 portfolios when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for all standard fields and mandatory udf fields
    """
    Fluent(request).portfolio('Portfolio-1')
    Fluent(request).portfolio('Portfolio-2')
    Fluent(request).portfolio('Portfolio-3')
    Fluent(request).portfolio('Portfolio-4')
    Fluent(request).portfolio('Portfolio-5')

    Fluent(request). \
        data_import().update_for_entity('PORTFOLIO') \
        .consider_entities(['Portfolio-1', 'Portfolio-2', 'Portfolio-3', 'Portfolio-4', 'Portfolio-5']) \
        .where_field_mapping_is('MANUAL') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('118')
def test_import_udf_fields_mapping_is_manual(request):
    """
    Validate data import for updation of 5 portfolios when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for only udf fields and mandatory standard fields
    """
    Fluent(request).portfolio('Portfolio-1')
    Fluent(request).portfolio('Portfolio-2')
    Fluent(request).portfolio('Portfolio-3')
    Fluent(request).portfolio('Portfolio-4')
    Fluent(request).portfolio('Portfolio-5')

    Fluent(request). \
        data_import().update_for_entity('PORTFOLIO') \
        .consider_entities(['Portfolio-1', 'Portfolio-2', 'Portfolio-3', 'Portfolio-4', 'Portfolio-5']) \
        .where_field_mapping_is('MANUAL') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('119')
def test_import_all_fields_mapping_is_manual(request):
    """
    Validate data import for updation of 5 portfolios when:
    a) dataimport field mapping is set to exact similar title based mapping
    b) file should have content for all standard fields and all udf fields
    """
    Fluent(request).portfolio('Portfolio-1')
    Fluent(request).portfolio('Portfolio-2')
    Fluent(request).portfolio('Portfolio-3')
    Fluent(request).portfolio('Portfolio-4')
    Fluent(request).portfolio('Portfolio-5')

    Fluent(request). \
        data_import().update_for_entity('PORTFOLIO') \
        .consider_entities(['Portfolio-1', 'Portfolio-2', 'Portfolio-3', 'Portfolio-4', 'Portfolio-5']) \
        .where_field_mapping_is('MANUAL') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('1110')
@pytest.mark.parametrize('text_comb', ['a&b', '^&', '5&', 'a>b', 'a<b', '5>b', '6<3', '%$&*'])
def test_dynamic_special_character_textbox(request, text_comb):
    """
    Validate data import for updation of two portfolio where special character is  in all text box fields
    """
    Fluent(request).portfolio('Portfolio-1')
    Fluent(request).portfolio('Portfolio-2')

    Fluent(request). \
        data_import().update_for_entity('PORTFOLIO') \
        .consider_entities(['Portfolio-1', 'Portfolio-2']) \
        .where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields() \
        .set_fields({'description': text_comb}) \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('1111')
@pytest.mark.parametrize('text_comb', ['a&b', '^&', '5&', 'a>b', 'a<b', '5>b', '6<3', '%$&*'])
def test_dynamic_special_character_string(request, text_comb):
    """
    Validate data import for updation of two portfolio where special character is  in all string fields
    """
    Fluent(request).portfolio('Portfolio-1')
    Fluent(request).portfolio('Portfolio-2')

    Fluent(request). \
        data_import().update_for_entity('PORTFOLIO') \
        .consider_entities(['Portfolio-1', 'Portfolio-2']) \
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
    Validate data import for updation of two portfolio where special character is in all string supporting fields
    """
    Fluent(request).portfolio('Portfolio-1')
    Fluent(request).portfolio('Portfolio-2')

    Fluent(request). \
        data_import().update_for_entity('PORTFOLIO') \
        .consider_entities(['Portfolio-1', 'Portfolio-2']) \
        .where_field_mapping_is('SAME').include_both_standard_and_udf_fields() \
        .turn_on_special_characters() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()
