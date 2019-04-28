import os
import pytest

from core.asserter import Asserter
from entities.rollups import helper
from core.src.custom_annotations import tags

PATH = os.path.join(os.path.dirname(__file__), './inputs/')
EXPECTED_DICT = {'Billable Cost': {'estimated': 0.00, 'actual': 3520.00, 'variance': -3520.00, '% recognized': 0.00},
                 'Non Billable Hrs': {'estimated': 0.00, 'actual': 40.00, 'variance': -40.00, '% recognized': 0.00},
                 'Total Hours': {'estimated': 0.00, 'actual': 70.00, 'variance': -70.00, '% recognized': 0.00},
                 'Billable Hrs': {'estimated': 0.00, 'actual': 30.00, 'variance': -30.00, '% recognized': 0.00},
                 'Non Billable Cost': {'estimated': 0.00, 'actual': 4800.00, 'variance': -4800.00,
                                       '% recognized': 0.00},
                 'Capitalized Cost': {'estimated': 0.00, 'actual': 5920.00, 'variance': -5920.00, '% recognized': 0.00},
                 'Non-Capitalized Cost': {'estimated': 0.00, 'actual': 2400.00, 'variance': -2400.00,
                                          '% recognized': 0.00},
                 'Total Cost': {'estimated': 0.00, 'actual': 8320.00, 'variance': -8320.00, '% recognized': 0.00},
                 'Revenue': {'estimated': 0.00, 'actual': 240.00, 'variance': -240.00, '% recognized': 0.00},
                 'Non Billable Amount': {'estimated': 0.00, 'actual': 0.00, 'variance': 0.00, '% recognized': 0.00},
                 'Profit': {'estimated': 0.00, 'actual': -8080.00, 'variance': 8080.00, '% recognized': 0.00},
                 'Margin': {'estimated': 0.00, 'actual': -3366.67, 'variance': 3366.67, '% recognized': 0.00}}


@tags('unittest')
def test_additional_column(request):
    filename = 'additional_column.html'
    file_path = PATH + filename
    expected_exception = 'HTML Parse Error : expected heading : actual and actual heading : additionalcolumn'
    with open(file_path, 'r') as html_file:
        html = html_file.read()
    with pytest.raises(Exception) as exception_info:
        helper.parse_to_dict(html)
    actual_exception = exception_info.value.args[0]
    assert actual_exception.lower() == expected_exception.lower()


@tags('unittest')
def test_additional_row_same_val(request):
    filename = 'additional_row_with_same_value.html'
    file_path = PATH + filename
    expected_exception = 'HTML Parse Error : expected row key : margin and actual row key : additional row'
    with open(file_path, 'r') as html_file:
        html = html_file.read()
    with pytest.raises(Exception) as exception_info:
        helper.parse_to_dict(html)
    actual_exception = exception_info.value.args[0]
    assert actual_exception.lower() == expected_exception.lower()


@tags('unittest')
def test_delete_column(request):
    filename = 'delete_column.html'
    file_path = PATH + filename
    expected_exception = 'HTML Parse Error : expected heading : actual and actual heading : variance'
    with open(file_path, 'r') as html_file:
        html = html_file.read()
    with pytest.raises(Exception) as exception_info:
        helper.parse_to_dict(html)
    actual_exception = exception_info.value.args[0]
    assert actual_exception.lower() == expected_exception.lower()


@tags('unittest')
def test_delete_row(request):
    filename = 'delete_row.html'
    file_path = PATH + filename
    expected_exception = 'HTML Parse Error : expected row key : capitalized cost and actual row key : non-capitalized cost'
    with open(file_path, 'r') as html_file:
        html = html_file.read()
    with pytest.raises(Exception) as exception_info:
        helper.parse_to_dict(html)
    actual_exception = exception_info.value.args[0]
    assert actual_exception.lower() == expected_exception.lower()


@tags('unittest')
def test_jumbled_columns(request):
    filename = 'jumbled_column_order.html'
    file_path = PATH + filename
    expected_exception = 'HTML Parse Error : expected heading : actual and actual heading : variance'
    with open(file_path, 'r') as html_file:
        html = html_file.read()
    with pytest.raises(Exception) as exception_info:
        helper.parse_to_dict(html)
    actual_exception = exception_info.value.args[0]
    assert actual_exception.lower() == expected_exception.lower()


@tags('unittest')
def test_jumbled_rows(request):
    filename = 'jumbled_row_order.html'
    file_path = PATH + filename
    expected_exception = 'HTML Parse Error : expected row key : billable hrs and actual row key : billable cost'
    with open(file_path, 'r') as html_file:
        html = html_file.read()
    with pytest.raises(Exception) as exception_info:
        helper.parse_to_dict(html)
    actual_exception = exception_info.value.args[0]
    assert actual_exception.lower() == expected_exception.lower()


@tags('unittest')
def test_updated_column_name(request):
    filename = 'update_column_name.html'
    file_path = PATH + filename
    expected_exception = 'HTML Parse Error : expected heading : estimated and actual heading : estimated-updated'
    with open(file_path, 'r') as html_file:
        html = html_file.read()
    with pytest.raises(Exception) as exception_info:
        helper.parse_to_dict(html)
    actual_exception = exception_info.value.args[0]
    assert actual_exception.lower() == expected_exception.lower()


@tags('unittest')
def test_updated_row_name(request):
    filename = 'update_row_name.html'
    file_path = PATH + filename
    expected_exception = 'HTML Parse Error : expected row key : billable hrs and actual row key : billable-updated hrs'
    with open(file_path, 'r') as html_file:
        html = html_file.read()
    with pytest.raises(Exception) as exception_info:
        helper.parse_to_dict(html)
    actual_exception = exception_info.value.args[0]
    assert actual_exception.lower() == expected_exception.lower()


@tags('unittest')
def test_additional_row_diff_value(request):
    filename = 'additional_row_with_different_value.html'
    file_path = PATH + filename
    expected_exception = 'HTML Parse Error : expected row key : margin and actual row key : additional row'
    with open(file_path, 'r') as html_file:
        html = html_file.read()
    with pytest.raises(Exception) as exception_info:
        helper.parse_to_dict(html)
    actual_exception = exception_info.value.args[0]
    assert actual_exception.lower() == expected_exception.lower()


@tags('unittest')
def test_positive(request):
    filename = 'positive.html'
    file_path = PATH + filename
    with open(file_path, 'r') as html_file:
        html = html_file.read()
    actual_dict = helper.parse_to_dict(html)
    status, remarks = Asserter().verify(actual_dict, expected_dct=EXPECTED_DICT)
    assert status
