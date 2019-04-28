from unittest.mock import patch
from entities.task.task import Task
from entities.schedule.schedule import Schedule
from core.src.custom_annotations import tags

@tags('unittest')
@patch('entities.task.task.Task.create_under_project')
def test_create(mock_task_create_under_project, request):
    title = 'auto_task'
    type = 'noncap_nonbill'
    Task(request).create(title, type)
    mock_task_create_under_project.assert_called_with(title, type)

@tags('unittest')
@patch('entities.task.base.Base.create')
@patch('entities.task.task.Task._update')
def test_create_under_project(mock_task__update, mock_base_create, request):
    title = 'auto_task'
    type = 'noncap_nonbill'
    project_id = None
    Task(request).create_under_project(title, type)
    mock_base_create.assert_called_with(project_id=project_id)
    mock_task__update.assert_called_with(title=title, payload=type)

@tags('unittest')
@patch('entities.task.task.Task._update')
def test_set_title(mock__update, request):
    title = 'auto_project'
    Task(request).set_title(title)
    mock__update.assert_called_with(payload='title', title=title)

@tags('unittest')
@patch('entities.task.task.Task._update')
def test_set_description(mock__update, request):
    description = 'auto_description'
    Task(request).set_description(description)
    mock__update.assert_called_with(payload='description', description=description)

@tags('unittest')
@patch('entities.task.task.Task._update')
def test_set_status(mock__update, request):
    status = 'HOLD'
    Task(request).set_status(status)
    mock__update.assert_called_with(payload='status',
                                    status_id=1040991875, status_value='Hold')

@tags('unittest')
@patch('entities.task.task.Task._update')
def test_set_duration(mock__update, request):
    duration = 28800
    Task(request).set_duration(duration)
    mock__update.assert_called_with(payload='duration', duration=duration)

@tags('unittest')
@patch('entities.task.task.Task._update')
def test_set_start_date(mock__update, request):
    start_date_time = '16-07-2018T00:00:00.000'
    Task(request).set_start_date(start_date_time)
    mock__update.assert_called_with(payload='start_date',
                                    start_date_time=start_date_time)

@tags('unittest')
@patch('entities.task.task.Task._update')
def test_set_complete_date(mock__update, request):
    complete_date_time = '16-07-2018T00:00:00.000'
    Task(request).set_complete_date(complete_date_time)
    mock__update.assert_called_with(payload='completed_date',
                                    complete_date_time=complete_date_time)

@tags('unittest')
def test_schedule(request):
    task_obj = Task(request)
    task_obj.task_id = 789801
    task_obj.project_id = 890131
    schedule_obj = task_obj.schedule()
    assert isinstance(schedule_obj, Schedule)
    assert schedule_obj.task_id == 789801
    assert schedule_obj.project_id == 890131
