from unittest.mock import patch, Mock, MagicMock
from mocking_in_python.working_classes.feature2 import Features


# Using Decorator
# @patch.object(Features, 'get_product')
# def test_get_product_artifact(mock_get_product):
#     f = Features()
#     mock_get_product.return_value = 'Innotas'
#     assert (f.is_innotas())


# Without using Decorator
def test_get_product_artifact_v2():#
    f = Features()

    # f.get_product = Mock()
    f.get_product = MagicMock()

    f.get_product.return_value = 'Innotas'
    assert (f.is_innotas())


