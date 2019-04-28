import pytest

from core.fluent import Fluent
from datetime import datetime

from core.src.custom_annotations import zid


@pytest.mark.parametrize('title', ['abcnd12345', '123455', 'spec!@#<>$', r'test\'te"test'])
@zid('549')
def test_title(request, title):
    """
    testing the api to set the task title
    """
    Fluent(request).task('task-1').set_title(title).verify()


@pytest.mark.parametrize('description', ['Sample description', '123456', 'spec!@#<>$', r'test\'te"test'])
@zid('549')
def test_description(request, description):
    """
    testing the api to set the task description
    """
    Fluent(request).task('task-1').set_description(description).verify()


@pytest.mark.parametrize('status', ['APPROVED', 'HOLD'])
@zid('549')
def test_status(request, status):
    """
    testing the api to set the task status
    """
    Fluent(request).task('task-1').set_status(status).verify()


@pytest.mark.parametrize('days', [1, 6, 2])
def test_549duration(request, days):
    """
    testing the api to set the task target date
    """
    days_in_sec = days * 60 * 60 * 8
    Fluent(request).task('task-1').set_duration(days_in_sec).verify()


@pytest.mark.parametrize('dd_mm_yy_hh_mm_ss', ['28-05-2018-10-23-22', '28-05-2018-13-10-10'])
def test_549startdate(request, dd_mm_yy_hh_mm_ss):
    """
    testing the api to set the task start date
    """
    date_time = datetime.strptime(dd_mm_yy_hh_mm_ss, '%d-%m-%Y-%H-%M-%S')
    start_date_time = date_time.strftime('%Y-%m-%dT%H:%M:%S.000')
    Fluent(request).task('task-1').set_start_date(start_date_time).verify()


@pytest.mark.parametrize('dd_mm_yy_hh_mm_ss', ['28-05-2018-10-23-22', '30-06-2018-13-10-10'])
def test_549completedate(request, dd_mm_yy_hh_mm_ss):
    """
    testing the api to set the task completed date
    """
    date_time = datetime.strptime(dd_mm_yy_hh_mm_ss, '%d-%m-%Y-%H-%M-%S')
    complete_date_time = date_time.strftime('%Y-%m-%dT%H:%M:%S.000')
    Fluent(request).task('task-1').set_complete_date(complete_date_time).verify()


def test_549delete(request):
    """
    testing the api to delete the task
    """
    Fluent(request).task('task-1').delete()
