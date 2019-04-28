from unittest.mock import patch, Mock, MagicMock
from mocking_in_python.working_classes.features4 import Features4


# Without using Decorator
# def test_call_prod():
#     f = Features4()
#
#     f.get_product = Mock(return_value='Innotas')
#     f.call_prod()
#
#     assert (f.get_product.call_count == 1)


# @patch.object(Features4, 'call_pve')
# def test_wrapper_get_pve(mock_call_pve):
#     artifact = 'project'
#     f = Features4()
#     f.wrapper_get_pve(artifact)
#     mock_call_pve.assert_called_once_with(artifact)



@patch.object(Features4, 'call_innotas')
@patch.object(Features4, 'call_pp')
@patch.object(Features4, 'call_pve')
def test_wrapper_get_pve_v2(m_call_pve, m_call_pp, m_call_innotas):
    artifact = 'project'
    f = Features4()
    f.wrapper_get_pve(artifact)
    m_call_pve.assert_called_once_with(artifact)
    assert (m_call_pp.call_count == 0)
    assert (m_call_innotas.call_count == 0)