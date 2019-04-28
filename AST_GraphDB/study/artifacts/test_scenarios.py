def test_captbill_logging_multitask(request):
    """
    This is to test the logging of capitalized and billable combinations of tasks
    """
    Fluent(request).project() \
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
