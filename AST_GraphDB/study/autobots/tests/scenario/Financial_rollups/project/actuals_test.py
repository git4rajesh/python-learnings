import pytest

from core.src.custom_annotations import zid
from core.fluent import Fluent


@zid('551')
def test_captbill_logging_multitask(request):
    """
    This is to test the logging of capitalized and billable combinations of tasks
    """
    Fluent(request) \
        .multipletasks([
        {'title': 'Auto_Task_1'},
        {'title': 'Auto_Task_2', 'type': 'cap_nonbill'},
        {'title': 'Auto_Task_3', 'type': 'noncap_bill'},
        {'title': 'Auto_Task_4', 'type': 'cap_bill'}])

    Fluent(request).timesheet() \
        .log('Auto_Task_1').set_entries(entries={'monday': 8}).save() \
        .log('Auto_Task_2').set_entries(entries={'tuesday': 8}).save() \
        .log('Auto_Task_3').set_entries(entries={'wednesday': 8}).save() \
        .log('Auto_Task_4').set_entries(entries={'thursday': 8}).save() \
        .verify_rollups('project')


@zid('xxxxx')
def test_captbill_logging_multitask_for_different_userypes(request):
    """
    This is to test the logging of capitalized and billable combinations of tasks
    """
    Fluent(request) \
        .multipletasks([
        {'title': 'Auto_Task_1'},
        {'title': 'Auto_Task_2', 'type': 'cap_nonbill'},
        {'title': 'Auto_Task_3', 'type': 'noncap_bill'},
        {'title': 'Auto_Task_4', 'type': 'cap_bill'}])

    Fluent(request).user('auto_te', 'support') \
        .login() \
        .timesheet() \
        .log('Auto_Task_1').set_entries(entries={'monday': 8}).save() \
        .log('Auto_Task_2').set_entries(entries={'tuesday': 8}).save() \
        .log('Auto_Task_3').set_entries(entries={'wednesday': 8}).save() \
        .log('Auto_Task_4').set_entries(entries={'thursday': 8}).save() \
        .logout() \
        .verify_rollups('project')


@zid('552')
def test_log_default(request):
    """
    Validate Rollups Page for Project Entity: Actual:
    Billable tasks charged as Non Billable for default internal rate
    """
    Fluent(request) \
        .multipletasks([{'title': 'Auto_Task_1', 'type': 'noncap_bill'},
                        {'title': 'Auto_Task_2', 'type': 'cap_bill'},
                        {'title': 'Auto_Task_3', 'type': 'noncap_nonbill'},
                        {'title': 'Auto_Task_4', 'type': 'cap_nonbill'}])

    Fluent(request) \
        .timesheet() \
        .log('Auto_Task_1').set_entries(
        {'all_working_days': 5}).save() \
        .log('Auto_Task_2').set_entries(
        {'all_working_days': 5}).save() \
        .log('Auto_Task_3').set_entries(
        {'all_working_days': 5}).save() \
        .log('Auto_Task_4').set_entries(
        {'all_working_days': 5}).save() \
        .verify_rollups('project')


@zid('xx')
def test_log_default_for_different_usertypes(request):
    """
    Validate Rollups Page for Project Entity: Actual:
    Billable tasks charged as Non Billable for default internal rate
    """
    Fluent(request)\
        .multipletasks([{'title': 'Auto_Task_1', 'type': 'noncap_bill'},
                        {'title': 'Auto_Task_2', 'type': 'cap_bill'},
                        {'title': 'Auto_Task_3', 'type': 'noncap_nonbill'},
                        {'title': 'Auto_Task_4', 'type': 'cap_nonbill'}])

    Fluent(request).user('auto_te', 'T&E') \
        .login() \
        .timesheet() \
        .log('Auto_Task_1').set_entries(
        {'all_working_days': 5}).save() \
        .log('Auto_Task_2').set_entries(
        {'all_working_days': 5}).save() \
        .log('Auto_Task_3').set_entries(
        {'all_working_days': 5}).save() \
        .log('Auto_Task_4').set_entries(
        {'all_working_days': 5}).save() \
        .logout() \
        .verify_rollups('project')


@zid('553')
def test_log_nonbillable_for_billable_tasks(request):
    """
    Validate Rollups Page for Project Entity: Actual:
    1. Add Multipletasks(4 variants of tasks)
    2. Log non billable time for Task1 and Task2 which are billable tasks
    Billable tasks charged as Non Billable for default internal rate
    """
    Fluent(request) \
        .multipletasks([{'title': 'Auto_Task_1', 'type': 'noncap_bill'},
                        {'title': 'Auto_Task_2', 'type': 'cap_bill'},
                        {'title': 'Auto_Task_3', 'type': 'noncap_nonbill'},
                        {'title': 'Auto_Task_4', 'type': 'cap_nonbill'}])

    Fluent(request) \
        .timesheet() \
        .log('Auto_Task_1').not_billable().set_entries(
        {'all_working_days': 5}).save() \
        .log('Auto_Task_2').not_billable().set_entries(
        {'all_working_days': 5}).save() \
        .log('Auto_Task_3').set_entries(
        {'all_working_days': 5}).save() \
        .log('Auto_Task_4').set_entries(
        {'all_working_days': 5}).save() \
        .verify_rollups('project')


