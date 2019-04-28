import pytest

from core.fluent import Fluent
from datetime import datetime
from core.src.custom_annotations import zid


@pytest.mark.parametrize('title', ['abcnd12345', '123455', 'a&b', 'a<b==&"s{>ss!s}d{', 'spec!@#<>$', r'test\'te"test'])
@zid('550')
def test_title(request, title):
    """
    testing the api to set the project title
    """
    Fluent(request).project().set_title(title).verify()


@pytest.mark.parametrize('description',
                         ['Sample description', '123456', 'a&b', 'a<b==&"s{>ss!s}d{', 'spec!@#<>$', r'test\'te"test'])
@zid('550')
def test_description(request, description):
    """
    testing the api to set the project description
    """
    Fluent(request).project().set_description(description).verify()


@pytest.mark.parametrize('department', ['PROGRAM2', 'PROGRAM3', 'PROGRAM4'])
@zid('550')
def test_department(request, department):
    """
    testing the api to set the project department
    """
    Fluent(request).project().set_department(department).verify()


@pytest.mark.parametrize('owner', ['PROJECT_OWNER1', 'PROJECT_OWNER2'])
@zid('550')
def test_owner(request, owner):
    """
    testing the api to set the project owner
    """
    Fluent(request).project().set_owner(owner).verify()


@pytest.mark.parametrize('is_confidential_value', ['Yes', 'No'])
@zid('550')
def test_confidential(request, is_confidential_value):
    """
    testing the api to set the project confidentiality
    """
    Fluent(request).project().set_confidential(is_confidential_value).verify()


@pytest.mark.parametrize('status', ['APPROVED', 'HOLD'])
@zid('550')
def test_status(request, status):
    """
    testing the api to set the project status
    """
    Fluent(request).project().set_status(status).verify()


@pytest.mark.parametrize('phase', ['PHASE1', 'PHASE2'])
@zid('550')
def test_phase(request, phase):
    """
    testing the api to set the project phase
    """
    Fluent(request).project().set_phase(phase).verify()


@pytest.mark.parametrize('dd_mm_yy', ['06-06-2018', '30-06-2018'])
@zid('550')
def test_completedate(request, dd_mm_yy):
    """
    testing the api to set the project completion date
    """
    date_time = datetime.strptime(dd_mm_yy, '%d-%m-%Y')
    complete_date_time = date_time.strftime('%Y-%m-%dT00:00:00.000')
    Fluent(request).project().set_complete_date(complete_date_time).verify()


@zid('550')
def test_550delete(request):
    """
    testing the api to delete the project
    """
    Fluent(request).project().delete()
