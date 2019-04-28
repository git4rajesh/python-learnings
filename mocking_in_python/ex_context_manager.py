from unittest.mock import patch, Mock, MagicMock
from mocking_in_python.working_classes.feature2 import Features


def test_get_product_artifact():
    with patch.object(Features, 'get_product') as mock_get_product:
        f = Features()
        mock_get_product.return_value = 'Innotas'
        assert (f.is_innotas())

# Decorator internally uses Context Manager.