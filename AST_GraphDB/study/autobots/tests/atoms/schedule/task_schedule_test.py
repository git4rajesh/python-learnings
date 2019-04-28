import pytest

from core.fluent import Fluent
from core.src.custom_annotations import zid


@pytest.mark.parametrize('resource_name, role_name, estimated_hrs', [('BA', 'BA', 24)])
@zid('549')
def test_schedule(request, resource_name, role_name, estimated_hrs):
    """
    testing the api to adding the resource and setting the role hours at the task level
    """
    Fluent(request).task('task-2').schedule().add_resource(resource_name, role_name).set_role_hrs(estimated_hrs).verify()


@pytest.mark.parametrize('resource_name, role_name, resource_hrs, resource_htc', [('BA', 'BA', 25, 20), ('BA', 'BA', 20, 20)])
@zid('549')
def test_scheduleresource(request, resource_name, role_name, resource_hrs, resource_htc):
    """
    testing the api to set the scheduled hours and hours to complete(htc) for the resource at task level
    """
    Fluent(request).task('task-1').schedule().add_resource(resource_name, role_name).set_resource_hrs(resource_hrs, resource_htc).verify()
