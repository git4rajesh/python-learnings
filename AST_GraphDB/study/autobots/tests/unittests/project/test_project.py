from unittest.mock import patch
from entities.project.project import Project
from core.src.custom_annotations import tags

@tags('unittest')
@patch('entities.project.base.Base.create')
def test_create(mock_base_create, request):
    data = {'title': 'auto_project'}
    Project(request).create(title='auto_project')
    mock_base_create.assert_called_with(**data)

@tags('unittest')
@patch('entities.project.project.Project._update')
def test_set_title(mock_update, request):
    title = 'auto_project'
    Project(request).set_title(title)
    mock_update.assert_called_with(payload='title', title=title)

@tags('unittest')
@patch('entities.project.project.Project._update')
def test_set_owner(mock_update, request):
    owner = 'PROJECT_OWNER1'
    Project(request).set_owner(owner)
    mock_update.assert_called_with(payload='owner', owner_id=1703118357, owner_value='User, Team')

@tags('unittest')
@patch('entities.project.project.Project._update')
def test_set_description(mock_update, request):
    description = 'auto_description'
    Project(request).set_description(description)
    mock_update.assert_called_with(payload='description', description=description)

@tags('unittest')
@patch('entities.project.project.Project._update')
def test_set_confidential(mock_update, request):
    is_confidential = 'yes'
    Project(request).set_confidential(is_confidential)
    mock_update.assert_called_with(payload='confidential', is_confidential_id=1, is_confidential_value='yes')

@tags('unittest')
@patch('entities.project.project.Project._update')
def test_set_phase(mock_update, request):
    phase = 'PHASE2'
    Project(request).set_phase(phase)
    mock_update.assert_called_with(payload='phase', phase_id=807336339, phase_value='Phase 2')

@tags('unittest')
@patch('entities.project.project.Project._update')
def test_set_complete_date(mock_update, request):
    complete_date_time = '16-07-2018T00:00:00.000'
    Project(request).set_complete_date(complete_date_time)
    mock_update.assert_called_with(payload='completed_date',
                                   complete_date_time=complete_date_time)

@tags('unittest')
@patch('entities.project.project.Project._update')
def test_set_status(mock_update, request):
    status = 'HOLD'
    Project(request).set_status(status)
    mock_update.assert_called_with(payload='status',
                                   status_id=1040991868, status_value='Hold')

@tags('unittest')
@patch('entities.project.project.Project._update')
def test_set_department(mock_update, request):
    department = 'PROGRAM2'
    Project(request).set_department(department)
    mock_update.assert_called_with(payload='department',
                                   department_id=1041056628, department_value='Program 301')
