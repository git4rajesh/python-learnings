import pytest

from core.fluent import Fluent


def test_timeadmin_rate(request):
    Fluent(request).project().task('Task-1', 'cap_bill').timesheet().log('Task-1').set_entries().save()
    Fluent(request).timeadmin().for_task('Task-1').for_user().on_date(1).update_internal_rate(200)
