import pytest

from core.src.custom_annotations import zid
from core.fluent import Fluent


@pytest.mark.parametrize('usertype', ['full', 'support', 'team', 't&e'])
@zid('543')
def test_captbill_nonbillable_log_different_user(request, usertype):
    """

    """
    Fluent(request).project() \
        .multipletasks([{'title': 'Task-1', 'type': 'cap_bill'},
                        {'title': 'Task-2', 'type': 'cap_bill'}])

    Fluent(request).user('auto-1', usertype) \
        .login() \
        .timesheet() \
        .log('Task-1').set_entries(entries={'monday': 2}).save() \
        .log('Task-2').set_entries().save() \
        .logout() \
        .verify_rollups('project')
