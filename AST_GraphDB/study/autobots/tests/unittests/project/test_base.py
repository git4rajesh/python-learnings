from unittest.mock import patch, ANY
from entities.project.base import Base
from core.src.custom_annotations import tags

@tags('unittest')
@patch('entities.project.base.Base.verify_create')
@patch('requests.session')
def test_create(mock_session, mock_verify_create, request):
    # Mocking the return value of requests post method
    mock_session.post.return_value.content = {'id': 18909}
    # Mocking verification of creation with response
    mock_verify_create.return_value = [mock_session.post.return_value, 31923]
    cmd_options = request.getfixturevalue('set_cmdline_opts')
    env = cmd_options['env']
    url = 'https://{0}/com.innotas.service.json.entity.detail.content.NewEntityDetailsContent.pa?entityType=project&categoryId=1320597422&action=update'.format(
        env)
    data = {'title': 'auto_project'}
    base_obj = Base(request)
    base_obj.rqst_session = mock_session
    base_obj.create(**data)
    mock_verify_create.assert_called_with(mock_session.post.return_value)
    payload = {'data': {'id': -1, 'parentInstance': {'value': '1085775460', 'displayText': 'Sample Program',
                                                     'type': 'Engagement'},
                        'title': 'auto_project',
                        'LLStatusId': {'value': '1040991866', 'displayText': 'Proposed', 'type': '[14:10:-1]'}}}

    mock_session.post.assert_called_with(url, json=payload, cookies={'JSESSIONID': ANY})
