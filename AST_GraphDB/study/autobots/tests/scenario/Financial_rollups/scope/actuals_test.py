# import pytest

from core.fluent import Fluent
from core.src.custom_annotations import zid


@zid('549')
def test_actuals(request):
    """
    This is to test the rollup at scope level after logging actual hours for scope and leaf tasks
    """
    # Create entities
    Fluent(request).project().task('Task-1').childtask('Task-1.1').childtask('Task-1.1.1') \
        .childtask('Task-1.1.2', parent='Task-1.1').childtask('Task-1.2', parent='Task-1')

    # Log timesheets and verify rollups
    Fluent(request).timesheet() \
        .log('Task-1').set_entries().save() \
        .log('Task-1.1').set_entries().save() \
        .log('Task-1.1.1').set_entries().save() \
        .log('Task-1.1.2').set_entries().save() \
        .log('Task-1.2').set_entries().save() \
        .verify_rollups('task')


@zid('xxxx')
def test_actuals_for_different_usertypes(request):
    """
    This is to test the rollup at scope level after logging actual hours for scope and leaf tasks
    """
    # Create entities
    Fluent(request).project().task('Task-1').childtask('Task-1.1').childtask('Task-1.1.1') \
        .childtask('Task-1.1.2', parent='Task-1.1').childtask('Task-1.2', parent='Task-1')

    # Log timesheets and verify rollups
    Fluent(request).user('auto_te', 'T&E') \
        .login() \
        .timesheet() \
        .log('Task-1').set_entries().save() \
        .log('Task-1.1').set_entries().save() \
        .log('Task-1.1.1').set_entries().save() \
        .log('Task-1.1.2').set_entries().save() \
        .log('Task-1.2').set_entries().save() \
        .logout() \
        .verify_rollups('task')


@zid('549')
def test_demo(request):
    """
    This is to test the rollup at scope level after logging actual hours for scope and leaf tasks
    """
    # Create entities
    Fluent(request) \
        .project().task('Task-1') \
        .childtask('Task-1.1') \
        .childtask('Task-1.1.1', parent='Task-1.1').childtask('Task-1.1.2', parent='Task-1.1')

    # Log timesheets and verify rollups
    Fluent(request).timesheet() \
        .log('Task-1.1').set_entries().save() \
        .log('Task-1.1.1').set_entries().save() \
        .log('Task-1.1.2').set_entries().save() \
        .verify_rollups('task')

@zid('xxxx')
def test_demo_for_different_usertypes(request):
    """
    This is to test the rollup at scope level after logging actual hours for scope and leaf tasks
    """
    # Create entities
    Fluent(request) \
        .project().task('Task-1') \
        .childtask('Task-1.1') \
        .childtask('Task-1.1.1', parent='Task-1.1').childtask('Task-1.1.2', parent='Task-1.1')

    # Log timesheets and verify rollups
    Fluent(request).user('auto_te', 'T&E') \
        .login() \
        .timesheet() \
        .log('Task-1.1').set_entries().save() \
        .log('Task-1.1.1').set_entries().save() \
        .log('Task-1.1.2').set_entries().save() \
        .logout() \
        .verify_rollups('task')


def test_entries(request):
    """
    This is to test the rollup at scope level after logging actual hours for a particular day
    """
    # Create entities
    Fluent(request) \
        .project().task('Task-1') \
        .childtask('Task-1.1') \
        .timesheet() \
        .log('Task-1.1').set_entries(entries={'monday': 2}).save() \
        .verify_rollups('task')


def test_entries_for_different_usertypes(request):
    """
    This is to test the permissions of user type for the rollup at scope level after logging actual hours for a particular day
    """

    # Create entities
    Fluent(request) \
        .project().task('Task-1') \
        .childtask('Task-1.1')

    # User belonging to different usertypes logs timesheet
    Fluent(request).user('auto_te', 'T&E') \
        .login() \
        .timesheet() \
        .log('Task-1').set_entries(entries={'monday': 2}).save() \
        .log('Task-1.1').set_entries(entries={'monday': 2}).save() \
        .logout() \
        .verify_rollups('task')