@zid('xxx')
def test_log_nonbillable_for_billable_tasks_for_different_usertypes(request):
    """
    Validate Rollups Page for Project Entity: Actual:
    1. Add Multipletasks(4 variants of tasks)
    2. Log non billable time for Task1 and Task2 which are billable tasks
    Billable tasks charged as Non Billable for default internal rate
    """
    Fluent(request) \
        .multipletasks([{'title': 'Auto_Task_1', 'type': 'noncap_bill'},
                        {'title': 'Auto_Task_2', 'type': 'cap_bill'},
                        {'title': 'Auto_Task_3', 'type': 'noncap_nonbill'},
                        {'title': 'Auto_Task_4', 'type': 'cap_nonbill'}])

    Fluent(request).user('auto_te', 'team') \
        .login() \
        .timesheet() \
        .log('Auto_Task_1').not_billable().set_entries(
        {'all_working_days': 5}).save() \
        .log('Auto_Task_2').not_billable().set_entries(
        {'all_working_days': 5}).save() \
        .log('Auto_Task_3').set_entries(
        {'all_working_days': 5}).save() \
        .log('Auto_Task_4').set_entries(
        {'all_working_days': 5}).save() \
        .logout() \
        .verify_rollups('project')


@zid('554')
def test_log_with_different_internal_rate(request):
    """
    Validate rollups for project entity:
    1. Internal rate for the admin user is changed before time is logged
    2. Add 4 variants of tasks
    4. Log time for all four
    """

    Fluent(request).user().set_internalrate('RATE100')

    Fluent(request) \
        .multipletasks([{'title': 'Auto_Task_1', 'type': 'noncap_bill'},
                        {'title': 'Auto_Task_2', 'type': 'cap_bill'},
                        {'title': 'Auto_Task_3', 'type': 'noncap_nonbill'},
                        {'title': 'Auto_Task_4', 'type': 'cap_nonbill'}])

    Fluent(request) \
        .timesheet() \
        .log('Auto_Task_1').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_2').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_3').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_4').set_entries({'all_working_days': 5}).save() \
        .verify_rollups('project')


@zid('xxxxx')
def test_log_with_different_internal_rate_for_different_usertypes(request):
    """
    Validate rollups for project entity:
    1. Internal rate for the admin user is changed before time is logged
    2. Add 4 variants of tasks
    4. Log time for all four
    """

    Fluent(request).user('auto_te', 'T&E').set_internalrate('RATE100')

    Fluent(request) \
        .multipletasks([{'title': 'Auto_Task_1', 'type': 'noncap_bill'},
                        {'title': 'Auto_Task_2', 'type': 'cap_bill'},
                        {'title': 'Auto_Task_3', 'type': 'noncap_nonbill'},
                        {'title': 'Auto_Task_4', 'type': 'cap_nonbill'}])

    Fluent(request).user('auto_te') \
        .login() \
        .timesheet() \
        .log('Auto_Task_1').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_2').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_3').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_4').set_entries({'all_working_days': 5}).save() \
        .logout() \
        .verify_rollups('project')


@zid('556')
def test_log_split_internal_rates(request):
    """
    Validate rollups for project entity:
    1. Internal rate for the admin user is split as
        a. Mon & Tue have a specific rate
        b. Wed, Thu & Fri have a different specific rate
    2. Add 4 variants of tasks
    4. Log time for all four
    """

    Fluent(request).user().set_internalrate('RATE100').set_internalrate('RATE250', 3)

    Fluent(request) \
        .multipletasks([{'title': 'Auto_Task_1', 'type': 'noncap_nonbill'},
                        {'title': 'Auto_Task_2', 'type': 'noncap_bill'},
                        {'title': 'Auto_Task_3', 'type': 'cap_nonbill'},
                        {'title': 'Auto_Task_4', 'type': 'cap_bill'}])

    Fluent(request) \
        .timesheet() \
        .log('Auto_Task_1').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_2').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_3').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_4').set_entries({'all_working_days': 5}).save() \
        .verify_rollups('project')


