import pytest
from core.fluent import Fluent
from core.src.custom_annotations import zid, tags


@tags('dataimport')
@zid('11111')
def test_import_same(request):
    """
    Validate data import for creation of 5 asset when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have content for all fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ASSET') \
        .where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('11112')
def test_import_same_only_standard_fields(request):
    """
    Validate data import for creation of 5 asset when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have content for standard fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ASSET') \
        .where_field_mapping_is('SAME') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('11113')
def test_import_same_only_udf_fields(request):
    """
    Validate data import for creation of 5 asset when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have content for udf fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ASSET') \
        .where_field_mapping_is('SAME') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=1) \
        .import_file().verify()


@tags('dataimport')
@zid('11114')
def test_import_similar(request):
    """
    Validate data import for creation of 5 asset when:
    a) dataimport field mapping is set to similar title based mapping
    b) file should have content for all fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ASSET') \
        .where_field_mapping_is('SIMILAR') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('11115')
def test_import_similar_only_standard_fields(request):
    """
    Validate data import for creation of 5 asset when:
    a) dataimport field mapping is set to similar title based mapping
    b) file should have content for standard fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ASSET') \
        .where_field_mapping_is('SIMILAR') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('11116')
def test_import_similar_only_udf(request):
    """
    Validate data import for creation of 5 asset when:
    a) dataimport field mapping is set to similar title based mapping
    b) file should have content for udf fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ASSET') \
        .where_field_mapping_is('SIMILAR') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('11117')
def test_import_manual(request):
    """
    Validate data import for creation of 5 asset when:
    a) dataimport field mapping is set to manual title based mapping
    b) file should have content for all fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ASSET') \
        .where_field_mapping_is('Manual') \
        .include_both_standard_and_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('11118')
def test_import_manual_only_standard(request):
    """
    Validate data import for creation of 5 asset when:
    a) dataimport field mapping is set to manual title based mapping
    b) file should have content for standard fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ASSET') \
        .where_field_mapping_is('MANUAL') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('11119')
def test_import_manual_only_udf_fields(request):
    """
    Validate data import for creation of 5 asset when:
    a) dataimport field mapping is set to manual title based mapping
    b) file should have content for udf fields and mandatory udf fields
    """
    Fluent(request). \
        data_import().create_for_entity('ASSET') \
        .where_field_mapping_is('MANUAL') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file(no_of_rows=5) \
        .import_file().verify()


@tags('dataimport')
@zid('111112')
def test_import_for_special_char_in_pick_list(request):
    """
    Validate data import for creation of asses when:
        Data import xls has "ASSET ASSIGNED TO" field value with 'T&E, Automation'
    """
    Fluent(request). \
        data_import().create_for_entity('ASSET') \
        .where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields() \
        .set_fields({'assigned to': 'T&E, Automation'}) \
        .populate_dynamic_data_to_excel_file(no_of_rows=1) \
        .import_file().verify()


@tags('dataimport')
@zid('111113')
def test_import_for_resource_with_middlename_in_pick_list(request):
    """
    Validate data import for creation of asses when:
        Data import xls has "ASSET ASSIGNED TO" field value with 'T&E, Automation'
    """
    Fluent(request). \
        data_import().create_for_entity('ASSET') \
        .where_field_mapping_is('SAME') \
        .include_both_standard_and_udf_fields() \
        .set_fields({'assigned to': 'TEUser, QA'}) \
        .populate_dynamic_data_to_excel_file(no_of_rows=1) \
        .import_file().verify()
