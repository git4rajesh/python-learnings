from unittest.mock import patch, Mock, MagicMock
from mocking_in_python.working_classes.features3 import Features3


# Without using Decorator
@patch.object(Features3, 'get_product')
def test_get_product_artifact_v3(mock_get_product):
    f = Features3()
    # expected = ['Innotas', 'PP']
    mock_get_product.side_effect = ['PP', 'Innotas']
    print('\n', f.get_innotas())
    print('--------------')
    print(f.get_innotas())