@zid('xxxxxx')
def test_log_split_internal_rates_for_different_usertypes(request):
    """
    Validate rollups for project entity:
    1. Internal rate for the admin user is split as
        a. Mon & Tue have a specific rate
        b. Wed, Thu & Fri have a different specific rate
    2. Add 4 variants of tasks
    4. Log time for all four
    """

    Fluent(request).user('auto_te', 'support').set_internalrate('RATE100').set_internalrate('RATE250', 3)

    Fluent(request) \
        .multipletasks([{'title': 'Auto_Task_1', 'type': 'noncap_nonbill'},
                        {'title': 'Auto_Task_2', 'type': 'noncap_bill'},
                        {'title': 'Auto_Task_3', 'type': 'cap_nonbill'},
                        {'title': 'Auto_Task_4', 'type': 'cap_bill'}])

    Fluent(request).user('auto_te') \
        .login() \
        .timesheet() \
        .log('Auto_Task_1').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_2').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_3').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_4').set_entries({'all_working_days': 5}).save() \
        .logout() \
        .verify_rollups('project')


@zid('557')
def test_log_nonbillable_for_billable_tasks_with_split_internalrates(request):
    """
    Validate rollups for project entity:
    1. Internal rate for the admin user is split as
        a. Mon & Tue have a specific rate
        b. Wed, Thu & Fri have a different specific rate
    2. Add 4 variants of tasks
    3. Log non billable time for Task2 and Task4 which are billable tasks
        Billable tasks charged as Non Billable for custom internal rate
    """

    Fluent(request).user().set_internalrate('RATE100').set_internalrate('RATE250', 3)

    Fluent(request) \
        .multipletasks([{'title': 'Auto_Task_1', 'type': 'noncap_nonbill'},
                        {'title': 'Auto_Task_2', 'type': 'noncap_bill'},
                        {'title': 'Auto_Task_3', 'type': 'cap_nonbill'},
                        {'title': 'Auto_Task_4', 'type': 'cap_bill'}])

    Fluent(request) \
        .timesheet() \
        .log('Auto_Task_1').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_2').not_billable().set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_3').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_4').not_billable().set_entries({'all_working_days': 5}).save() \
        .verify_rollups('project')


@zid('xxxxxxx')
def test_log_nonbillable_for_billable_tasks_with_split_internalrates_for_different_usertypes(request):
    """
    Validate rollups for project entity:
    1. Internal rate for the admin user is split as
        a. Mon & Tue have a specific rate
        b. Wed, Thu & Fri have a different specific rate
    2. Add 4 variants of tasks
    3. Log non billable time for Task2 and Task4 which are billable tasks
        Billable tasks charged as Non Billable for custom internal rate
    """

    Fluent(request).user('auto_te', 'T&E').set_internalrate('RATE100').set_internalrate('RATE250', 3)

    Fluent(request) \
        .multipletasks([{'title': 'Auto_Task_1', 'type': 'noncap_nonbill'},
                        {'title': 'Auto_Task_2', 'type': 'noncap_bill'},
                        {'title': 'Auto_Task_3', 'type': 'cap_nonbill'},
                        {'title': 'Auto_Task_4', 'type': 'cap_bill'}])

    Fluent(request).user('auto_te') \
        .login() \
        .timesheet() \
        .log('Auto_Task_1').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_2').not_billable().set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_3').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_4').not_billable().set_entries({'all_working_days': 5}).save() \
        .logout() \
        .verify_rollups('project')


@zid('559')
def test_log_admin_changes_resource_internal_split_rate_table(request):
    """
    Validate rollups for project entity:
    1. Internal rate for the admin user is split as
        a. Mon & Tue have a specific rate
        b. Wed, Thu & Fri have a different specific rate
    2. Add 4 variants of tasks
    3. Log time for all four tasks
    4. Admin changes the internal rate table for the same period
        a. Mon, Tue, Wed, Thu & Fri with a new rate
    5. Validate the rollups at project level

    Expected result is project rollups should calculate with old rates(rates set at 1a & 1b steps) for the hours logged

    """

    Fluent(request).user().set_internalrate('RATE100').set_internalrate('RATE250', 3)

    Fluent(request) \
        .multipletasks([{'title': 'Auto_Task_1', 'type': 'noncap_nonbill'},
                        {'title': 'Auto_Task_2', 'type': 'noncap_bill'},
                        {'title': 'Auto_Task_3', 'type': 'cap_nonbill'},
                        {'title': 'Auto_Task_4', 'type': 'cap_bill'}])

    Fluent(request) \
        .timesheet() \
        .log('Auto_Task_1').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_2').not_billable().set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_3').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_4').set_entries({'all_working_days': 5}).save() \
        .verify_rollups('project')

    Fluent(request).user().set_internalrate('RATE90')

    Fluent(request).timesheet().log('Auto_Task_1').set_entries({'all_working_days': 5}).save().verify_rollups('project')


