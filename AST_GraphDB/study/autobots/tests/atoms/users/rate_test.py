from core.fluent import Fluent
from core.src.custom_annotations import zid, tags


@zid('123456')
def test_captbill_nonbillable_charge_different_internal_rate(request):
    """
    Atom Test: Create a new user, and set internal rate
               Create multiple tasks with the default user
               Log time for task1 with new user
               Log time for task2 with default user
               Verify project rollups
    """
    Fluent(request).user('auto-1').set_internalrate('RATE100')

    Fluent(request).project()\
        .multipletasks([{'title': 'Auto_Task_1', 'type': 'cap_bill'},
                        {'title': 'Auto_Task_2', 'type': 'cap_bill'}])

    Fluent(request).user('auto-1', 'T&E') \
        .login() \
        .timesheet() \
        .log('Auto_Task_1').set_entries(entries={'monday': 2}).save() \
        .log('Auto_Task_2').set_entries().save() \
        .logout() \
        .verify_rollups('project')
