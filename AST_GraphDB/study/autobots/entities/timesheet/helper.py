import calendar
import datetime

from core import utils
from datetime import timedelta


def append_entries(func):
    def append_entries_to_timesheet(self, **data):
        api = self.urls['timesheet']['read_all']
        url = api.format(
            protocol='https',
            env=self.cmd_options['env'],
            previouscount=2,
            futurecount=0)
        response = self.rqst_session.get(url, cookies={'JSESSIONID': self.jsessionid})
        timesheet_id, start_date = _get_timesheet_id_for_previous_week(response.json()['items'])
        entries = data.get('entries')
        if entries:
            if 'all_working_days' in entries:
                calendar_week = entries['all_working_days']
                entries, total_hrs = _log_for_all_working_days(start_date, calendar_week)
            else:
                entries, total_hrs = _log_time_with_entries(start_date, entries)
        else:
            calendar_week = 'less_than_planned'
            entries, total_hrs = _log_for_all_working_days(start_date, calendar_week)

        data.update(timesheet_id=timesheet_id, entries=entries, total_hrs=total_hrs)
        return func(self, **data)

    return append_entries_to_timesheet


def _get_timesheet_id_for_previous_week(item_lst):
    today = datetime.date.today()
    prev_monday = today - datetime.timedelta(days=today.weekday(), weeks=1)
    for item in item_lst:
        date = item['startDate']
        if date == str(prev_monday):
            return item['id'], prev_monday


def _log_time_with_entries(start_date, entries):
    lst_entries = []
    total_hrs = 0
    for day in range(5):
        start_date = start_date + timedelta(days=day)
        day_name = calendar.day_name[start_date.weekday()].lower()
        if day_name in entries.keys():
            tmp = {}
            tmp['entryDate'] = str(start_date)
            tmp['entryHours'] = entries[day_name]
            total_hrs += entries[day_name]
            lst_entries.append(tmp)
    return lst_entries, total_hrs


def _log_for_all_working_days(start_date, calendar_week):
    lst_entries = []
    total_hrs = 0
    if calendar_week == 'planned':
        total_hrs = 40
        lst_entries = _generate_entries(total_hrs, start_date)
    elif calendar_week == 'more_than_planned':
        total_hrs = 50
        lst_entries = _generate_entries(total_hrs, start_date)
    elif calendar_week == 'less_than_planned':
        total_hrs = 10
        lst_entries = _generate_entries(total_hrs, start_date)
    elif isinstance(calendar_week, int):
        total_hrs = calendar_week
        lst_entries = _generate_entries(total_hrs, start_date)
    return lst_entries, total_hrs


def _generate_entries(total_hrs, start_date):
    lst_entries = []
    no_of_working_days = 5
    hours = total_hrs / no_of_working_days
    for day in range(no_of_working_days):
        entries = {}
        entries['entryDate'] = str(start_date + timedelta(days=day))
        entries['entryHours'] = hours
        lst_entries.append(entries)
        total_hrs += hours
    return lst_entries