@zid('xxxxxxxx')
def test_log_admin_changes_resource_internal_split_rate_table_for_different_usertypes(request):
    """
    Validate rollups for project entity:
    1. Internal rate for the admin user is split as
        a. Mon & Tue have a specific rate
        b. Wed, Thu & Fri have a different specific rate
    2. Add 4 variants of tasks
    3. Log time for all four tasks
    4. Admin changes the internal rate table for the same period
        a. Mon, Tue, Wed, Thu & Fri with a new rate
    5. Validate the rollups at project level

    Expected result is project rollups should calculate with old rates(rates set at 1a & 1b steps) for the hours logged

    """

    Fluent(request).user('auto_te', 'T&E').set_internalrate('RATE100').set_internalrate('RATE250', 3)

    Fluent(request) \
        .multipletasks([{'title': 'Auto_Task_1', 'type': 'noncap_nonbill'},
                        {'title': 'Auto_Task_2', 'type': 'noncap_bill'},
                        {'title': 'Auto_Task_3', 'type': 'cap_nonbill'},
                        {'title': 'Auto_Task_4', 'type': 'cap_bill'}])

    Fluent(request).user('auto_te', 'T&E') \
        .login() \
        .timesheet() \
        .log('Auto_Task_1').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_2').not_billable().set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_3').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_4').set_entries({'all_working_days': 5}).save() \
        .logout() \
        .verify_rollups('project')

    Fluent(request).user('auto_te', 'T&E').set_internalrate('RATE90')

    Fluent(request).user('auto_te', 'T&E') \
        .login() \
        .timesheet() \
        .log('Auto_Task_1').set_entries({'all_working_days': 5}).save() \
        .logout() \
        .verify_rollups('project')

@zid('560')
def test_log_timeadmin_changes_rate_in_timesheet_page(request):
    """
    Validate rollups for project entity:
    1. Internal rate for the admin user is split as
        a. Mon & Tue have a specific rate
        b. Wed, Thu & Fri have a different specific rate
    2. Add 4 variants of tasks
    3. Log time for all four tasks
    4. Timeadmin changes the internal rate for Mon for a specific task
    5. Validate rollups at project level

    Expected result is project rollups should calculate based on the new rate input by timeadmin
    """

    Fluent(request).user().set_internalrate('RATE100').set_internalrate('RATE250', 3)

    Fluent(request).project() \
        .multipletasks([{'title': 'Auto_Task_1', 'type': 'noncap_nonbill'},
                        {'title': 'Auto_Task_2', 'type': 'noncap_bill'},
                        {'title': 'Auto_Task_3', 'type': 'cap_nonbill'},
                        {'title': 'Auto_Task_4', 'type': 'cap_bill'}])

    Fluent(request) \
        .timesheet() \
        .log('Auto_Task_1').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_2').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_3').set_entries({'all_working_days': 5}).save()

    Fluent(request).timeadmin().for_task('Auto_Task_1').for_user().on_date(1).update_internal_rate(150)

    Fluent(request).timesheet().log('Auto_Task_4').not_billable().set_entries(
        {'all_working_days': 5}).save().verify_rollups('project')


@zid('xxxxxxxxx')
def test_log_timeadmin_changes_rate_in_timesheet_page_for_different_usertypes(request):
    """
    Validate rollups for project entity:
    1. Internal rate for the admin user is split as
        a. Mon & Tue have a specific rate
        b. Wed, Thu & Fri have a different specific rate
    2. Add 4 variants of tasks
    3. Log time for all four tasks
    4. Timeadmin changes the internal rate for Mon for a specific task
    5. Validate rollups at project level

    Expected result is project rollups should calculate based on the new rate input by timeadmin
    """

    Fluent(request).user('auto_te', 'T&E').set_internalrate('RATE100').set_internalrate('RATE250', 3)

    Fluent(request) \
        .multipletasks([{'title': 'Auto_Task_1', 'type': 'noncap_nonbill'},
                        {'title': 'Auto_Task_2', 'type': 'noncap_bill'},
                        {'title': 'Auto_Task_3', 'type': 'cap_nonbill'},
                        {'title': 'Auto_Task_4', 'type': 'cap_bill'}])

    Fluent(request).user('auto_te', 'T&E') \
        .login() \
        .timesheet() \
        .log('Auto_Task_1').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_2').set_entries({'all_working_days': 5}).save() \
        .log('Auto_Task_3').set_entries({'all_working_days': 5}).save() \
        .logout()

    Fluent(request).timeadmin().for_task('Auto_Task_1').for_user('auto_te').on_date(1).update_internal_rate(150)

    Fluent(request).user('auto_te', 'T&E') \
        .login() \
        .timesheet().log('Auto_Task_4').not_billable().set_entries(
        {'all_working_days': 5}).save() \
        .logout() \
        .verify_rollups('project')
