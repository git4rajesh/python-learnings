from unittest.mock import patch
from mocking_in_python.working_classes.features1 import is_innotas

@patch('mocking_in_python.working_classes.features1.get_product')
def test_is_innotas(mock_get_product):
    mock_get_product.return_value = 'Innotas'
    assert(is_innotas())



# def test_is_innotas():
#     assert (is_innotas())