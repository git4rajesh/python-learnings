import pytest

from core.fluent import Fluent
from core.src.custom_annotations import zid, tags


@tags('dataimport')
@zid('11121')
def test_import_exact_same_title_standard_fieldmapping(request):
    """
    Validate data import for updation of 5 assets when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have content for all standard fields and mandatory udf fields
    """
    Fluent(request).asset('Asset-1')
    Fluent(request).asset('Asset-2')
    Fluent(request).asset('Asset-3')
    Fluent(request).asset('Asset-4')
    Fluent(request).asset('Asset-5')

    Fluent(request). \
        data_import().update_for_entity('ASSET') \
        .consider_entities(['Asset-1', 'Asset-2', 'Asset-3', 'Asset-4', 'Asset-5']) \
        .where_field_mapping_is('SAME') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('11122')
def test_import_similar_title_standard_fieldmapping(request):
    """
    Validate data import for updation of 5 assets when:
    a) dataimport field mapping is set to similar title based mapping
    b) file should have contents for all standard fields and mandatory udf fields
    """
    Fluent(request).asset('Asset-1')
    Fluent(request).asset('Asset-2')
    Fluent(request).asset('Asset-3')
    Fluent(request).asset('Asset-4')
    Fluent(request).asset('Asset-5')

    Fluent(request). \
        data_import().update_for_entity('ASSET') \
        .consider_entities(['Asset-1', 'Asset-2', 'Asset-3', 'Asset-4', 'Asset-5']) \
        .where_field_mapping_is('SIMILAR') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('11123')
def test_import_manual_standard_fieldmapping(request):
    """
    Validate data import for updation of 5 assets when:
    a) dataimport field mapping is set to manual field mapping
    b) file should have contents for all standard fields and mandatory udf fields
    """
    Fluent(request).asset('Asset-1')
    Fluent(request).asset('Asset-2')
    Fluent(request).asset('Asset-3')
    Fluent(request).asset('Asset-4')
    Fluent(request).asset('Asset-5')

    Fluent(request). \
        data_import().update_for_entity('ASSET') \
        .consider_entities(['Asset-1', 'Asset-2', 'Asset-3', 'Asset-4', 'Asset-5']) \
        .where_field_mapping_is('MANUAL') \
        .include_only_standard_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('11124')
def test_import_with_udf_fields(request):
    """
    Validate data import for updation of 5 assets when:
    a) dataimport field mapping is set to exact same title based mapping
    b) file should have contents for all udf fields and mandatory standard fields
    """
    Fluent(request).asset('Asset-1')
    Fluent(request).asset('Asset-2')
    Fluent(request).asset('Asset-3')
    Fluent(request).asset('Asset-4')
    Fluent(request).asset('Asset-5')

    Fluent(request). \
        data_import().update_for_entity('ASSET') \
        .consider_entities(['Asset-1', 'Asset-2', 'Asset-3', 'Asset-4', 'Asset-5']) \
        .where_field_mapping_is('SAME') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('11125')
def test_import_similar_title_udf_fieldmapping(request):
    """
    Validate data import for updation of 5 assets when:
    a) dataimport field mapping is set to similar title based mapping
    b) file should have contents for all udf fields and mandatory standard fields
    """
    Fluent(request).asset('Asset-1')
    Fluent(request).asset('Asset-2')
    Fluent(request).asset('Asset-3')
    Fluent(request).asset('Asset-4')
    Fluent(request).asset('Asset-5')

    Fluent(request). \
        data_import().update_for_entity('ASSET') \
        .consider_entities(['Asset-1', 'Asset-2', 'Asset-3', 'Asset-4', 'Asset-5']) \
        .where_field_mapping_is('SIMILAR') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()


@tags('dataimport')
@zid('11126')
def test_import_manual_udf_fieldmapping(request):
    """
    Validate data import for updation of 5 assets when:
    a) dataimport field mapping is set to manual field mapping
    b) file should have contents for all udf fields and mandatory standard fields
    """
    Fluent(request).asset('Asset-1')
    Fluent(request).asset('Asset-2')
    Fluent(request).asset('Asset-3')
    Fluent(request).asset('Asset-4')
    Fluent(request).asset('Asset-5')

    Fluent(request). \
        data_import().update_for_entity('ASSET') \
        .consider_entities(['Asset-1', 'Asset-2', 'Asset-3', 'Asset-4', 'Asset-5']) \
        .where_field_mapping_is('MANUAL') \
        .include_only_udf_fields() \
        .populate_dynamic_data_to_excel_file() \
        .import_file().verify()
