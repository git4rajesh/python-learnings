import pytest

from core.fluent import Fluent
from core.src.custom_annotations import zid


@zid('549')
def test_log_for_all_workingdays(request):
    """
    This is to test the time sheet logging atom of task under project
    """
    Fluent(request) \
        .project() \
        .task('Task-1') \
        .timesheet() \
        .log('Task-1').set_entries(entries={'all_working_days': 'planned'}).save() \
        .verify_rollups('task')


@zid('xxxx')
def test_log_for_all_workingdays_for_different_usertypes(request):
    """
    This is to test the time sheet logging atom of task under project
    """
    Fluent(request) \
        .project() \
        .task('Task-1')

    Fluent(request).user('auto_te', 'T&E') \
        .login() \
        .timesheet() \
        .log('Task-1').set_entries(entries={'all_working_days': 'planned'}).save() \
        .logout() \
        .verify_rollups('task')


@zid('549')
def test_log_for_one_day(request):
    """
    This is to test the time sheet logging atom of task under project
    """
    Fluent(request) \
        .project() \
        .task('task-1') \
        .timesheet() \
        .log('task-1').set_entries(entries={'monday': 4}).save() \
        .verify_rollups('task')


@zid('xxxx')
def test_log_for_one_day_different_usertypes(request):
    """
    This is to test the time sheet logging atom of task under project
    """
    Fluent(request) \
        .project().task('task-1')

    Fluent(request).user('auto_te', 'T&E') \
        .login() \
        .timesheet() \
        .log('task-1').set_entries(entries={'monday': 4}).save() \
        .logout() \
        .verify_rollups('task')


def test_nonbillable_logging(request):
    """
    This is to test the time sheet logging atom of task under project
    """
    Fluent(request) \
        .project() \
        .task('task-1', 'cap_bill') \
        .timesheet() \
        .log('task-1').not_billable().set_entries(entries={'monday': 4}).save() \
        .verify_rollups('task')


@zid('xxxx')
def test_nonbillable_logging_for_different_usertypes(request):
    """
    This is to test the time sheet logging atom of task under project
    """
    Fluent(request) \
        .project().task('task-1', 'cap_bill')

    Fluent(request).user('auto_te', 'T&E') \
        .login() \
        .timesheet() \
        .log('task-1').not_billable().set_entries(entries={'monday': 4}).save() \
        .logout() \
        .verify_rollups('task')


def test_logging(request):
    """
    This test is to validate the rollups at Project entity level where
    billable tasks are logged with billable entries and non-billable tasks are logged with non-billable entries.
    """
    Fluent(request).project().multipletasks([{'title': 'Auto_Task-1', 'type': 'noncap_bill'},
                                             {'title': 'Auto_Task-2', 'type': 'cap_bill'},
                                             {'title': 'Auto_Task-3', 'type': 'noncap_nonbill'},
                                             {'title': 'Auto_Task-4', 'type': 'cap_nonbill'}])

    Fluent(request) \
        .timesheet() \
        .log('Auto_Task-1').set_entries(entries={'monday': 5, 'tuesday': 5, 'wednesday': 5, 'thursday': 5, 'friday': 5}) \
        .save() \
        .log('Auto_Task-2').set_entries(entries={'monday': 5, 'tuesday': 5, 'wednesday': 5, 'thursday': 5, 'friday': 5}) \
        .save() \
        .log('Auto_Task-3').set_entries(entries={'monday': 5, 'tuesday': 5, 'wednesday': 5, 'thursday': 5, 'friday': 5}) \
        .save() \
        .log('Auto_Task-1').set_entries(entries={'monday': 5, 'tuesday': 5, 'wednesday': 5, 'thursday': 5, 'friday': 5}) \
        .save() \
        .verify_rollups('project')

# @pytest.mark.debug
# @zid('xxxx')
# def test_logging_for_different_usertypes(request):
#     """
#     This test is to validate the rollups at Project entity level where
#     billable tasks are logged with billable entries and non-billable tasks are logged with non-billable entries.
#     """
#     Fluent(request).multipletasks([{'title': 'Auto_Task-1', 'type': 'noncap_bill'},
#                                    {'title': 'Auto_Task-2', 'type': 'cap_bill'},
#                                    {'title': 'Auto_Task-3', 'type': 'noncap_nonbill'},
#                                    {'title': 'Auto_Task-4', 'type': 'cap_nonbill'}])
#
#     Fluent(request).user('auto_te', 'T&E') \
#         .login() \
#         .timesheet() \
#         .log('Auto_Task-1').set_entries(entries={'monday': 5, 'tuesday': 5, 'wednesday': 5, 'thursday': 5, 'friday': 5}) \
#         .save() \
#         .log('Auto_Task-2').set_entries(entries={'monday': 5, 'tuesday': 5, 'wednesday': 5, 'thursday': 5, 'friday': 5}) \
#         .save() \
#         .log('Auto_Task-3').set_entries(entries={'monday': 5, 'tuesday': 5, 'wednesday': 5, 'thursday': 5, 'friday': 5}) \
#         .save() \
#         .log('Auto_Task-1').set_entries(entries={'monday': 5, 'tuesday': 5, 'wednesday': 5, 'thursday': 5, 'friday': 5}) \
#         .save() \
#         .logout() \
#         .verify_rollups('project')
