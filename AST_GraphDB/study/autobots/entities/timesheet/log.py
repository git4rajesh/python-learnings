from overloading import overload

from core.src import userpool
from entities.timesheet.base import Base

ENTITY = 'timesheet'


class Log:
    """
    This class is to log time sheets for the selected task
    """

    def __init__(self, timesheet):
        self.timesheet = timesheet
        self.request = timesheet.request
        self.base = Base(self.request)
        self.urls = self.request.getfixturevalue('read_urls')
        self.cmd_options = self.request.getfixturevalue('set_cmdline_opts')
        self.db_store = self.request.getfixturevalue('tiny_db_store')
        self.billable_log = True
        self.data = {}

    def select_a_task(self, title):
        """
        selet the task for which you want to log entries in the timesheet period
        :param title: title of the task
        """
        task_dict = self._get_task_dict(title)
        self.task_id = task_dict['id']
        self.timesheet.task_id = self.task_id
        self.project_id = task_dict['projectId']['value']
        self.timesheet.project_id = self.project_id
        self.billable_task = bool(task_dict['billingTypeId']['value'])
        self.capitalized_task = task_dict['isCapitalized']
        self.data.update({'project_id': self.project_id, 'task_id': self.task_id, 'billable_flag': self.billable_task,
                          'capitalized_flag': self.capitalized_task})
        return self

    def not_billable(self):
        """
        This atom is used to convert billable task to non billable task
        """
        self.billable_log = False
        return self

    @overload
    def set_entries(self):
        """
        overloaded atom to log time with entries only, entries are of two types,
            1. we can log time for all working days together
            2. we can log time for individual days of the week
        :param entries: examples for the above 2 points
            ex1 : entries={'all_working_days':'planned' or 'more_than_planned' or 'less_than_planned'} default is 'less_than_planned'
            ex2 : entries={'monday':4} or {'monday':2, 'tuesday':3, 'wednesday':5}
        :return: self object
        """
        self.set_entries(entries={'all_working_days': 'planned'})
        return self

    @overload
    def set_entries(self, entries: dict):
        """
        overloaded atom to log time with entries only, entries are of two types,
            1. we can log time for all working days together
            2. we can log time for individual days of the week
        :param entries: examples for the above 2 points
            ex1 : entries={'all_working_days':'planned' or 'more_than_planned' or 'less_than_planned'} default is 'less_than_planned'
            ex2 : entries={'monday':4} or {'monday':2, 'tuesday':3, 'wednesday':5}
        :return: self object
        """
        self.data.update({'entries': entries})
        return self

    def save(self):
        """
        Once all below actions are done on a timesheet row,
        then this method is used to save the row
        1. Select the task
        2. with user: if want to log the time with different user
        3. log: entries for the week along with hours
        :return:
        """
        data = self.data
        billable = (self.billable_log and self.billable_task)
        data.update({'billable_flag': billable})
        self.base.jsessionid = userpool.get_usertoken_of_current_user(self.request)
        self.timesheet.timesheet_id = self.base.create(**data)
        return self.timesheet

    def _get_task_dict(self, title):
        # task_dict = self.data_store.search.get_details_based_on_attributes(self.data_store.get(), 'task', title=title)
        task_dict = self.db_store.search_by_key('task', 'title', title)[0]
        return task_dict
