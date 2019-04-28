import datetime

from core.src import userpool
from entities.timeadmin.base import Base

ENTITY = 'timeadmin'


class Timeadmin(Base):
    def __init__(self, request):
        super().__init__(request)

    def for_user(self, user=None):
        if not user:
            self.user_id = self.constants['USERS']['ADMIN']['USERID']
        else:
            self.user_id = userpool.get_userid_from_pool(self.request, user)
        return self

    def for_task(self, task_title):
        self.task_det = self.db_store.search_by_key('task', 'title', task_title)[0]
        return self

    def on_date(self, days_offset=1):
        today = datetime.date.today()
        prev_monday = today - datetime.timedelta(days=today.weekday(), weeks=1)
        effective_date = prev_monday + datetime.timedelta(days=days_offset - 1)
        self.date = effective_date.strftime('%Y-%m-%d')
        return self

    # TODO: Should make independent of atom order (eg: self.date is populated after on_date function)
    def update_internal_rate(self, rate):
        project_id = self.task_det['projectId']['value']
        timesheet_row_ids = self.task_det['timesheet_row_ids']
        # TODO:Two users log on same day
        timesheet_row_id_det = self._get_timesheet_for_a_date(timesheet_row_ids, self.date)
        timesheet_row_id = timesheet_row_id_det['timesheet_row_id']
        timesheet_row_date_id = timesheet_row_id_det['timesheet_row_date_id']
        timesheet_id = timesheet_row_id_det['timesheet_id']
        is_billable = timesheet_row_id_det['isBillable']
        is_capitalized = timesheet_row_id_det['isCapitalized']
        role = timesheet_row_id_det['role']
        entry_hours = timesheet_row_id_det['entry_hours']
        data = {'user_id': self.user_id, 'task_id': self.task_det['id'], 'input_rate': rate, 'entry_date': self.date,
                'timesheet_id': timesheet_id, 'timesheet_row_id': timesheet_row_id,
                'timesheet_row_date_id': timesheet_row_date_id,
                "billable_flag": is_billable, "capitalized_flag": is_capitalized, "role": role,
                'payload': 'timeadmin_rate', 'entry_hours': entry_hours, 'project_id': project_id
                }
        super().update(**data)
        self._update_timesheet(timesheet_row_id, timesheet_row_date_id, rate)
        return self

    def _get_timesheet_for_a_date(self, timesheet_row_ids, date):
        # data_store = self.data_store.get()
        for timesheet_row_id in timesheet_row_ids:
            timesheet_row_id_det = self.db_store.search_by_key('timesheet', 'id', timesheet_row_id)[0]
            for entry in timesheet_row_id_det['entries']:
                entry_date = entry['entryDate']
                if entry_date == date:
                    data = {'role': timesheet_row_id_det['role'], 'isBillable': timesheet_row_id_det['isBillable'],
                            'isCapitalized': timesheet_row_id_det['isCapitalized'],
                            'timesheet_id': timesheet_row_id_det['timesheet_id'], 'timesheet_row_date_id': entry['id'],
                            'entry_hours': entry['entryHours'],
                            'timesheet_row_id': timesheet_row_id}
                    return data

    def _update_timesheet(self, timesheet_row_id, timesheet_row_date_id, rate):
        timesheet_details = self.db_store.search_by_key('timesheet', 'id', timesheet_row_id)
        entries = timesheet_details[0]['entries']
        for entry in entries:
            if entry['id'] == timesheet_row_date_id:
                entry['internalRate'] = rate
                return True
        return False
